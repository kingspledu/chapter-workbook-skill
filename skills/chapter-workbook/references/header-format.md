# Main header format contract

This contract fixes the appearance of the repeated upper header used by the verified Book 1 later chapters. It is separate from the page-room template because a correct room does not guarantee a compatible generated header.

## Immutable canvas and structure

- Generate the color header on a native 2172 × 724 px canvas.
- Preserve the shallow ultrawide composition. Do not substitute a square, tall poster, or a freeform 16:9 scene.
- Keep the full-width rainbow diagonal stripe along the top edge.
- Keep the circular pig badge at the far left, partly overlapping the header scene.
- Keep the white scalloped brand plaque in the upper-left after the badge.
- Keep the cream/gold rounded Grade plaque in the upper-right.
- Keep the wide pink scalloped title ribbon across the lower portion.
- Keep the open-book icon at the lower-left edge and the small garden/edge decoration at the lower-right.
- Leave the three text rooms empty in generated art. Typeset all wording after placement.

The chapter-specific scene occupies the middle illustration band between the plaques and above/behind the pink ribbon. The scene may show a chapter-supported room, yard, kitchen or action, but it must not change the structure or relative placement of the shared header elements.

## Geometry and crop

- Use the same 2172 × 724 aspect ratio for color and the padded Flow reference.
- Keep full left and right ends. Remove only verified exterior white padding outside the illustrated band; never crop a badge, plaque, ribbon, book icon or fine outline tip.
- Place the final cropped band with equal X/Y scale. Never stretch it to fill a page header room.
- Measure the actual inner rooms of the generated brand plaque, grade plaque and title ribbon after crop. If any room is missing, merged, moved materially or changed from scalloped to a different shape, reject the image and regenerate.
- Compare the new header against a verified reference by overlay/contact sheet before inserting it into pages.

## Prompt and acceptance checks

Prompt for “same established header format, same plaque geometry and same ribbon geometry; replace only the chapter scene.” Explicitly exclude text, pseudo-text, new plaques, extra ribbons, tall poster composition, decorative night sky and unsupported objects.

Reject any result with:

- a different canvas proportion or vertically expanded scene;
- missing, duplicated or relocated brand/grade/title rooms;
- a title ribbon that is rectangular, narrow, floating or differently colored;
- a badge or book icon moved into a text room;
- characters or props crossing plaque interiors;
- generated lettering or pseudo-text;
- a scene that belongs to another chapter.

Only after these checks pass should the header be cropped, placed and reused across the chapter's 13 pages. The header contract does not authorize copying another chapter's story scene, vocabulary or private artwork.
