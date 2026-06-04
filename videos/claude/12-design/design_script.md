# Video 2.12 - Claude Design: describe it, and watch it get designed, on-brand
### Production pack: Excalidraw board + narration script + demo steps

**Format:** one flowing Excalidraw board (`claude-design.excalidraw`) you pan across left-to-right and talk over, cutting to live Claude Design between beats · ~4:30 Loom · British English · invented, generic examples (no Phlo branding, no patient or clinical data) · current to today.

**How to use this pack**
- Open `claude-design.excalidraw` full-screen and frame **one beat at a time** - the whitespace gaps are the camera moves. Pan left-to-right, ~3s of narration per beat.
- `[BEAT n]` maps **1:1** to board beat *n*. `[CUT TO CLAUDE DESIGN]` / `[BACK TO BOARD]` mark the cut-away inside the beat it belongs to.

> Claude Design is an **Anthropic Labs research preview** - it's newer and rougher than the other tools in this series. Say so plainly (beats 2 and 8); don't oversell it as finished.

---

## Section 2 - Narration script (~4:30)

Voice: warm, plain, a colleague showing you something genuinely new - honest that it's early.

**[BEAT 1] 0:00 - 0:16 (Hook)**
"Ask Claude to 'design a landing page' and you might expect a description of one - headings, a paragraph about layout. Claude Design gives you an actual, polished design you can look at, click and react to. It's the difference between being told about a screen and seeing it. Four and a half minutes."

**[BEAT 2] 0:16 - 0:42 (What it is)**
"So what is it? A design partner from Anthropic Labs - you work *with* Claude to make polished visual things: interactive prototypes, on-brand decks, one-pagers. Two honest flags up front: it's a research preview, so it's newer and rougher than the rest of this series; and it's powered by one of the strongest models, on the Pro plan and above. New, capable, still finding its edges."

**[BEAT 3] 0:42 - 1:12 (It learns your house style)**
"Here's the part that makes it special. There's a one-time onboarding where Claude reads your codebase and your design files and builds your *design system* - your actual colours, type and components. And then every project after that uses them automatically. So you're not fighting to make things look like you - it's on-brand by default, not by copy-paste. That's the bit you don't get from a generic image generator."

**[BEAT 4] 1:12 - 1:38 (Start from almost anything)**
"You can start from almost anything. A text prompt. A pile of files you upload - images, Word, PowerPoint, Excel. Your codebase. Or - and this is clever - it can grab real elements off your live website, so a prototype looks like the actual product, not a generic template. It meets you wherever your idea already is."

**[BEAT 5] 1:38 - 2:05 (What you get out)**
"And what comes out is stuff you can use, not just admire. Interactive prototypes you can share and user-test - no code review, no pull requests. Feature flows you sketch and then hand to Claude Code to actually build. And on-brand decks you export to PowerPoint, or send straight to Canva. Things you can share, test and ship."

**[BEAT 6] 2:05 - 2:32 (Three handy flows) → [CUT TO CLAUDE DESIGN]**
"Who's it for? Three quick flows. Designers turn a static mockup into an interactive prototype to user-test. Product managers sketch a feature flow and hand it to Claude Code. Founders and account execs go from a rough outline to a complete, on-brand deck. Let me make one."

**[CUT TO CLAUDE DESIGN] 2:32 - 3:08 (Demo - see Section 3)**
From a prompt, generate an on-brand mockup, refine it once in plain English, then export.

**[BACK TO BOARD] [BEAT 7] 3:08 - 3:28 (What to make first)**
"So what to make first? A quick prototype - something clickable to user-test today instead of next sprint. An on-brand deck for a pitch or a review. A tidy one-pager that makes an idea look finished. And a feature flow, to agree the shape *before* anyone builds it. It turns 'I'll mock that up later' into 'here it is'."

**[BEAT 8] 3:28 - 3:55 (A preview - treat the output as a draft)**
"Remember it's a research preview - so treat the output as a draft. It has rough edges, and it changes. Keep anything sensitive out of it unless that's been approved - confidential designs, patient-facing material, or a private codebase. And bear in mind Claude gives you a strong first design, but a person owns the final look: it's a fast draft to refine, not the finished brand."

**[BEAT 9] 3:55 - 4:12 (Describe one screen you wish existed)**
"So try it: describe one screen or deck you wish already existed - a landing page, a pitch deck, a settings screen. See the first design, then refine it in plain English. Claude gets you a polished start - you shape it into the finished thing. And that's the end of the Claude module - nice work getting through it. Docs below."

---

## Section 3 - On-screen demo steps

Everything below is invented, generic content. No Phlo branding, no patient or confidential material, no private codebase, at any point.

### Demo - a prompt to an on-brand mockup (~35s)

1. In **Claude Design** (Pro+ account, research preview), start a new project. If onboarding offers to build a design system, use a **generic/sample** style - do **not** point it at any real Phlo codebase or confidential design files on camera.
2. Prompt: `Design a clean landing page for a fictional internal tool called "Tidy" - a hero, three feature cards, and a sign-up button.`
3. Show the polished design appearing. Refine once in plain English: `Make the hero friendlier and move the sign-up button into the header.`
4. Show an **export** option - to PPTX, or "send to Canva" - and (if relevant) the interactive-prototype share.
5. Say the caveat out loud: "research preview - a strong draft I'd refine, and nothing confidential goes in." Switch back to the board.

> Keep all inputs invented and generic. The teaching point is "polished start, human finishes" - so refine something on camera rather than accepting the first output as final.

---

## Section 4 - Design rationale

- **House Style B**, built by `build_design.py` (imports the shared `excalidraw_kit`); re-run to regenerate.
- **The signature beat is 3 (it learns your design system)** - that's what distinguishes Claude Design from a generic image/UI generator, and from the Artifacts video (2.3), so the deck leans on it. Beat 5 (what you get out) keeps it concrete: prototypes, flows, decks - things you ship.
- **Verified behaviour**: Anthropic Labs research preview, powered by Claude Opus 4.7, Pro+; designs/prototypes/decks/one-pagers; design-system onboarding from codebase + design files; start from prompt/uploads/codebase/web-capture; export to PPTX or Canva; hand feature flows to Claude Code - all from the current Anthropic/Claude docs.
- **Honesty about maturity**: because it's a research preview, the script flags rough edges twice and the safety beat warns against uploading confidential/patient material or private codebases - aligned with Phlo's guardrails.

## Resources to link under the video
- Anthropic - *Introducing Claude Design by Anthropic Labs*: https://www.anthropic.com/news/claude-design-anthropic-labs
- Claude - *Get started with Claude Design*: https://support.claude.com/en/articles/14604416-get-started-with-claude-design
