---
name: chapter-workbook
description: Build chapter-based early-reader workbooks from supplied books and a workbook reference, with editable publishing sources, A4 flattened PDFs, and Canva import files. Use for chapter reading and spelling workbooks, not generic book summaries.
---

# Chapter workbook

Read [the content contract](references/content-contract.md) before authoring. The content reference controls activities and answers; the design reference controls appearance only. Preserve that separation when references disagree.

For illustrated workbooks, read [the region/image workflow](references/image-led-layout.md) and [text placement and QA](references/text-layout.md). Compose independent regions with editable type; never generate a continuous full-page painting. The basic renderer below is a typography-first fallback, not an implementation of the illustrated workflow.

For an additional black-and-white coloring edition, read [coloring editions](references/coloring-edition.md). Preserve the color edition, generate genuine coloring line art with the user's chosen provider, and reuse the reviewed content model. For accepted chapters and later-chapter production, read [acceptance and delivery](references/acceptance-delivery.md).

For replacing existing headers or integrating artwork with exterior white padding, read [header revision and crop verification](references/header-revision.md). Preserve fine outline tips, use proportional placement, and verify the final exported text rooms and unchanged body content.

For the canonical 13-page layout extracted from the verified later-chapter editions, read [the workbook template](references/workbook-template-v1.md). Use its room ranges and asset contracts as the starting template; replace chapter content and artwork only after evidence review.

For the fixed main-header appearance, read [the header format contract](references/header-format.md). A new chapter may change only the central story scene and chapter title; the header canvas, plaques, ribbon, badge and edge ornaments must retain the established format.

1. Inventory supplied PDFs with `scripts/inspect_books.py`. For image-only PDFs, render pages and read them visually or use OCR followed by visual verification. Empty extraction does not mean an empty chapter. Record both physical PDF page numbers and printed page numbers. Confirm chapter start/end before writing questions.
2. Build a chapter evidence ledger: people, setting, event order, motivations, exact vocabulary occurrences and page references. Stop at the chapter boundary. Distinguish source text, an adapted reading, and newly authored practice sentences.
3. Write a reviewed chapter JSON following the contract. Default to the pilot's 13-page activity progression only when the user's content reference matches it. Choose 12 chapter-attested words with varied usefulness and age-appropriate spelling, then derive all word exercises from that single ordered list. Do not force absent vocabulary or a bedtime theme into another chapter.
4. A four-line oral-reading passage may be an actual chapter passage or a newly authored recap. Label a recap as adapted. Never attribute invented words to the book. Write cloze items with a unique intended answer, plausible comprehension distractors, and a bilingual teacher guide whose translation matches its English.
5. Validate each answer against the evidence ledger. Generate matching answers in question order, not definition order. Scrambles must preserve every letter. Keep teacher material after all student pages.
6. Build a page-to-asset map: a new chapter-specific header reused only within that chapter, one different content-related main illustration per page, activity-related ornaments and independent empty Word Bank frames. Generate color artwork with Codex's built-in `image_gen`, then use those completed color assets as references for Google Flow coloring line art. In this user's workflow, “이마젠” means Codex image generation, not Google Imagen. Do not generate color in Flow. Use the design reference for appearance only. Exclude supplied books, chapter readings and artwork from public skill packages.
7. For a basic typography-first workbook, run `python scripts/render_workbook.py --chapter chapter.json --assets assets --output output`. For the illustrated workflow, implement the reviewed region plan and asset map; this basic renderer does not reproduce it. Install dependencies from the repository requirements. On Windows the basic renderer uses Trebuchet MS and Malgun Gothic from Windows Fonts; an established illustrated theme may use Comic Sans MS with Malgun Gothic. Use the actual chosen font metrics in every output. Elsewhere provide licensed equivalents and adapt the font map.
8. Inspect every rendered page at readable size. Measure titles against visible inner ribbons excluding badges and scallops; check box containment, padding and art/text collisions, not just A4 bounds. A contact sheet alone is insufficient. The basic renderer does not perform these visual or semantic checks. Adjust regions instead of compressing text.
9. Deliver publishing PDF plus the editable InDesign JSX and linked art, 300dpi image-flattened A4 PDF, editable Canva PPTX and PNG ZIP. InDesign JSX generates INDD and IDML only when run in InDesign. Check font substitutions and overset there. Check PPTX import in Canva when available. Do not claim those application checks without performing them. RGB mockups require printer-specific bleed, color profile and PDF/X mastering before commercial press use.

Publish the reusable skill and tools only when requested; publishing a workbook or source book is a separate action. Report the repository URL and any unverified application handoffs.
