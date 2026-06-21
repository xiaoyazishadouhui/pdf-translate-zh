---
name: pdf-translate-zh
description: Translate complete PDFs, saved webpages, and collected document folders into polished Simplified Chinese DOCX files while preserving headings, lists, tables, citations, links, contact details, and document hierarchy. Use when the user asks to translate a PDF, report, brochure, handbook, academic programme, admissions folder, policy, manual, or other long document into Chinese; requests a Chinese Word version; says “全文翻译”, “翻译这个PDF”, “把收集到的资料全部翻译出来”, “翻译成中文文档”; supplies a quality sample; or wants iterative translation review, layout reconstruction, and visual QA rather than a summary.
---

# PDF 全文中文翻译

Produce a complete Chinese translation, not a summary. Deliver a visually verified `.docx` unless the user explicitly requests another format.

## Required Companion Skill

Use the `documents` skill for DOCX design, rendering, and visual QA. Read its instructions before creating the final document.

## Python Runtime

- Resolve the bundled workspace dependencies before running the helper scripts.
- Prefer the bundled Python executable because it includes `pypdf` and `python-docx`.
- Before starting a long job, run both scripts with `--help` using the selected Python executable.
- If a custom Python is required, verify `import pypdf, docx` first. Do not install packages silently.

## Core Operating Principle

Treat translation as a controlled quality loop, not a one-pass pipeline:

`inspect -> classify -> calibrate -> translate -> audit -> repair -> re-audit -> render -> visual repair`

Read `references/execution-loop.md` and `references/quality-loop.md` before translating. Run the execution loop first: every working turn must advance a concrete artifact or produce a real blocker. A draft may leave the quality loop only when every hard gate passes.

## Anti-Stall Execution Gate

- After a progress update, call a task tool in the same turn. Do not end the turn with a promise to act later.
- Count only files, saved checkpoints, command results, render images, QA findings, or explicit errors as progress.
- If no new verifiable result exists, do not send another progress update.
- Treat “继续”, “continue”, or equivalent messages as an instruction to resume immediately from the latest checkpoint. Do not restate the plan.
- Do not ask the user to keep authorizing ordinary next steps. Continue through translation, DOCX generation, rendering, and repair unless a genuine external decision or permission is required.
- Create the first tangible draft early. Quality review improves an existing artifact; it must not indefinitely delay artifact creation.
- If two consecutive working turns produce no artifact or diagnostic result, declare an execution stall internally and apply the recovery procedure in `execution-loop.md`.

## Workflow

1. Inventory and inspect the complete source set.
   - Recursively inventory every relevant PDF, saved webpage, DOCX, spreadsheet, appendix, and README when the user refers to a folder, programme, or collected materials.
   - Identify primary sources, supporting sources, duplicates, navigation noise, and unrelated global information.
   - Define the deliverable map before writing: one translation per source, one integrated guide, or both.
   - Use bundled workspace `pdfinfo` when available.
   - Render representative source pages to understand layout. Do not use contact sheets as a substitute for final page-by-page QA.
   - Run `PYTHON scripts/extract_pdf.py INPUT --out WORKDIR` with the verified Python runtime.
   - If many pages have little extractable text, treat them as scans and OCR before translation.
   - Record file count, page count, source language, document type, extraction quality, tables, figures, links, and likely applicability.
   - Create or update the execution state record defined in `references/execution-loop.md`.

2. Classify the translation path.
   - `short-form`: brochures, one-page requirements, notices, and documents with limited prose. Translate directly and reconstruct deliberately.
   - `long-form structured`: module handbooks, policies, catalogues, and reports with repeated fields. Normalize extraction, build a glossary, and translate in resumable sections.
   - `mixed-source guide`: multiple official webpages and files describing one programme. Translate all applicable content, remove navigation noise and exact duplicates, and distinguish source translation from editor-added applicability notes.
   - `scan-heavy`: OCR first, then manually verify names, numbers, formulas, tables, and broken characters.
   - Do not force all documents in a batch through one method merely because they share a folder.

3. Plan the output and terminology.
   - Preserve title, metadata, section hierarchy, numbered/bulleted lists, tables, footnotes, URLs, emails, phone numbers, dates, credits, units, and language markers.
   - Rebuild dense landscape diagrams or matrices as readable Chinese tables when literal reproduction would be illegible.
   - State clearly when a figure is summarized or structurally rebuilt.
   - Create a project glossary before bulk translation. Include programme names, degrees, tracks, course categories, admissions terms, recurring technical terms, and terms that must remain in the source language.
   - Separate translation from interpretation. Label editor-added notes such as “适用于中国申请人”; never present an inference as quoted source text.
   - For time-sensitive admissions information, retain the source or verification date and state that the current official page controls.

4. Calibrate on a representative sample.
   - Translate one representative section from each document class before processing the full batch.
   - Include prose, a list or repeated field, and a difficult element such as a table, eligibility rule, or technical paragraph.
   - Audit the sample with `references/quality-checklist.md`.
   - Fix glossary choices, segmentation, tone, and layout mapping before scaling up. Do not bulk-produce known-bad prose.
   - Time-box calibration to the minimum representative sample. Once it passes, immediately create the first output artifact or saved translation checkpoint.

5. Translate in checkpoints.
   - Translate page-by-page or section-by-section.
   - Save every completed unit immediately into `translation.json`.
   - Resume from existing translated units; never restart a long document unnecessarily.
   - Translate with the model directly. External translation APIs are optional accelerators only, never the sole path.
   - Treat API output as a draft requiring source-aware review.
   - Normalize extraction artifacts before translation: repair discretionary hyphenation, repeated headers/footers, broken lines, split words, duplicated text, and reading-order errors.
   - Preserve a stable link between source and translated units so failed passages can be repaired without retranslating accepted content.
   - After each checkpoint, check for empty units, duplicates, untranslated prose, altered numbers, and API/error strings.
   - For documents over 15 pages, create the output shell early so the task always produces a tangible artifact.
   - Update the execution state after every accepted checkpoint. Never rely on conversational memory as the only record of progress.

6. Run the language and fidelity quality loop.
   - Apply `references/quality-loop.md` and `references/quality-checklist.md`.
   - Score completeness, fidelity, Chinese fluency, terminology, structure, and usability after each round.
   - Let hard failures override numeric scores.
   - Route each defect to its cause:
     - extraction defect -> re-extract or OCR;
     - segmentation defect -> re-segment from source;
     - terminology defect -> update glossary and propagate consistently;
     - semantic defect -> retranslate from the original passage;
     - fluency defect -> rewrite in Chinese and recheck the source;
     - structural defect -> rebuild the affected list, table, caption, or hierarchy.
   - Re-audit repaired units, neighbouring context, and repeated occurrences of changed terminology.
   - Stop only when every hard gate passes and the score reaches the threshold in `quality-loop.md`.
   - Keep acronyms such as OEM, ECTS, CP, ISO, and official program names where useful.
   - Preserve proper nouns and contact details exactly.
   - Search for broken words, untranslated prose, mojibake, accidental term substitutions, duplicated lines, and API error text.
   - Prefer natural professional Chinese over rigid word-for-word syntax.

7. Build the DOCX.
   - Prepare JSON in the schema documented by `scripts/build_docx.py --help`.
   - Run `PYTHON scripts/build_docx.py TRANSLATION_JSON OUTPUT.docx` with the same verified Python runtime.
   - Use A4 for source PDFs that are A4; otherwise preserve the source paper size when practical.
   - Use real Word headings, lists, tables, headers, footers, and page numbers.
   - Match an approved sample when the user supplies one. Treat its hierarchy, typography, spacing, table density, and editorial polish as acceptance criteria.
   - Do not let extracted source line breaks dictate Chinese paragraph breaks.

8. Run a separate visual quality loop.
   - Render with the `documents` skill `render_docx.py`.
   - Inspect every page image at 100%.
   - Fix missing Chinese glyphs, clipping, table overflow, awkward page breaks, oversized gaps, and header/footer errors.
   - Re-render after any layout-sensitive fix.
   - Prefer style, spacing, table geometry, pagination, or controlled paragraph adjustments over rewriting accepted content to solve layout.
   - Repeat until every page passes and the inspected render matches the latest DOCX.

9. Organize and deliver.
   - Keep each original and its translation in the same programme folder when the user requests paired organization.
   - Return only the final requested document unless the user asks for intermediates.
   - Mention output file count, page count, quality-loop result, and that every final page was inspected.
   - If OCR or rendering could not be completed, disclose that limitation explicitly.

## Non-Negotiable Rules

- Do not silently omit pages, tables, captions, references, appendices, or contact information.
- Do not call a summary a translation.
- Do not translate a global page wholesale when only one country or programme entry is applicable without explaining the scope decision.
- Do not disguise editorial synthesis as literal translation.
- Do not accept bulk machine translation without source-aware review.
- Do not continue bulk translation after the calibration sample reveals systemic defects.
- Do not wait indefinitely for a translation API; continue with model translation.
- Do not provide repeated progress messages without producing files or saved checkpoints.
- Do not use planning, calibration, self-assessment, or status reporting as a reason to postpone the first draft.
- Do not require repeated “continue” messages to carry out already-authorized work.
- Do not claim completion before the final DOCX exists, all quality hard gates pass, and its latest render has been inspected page by page.
