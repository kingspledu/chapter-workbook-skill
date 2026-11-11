# Independent regions and atlas generation

Use this workflow for the user's established illustrated workbook style. The reviewed chapter model/HTML controls content and activity order; the design sample controls appearance only.

## Architecture and sheets

Define independent rooms for header, title, instructions, reading/word bank, exercises, answer writing, main illustration and checklist/teacher note. Record each room's outer bounds, safe inner rectangle, padding, role and layer. Painted edges and icons must not intrude into text or handwriting rooms. Generate regions, never one continuous page painting.

Reuse the header. Each page receives exactly one DIFFERENT main illustration related to its activity or chapter event. Reading can show the story; spelling a book/pencils; scrambles tiles; meanings a comparison; comprehension a magnifier/book; speaking a song; dictation word cards; guides chapter scenes; answer key checking work. Classroom metaphors are not source-book events. Keep the same characters, proportions, wardrobe, palette and medium.

For this user's established mode, use these defaults unless they request different grids:

| Asset | Grid | Use |
|---|---|---|
| Small ornaments | 5 columns x 5 rows | One 25-element sheet |
| Main illustrations | 2 columns x 2 rows | Four scenes per sheet; 13 pages need four sheets, three spares |
| Empty Word Bank frames | 1 column x 4 rows | Four stacked horizontal variants; explicitly state orientation |

Specify all cells in reading order, safe insets, white gutters, no labels, and no cross-cell subjects. Inspect actual grid geometry. Split at native resolution with `scripts/split_atlas.py --columns N --rows N`; its default remains 4x4 for compatibility. Uniform inset can remove a grid line only if it does not cut the subject. Inspect every crop for neighboring-cell fragments. Separate a frame's outside pictogram using its actual boundary, never a fixed crop percentage inherited from another sheet. Preserve original sheets.

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

Use a single reviewed content model and ordered drawing records. Preserve paint order: page base/header, empty frames, worksheet shapes/rules, supplementary art, editable text. InDesign layer grouping must preserve those relationships. Match actual fonts across PDF/PPTX/HTML/InDesign; font-alias re-registration can be ignored by registries, so inspect the PDF font name.

Deliver publishing PDF/editable handoff, flattened A4 PDF, Canva PPTX/PNG ZIP, source sheets, split assets, exact prompts, page map and validation report. Distinguish native art DPI from final 300dpi rasterization. Report unverified InDesign/Canva imports. Keep book text and generated/user artwork outside the public skill repository.

Read [text-layout.md](text-layout.md) before typography and final QA.
