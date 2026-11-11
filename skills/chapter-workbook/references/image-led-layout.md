# Independent regions and atlas generation

Use this workflow for the user's established illustrated workbook style. The reviewed chapter model/HTML controls content and activity order; the design sample controls appearance only.

## Architecture and sheets

Define independent rooms for header, title, instructions, reading/word bank, exercises, answer writing, main illustration and checklist/teacher note. Record each room's outer bounds, safe inner rectangle, padding, role and layer. Painted edges and icons must not intrude into text or handwriting rooms. Generate regions, never one continuous page painting.

Create a fresh header for each chapter, using its setting, events or central objects. Reuse that header across pages within the same chapter only. A generic brand identity may remain consistent, but do not copy the pilot's complete scenery, scene or header bitmap into every chapter. Record the chapter-to-header assignment and check both hashes and visual meaning across chapters. Each page also receives exactly one DIFFERENT main illustration related to its activity or chapter event. Reading can show the story; spelling a book/pencils; scrambles tiles; meanings a comparison; comprehension a magnifier/book; speaking a song; dictation word cards; guides chapter scenes; answer key checking work. Classroom metaphors are not source-book events. Keep the same characters, proportions, wardrobe, palette and medium.

For this established workflow, generate all new COLOR images with Codex's built-in `image_gen`. The user's term “이마젠” refers to this tool. Google Flow is reserved for the black-and-white coloring variants, using the actual completed color images as references. Do not silently generate color in Flow or describe Flow's color output as Codex image generation.

For a header-only revision, replace the complete upper header region in both editions and all exports. Preserve body illustrations, ornaments, Word Banks, wording and answer records unless the user expands the scope. Save a new version and compare unchanged body drawing records (and rendered pixels where practical) with the baseline. Re-measure each new brand plaque, grade plaque and title ribbon; their interiors need not match the pilot's coordinates.

Derive setting and visual atmosphere from the chapter evidence and original illustrations. A continuing nighttime story does not require a moon/star/blue-sky panorama on every header. Interior rooms, bedding, kitchen surfaces and gardens should use the scene's actual palette and props. Do not invent daylight either; omit decorative sky when it adds an unsupported or repetitive time-of-day claim. Keep a character identity reference across chapter headers.

For generated outer white padding, record the crop rectangle in native pixels and preserve all illustration outlines. Remove only verified exterior margins, keeping the white interiors of text plaques intact. Place the cropped asset with equal X/Y scale; never stretch it to match a header box. Validate the resulting painted bounds against the instruction area and each text span against its own measured inner plaque, then inspect the final header on every worksheet.

For this user's established mode, use these defaults unless they request different grids:

| Asset | Grid | Use |
|---|---|---|
| Small ornaments | 5 columns x 5 rows | One 25-element sheet |
| Main illustrations | 2 columns x 2 rows | Four scenes per sheet; 13 pages need four sheets, three spares |
| Empty Word Bank frames | 1 column x 4 rows | Four stacked horizontal variants; explicitly state orientation |

Specify all cells in reading order, safe insets, white gutters, no labels, and no cross-cell subjects. Inspect actual grid geometry. Split at native resolution with `scripts/split_atlas.py --columns N --rows N`; its default remains 4x4 for compatibility. Uniform inset can remove a grid line only if it does not cut the subject. Inspect every crop for neighboring-cell fragments. Separate a frame's outside pictogram using its actual boundary, never a fixed crop percentage inherited from another sheet. Preserve original sheets.

The earlier 4x4 atlas was an exploration format. For this established workbook, the later 5x5 ornaments, 2x2 scenes and 1-column x 4-row frames supersede it. State both columns and rows so “1x4” cannot be interpreted as four narrow vertical boxes. If the generator cannot maintain four usable shallow frames in one sheet, use three stacked frames plus one separately generated shallow frame and record the exception.

Small design elements must be real transparent-background PNGs with an alpha channel. Request transparency during generation where supported. Verify that corners contain alpha=0, that antialiased edges retain partial alpha, and that no white/checkerboard rectangle or matte halo remains. Preserve RGBA while splitting and trimming. Export transparency correctly in PDF (soft mask), PPTX and linked InDesign artwork; inspect the actual PDF, not just the PNG. A white-background image or a painted checkerboard is not transparent. If the selected service lacks alpha output, isolate the generated ornament with a suitable background-removal workflow and inspect edges; do not describe the unprocessed original as transparent.

Record semantic page/scene/ornament/frame assignments in `page-asset-map.json`. Choose ornaments by the activity or vocabulary, not arbitrary round-robin decoration. Each page has one main scene; spare sheet scenes remain alternatives. Put tiny ornaments in dedicated free rooms, leaving answer rules clear.

## Prompt contract

Use an available image-generation tool and follow its instructions. Identify style, character and edit inputs. Do not silently substitute a different provider/model when the user specifically names one.

Specify the region, aspect ratio, crop boundaries, safe interior and exclusions. Describe crisp dark-navy ink contours, fine watercolor-paper grain, controlled cobalt/sky-blue washes, rosy pink, warm golden lamplight and consistent cool moonlight. Preserve identity and visual language, but explicitly reject smeared pigment, fuzzy contours, illegible glyphs and compression artifacts. Do not promise native pixel dimensions unsupported by the tool.

Generated art has NO text, letters, numbers, pseudo-text, watermark, answer marks or writing rules. Books/cards may have blank pages. Word Bank frames need large clean white interiors and delicate painted edges, with tiny toast/moon/music/book motifs outside the text room. Typeset exact labels, vocabulary, questions and Korean translations afterwards.

```text
Asset: [explicit row/column grid] of [independent regions].
References: style/character only; do not reproduce blur or text.
Cells in reading order: [one distinct subject per cell].
Medium: sharp navy contours, fine paper grain, controlled watercolor/gouache,
consistent light, character proportions and wardrobe.
Composition: complete subjects, safe inset, white gutters, no cross-cell objects.
Reserved interior: [white text room or illustration-only slot].
Exclude: typography, pseudo-text, labels, numbers, watermark, smeared edges.
```

## Composition and export

Fit scenes proportionally; never stretch faces/bodies. Design empty frames for their final aspect ratio. If painted edges cannot accommodate type, adjust the region or use a controlled vector frame. Do not accept a collision to retain a scallop. Do not flatten the whole composition before producing editable editions.

For Word Bank frames, derive the target outer and safe-inner width/height from the final text layout BEFORE generation. Prompt for that object ratio, including white margins outside it. Measure and crop the actual frame rather than its whole square sheet. Place with equal X/Y scale. If it becomes too short, too tall or too narrow when proportionally fitted, regenerate the frame for the target ratio and integrate it in every deliverable. Never repair it by stretching left/right. A request to “reflect it in the mockup” requires rebuilding and inspecting the PDFs and editable exports, not merely saving the new asset.

Use a single reviewed content model and ordered drawing records. Preserve paint order: page base/header, empty frames, worksheet shapes/rules, supplementary art, editable text. InDesign layer grouping must preserve those relationships. Match actual fonts across PDF/PPTX/HTML/InDesign; font-alias re-registration can be ignored by registries, so inspect the PDF font name.

Deliver publishing PDF/editable handoff, flattened A4 PDF, Canva PPTX/PNG ZIP, source sheets, split assets, exact prompts, page map and validation report. Distinguish native art DPI from final 300dpi rasterization. Report unverified InDesign/Canva imports. Keep book text and generated/user artwork outside the public skill repository.

Read [text-layout.md](text-layout.md) before typography and final QA.
