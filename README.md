# Chapter Workbook Skill

A Codex skill for source-grounded chapter workbooks with a 13-page early-reader activity progression.

Copy `skills/chapter-workbook` into your Codex skills directory. Read its SKILL.md, then install `requirements.txt`. Bring your own source books, reviewed chapter JSON and authorized illustrations. Nothing from the pilot book or its reference artwork is included.

The skill covers chapter evidence, spelling and comprehension authoring, bilingual teacher notes, validation, editable publishing handoff, flattened A4 output and Canva import. The deterministic renderer handles a reviewed model; an AI/teacher must author and verify the chapter content. It does not automatically understand arbitrary scanned books.

For richly illustrated references, the skill includes an image-led workflow: one coordinated 4×4 design-element atlas, a separate image generation for every page, then accurate editable typesetting over the paintings. The basic renderer is a typography-first fallback, not a substitute for that visual workflow. A grid-slicing helper is included; source books and artwork are not.

```powershell
python skills/chapter-workbook/scripts/inspect_books.py books --output inspection
python skills/chapter-workbook/scripts/render_workbook.py --chapter chapter.json --assets assets --output output
```

Outputs: vector-text publishing PDF, 300dpi flattened PDF, editable PPTX, PNG ZIP, browser preview, chapter JSON, validation report and InDesign JSX. Run the JSX in InDesign to create INDD/IDML. Fonts and layout must be checked in InDesign and Canva; the PDF is an RGB mockup, not certified PDF/X. On Windows the font map uses installed Trebuchet MS and Malgun Gothic. See the skill for other environments.

Code and instructions: MIT. Source books and user artwork remain subject to their respective rights.
