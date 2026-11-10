---
name: chapter-workbook
description: Build chapter-based early-reader workbooks from supplied books and a workbook reference, with editable publishing sources, A4 flattened PDFs, and Canva import files. Use for chapter reading and spelling workbooks, not generic book summaries.
---

# Chapter workbook

Read [the content contract](references/content-contract.md) before authoring. The content reference controls activities and answers; the design reference controls appearance only. Preserve that separation when references disagree.

1. Inventory supplied PDFs with `scripts/inspect_books.py`. For image-only PDFs, render pages and read them visually or use OCR followed by visual verification. Empty extraction does not mean an empty chapter. Record both physical PDF page numbers and printed page numbers. Confirm chapter start/end before writing questions.
2. Build a chapter evidence ledger: people, setting, event order, motivations, exact vocabulary occurrences and page references. Stop at the chapter boundary. Distinguish source text, an adapted reading, and newly authored practice sentences.
3. Write a reviewed chapter JSON following the contract. Default to the pilot's 13-page activity progression only when the user's content reference matches it. Choose 12 chapter-attested words with varied usefulness and age-appropriate spelling, then derive all word exercises from that single ordered list. Do not force absent vocabulary or a bedtime theme into another chapter.
4. A four-line oral-reading passage may be an actual chapter passage or a newly authored recap. Label a recap as adapted. Never attribute invented words to the book. Write cloze items with a unique intended answer, plausible comprehension distractors, and a bilingual teacher guide whose translation matches its English.
5. Validate each answer against the evidence ledger. Generate matching answers in question order, not definition order. Scrambles must preserve every letter. Keep teacher material after all student pages.
6. Supply authorized `sky.png` and `bed.png` (these are renderer slot names, not mandatory illustration subjects). Use the design reference for palette, hierarchy and mood; do not use its illustrated exercise text as content. Public skill packages must exclude supplied books, chapter readings and proprietary reference artwork.
7. Run `python scripts/render_workbook.py --chapter chapter.json --assets assets --output output`. Install dependencies from the repository requirements. On Windows it uses Trebuchet MS and Malgun Gothic from Windows Fonts; elsewhere set `WORKBOOK_FONT_DIR` to licensed fonts with the required filenames, or adapt the font map.
8. Inspect every rendered page at readable size, including Korean, writing space, teacher answers and illustration crops. The renderer checks bounds and letter sets; it does not verify chapter truth or semantic ambiguity. Revise overlong material or change layout instead of shrinking student text until unreadable.
9. Deliver publishing PDF plus the editable InDesign JSX and linked art, 300dpi image-flattened A4 PDF, editable Canva PPTX and PNG ZIP. InDesign JSX generates INDD and IDML only when run in InDesign. Check font substitutions and overset there. Check PPTX import in Canva when available. Do not claim those application checks without performing them. RGB mockups require printer-specific bleed, color profile and PDF/X mastering before commercial press use.

Publish the reusable skill and tools only when requested; publishing a workbook or source book is a separate action. Report the repository URL and any unverified application handoffs.
