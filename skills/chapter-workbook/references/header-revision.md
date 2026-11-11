# Header replacement, cropping and verification

Use for a scoped header revision or generated art with exterior blank padding. This supplements the region, typography and coloring workflows; it does not expand a header-only request to body illustrations.

## Source and generation

Check the original chapter text AND illustrations for place, action, characters, props and palette before drafting the header prompt. A story continuing at night can show a brightly colored interior or green garden without decorative moons and stars. Neither a default night panorama nor invented daylight is appropriate. Reuse character identity across chapters while making each chapter's complete header distinct. Within a chapter the header may repeat with different editable activity titles.

Generate color with Codex built-in `image_gen`; generate the matching coloring header in Google Flow using the approved final color asset. Verify the actual reference selected in Flow and the meaning of the downloaded result. Keep wrong-chapter, superseded and rejected results out of delivery packages.

When a generator lacks the required ultrawide aspect ratio, paste the completed color header unaltered onto a white canvas of a supported ratio. Record the source size, padding and placement. In the Flow prompt explicitly reserve the outer white bands, preserve the shallow header ratio and complete left/right subjects, and request empty enclosed text plaques. Reject vertically expanded or altered compositions rather than stretching them back.

## Exterior-only crop

1. Keep the native generated original. Identify the illustrated band from row-wise foreground coverage, then extend it to include isolated fine contours. A dense-row threshold alone can miss a thin bedpost, whisker or border tip.
2. Distinguish exterior blank padding from intentional white plaque/scene interiors. Do not remove connected white rooms or treat every white pixel as transparent. Preserve existing alpha for transparent ornaments.
3. Record the native-pixel crop rectangle `[left, top, right, bottom]`, cropped dimensions and final placement transform. Remove lateral margins only when independently verified empty; a full-width crop is appropriate when artwork reaches the left/right edges.
4. Check discarded bands for meaningful foreground pixels. In the recent clean RGB/line-art workflow, a channel minimum below 225/255 caught fine dark tips missed by the dense-band detector; this is a configurable diagnostic, not a universal threshold for textured/color references. Inspect near-white paint and antialiased edges visually. Extend the crop and leave a small safe inset when in doubt.
5. Fit with one scale: `scale = min(room_width / crop_width, room_height / crop_height)`. Apply the same scale on both axes and center within the intended room. Never force the artwork to fill both dimensions independently.

## Re-measure and typeset

Find the actual empty brand plaque, grade plaque and activity ribbon in each cropped image. Measure color and Flow assets separately. Flood-filled white rooms can assist with enclosed line-art plaques, but check that the detected room has not leaked into the outside background. Convert each measured inner room through the crop and placement transform; inset from outlines, scallops and badges.

Fit exact editable wording using the real output font's width AND glyph height. Center each label independently, including the vertical baseline correction. Make long and short titles readable with optical padding. Do not copy one chapter's coordinates or font size into another generated frame. Recent title fits used about 93% of an already inset safe rectangle; brand/grade fits used about 86%. These are local starting points, not compulsory occupancy targets. The visible outer plaque always retains breathing room.

## Verify the saved exports

- Wait for every exporter to finish and close all PDF handles before rebuilding or validating. Reopen the final files, not stale editor tabs.
- Assert equal X/Y scale, retained foreground at crop boundaries, correct chapter-to-header assignment, text-span containment in each of the three measured rooms and no overlap with the instruction/name area. Audit every activity title on every worksheet, including guides and answer keys.
- Render every changed header at readable size and review each one. Check representative full pages as well. For a new complete workbook, inspect every full page under the normal workflow. A header-only revision can prove untouched bodies through unchanged drawing records, exact wording/order and rendered comparisons; state the actual comparison region.
- Compare unchanged body records and content with the baseline. For pixel comparison, start below the full old header bitmap, including its white padding, rather than below only its painted band. Verify any intervening instruction/name rows separately. Record the actual boundary; the recent workbook used y=185 pt, not a universal value.
- Use fresh PDF document handles per page if a renderer produces cross-page image-mask cache differences. Investigate differences with bounding boxes and actual rendered crops; do not loosen tolerances or declare a pass to conceal a mismatch.
- Verify publishing and flattened PDFs have matching A4 counts; flattened pages are image-only at the intended raster size with no text/widgets. Check editable PPTX slide count and black text/neutral artwork in the coloring edition. Native source resolution remains distinct from final 300dpi rasterization.
- Save crop geometry, per-page text audits, visual proof and a validation report with the project. Verify accepted-chapter and original-export hashes remain unchanged. Regenerate all delivery forms after the final asset change.

For multi-chapter delivery, retain each chapter/edition's publishing PDF, flattened PDF, Canva PNG ZIP and editable package. An ordered combined PDF and a color/line-art comparison preview make review easier. Package only used final assets and private provenance; exclude obsolete candidates. Keep application imports marked unverified until actually tested in InDesign/Canva. Public skill updates contain these generic rules and tools, never workbook art, chapter prose, private paths or signed URLs.
