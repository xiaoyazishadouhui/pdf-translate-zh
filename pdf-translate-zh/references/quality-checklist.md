# Translation Quality Checklist

Use this checklist inside `quality-loop.md`. A checked list is not enough while a hard gate remains.

## Source Preparation

- The complete source folder or source set was inventoried recursively.
- Primary sources, supporting sources, duplicates, navigation noise, and out-of-scope content were identified.
- Extraction reading order was checked against representative source pages.
- Broken words, discretionary hyphens, repeated headers/footers, duplicate lines, and OCR corruption were repaired before translation.
- A representative sample passed calibration before bulk translation began.

## Completeness

- Page/section coverage matches the source.
- All headings, paragraphs, bullets, tables, captions, notes, references, and appendices are represented.
- URLs, emails, phone numbers, dates, names, units, scores, credits, and course codes are unchanged unless localization is required.
- Every translated unit is traceable to a source unit.
- Any omitted global or unrelated content has an explicit scope decision.
- Editor-added applicability notes are distinguished from translated source content.

## Language

- Chinese is fluent and professional, not mechanically literal.
- Terminology is consistent across the whole document.
- Acronyms are expanded at first use when helpful, then reused consistently.
- Official institution, degree, program, law, standard, and product names retain their official spelling.
- No accidental semantic substitutions caused by abbreviations.
- Chinese paragraph boundaries follow meaning rather than source line breaks.
- Long sentences are reorganized for Chinese logic without losing conditions.
- Repeated fields use the approved project glossary.
- Context-blind substitutions such as `信用点` or `简体中文` as a language label do not remain.

## Fidelity

- Admission requirements, exclusions, exceptions, deadlines, fees, scores, credits, durations, and language requirements were checked against the source.
- Modal force is preserved: `must`, `may`, `should`, `recommended`, and `not accepted` remain distinct.
- Negation, scope, comparison, cause, condition, and cross-reference relationships are preserved.
- Official names, titles, course codes, legal references, and accreditation statements are correct.
- No inference, summary, or explanation is presented as literal source translation.
- Tables were checked cell by cell.

## Automated Searches

Search translation artifacts for:

```text
undefined
null
HTTP 429
translation failed
翻译失败
错误
mojibake
```

Also search for suspicious source-language fragments. Ignore legitimate proper nouns, course titles, citations, and URLs.

Search for empty units, identical adjacent paragraphs, abnormal repetition, number mismatches, glossary inconsistencies, suspicious language labels, and broken words near boundaries.

## Document QA

- Chinese glyphs render correctly.
- Heading levels are visually distinct and structurally correct.
- Lists wrap beneath item text.
- Tables do not clip, overflow, or use unreadably small text.
- Captions stay near their figures/tables.
- No accidental blank pages or large unexplained gaps.
- Headers, footers, and page numbers are consistent.
- The final file opens and renders successfully.
- Every page of the latest DOCX render was inspected at 100%.
- The rendered page count is plausible.
- The layout matches any user-supplied benchmark in hierarchy, polish, and readability.

## Exit Record

- No hard gate in `quality-loop.md` remains.
- Final score is at least 92/100.
- Completeness is at least 24/25.
- Semantic fidelity is at least 28/30.
- Chinese fluency is at least 18/20.
- The quality record identifies the inspected DOCX and render version.

## Translation Note

Include a restrained note when appropriate:

> 本文件为中文译文。正式申请、法律解释、课程认定或政策执行应以发布机构的最新原文为准。
