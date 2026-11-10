# Chapter model and algorithm

The renderer consumes UTF-8 JSON with these fields:

| Field | Contract |
|---|---|
| book, chapter, title, brand | Integers and display strings |
| source_pdf_pages | Physical PDF pages, 1-based; verify chapter boundaries visually |
| evidence | Recommended entries: claim, pdf_page, printed_page, source_excerpt, activity_ids |
| story_paragraphs | Reviewed reading paragraphs. Preserve the user's reference when requested; label later adaptations |
| words | Exactly 12 distinct words in stable order |
| clues | Two lists of six sentences, each blank written as `________` |
| clue_answers | Corresponding six answers; each half uses its own six-word bank once |
| scrambles | Twelve nonidentical permutations of the corresponding word |
| definitions | Twelve strings prefixed a. through l.; shuffled meanings |
| match_answers | Twelve definition letters in WORD order |
| questions | Four objects: question and options (three distinct strings) |
| comprehension_answers | Four correct answer strings; must match options |
| song | Four oral-reading lines, source-grounded or explicitly adapted |
| sentence_bank | Six tokens used in oral-reading cloze |
| sentence_prompts | Four lines with six total blanks, derived from song |
| sentence_answers | Four answer strings in prompt order |
| guides | Two lists of [English sentence, Korean translation] pairs |
| teaching_focus | Short teacher note |
| corrections | Corrections made to an inconsistent supplied answer key |

Default pagination: (1) reading + word hunt, (2) spelling copy, (3–4) context cloze, (5) scrambles, (6) meanings, (7) comprehension, (8) oral reading, (9) passage cloze, (10) dictation, (11–12) bilingual guide, (13) answer key.

Algorithm for later chapters:

- Detect chapter boundaries; visually confirm the first and last page. OCR output is a transcription aid.
- Rank attested vocabulary for usefulness, spelling diversity and context relevance. Keep all 12 in the single ordered word list. Never inherit previous chapter words unless attested again.
- Author six context sentences per word-bank half. Solve each using every bank word; revise if two answers are plausible. Use each intended answer once.
- Generate scrambles using a seeded shuffle, retry when unchanged; reject if sorted letters differ.
- Define words using their chapter sense. Shuffle definition records with stable IDs; derive letters after shuffling. Answer keys reference IDs, not manually copied positions.
- Ask four questions covering literal detail, feeling/motivation and action sequence only where supported. Distractors must be false within the question's scope.
- Align each question and teacher note to evidence. Keep later-chapter events out of current-chapter readings.
- Calculate wrapped text extents before placing cards. Use the 13-page pilot as a starting layout, not proof that arbitrary text will fit. Add pages or adapt layout with user scope when needed.

Outputs share a single content model and drawing-operation list, preventing edition drift. PNGs and flattened PDF are derived from publishing PDF; PPTX and InDesign retain editable text/shape records. No public demo book text or reference images are bundled.
