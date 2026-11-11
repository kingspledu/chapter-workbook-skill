# Workbook template v1

This is the generic layout contract extracted from a verified set of repeated early-reader workbook chapters. It contains no project text, images or private paths.

## Fixed document contract

- 13 pages per chapter edition.
- A4 page: 595.276 × 841.89 pt.
- Editable publishing PDF and InDesign JSX; image-only 300 dpi A4 PDF; Canva PPTX and PNG ZIP.
- Comic Sans MS (or a licensed metric-compatible substitute) for English display/body text; a Korean-capable font for translations.
- Color and coloring editions use the same reviewed `chapter.json`, ordered text records and page map.

## Page roles

1. Adapted chapter reading and word hunt.
2. Spelling practice.
3–4. Context cloze with two six-word banks.
5. Scrambled words.
6. Match the meanings.
7. Comprehension check.
8. Oral reading.
9. Passage cloze with a six-token bank.
10. Dictation/spelling test.
11–12. Bilingual teacher guides.
13. Answer key.

Every page has one chapter header reused within that chapter, one different activity-related main illustration, and relevant transparent ornaments. The header scene changes between chapters; page rooms and roles remain stable.

## Room ranges and transforms

Treat these as room ranges, not instructions to stretch an asset:

| Room | Starting bounds | Rule |
|---|---:|---|
| Header | x 0–595.276, y 0–151 pt | Measure each generated plaque and fit text independently. |
| Small activity scene | roughly x 360–580, y 585–796 pt | Preserve the scene's aspect ratio; center within the available room. |
| Answer-key scene | roughly x 325–565, y 345–482 pt | Preserve the scene's aspect ratio. |
| Word Bank frame | roughly x 22–573, y 196–292 pt | Use an independently generated 1-column × 4-row frame cell. |
| Word Bank label | roughly x 43, y 211 pt | Keep the label outside the frame and away from its pictogram. |
| Ornaments | roughly 22–30 pt | Transparent PNG; place in free rooms only. |

The repeated editions showed Word Bank frame placements around 551 × 95 pt. The native frame ratio must be measured before placement; approximately 3.94:1 is a useful starting measurement for this theme. If the generated cell differs, fit it with equal X/Y scale and adjust the room rather than stretching the frame.

## Asset contracts

- Header: one new chapter-specific color asset from Codex built-in `image_gen`; reuse only within its chapter.
- Main illustrations: four 2×2 sheets for 13 distinct page scenes. Cells are split at native geometry and assigned semantically in `page-asset-map.json`.
- Small ornaments: one 5×5 sheet with transparent corners and no labels.
- Word Banks: one 1×4 horizontal frame sheet; state explicitly that “1×4” means one column and four stacked horizontal cells.
- Coloring edition: generate line art in Google Flow from the completed color references. Do not substitute grayscale conversion for Flow generation.
- Generated art contains no typeset words, labels, pseudo-text, numbers, answer marks or watermarks. Typeset all workbook wording afterward.

## Typography and QA

- Measure each generated plaque's safe inner rectangle after crop and placement. Exclude borders, scallops, badges and pictograms.
- Fit titles from actual font width and glyph height. Center brand, grade and activity title independently. Preserve visible padding.
- Compare body wording, punctuation, line order, questions, answers and Korean translations against the reviewed chapter model.
- Verify every Word Bank word lies inside its actual white interior. Check frame ratio, crop, placement and text containment in a rendered close crop.
- Verify one distinct relevant scene per page, no art/text collision, and no white/black matte around transparent ornaments.
- Reopen the flattened PDF: 13 A4 pages, image-only, 2481 × 3508 pixel page raster, no widgets or text layer.
- Re-render and inspect all pages after the last asset or geometry change. Do not validate a stale editor tab or pre-change export.

The template defines layout and production decisions. It does not authorize copying another chapter's story, vocabulary, scene, header bitmap or private provenance.
