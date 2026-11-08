#!/usr/bin/env python3
"""Run marker-pdf with a compatibility patch for older pdftext/pypdfium2 combos."""

import argparse
import os

import pypdfium2 as pdfium
import pdftext.extraction as pdftext_extraction


_orig_load_pdf = pdftext_extraction._load_pdf


def _patched_load_pdf(pdf, flatten_pdf=False):
    if isinstance(pdf, pdfium.PdfDocument):
        pdf = pdf._input
    return _orig_load_pdf(pdf, flatten_pdf)


pdftext_extraction._load_pdf = _patched_load_pdf

from marker.convert import convert_single_pdf  # noqa: E402
from marker.logger import configure_logging  # noqa: E402
from marker.models import load_all_models  # noqa: E402
from marker.output import save_markdown  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert one PDF to markdown with marker.")
    parser.add_argument("filename", help="PDF file to parse")
    parser.add_argument("output", help="Output base folder path")
    parser.add_argument("--max_pages", type=int, default=None, help="Maximum number of pages to parse")
    parser.add_argument("--langs", type=str, default=None, help="Languages to use for OCR, comma separated")
    parser.add_argument("--batch_multiplier", type=int, default=2, help="How much to increase batch sizes")
    args = parser.parse_args()

    configure_logging()
    langs = args.langs.split(",") if args.langs else None

    model_lst = load_all_models()
    full_text, images, out_meta = convert_single_pdf(
        args.filename,
        model_lst,
        max_pages=args.max_pages,
        langs=langs,
        batch_multiplier=args.batch_multiplier,
    )

    fname = os.path.basename(args.filename)
    subfolder_path = save_markdown(args.output, fname, full_text, images, out_meta)
    print(f"Saved markdown to the {subfolder_path} folder")


if __name__ == "__main__":
    main()
