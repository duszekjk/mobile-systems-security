"""Runtime compatibility patches for marker-pdf 0.2.6 on pypdfium2 4.29+."""

try:
    import pypdfium2 as pdfium
    import pdftext.extraction as pdftext_extraction
except Exception:
    pdfium = None
    pdftext_extraction = None


if pdfium is not None and pdftext_extraction is not None:
    _orig_load_pdf = pdftext_extraction._load_pdf

    def _patched_load_pdf(pdf, flatten_pdf=False):
        if isinstance(pdf, pdfium.PdfDocument):
            pdf = pdf._input
        return _orig_load_pdf(pdf, flatten_pdf)

    pdftext_extraction._load_pdf = _patched_load_pdf

try:
    import huggingface_hub
except Exception:
    huggingface_hub = None

if huggingface_hub is not None and not hasattr(huggingface_hub, "is_offline_mode"):
    try:
        from huggingface_hub.constants import HF_HUB_OFFLINE
    except Exception:
        HF_HUB_OFFLINE = False

    def _is_offline_mode():
        return bool(HF_HUB_OFFLINE)

    huggingface_hub.is_offline_mode = _is_offline_mode

try:
    import docling_parse.pdf_parser as _docling_pdf_parser
except Exception:
    _docling_pdf_parser = None

if _docling_pdf_parser is not None and not hasattr(_docling_pdf_parser, "DoclingThreadedPdfParser"):
    if hasattr(_docling_pdf_parser, "DoclingPdfParser"):
        _docling_pdf_parser.DoclingThreadedPdfParser = _docling_pdf_parser.DoclingPdfParser

try:
    from docling_parse.pdf_parser import PdfDocument as _DoclingPdfDocument
except Exception:
    _DoclingPdfDocument = None

if _DoclingPdfDocument is not None:
    _orig_get_page = _DoclingPdfDocument.get_page

    def _patched_get_page(
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
        return _orig_get_page(
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

    _DoclingPdfDocument.get_page = _patched_get_page
