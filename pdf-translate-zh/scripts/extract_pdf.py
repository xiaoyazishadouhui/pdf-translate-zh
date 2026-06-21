#!/usr/bin/env python3
"""Extract PDF text page-by-page and flag pages that likely require OCR."""

import argparse
import json
from pathlib import Path

PYPDF_IMPORT_ERROR = None
try:
    from pypdf import PdfReader
except ModuleNotFoundError as exc:
    PYPDF_IMPORT_ERROR = exc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf")
    parser.add_argument("--out", required=True, help="Writable output directory")
    parser.add_argument(
        "--min-chars",
        type=int,
        default=80,
        help="Pages below this extracted character count are flagged for OCR",
    )
    args = parser.parse_args()
    if PYPDF_IMPORT_ERROR is not None:
        parser.error(
            "missing dependency 'pypdf'; use the bundled workspace Python "
            "or install pypdf in the selected environment"
        )

    source = Path(args.input_pdf).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(source))
    pages = []
    for index, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").replace("\x00", "").strip()
        pages.append(
            {
                "page": index,
                "source_text": text,
                "needs_ocr": len(text) < args.min_chars,
                "translated_paragraphs": [],
            }
        )

    payload = {
        "source_pdf": str(source),
        "page_count": len(pages),
        "pages": pages,
    }
    json_path = out / "translation.json"
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out / "source.txt").write_text(
        "\n\n".join(
            f"===== PAGE {p['page']} =====\n{p['source_text']}" for p in pages
        ),
        encoding="utf-8",
    )
    print(json_path)
    print(
        f"pages={len(pages)} ocr_candidates="
        f"{sum(1 for page in pages if page['needs_ocr'])}"
    )


if __name__ == "__main__":
    main()
