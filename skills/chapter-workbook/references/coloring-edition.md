# Additional black-and-white coloring edition

This is a separate edition of the accepted workbook, with the same reading, vocabulary, activities, questions, Korean translations and answers. Keep the approved color files intact. Use a separate output folder and preserve the common content model; reflow may change line breaks but never wording or sentence order.

## Provider and generation

When this user requests the established coloring workflow, generate the line art in Google Flow. Follow a different provider only when the user asks for that change. Do not silently replace Flow with another generator or label local edge detection, thresholding or grayscale conversion of color illustrations as Flow generation.

Use the actual connected Flow interface or a supported tool. Continue in the user's logged-in session. If authentication or a rights-consent screen blocks progress, explain the exact block and request the needed user action; reuse explicit consent already granted for this same upload/use scope. A skill does not grant new consent. Never claim completed generation from prepared prompts or uploaded references alone.

Upload authorized references and generate independent regions: reusable header/plaque components, 5-column x 5-row ornaments, four 2-column x 2-row scene sheets for a 13-page workbook, and proportioned empty Word Bank frames. The color sheet can guide identity, pose and cell order, but the output must be newly generated clean line art. An isolated replacement plaque is appropriate if the header's new geometry cannot be cropped safely.

Record each reference, exact submitted prompt, provider/model when shown, project URL, result URL/identifier, local file and native pixel size. Download actual completed outputs before composing. Preserve original sheets and provenance privately with the workbook; do not publish references, artwork or signed result URLs in the public skill repository.

## Prompt template

```text
Convert the attached [region / explicit columns and rows] into crisp children's
coloring-book line art. Preserve character identity, expression, pose, important
objects, composition and cell order. Pure black clean continuous contours on
pure white; medium-bold exterior contours and finer interior details. All
interiors remain open white for coloring. White sky, moon, bedding and clothes;
patterns use outline-only checks. No color, gray washes, halftone, shadows,
solid black backgrounds, gradients, crosshatching or paper texture. No words,
letters, numbers, watermark or labels. Complete subjects, safe insets and white
gutters; no objects crossing cells. [For frames: exact object aspect ratio,
empty interior, thin scalloped outline, no motifs within the writing area.]
```

Inspect actual results for missing cells, changed scene order, filled night skies, dense black patches, malformed faces and fragments from adjacent cells. Regenerate unsuitable regions. Split and trim at native resolution without cutting complete outlines. Preserve the page-to-asset meaning map and one different main scene on every page, excluding the reusable header.

## Composition and validation

- Typeset all text, numbering, answer rules and box outlines in black; backgrounds and box fills are white. Keep exact editable type outside generated art. Decorative ornaments retain transparency; white scene/frame interiors are intentional.
- Fit every scene and frame with equal X/Y scale. Measure new plaques and frames independently instead of inheriting color-edition coordinates. A square generation canvas is not the artwork's object ratio.
- A generated near-black JPEG may contain tiny residual chroma. Neutral grayscale color-space normalization AFTER genuine Flow line-art generation is permitted for print preparation; it is not the coloring-generation step. Do not thicken, threshold or destroy antialiased detail as a substitute for generation.
- Compare edition content against the shared reviewed model, including sentence order and answer mapping. `scripts/verify_edition_pair.py` additionally checks PDF page count, page size, per-page character inventory, black text and neutral raster colors; it cannot establish semantic correctness or sentence order.
- Inspect all pages at readable size after the last export, plus close crops of both brand plaques, ribbons, Word Banks and teacher notes. Confirm unique relevant main scenes, intact contours, writing room and no art/text collisions.
- Reopen the flattened edition and verify page count, image-only content and intended rasterization. Final 300dpi export does not make 1024px native artwork higher resolution. State actual source resolution and any unverified application imports.

Deliver separate coloring publishing PDF, 300dpi A4 flattened PDF, editable Canva PPTX/PNG ZIP, and InDesign JSX with only its used linked assets. Keep provenance and validation with the edition. Remove unused color assets or legacy color ZIPs from the coloring delivery package.
