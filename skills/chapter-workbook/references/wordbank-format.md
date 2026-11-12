# Word Bank format contract

This contract fixes the reusable Word Bank object used by the verified later-chapter editions.

## Source object

- Generate one atlas with exactly **1 column × 4 rows**: four stacked horizontal frame cells.
- Each cell is a wide shallow object, approximately 5.6–5.8:1 in the color edition and approximately 5.5–5.7:1 in the coloring edition.
- Split using the native cell boundaries and a small white gutter. Do not use a square crop or a fixed percentage copied from another atlas.
- Preserve the original source atlas and each native split cell for editable delivery.

## Frame geometry

Each cell contains:

- a complete scalloped or softly rounded outer border;
- a large uninterrupted white writing/interior room;
- a thin, legible border with no gaps or clipped corners;
- at most one small chapter/activity motif outside the writing room, normally at the left;
- no labels, words, letters, numbers, pseudo-text, answer marks, rules or watermark.

The generated frame must be suitable for both a six-word bank and a six-token sentence bank. The interior must support three columns and two rows of editable words with breathing room. If a motif reduces the usable room, move it outside the frame or regenerate the cell.

## Page placement

Use the common page room around x 22–573 and y 196–292 pt as a starting box. The verified color frame placements are approximately 551 × 95 pt; verified coloring placements are approximately 537–544 × 96 pt. These are room ranges, not permission to distort the asset.

Fit every cell with equal X/Y scale. If the native ratio does not fit the room, adjust the room or regenerate the frame at the required ratio. Never stretch left/right, compress vertically, or place a whole 1×4 atlas as one frame.

Keep the `Word Bank` label in its own room near x 43, y 211 pt, outside the pictogram and away from the scalloped border. Place word text inside the measured white interior; measure actual font width, column width, row height and safe padding before exporting.

## Coloring edition

Generate the coloring frame in Google Flow from the completed color frame reference. It must be pure white inside with crisp black contours and no gray wash or filled background. A grayscale conversion of a color frame is not a Flow-generated coloring frame.

## Acceptance checks

- Native split ratio recorded for every cell.
- Transparent corners/alpha or intentional white scene interior distinguished correctly.
- No neighboring cell fragment, gutter line, matte halo or clipped outline.
- Frame and all six words visible in a readable PDF close crop.
- Color and coloring editions keep the same word order and text rooms.
- Final flattened A4 PDF contains the intended frame and no text overflow.
