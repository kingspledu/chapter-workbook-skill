# Text placement and final QA

## Titles and visible frames

Measure the actual generated frame, not its prompt coordinates or whole canvas. Define a safe inner rectangle excluding pig badges, pictograms, ribbon tails, scalloped ends, painted border thickness and shadows. Convert pixel bounds through the actual placed transform. Distinguish top-left layout coordinates, PDF baselines and glyph bounding boxes.

In this theme, target roughly 80-85% title/nameplate width occupancy, with optical breathing room. This is a design target, not a universal hard limit. Measure brand plaque, grade plaque, activity ribbon, Word Bank label and teacher heading separately. Short titles should not remain tiny because another title is long. Never enlarge letters until they touch the painted border.

Compute font size from actual font width AND available height. Center using measured width and ascent/descent or visible glyph bounds. Verify optical vertical alignment in a rendered crop. Exclude the pig badge from the centering area. Center the grade plaque independently; a fixed left coordinate copied from the brand plaque is wrong.

## Body and labels

- Use equal left/right padding. Center note headings; left-align paragraphs in the full safe width. A teacher/parent heading begins BELOW the top padding, not on its box border. Avoid the earlier narrow paragraph column shifted far to the right.
- Word Bank: reserve separate label and word columns. Keep the generated outside pictogram out of the label. Measure column widths and row heights; every word stays inside the actual white room.
- Preserve wording, spelling, punctuation, Korean translation and sentence order. Respect user-supplied explicit line breaks; otherwise wrap from final font/width and share the resulting lines across editions. Reflow whenever a box changes.
- If text does not fit, grow/rearrange the region or redistribute decorative whitespace. Never horizontally compress glyphs, hide overflow, omit words or shrink everything. Preserve useful handwriting rules and answer boxes.
- Reduce dead margins by enlarging useful type, writing space and scene slots, without crowding unrelated rooms. The pilot's 12% exercise expansion and guide-spacing factors were local fixes, not universal constants.
- Match the selected font family in all outputs; use a Korean-capable font. Keep editable text separate until exporting the explicitly flattened edition.

## Final validation

1. Compare all reading paragraphs, banks, cloze prompts, scrambles, options, translations and answers with the reviewed model. Correct the source HTML's known meaning-match ordering issue instead of duplicating it.
2. Check each paragraph against ITS safe inner box, not just the A4 page. Check wrapped block height, row separation, padding, artwork/text intersections and handwriting space.
3. Measure title occupancy and horizontal/vertical offsets against each usable plaque. Use `scripts/audit_pdf_regions.py` with measured rectangles for a reproducible text audit. Report measurements and unresolved failures honestly; page bounds alone do not prove alignment.
4. Inspect every final rendered page at readable size after the last change. Use a contact sheet for consistency and close crops for both header plaques, activity ribbons, Word Bank frames and teacher notes. Look for white seams, grid lines, neighboring-cell fragments, distorted faces and painted edges touching letters. Crop according to actual cell geometry; use an image tool for repainting.
5. Verify one different activity-related main scene per page using the asset map, hashes AND visual review. Different hashes do not alone prove distinct scenes. Check ornament relevance.
6. Reopen the flattened PDF: same A4 count, no text/form widgets, intended image resolution. Check PPTX text/count. Open/import in target apps when available; report unverified imports.

If a previous PDF is locked by an editor, save a new version and link that exact file; do not claim the open older file changed. When asked only to verify, report measurements without silently editing. When asked to fix, complete and inspect the revised output.
