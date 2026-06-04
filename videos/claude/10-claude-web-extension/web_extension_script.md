# Video 2.10 - Claude in Chrome: Claude that can actually use your browser
### Production pack: Excalidraw board + narration script + demo steps

**Format:** one flowing Excalidraw board (`claude-chrome.excalidraw`) you pan across left-to-right and talk over, cutting to a live Chrome window between beats · ~4:30 Loom · British English · invented, generic examples (no Phlo branding, no patient or clinical data) · current to today.

**How to use this pack**
- Open `claude-chrome.excalidraw` full-screen and frame **one beat at a time** - the whitespace gaps are the camera moves. Pan left-to-right, ~3s of narration per beat.
- `[BEAT n]` maps **1:1** to board beat *n*. `[CUT TO CHROME]` / `[BACK TO BOARD]` mark the cut-away inside the beat it belongs to.

> This is the first **agentic** tool in the series - it acts on your behalf - so the permission model (beat 4) and the safety beat (beat 8) carry more weight than in the file-type videos. Lean into them.

---

## Section 2 - Narration script (~4:30)

Voice: warm, plain, a colleague showing you something useful - but straight about the risks.

**[BEAT 1] 0:00 - 0:16 (Hook)**
"Everything so far has been Claude in its own window. This one lives *in* your browser - right beside the page you're on. You can ask it a question about what's on screen, or ask it to actually *do* something on the sites you already use. It's a different kind of tool, so stay with me on the safety bits. Four and a half minutes."

**[BEAT 2] 0:16 - 0:42 (It sees the page like you do)**
"First, what it can see. Claude reads the page the way you do - it recognises buttons, forms, menus and the content, and understands what they're for. It's in beta right now, on all the paid plans, in the Chrome browser. So this isn't pasting a URL into a chat; Claude is genuinely looking at the live page with you."

**[BEAT 3] 0:42 - 1:05 (It can act, not just read)**
"And it doesn't just read - it can act. It navigates, it clicks, it types, it fills in forms. It can work across every tab in a tab group, and it keeps going when you switch away. So 'summarise this' becomes 'go through these and pull the bits I need' - Claude does the clicking."

**[BEAT 4] 1:05 - 1:35 (It works with your permission)**
"Which immediately raises the question - acting *as who?* The answer: as you, with your logins and your context, but only where you let it. There's a multi-layered permission system. You grant access site by site. You approve actions before they run. And you can stop it or take over at any moment. This is control, not blind trust - and it's the whole reason the tool is safe to use."

**[BEAT 5] 1:35 - 2:00 (Teach it, schedule it)**
"Two things make it more than a one-off helper. You can record a workflow - do a task once with Claude watching, and it learns the steps to repeat: open the report, copy the figures, paste them into the tracker. And you can put that on a schedule - recurring browser tasks that run daily, weekly or monthly, on their own."

**[BEAT 6] 2:02 - 2:30 (What you'd actually ask it) → [CUT TO CHROME]**
"In practice you just ask in plain English and it works out the clicks. 'Pull these rows into a summary.' 'Fill this form from my notes.' 'Find this part across the three open tabs.' 'Summarise this long page in five bullets.' Let me show a safe one live."

**[CUT TO CHROME] 2:30 - 3:05 (Demo - see Section 3)**
On a public page, ask Claude to summarise it, then pull a table into a list. Keep it read-only.

**[BACK TO BOARD] [BEAT 7] 3:05 - 3:25 (Everyday browser drudgery)**
"Think of the everyday browser drudgery you do without thinking. Pulling data off a page - rows from a dashboard into a list. Filling repetitive forms - the same fields, again and again. Reading a long page or PDF fast. And gathering one answer from several tabs. That's where it pays off."

**[BEAT 8] 3:25 - 3:55 (Powerful - keep it on a short lead)**
"Now the serious bit - it's powerful, so keep it on a short lead. Watch for prompt injection: a web page can hide instructions that try to hijack Claude, so grant the least access that works. And never point it at patient systems, banking, or anything regulated. Remember it's beta, and it acts on your behalf - so watch it on anything that matters, and approve consequential actions yourself. Treat it like a capable new starter, not autopilot."

**[BEAT 9] 3:55 - 4:12 (Start with something it can't break)**
"So if you try it, start with something it can't break - a read-only task. 'Summarise this page.' 'Pull a table into a list.' 'Compare these two open tabs.' Watch what it does, and let that tell you what you'd trust it to click next. Claude can use the browser for you - you decide what it's allowed to touch. Docs below, including the safety guide. See you in the next one."

---

## Section 3 - On-screen demo steps

Everything below uses **public, non-sensitive** pages. No logged-in accounts, no patient systems, no Phlo systems, at any point.

### Demo - a safe, read-only browse (~35s)

1. In Chrome with the Claude extension installed (paid plan), open a long public article or a public data table (e.g. a Wikipedia page).
2. Open the Claude side panel and ask: `Summarise this page in five bullets.` Point at the panel reading the live page.
3. On a page with a table, ask: `Pull this table into a clean bulleted list.` Show it reading and reformatting.
4. **Show the permission prompt / approval step** when it appears - narrate "I approve each action; I can stop any time." Do **not** demo form-filling on any logged-in or sensitive site.
5. Switch back to the board.

> Keep the whole demo read-only and on public pages - that *is* the safety message. If it offers to click something consequential, decline on camera and say why.

---

## Section 4 - Design rationale

- **House Style B**, built by `build_web_extension.py` (imports the shared `excalidraw_kit`); re-run to regenerate.
- **Different shape from the file-type videos**: this is an *agentic* tool, so there's no "build a real file" beat. Instead the signature beats are 3 (it can act), 4 (the permission model) and 8 (prompt-injection safety) - the order deliberately introduces the power, then immediately the control.
- **Verified behaviour**: agentic clicking/forms/JS, cross-tab context, record-a-workflow and scheduled browser tasks, beta on all paid plans in Chrome, multi-layered permissions - all from the current Claude docs.
- **Safety is load-bearing, not decorative**: the prompt-injection warning and "never point it at patient systems / regulated tools" map directly onto Phlo's regulated-pharmacy guardrails. The demo is constrained to public, read-only pages on purpose.

## Resources to link under the video
- Claude - *Get started with Claude in Chrome*: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
- Claude - *Using Claude in Chrome safely*: https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely
- Claude - *Claude in Chrome permissions guide*: https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide
