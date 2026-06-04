# Video 2.9 - Claude + Word: an editor that works in the document, not around it
### Production pack: Excalidraw board + narration script + demo steps

**Format:** one flowing Excalidraw board (`claude-word.excalidraw`) you pan across left-to-right and talk over, cutting to live Claude / live Word between beats · ~4:30 Loom · British English · invented, generic examples (no Phlo branding, no patient or clinical data) · current to today.

**How to use this pack**
- Open `claude-word.excalidraw` full-screen and frame **one beat at a time** - the whitespace gaps are the camera moves. Pan left-to-right, ~3s of narration per beat.
- `[BEAT n]` maps **1:1** to board beat *n*. `[CUT TO …]` / `[BACK TO BOARD]` mark the cut-aways inside the beat they belong to.

---

## Section 2 - Narration script (~4:30)

Voice: warm, plain, a colleague showing you something useful.

**[BEAT 1] 0:00 - 0:18 (Hook)**
"The usual way people use AI on a document is a copy-paste shuttle: lift a paragraph out, paste it into a chat, paste the answer back. Claude works *in* the document instead, like an editor with a red pen - its changes land as tracked edits you can accept or reject, one by one. You're always in control. Four and a half minutes."

**[BEAT 2] 0:18 - 0:46 (A real document)**
"Two ways in - here's the first. Ask in the chat and Claude builds a genuine Word file: a real dot-docx with proper headings, lists and styles, ready to download or save to Drive. It opens in Word or Google Docs as a properly formatted document, not a wall of text. That part's on every plan - web, desktop and mobile."

**[BEAT 3] 0:46 - 1:10 (Ask the document questions)**
"Second, it can read a document *with* you. Ask a question - 'what does clause four actually commit us to?' - and the answer cites the exact passage, with a click that jumps you straight there. And it's not keyword search: ask it to 'find every passage about data retention' and it finds them by *meaning*, including the ones that never use those words."

**[BEAT 4] 1:10 - 1:38 (It edits only what you select)**
"Now the editing itself, and this is the careful bit. Highlight one passage and tell Claude what to change, and it touches *that* and nothing else - your surrounding styles and numbering survive. Turn on suggested-edits mode and every change lands as a tracked revision, so nothing is silently rewritten. You see exactly what moved."

**[BEAT 5] 1:38 - 2:02 (Make one, or mark up your own)**
"That in-document editing is the second way in: the Claude add-in, working on the document you've already got open. So - same Claude, two front doors: build a fresh file from the chat, on any plan; or work your open document from the add-in, which needs a Pro plan or above. You'll find it in Word's Add-ins menu."

**[BEAT 6] 2:02 - 2:35 (Ask, and read the changes back) → [CUT TO WORD]**
"And you steer it by asking. 'Cut this by a third but keep the headings.' 'Make the tone more formal.' 'Find every mention of liability.' 'Turn these notes into a one-page brief.' Each one comes back as tracked changes you read before you accept. Let me show the add-in editing a real paragraph."

**[CUT TO WORD] 2:35 - 3:05 (Demo - see Section 3)**
In an open document, select a paragraph, ask Claude to tighten it, and show the tracked change appearing - accept one, reject one.

**[BACK TO BOARD] [BEAT 7] 3:05 - 3:25 (Reach for it when...)**
"Reach for it when you've got the long, wordy jobs. A first draft - a policy, a brief, a report you'd rather react to than start. Tightening a long document - cut the waffle, keep the structure. Reviewing for a theme - every clause that touches one topic. And filling a template in your house style and headings."

**[BEAT 8] 3:25 - 3:48 (Read every change before you accept)**
"Read every change before you accept it. Go change by change - read each tracked edit and accept or reject it; don't bulk-accept, especially anything legal, client-facing or regulated. And trust the source: don't open documents you don't trust - an outside contract, a stray file - because a booby-trapped doc can hijack the request, so keep confidential wording out of anything you share."

**[BEAT 9] 3:48 - 4:05 (Take a long doc, ask for a third less)**
"So try it: take a long document you wrote - a process note, a long email, a draft policy - and ask Claude to cut it by a third. Read the tracked changes, then accept only the ones you like. Claude works in the document - you keep the final word on the words. Docs below. See you in the next one."

---

## Section 3 - On-screen demo steps

Everything below is invented, generic data. No patient information, no Phlo specifics, at any point.

### Demo - tracked edits in Word (~30s)

1. Open Word (web or desktop) on a fictional wordy document - e.g. a one-page "remote-working guidelines" draft. Open the **Claude** add-in (Add-ins menu) and turn on **suggested-edits** mode.
2. Select one bloated paragraph. In the add-in, type: `Tighten this paragraph by about a third, keep the meaning, don't touch the heading.`
3. Show the change arriving as **tracked revisions**. **Accept** one sentence, **reject** another, to make the point you're in control.
4. (Optional) Ask `Find every passage about confidentiality` to show thematic search jumping between matches. Switch back to the board.

> Tip: ask in plain English and keep it to invented content. Re-runs are cheap; never bulk-accept on camera - that's the teaching point.

---

## Section 4 - Design rationale

- **House Style B**, built by `build_word.py` (imports the shared `excalidraw_kit`); re-run to regenerate.
- **Distinct angle from its file-type siblings**: PowerPoint (2.7) owns decks; Excel (2.8) owns formulas; **this one owns long-form prose - tracked-change editing on a selection, cited Q&A, and thematic (meaning-based) search.** Beats 3 (citations/thematic search) and 4 (selection + tracked changes) are the signature beats.
- **Two real capabilities, not conflated**: (1) "Create and edit files with Claude" - chat builds a genuine .docx, all plans; (2) "Claude for Word" - the add-in, Pro+. Beat 5 is the hinge.
- **Safety kept honest**: documented prompt-injection caution on untrusted files, plus "read tracked changes, don't bulk-accept" - maps onto Phlo's human-owns-the-final guardrail for legal/regulated wording.

## Resources to link under the video
- Claude - *Create and edit files with Claude*: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- Claude - *Use Claude for Word*: https://support.claude.com/en/articles/14465370-use-claude-for-word
- Claude - *Collaborate with Claude across Excel, PowerPoint, Word and Outlook*: https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
