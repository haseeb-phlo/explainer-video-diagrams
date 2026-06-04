# Video 2.8 - Claude + Excel: a spreadsheet helper that keeps your formulas alive
### Production pack: Excalidraw board + narration script + demo steps

**Format:** one flowing Excalidraw board (`claude-excel.excalidraw`) you pan across left-to-right and talk over, cutting to live Claude / live Excel between beats · ~4:30 Loom · British English · invented, generic examples (no Phlo branding, no patient or clinical data) · current to today.

**How to use this pack**
- Open `claude-excel.excalidraw` full-screen and frame **one beat at a time** - the whitespace gaps are the camera moves. Pan left-to-right, ~3s of narration per beat.
- `[BEAT n]` maps **1:1** to board beat *n*. `[CUT TO …]` / `[BACK TO BOARD]` mark the cut-aways inside the beat they belong to.

---

## Section 2 - Narration script (~4:30)

Voice: warm, plain, a colleague showing you something useful.

**[BEAT 1] 0:00 - 0:18 (Hook)**
"Most people use AI on a spreadsheet by copying numbers out into a chat and pasting answers back. Claude doesn't need that - it works *inside* your spreadsheet. You can sit on a workbook nobody can explain and just say 'walk me through this', and it answers about your actual cells, and cites them. Four and a half minutes."

**[BEAT 2] 0:18 - 0:48 (A real spreadsheet)**
"Two ways in - here's the first. Ask Claude in the chat and it builds a genuine Excel file: a real dot-xlsx with working formulas, that you download or save to Drive and open in Excel or Google Sheets. Crucially, it's working formulas, not flat values you'd have to wire up yourself. That part's on every plan - web, desktop and mobile."

**[BEAT 3] 0:48 - 1:08 (Start from the mess you inherited)**
"And the best starting point is usually a mess you didn't make. A model you inherited, a raw CSV export, a half-built template. Point Claude at it and ask it to explain itself - 'this tab is the revenue model; cell B7 feeds every quarter total'. It reads across tabs and gives you the lay of the land before you touch anything."

**[BEAT 4] 1:08 - 1:35 (It keeps the formulas alive)**
"Here's the bit that makes it different from a chatbot. Claude edits the *model*, not just a number. Change one assumption over here, and every dependent cell down there recomputes - because the formulas reference the right cells, not frozen values. Every change is highlighted and explained, and when it answers a question it cites the exact cell, across tabs. You can always see what it did and why."

**[BEAT 5] 1:35 - 2:00 (From the chat, or in the ribbon)**
"That live editing happens in the second way in: the Claude add-in that lives right in Excel's Home ribbon, working on the sheet you've already got open. So - same Claude, two front doors: build a fresh file from the chat, on any plan; or work your open workbook from the sidebar, which needs a Pro plan or above. Open it with Control-Alt-C."

**[BEAT 6] 2:00 - 2:35 (It finds what's broken) → [CUT TO EXCEL]**
"And it's genuinely good at the worst job in spreadsheets: finding what's broken. One broken reference cascades - a single bad cell becomes three knock-on errors three tabs away. Claude traces it and shows you every cell it touched, so you choose the fix instead of hunting. 'Where does this hash-REF come from?' 'Trace what the Q4 total depends on.' Let me show it on a real workbook."

**[CUT TO EXCEL] 2:35 - 3:10 (Demo - see Section 3)**
In an inherited workbook, open the Claude add-in, ask "walk me through this workbook", then introduce/locate a #REF and ask Claude to trace and fix it.

**[BACK TO BOARD] [BEAT 7] 3:10 - 3:28 (The jobs it's best at)**
"So which jobs is it best at? Understanding a handover - a sheet you didn't build. Building a quick model - headcount, a budget, a forecast. Sanity-checking the maths before you trust it. And cleaning a data dump - tidy a CSV, then summarise it. Anywhere a spreadsheet is in the way of the answer."

**[BEAT 8] 3:28 - 3:50 (Trust the model, check the numbers)**
"Trust the model, but check the numbers. Here's where it can bite: an untrusted workbook can hijack the request, so don't open files you don't trust - and keep confidential figures out of anything you share. And here's what you still own: Claude does the legwork, but the numbers are yours - always check the figures before they drive a decision, especially finance or anything regulated."

**[BEAT 9] 3:50 - 4:05 (Try it on a sheet you didn't build)**
"So try it - on a sheet you didn't build. A budget tracker, a forecast model, a messy export: just say 'walk me through this'. Let it explain the sheet, then change one assumption and watch it update. Claude keeps your formulas alive - you keep the final say on the numbers. Docs below. See you in the next one."

---

## Section 3 - On-screen demo steps

Everything below is invented, generic data. No patient information, no Phlo specifics, at any point.

### Demo - the inherited workbook (~35s)

1. Open Excel (web or desktop) on a fictional inherited workbook - e.g. a small "Q3 budget" with a couple of tabs and a SUM that rolls up to a total. Open the **Claude** add-in (Home ribbon, or Ctrl+Alt+C / Ctrl+Option+C).
2. Type: `Walk me through this workbook.` Point at the **cited cells** as Claude references them.
3. Break something on camera: delete a column the total depends on so a `#REF!` appears. Then ask: `Where does this #REF come from, and how do I fix it without breaking the totals?`
4. Show Claude tracing the cascade and proposing a fix; **review** before accepting. Note: "every change highlighted and explained."
5. (Optional) Ask `Change the headcount assumption to 12 and update the totals` to show dependents recompute. Switch back to the board.

> Tip if it wobbles: just describe the problem plainly ("the Q4 column isn't summing") - re-runs are cheap, keep talking. Use only invented numbers.

---

## Section 4 - Design rationale

- **House Style B**, built by `build_excel.py` (imports the shared `excalidraw_kit`); re-run to regenerate.
- **Distinct angle from its file-type siblings**: PowerPoint (2.7) owns decks/structure; Word (2.9) owns long-form/formatting; **this one owns live formula relationships, cell-cited answers and debugging** - the things only a spreadsheet has. Beat 4 (formulas stay alive) and beat 6 (tracing a #REF) are the signature beats.
- **Two real capabilities, not conflated**: (1) "Create and edit files with Claude" - chat builds a genuine .xlsx, all plans; (2) "Claude for Excel" - the Home-ribbon add-in, Pro+. Beat 5 is the hinge.
- **Safety kept honest**: documented prompt-injection caution on untrusted files, plus human ownership of figures that drive decisions - maps onto Phlo's "human owns the final" guardrail.

## Resources to link under the video
- Claude - *Create and edit files with Claude*: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- Claude - *Use Claude for Excel*: https://support.claude.com/en/articles/12650343-use-claude-for-excel
- Claude - *Getting started with Claude in Excel*: https://claude.com/resources/tutorials/getting-started-with-claude-in-excel
