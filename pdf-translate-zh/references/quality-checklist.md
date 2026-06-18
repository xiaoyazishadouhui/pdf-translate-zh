# Translation Quality Checklist

## Completeness

- Page/section coverage matches the source.
- All headings, paragraphs, bullets, tables, captions, notes, references, and appendices are represented.
- URLs, emails, phone numbers, dates, names, units, scores, credits, and course codes are unchanged unless localization is required.

## Language

- Chinese is fluent and professional, not mechanically literal.
- Terminology is consistent across the whole document.
- Acronyms are expanded at first use when helpful, then reused consistently.
- Official institution, degree, program, law, standard, and product names retain their official spelling.
- No accidental semantic substitutions caused by abbreviations.

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

## Document QA

- Chinese glyphs render correctly.
- Heading levels are visually distinct and structurally correct.
- Lists wrap beneath item text.
- Tables do not clip, overflow, or use unreadably small text.
- Captions stay near their figures/tables.
- No accidental blank pages or large unexplained gaps.
- Headers, footers, and page numbers are consistent.
- The final file opens and renders successfully.

## Translation Note

Include a restrained note when appropriate:

> 本文件为中文译文。正式申请、法律解释、课程认定或政策执行应以发布机构的最新原文为准。
