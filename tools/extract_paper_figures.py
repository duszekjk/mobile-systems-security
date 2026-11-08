#!/usr/bin/env python3
"""Extract high-quality figure crops from a PDF using page geometry.

This script renders pages at high DPI and crops high-value page regions from the
rendered page using PyMuPDF bounding boxes. It writes:

- raw crops centered on the original figure region
- transparent-padded 3:4 variants for side-column slide layouts
- transparent-padded 3:2 variants for hero slide layouts
- a full-page render for reference/debugging

It is intentionally separate from Marker so Marker can remain the text/layout
reader while this script handles final slide assets.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import fitz  # PyMuPDF
from PIL import Image


@dataclass(frozen=True)
class FigureAsset:
    page_number: int
    index: int
    bbox: tuple[float, float, float, float]
    width: int
    height: int
    kind: str
    text_len: int = 0


def _render_page(page: fitz.Page, dpi: int) -> Image.Image:
    zoom = dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True)
    return Image.frombytes("RGBA", [pix.width, pix.height], pix.samples)


def _crop_with_margin(img: Image.Image, bbox: tuple[float, float, float, float], dpi: int, margin_px: int) -> Image.Image:
    scale = dpi / 72.0
    x0, y0, x1, y1 = bbox
    left = max(0, int(round(x0 * scale)) - margin_px)
    top = max(0, int(round(y0 * scale)) - margin_px)
    right = min(img.width, int(round(x1 * scale)) + margin_px)
    bottom = min(img.height, int(round(y1 * scale)) + margin_px)
    return img.crop((left, top, right, bottom))


def _pad_to_ratio(img: Image.Image, ratio: float) -> Image.Image:
    w, h = img.size
    current = w / h
    if abs(current - ratio) < 1e-4:
        return img

    if current > ratio:
        # Image is too wide; increase height.
        new_w = w
        new_h = int(round(w / ratio))
    else:
        # Image is too tall; increase width.
        new_h = h
        new_w = int(round(h * ratio))

    canvas = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    x = (new_w - w) // 2
    y = (new_h - h) // 2
    canvas.paste(img, (x, y))
    return canvas


def _block_text_len(block: dict) -> int:
    text_parts = []
    for line in block.get("lines", []):
        for span in line.get("spans", []):
            text_parts.append(span.get("text", ""))
    return len("".join(text_parts).strip())


def _iter_candidates(page: fitz.Page) -> Iterable[FigureAsset]:
    page_area = page.rect.width * page.rect.height
    blocks = page.get_text("dict").get("blocks", [])
    for idx, block in enumerate(blocks):
        bbox = tuple(float(v) for v in block["bbox"])
        x0, y0, x1, y1 = bbox
        w = int(round(x1 - x0))
        h = int(round(y1 - y0))
        area = w * h

        if block.get("type") == 1:
            # Real image blocks must be materially large; small icons are noise.
            if area < page_area * 0.01 or max(w, h) < 80:
                continue
            yield FigureAsset(
                page_number=page.number + 1,
                index=idx,
                bbox=bbox,
                width=w,
                height=h,
                kind="image",
            )
            continue

        if block.get("type") != 0:
            continue

        text_len = _block_text_len(block)
        # Ignore tiny fragments and decorative page junk.
        if text_len < 80 or area < page_area * 0.015:
            continue

        # Code listings and tables often live in text blocks with moderate width.
        if w < page.rect.width * 0.20 and h < page.rect.height * 0.06:
            continue

        yield FigureAsset(
            page_number=page.number + 1,
            index=idx,
            bbox=bbox,
            width=w,
            height=h,
            kind="text",
            text_len=text_len,
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract high-quality PDF figure crops.")
    parser.add_argument("pdf", help="Input PDF path")
    parser.add_argument("output", help="Output directory")
    parser.add_argument("--dpi", type=int, default=300, help="Render DPI for crops")
    parser.add_argument("--margin", type=int, default=12, help="Pixel margin around each crop")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of figures to write")
    parser.add_argument("--manifest", action="store_true", help="Write a JSON manifest")
    args = parser.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    out_root = Path(args.output).expanduser().resolve()
    page_dir = out_root / "pages"
    raw_dir = out_root / "raw"
    p34_dir = out_root / "p3x4"
    p32_dir = out_root / "p3x2"
    page_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)
    p34_dir.mkdir(parents=True, exist_ok=True)
    p32_dir.mkdir(parents=True, exist_ok=True)

    manifest = []
    written = 0

    doc = fitz.open(pdf_path)
    for page in doc:
        rendered = _render_page(page, args.dpi)
        rendered.save(page_dir / f"p{page.number + 1:02d}.png")

        for asset in _iter_candidates(page):
            if args.limit is not None and written >= args.limit:
                break

            crop = _crop_with_margin(rendered, asset.bbox, args.dpi, args.margin)
            if crop.width == 0 or crop.height == 0:
                continue

            stem = f"p{asset.page_number:02d}_{asset.kind}_{asset.index:02d}"
            raw_path = raw_dir / f"{stem}.png"
            p34_path = p34_dir / f"{stem}_3x4.png"
            p32_path = p32_dir / f"{stem}_3x2.png"

            crop.save(raw_path)
            _pad_to_ratio(crop, 3 / 4).save(p34_path)
            _pad_to_ratio(crop, 3 / 2).save(p32_path)

            manifest.append(
                {
                    "page": asset.page_number,
                    "index": asset.index,
                    "kind": asset.kind,
                    "text_len": asset.text_len,
                    "bbox": [round(v, 2) for v in asset.bbox],
                    "source_size": [asset.width, asset.height],
                    "raw": str(raw_path),
                    "portrait": str(p34_path),
                    "landscape": str(p32_path),
                }
            )
            written += 1
        if args.limit is not None and written >= args.limit:
            break

    if args.manifest:
        with open(out_root / "manifest.json", "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

    print(f"Wrote {written} figure assets to {out_root}")


if __name__ == "__main__":
    main()
