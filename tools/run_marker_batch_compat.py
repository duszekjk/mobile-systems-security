#!/usr/bin/env python3
"""Batch convert PDFs with marker-pdf 0.2.6 using a pdftext compatibility patch."""

import argparse
import os
from pathlib import Path

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
    parser = argparse.ArgumentParser(description="Batch convert PDFs to markdown with marker.")
    parser.add_argument("in_folder", help="Input folder with PDFs.")
    parser.add_argument("out_folder", help="Output folder.")
    parser.add_argument("--max_pages", type=int, default=None, help="Maximum number of pages per PDF.")
    parser.add_argument("--langs", type=str, default=None, help="Languages to use for OCR, comma separated")
    parser.add_argument("--batch_multiplier", type=int, default=2, help="How much to increase batch sizes")
    parser.add_argument("--max_files", type=int, default=None, help="Maximum number of PDFs to convert")
    args = parser.parse_args()

    configure_logging()
    in_folder = Path(args.in_folder).expanduser().resolve()
    out_folder = Path(args.out_folder).expanduser().resolve()
    out_folder.mkdir(parents=True, exist_ok=True)

    langs = args.langs.split(",") if args.langs else None
    files = sorted([p for p in in_folder.iterdir() if p.is_file() and p.suffix.lower() == ".pdf"])
    if args.max_files is not None:
        files = files[: args.max_files]

    model_lst = load_all_models()
    for pdf_path in files:
        print(f"Converting {pdf_path.name}")
        full_text, images, out_meta = convert_single_pdf(
            str(pdf_path),
            model_lst,
            max_pages=args.max_pages,
            langs=langs,
            batch_multiplier=args.batch_multiplier,
        )
        subfolder_path = save_markdown(str(out_folder), pdf_path.name, full_text, images, out_meta)
        print(f"Saved markdown to {subfolder_path}")


if __name__ == "__main__":
    main()
