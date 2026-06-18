---
name: pdf-translate-zh
description: Translate complete PDF documents into polished Simplified Chinese DOCX files while preserving headings, lists, tables, citations, links, contact details, and document hierarchy. Use when the user asks to translate a PDF, report, brochure, handbook, academic program document, policy, manual, or other long document into Chinese; requests a Chinese Word version; says “全文翻译”, “翻译这个PDF”, “翻译成中文文档”, or wants layout reconstruction and visual QA rather than a summary.
---

# PDF 全文中文翻译

Produce a complete Chinese translation, not a summary. Deliver a visually verified `.docx` unless the user explicitly requests another format.

## Required Companion Skill

Use the `documents` skill for DOCX design, rendering, and visual QA. Read its instructions before creating the final document.

## Workflow

1. Inspect the PDF.
   - Use bundled workspace `pdfinfo` when available.
   - Render contact sheets or representative pages to understand layout.
   - Run `scripts/extract_pdf.py INPUT --out WORKDIR`.
   - If many pages have little extractable text, treat them as scans and OCR before translation.

2. Plan the output.
   - Preserve title, metadata, section hierarchy, numbered/bulleted lists, tables, footnotes, URLs, emails, phone numbers, dates, credits, units, and language markers.
   - Rebuild dense landscape diagrams or matrices as readable Chinese tables when literal reproduction would be illegible.
   - State clearly when a figure is summarized or structurally rebuilt.

3. Translate in checkpoints.
   - Translate page-by-page or section-by-section.
   - Save every completed unit immediately into `translation.json`.
   - Resume from existing translated units; never restart a long document unnecessarily.
   - Translate with the model directly. External translation APIs are optional accelerators only, never the sole path.
   - For documents over 15 pages, create the output shell early so the task always produces a tangible artifact.

4. Review the language.
   - Apply `references/quality-checklist.md`.
   - Keep acronyms such as OEM, ECTS, CP, ISO, and official program names where useful.
   - Preserve proper nouns and contact details exactly.
   - Search for broken words, untranslated prose, mojibake, accidental term substitutions, duplicated lines, and API error text.
   - Prefer natural professional Chinese over rigid word-for-word syntax.

5. Build the DOCX.
   - Prepare JSON in the schema documented by `scripts/build_docx.py --help`.
   - Run `scripts/build_docx.py TRANSLATION_JSON OUTPUT.docx`.
   - Use A4 for source PDFs that are A4; otherwise preserve the source paper size when practical.
   - Use real Word headings, lists, tables, headers, footers, and page numbers.

6. Render and inspect.
   - Render with the `documents` skill `render_docx.py`.
   - Inspect every page image at 100%.
   - Fix missing Chinese glyphs, clipping, table overflow, awkward page breaks, oversized gaps, and header/footer errors.
   - Re-render after any layout-sensitive fix.

7. Deliver.
   - Return only the final requested document unless the user asks for intermediates.
   - Mention the output page count and that visual QA was completed.
   - If OCR or rendering could not be completed, disclose that limitation explicitly.

## Non-Negotiable Rules

- Do not silently omit pages, tables, captions, references, appendices, or contact information.
- Do not call a summary a translation.
- Do not wait indefinitely for a translation API; continue with model translation.
- Do not provide repeated progress messages without producing files or saved checkpoints.
- Do not claim completion before the final DOCX exists and its latest render has been inspected.
