# Translation Quality Loop

Use this protocol for every substantial translation and whenever the user supplies a quality benchmark.

## Loop State

Maintain a quality record in the work directory. Record:

- source inventory and expected deliverables;
- document class and chosen translation path;
- glossary version;
- completed checkpoints;
- defects by round and affected unit IDs;
- repairs made and current scores;
- unresolved hard failures;
- final DOCX, render version, and inspected page count.

Keep accepted units stable. Rework only failed units and repeated terminology affected by a glossary change.

## Phase 0: Calibration

Before bulk translation:

1. Select representative samples from every document class.
2. Translate them with the intended workflow.
3. Audit fidelity, fluency, terminology, structure, and layout mapping.
4. Diagnose systemic problems.
5. Update extraction cleanup, segmentation, glossary, prompt, or translation method.
6. Repeat until the sample has no hard failures and scores at least 90/100.

Do not start bulk translation while the sample contains mechanical Chinese, source-order damage, mistranslated labels, or inconsistent core terminology.

## Phase 1: Checkpoint Loop

For each checkpoint:

1. Normalize the source.
2. Translate from the original, not from a previous Chinese draft.
3. Run structural checks.
4. Compare source and translation unit by unit.
5. Record and classify defects.
6. Repair failed units.
7. Recheck repaired units, neighbouring context, and repeated terms.
8. Mark the checkpoint accepted only when all hard gates pass.

Recommended checkpoint sizes:

- short documents: one complete document;
- prose-heavy documents: one section or 3-5 pages;
- repetitive handbooks: 20-40 structured blocks;
- tables: one complete table, never an arbitrary row split.

## Phase 2: Document-Level Loop

After checkpoints are accepted:

1. Compare source and translation inventories.
2. Verify headings, paragraphs, lists, tables, captions, notes, references, appendices, links, and contacts.
3. Run terminology and repeated-field consistency searches.
4. Check every number, date, score, fee, deadline, credit, duration, language label, and eligibility condition.
5. Read the Chinese continuously, not only sentence by sentence.
6. Repair transitions, duplicated explanations, and awkward paragraph boundaries.
7. Re-score the complete translation.

## Phase 3: Visual Loop

1. Build the DOCX from accepted translation.
2. Render the entire current DOCX.
3. Inspect every page at 100%.
4. Record page-specific defects.
5. Repair layout without weakening accepted content.
6. Re-render after layout-sensitive changes.
7. Exit only when every page passes and the inspected render matches the final DOCX.

## Hard Gates

Any item below forces another repair round regardless of score:

- in-scope source content is missing without an explicit scope decision;
- an admission requirement, deadline, fee, score, credit, duration, language, course status, or eligibility condition changes meaning;
- extraction damage remains in the Chinese;
- substantial source-language prose remains untranslated;
- content is fabricated, over-interpreted, or presented as source text when it is editorial guidance;
- terminology changes meaning across sections;
- an API error, placeholder, empty block, duplicate, or corrupted character remains;
- the DOCX cannot open, Chinese glyphs are missing, or any page clips, overlaps, overflows, contains accidental large gaps, or has unreadable tables;
- the output falls materially below a user-supplied benchmark in hierarchy, accuracy, readability, or polish.

## Scoring

| Category | Weight | Passing expectation |
|---|---:|---|
| Completeness | 25 | All in-scope content represented and traceable |
| Semantic fidelity | 30 | Requirements, relationships, qualifications, and nuance preserved |
| Chinese fluency | 20 | Natural professional Chinese without machine cadence |
| Terminology | 10 | Stable glossary and correct official names |
| Structure and usability | 10 | Hierarchy, lists, tables, links, and navigation preserved |
| Visual quality | 5 | Every final page readable and polished |

Exit only when:

- total score is at least 92/100;
- completeness is at least 24/25;
- semantic fidelity is at least 28/30;
- Chinese fluency is at least 18/20;
- no hard failure remains.

A strong user-supplied sample overrides optimistic self-scoring. A materially weaker draft does not pass.

## Defect Routing

| Defect | Repair action |
|---|---|
| Missing or scrambled text | Re-extract, change parser, inspect reading order, or OCR |
| Split words or repeated headers | Normalize source before retranslating |
| Wrong paragraph boundaries | Re-segment from source semantics |
| Wrong meaning | Retranslate the affected unit from the original |
| Mechanical Chinese | Rewrite for Chinese logic, then compare with the source |
| Inconsistent term | Update glossary, search all occurrences, repair globally |
| Wrong number or label | Copy from source and verify neighbouring values |
| Duplicate content | Remove exact duplicate and verify no unique detail is lost |
| Dense or broken table | Rebuild as a readable Chinese table with preserved data |
| Layout failure | Adjust styles, geometry, spacing, or pagination and re-render |

## Loop Limits

- After two rounds with the same systemic defect, change the method instead of repeating the repair.
- After three rounds on one unit, inspect the original visually and translate it manually from scratch.
- If the source is ambiguous or corrupted, record the limitation and use a restrained translator's note.
- Never lower the threshold to finish faster.
- Never restart accepted sections unless a glossary or source interpretation change affects them.
