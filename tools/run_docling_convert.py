#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import os
import sys


def patch_docling_compat() -> None:
    try:
        import huggingface_hub
    except Exception:
        huggingface_hub = None

    if huggingface_hub is not None and not hasattr(huggingface_hub, "is_offline_mode"):
        huggingface_hub.is_offline_mode = lambda: False

    import docling_parse.pdf_parser as pdf_parser
    import docling_parse.pdf_parsers as pdf_parsers
    from docling_core.types.doc.page import SegmentedPdfPage

    if not hasattr(pdf_parsers, "DecodePageConfig"):
        @dataclass
        class DecodePageConfig:
            keep_char_cells: bool = False
            keep_shapes: bool = False
            keep_bitmaps: bool = True
            create_word_cells: bool = True
            create_line_cells: bool = True
            enforce_same_font: bool = True
            materialize_bitmap_bytes: bool = False
            release_native_memory_every_n_pages: int | None = None

        pdf_parsers.DecodePageConfig = DecodePageConfig

    if not hasattr(pdf_parser, "RenderConfig"):
        @dataclass
        class RenderConfig:
            scale: float = 1.0

        pdf_parser.RenderConfig = RenderConfig

    if not hasattr(pdf_parser, "ThreadedPdfParserConfig"):
        @dataclass
        class ThreadedPdfParserConfig:
            loglevel: str = "fatal"
            threads: int = 4
            render_config: object = None

        pdf_parser.ThreadedPdfParserConfig = ThreadedPdfParserConfig

    if not hasattr(pdf_parser, "PageParseResult"):
        @dataclass
        class PageParseResult:
            page_number: int
            success: bool
            page_width: float
            page_height: float
            _seg_page: SegmentedPdfPage

            def get_page(self):
                return self._seg_page

            def get_image(self, scale=1, cropbox=None):
                return self._seg_page.render_as_image(cell_unit=None)

        pdf_parser.PageParseResult = PageParseResult

    if not hasattr(pdf_parser, "DoclingThreadedPdfParser"):
        class DoclingThreadedPdfParser:
            def __init__(self, parser_config=None, decode_config=None):
                self._parser = pdf_parser.DoclingPdfParser(
                    loglevel=getattr(parser_config, "loglevel", "fatal")
                    if parser_config
                    else "fatal"
                )
                self._doc = None

            def load(self, path_or_stream, password=None, page_numbers=None):
                self._doc = self._parser.load(path_or_stream, password=password)
                return "doc"

            def page_count(self, doc_key):
                return self._doc.number_of_pages()

            def iterate_results(self):
                for page_number, seg_page in self._doc.iterate_pages():
                    yield pdf_parser.PageParseResult(
                        page_number=page_number,
                        success=True,
                        page_width=seg_page.dimension.rect.width,
                        page_height=seg_page.dimension.rect.height,
                        _seg_page=seg_page,
                    )

            def unload(self, doc_key):
                if self._doc is not None:
                    self._doc.unload()

        pdf_parser.DoclingThreadedPdfParser = DoclingThreadedPdfParser

    if hasattr(pdf_parser, "PdfDocument"):
        orig_get_page = pdf_parser.PdfDocument.get_page

        def patched_get_page(
            self,
            page_no,
            *,
            keep_chars=True,
            keep_lines=True,
            keep_bitmaps=True,
            create_words=True,
            create_textlines=True,
            enforce_same_font=True,
            do_sanitization=False,
            config=None,
        ):
            if config is not None:
                keep_chars = getattr(config, "keep_char_cells", keep_chars)
                keep_lines = getattr(config, "keep_lines", keep_lines)
                keep_bitmaps = getattr(config, "keep_bitmaps", keep_bitmaps)
                create_words = getattr(config, "create_word_cells", create_words)
                create_textlines = getattr(config, "create_line_cells", create_textlines)
                enforce_same_font = getattr(
                    config, "enforce_same_font", enforce_same_font
                )
                do_sanitization = getattr(config, "do_sanitization", do_sanitization)
            return orig_get_page(
                self,
                page_no,
                keep_chars=keep_chars,
                keep_lines=keep_lines,
                keep_bitmaps=keep_bitmaps,
                create_words=create_words,
                create_textlines=create_textlines,
                enforce_same_font=enforce_same_font,
                do_sanitization=do_sanitization,
            )

        pdf_parser.PdfDocument.get_page = patched_get_page


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path.home() / ".cache" / "docling" / "models",
    )
    parser.add_argument("--no-tables", action="store_true")
    parser.add_argument("--ocr", action="store_true")
    parser.add_argument("--export-images", action="store_true")
    parser.add_argument("--images-scale", type=float, default=5.0)
    args = parser.parse_args()

    mpl_cache = Path("/private/tmp/docling-mplconfig")
    mpl_cache.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("MPLCONFIGDIR", str(mpl_cache))
    os.environ.setdefault("XDG_CACHE_HOME", "/private/tmp/docling-cache")

    patch_docling_compat()

    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions

    args.out_dir.mkdir(parents=True, exist_ok=True)

    opts = PdfPipelineOptions(
        generate_page_images=True,
        generate_picture_images=True,
        do_picture_classification=False,
        do_picture_description=False,
        do_ocr=args.ocr,
        do_table_structure=not args.no_tables,
        images_scale=args.images_scale,
        artifacts_path=args.cache_dir,
    )

    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )
    result = converter.convert(args.pdf)
    md = result.document.export_to_markdown()
    (args.out_dir / f"{args.pdf.stem}.md").write_text(md)
    if args.export_images:
        pages_dir = args.out_dir / "pages"
        pics_dir = args.out_dir / "pictures"
        pages_dir.mkdir(parents=True, exist_ok=True)
        pics_dir.mkdir(parents=True, exist_ok=True)
        for page_no, page in result.document.pages.items():
            page.image.pil_image.save(pages_dir / f"page-{page_no:03}.png")
        for idx, picture in enumerate(result.document.pictures, start=1):
            picture.get_image(result.document).save(pics_dir / f"picture-{idx:03}.png")
    print(f"status={result.status}")
    print(f"markdown_chars={len(md)}")
    print(f"out_dir={args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
