# Chapter Workbook Skill

A Codex skill for source-grounded chapter workbooks with a 13-page early-reader activity progression.

Copy `skills/chapter-workbook` into your Codex skills directory. Read its SKILL.md, then install `requirements.txt`. Bring your own source books, reviewed chapter JSON and authorized illustrations. Nothing from the pilot book or its reference artwork is included.

The skill covers chapter evidence, spelling and comprehension authoring, bilingual teacher notes, validation, editable publishing handoff, flattened A4 output and Canva import. The deterministic renderer handles a reviewed model; an AI/teacher must author and verify the chapter content. It does not automatically understand arbitrary scanned books.

For illustrated workbooks, use independent white-room regions: a reusable header, a different main scene per page generated in 2x2 sheets, 25 small ornaments in a 5x5 sheet, and four Word Bank frames in a 1-column x 4-row sheet. Exact type stays editable. The skill includes safe-box/title-occupancy rules, a configurable atlas splitter and a PDF region audit. The basic renderer remains a typography-first fallback; it does not implement the illustrated composition workflow.

```powershell
python skills/chapter-workbook/scripts/inspect_books.py books --output inspection
python skills/chapter-workbook/scripts/render_workbook.py --chapter chapter.json --assets assets --output output
```

Outputs: vector-text publishing PDF, 300dpi flattened PDF, editable PPTX, PNG ZIP, browser preview, chapter JSON, validation report and InDesign JSX. Run the JSX in InDesign to create INDD/IDML. Fonts and layout must be checked in InDesign and Canva; the PDF is an RGB mockup, not certified PDF/X. On Windows the font map uses installed Trebuchet MS and Malgun Gothic. See the skill for other environments.

Code and instructions: MIT. Source books and user artwork remain subject to their respective rights.
