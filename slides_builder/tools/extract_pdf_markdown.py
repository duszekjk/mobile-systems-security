#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from collections import defaultdict
from pathlib import Path


def run(cmd: list[str]) -> str:
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout


def parse_pdfimages_list(output: str) -> dict[int, list[tuple[int, str, str]]]:
    page_map: dict[int, list[tuple[int, str, str]]] = defaultdict(list)
    lines = [line for line in output.splitlines() if line.strip()]
    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 3:
            continue
        if not parts[0].isdigit() or not parts[1].isdigit():
            continue
        page = int(parts[0])
        num = int(parts[1])
        kind = parts[2]
        page_map[page].append((num, kind, line))
    return page_map


def find_extracted_file(prefix: Path, num: int) -> Path | None:
    candidates = []
    stem = f"{prefix.name}-{num:03d}"
    for match in prefix.parent.glob(f"{stem}.*"):
        if match.is_file():
            candidates.append(match)
    if not candidates:
        return None
    candidates.sort()
    return candidates[0]


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract readable markdown and image references from a PDF.")
    ap.add_argument("--pdf", required=True, help="Path to the source PDF.")
    ap.add_argument("--out-dir", required=True, help="Root output directory for markdown and extracted images.")
    args = ap.parse_args()

    pdf = Path(args.pdf).resolve()
    out_dir = Path(args.out_dir).resolve()
    markdown_dir = out_dir / "markdown"
    images_dir = out_dir / "pdfimages" / pdf.stem
    markdown_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    text = run(["pdftotext", "-layout", str(pdf), "-"])
    images_list = run(["pdfimages", "-list", str(pdf)])
    page_map = parse_pdfimages_list(images_list)

    prefix = images_dir / pdf.stem
    subprocess.run(["pdfimages", "-all", str(pdf), str(prefix)], check=True)

    pages = text.split("\f")
    md_path = markdown_dir / f"{pdf.stem}.md"
    with md_path.open("w", encoding="utf-8") as fh:
        fh.write(f"# {pdf.stem}\n\n")
        fh.write(f"Źródło: `{pdf.name}`\n\n")
        for page_no, page_text in enumerate(pages, start=1):
            page_text = page_text.strip()
            if not page_text and page_no > len(pages):
                continue
            fh.write(f"## Strona {page_no}\n\n")
            if page_text:
                fh.write(page_text)
                fh.write("\n\n")

            entries = page_map.get(page_no, [])
            image_entries = [entry for entry in entries if entry[1] == "image"]
            smask_entries = [entry for entry in entries if entry[1] == "smask"]
            if image_entries or smask_entries:
                fh.write("### Obrazy na stronie\n\n")
                for num, kind, _line in entries:
                    extracted = find_extracted_file(prefix, num)
                    if extracted is None:
                        fh.write(f"- `{kind}` obiekt {num}\n")
                    else:
                        rel = extracted.relative_to(out_dir)
                        fh.write(f"- `{kind}` obiekt {num}: ![{kind} strona {page_no} obiekt {num}]({rel.as_posix()})\n")
                fh.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
