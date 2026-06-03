# Video 2.3 - Artifacts: when Claude makes things, not just text
### Production pack: Excalidraw (Claude Code) prompt + narration script + demo steps

**Format:** discrete Excalidraw frames you talk over, cutting to live Claude between them · ~5 min Loom · British English · invented design system (no Phlo branding) · current to today.

**How to use this pack**

2. Record using **Section 2** (narration) and **Section 3** (the two live demos). The board carries the structure; you carry the voice; the demos prove it is real.

---

## Section 2 - Narration script (~5:00)

Voice: warm, plain, a colleague showing you something useful - not a corporate voiceover. Times are a guide. `[FRAME n]` = the frame on screen. `[TO CLAUDE]` / `[BACK]` = switch between the board and the live Claude window.

**[FRAME 1] 0:00 - 0:12 (Hook)**
"Ask Claude for a calculator and most people expect a description of one. Claude can just build it - a working tool, sitting right there for you to use. That's an Artifact, and it's the feature that turns Claude from something that advises you into something that makes things for you. Five minutes."

**[FRAME 2] 0:12 - 0:45 (What it is)**
"Here's the whole idea in one picture. Normally Claude talks to you in the chat, on the left. An Artifact is what appears on the right: a separate panel holding an actual thing - a document, a tool, a chart - that you can edit, run, and come back to. Words on the left; something you can use on the right. That split is the entire concept. Once you've seen it, you'll spot Artifacts everywhere."

**[FRAME 3] 0:45 - 1:05 (Range)**
"And 'a thing' covers a lot. A tidy one-pager. A little calculator. A small interactive app. A chart. A diagram. Or a proper file you download - Word, PowerPoint, Excel, PDF. Same feature, very different outputs. The skill is simply knowing it's there and asking for it."

**[FRAME 4] 1:05 - 1:25 (Auto vs ask)**
"You'll get an Artifact one of two ways. Sometimes Claude makes one on its own - for a long document, for code, for anything structured you're obviously going to reuse. And sometimes you ask, on purpose. Two phrasings do most of the work: 'make me a one-page Artifact summarising X', and 'build me a tool to calculate Y'. Let's actually do both."

**[FRAME 5] 1:25 - 1:35 (Handoff) → [TO CLAUDE]**
"First, the one-pager. Watch the right-hand side."

**[TO CLAUDE] 1:35 - 2:25 (Demo 1 - see Section 3.1)**
Talk over it: name what you're typing, point at the panel as it builds, make one change, then show that older versions are kept. Keep it moving.

**[BACK] [FRAME 6] 2:25 - 2:55 (Iterate)**
"Notice what just happened - that wasn't one-and-done. An Artifact is clay, not stone. You build it, you edit it on the spot, you ask Claude to refine it, and every version is kept so you can roll back. You change it either way: drag and type on the canvas yourself, or just tell Claude in plain English. Now something more ambitious - a tool that actually does a calculation."

**[FRAME 7] 2:55 - 3:05 (Handoff) → [TO CLAUDE]**
"A supply calculator. Quantity in, daily dose in, days of supply and a reorder date out."

**[TO CLAUDE] 3:05 - 3:55 (Demo 2 - see Section 3.2)**
Build it, type sample numbers so it visibly calculates, make one refinement, then publish and copy the link. Say the one rule out loud as you publish.

**[BACK] [FRAME 8] 3:55 - 4:15 (Share - the unlock)**
"And that link is the part that matters for us. Build something once, publish it, drop the link in Slack - and the whole team uses it, no account needed to open it. The Patient Care reply-template one person perfects; the meeting-prep sheet anyone can grab; the reorder calculator ops keeps handy. One person's good idea becomes everyone's tool."

**[FRAME 9] 4:15 - 4:30 (New, light)**
"Two quick things that are newer, so you're current: Artifacts can now have Claude running inside them - so the thing can actually think, not just sit there. They can refresh their data when you reopen them, remember what you put in, and connect to tools like your calendar or email. Same five-minute skill, a lot more range."

**[FRAME 10] 4:30 - 4:45 (Rule + when not)**
"One rule, one reality check. The rule: publishing or connecting an Artifact changes who can see it, so keep anything patient-identifiable, and any logins or keys, out of anything you share. The reality check: a quick one-off answer doesn't need an Artifact. Reach for one when you'll reuse it, edit it, or hand it on."

**[FRAME 11] 4:45 - 4:55 (Pause and try)**
"So pause here and try it. Ask Claude to make you a one-page Artifact for something you do every week - a status update, a meeting-prep sheet, a checklist. See what it gives you, then change one thing."

**[FRAME 12] 4:55 - 5:05 (Close)**
"Artifacts turn Claude from advisor to maker. Once you start asking for them, you'll wonder how you worked without them. The docs are linked below. See you in the next one."

---

## Section 3 - On-screen demo steps

Use a Team workspace (ideally inside a Project so it's easy to find again), or a single account - both behave the same here. Everything below is invented, generic data. No patient information at any point.

### 3.1 Demo 1 - the reusable one-pager (~50s)

1. In a new chat, type:
   > Make me a one-page meeting-prep template as an Artifact I can reuse. Sections: meeting title and date, attendees, objective, three key points, decisions needed, and actions with owners and due dates. Keep it clean and printable.
2. The Artifact panel opens on the right and builds the one-pager. Point at it: "there's the thing, not a description of it."
3. Iterate - type:
   > Add a short 'risks and open questions' box, and move actions to the bottom.
   Show it update in place (this is now v2).
4. Edit directly: click a heading in the Artifact and change one word (e.g. "Objective" to "Goal"), to show you can edit it yourself.
5. Open the version control on the Artifact and show v1 is still there. Say: "every version is kept - roll back any time." Switch back to the board.

### 3.2 Demo 2 - the working tool, then share it (~50s)

1. Type:
   > Build me a small interactive tool as an Artifact. I enter the quantity dispensed and the number of tablets taken per day; it shows the days of supply and the reorder date, which is today's date plus the days of supply. Add an optional 'buffer' field in days that brings the reorder date forward. Make it clean and work well on mobile.
2. The interactive tool builds in the panel. Enter sample numbers so it visibly calculates:
   - quantity **56**, **2** per day, buffer **7** → 28 days of supply, reorder date shown ~21 days out.
   - Change to **84** at **3** per day to show it recalculating live.
3. Iterate - type:
   > Also show the run-out date, and label every field clearly.
   (v2.)
4. Share it: click **Publish** (top-right of the Artifact panel) and **copy the link**. As you do, say the rule: "made-up numbers only - nothing patient-identifiable goes into anything I publish." Mention the link is version-specific and that all your shared Artifacts live in the **Published** tab.
5. (Optional, Team) Note you'd drop that link into a Slack channel so the team can use it. Switch back to the board.

> Tip if a demo wobbles on camera: there's a **Fix with Claude** button on a broken Artifact, or just describe the problem in plain English ("the buffer field isn't subtracting") - no need to read the error. Re-runs are cheap; keep talking.

---

## Section 4 - Design rationale (why it looks the way it does)

- **Concept: "words left, thing right."** The recurring split motif mirrors the real Artifacts side panel, so the layout itself teaches the idea before you say a word. The deck reuses it as a spine rather than decorating each frame differently.
- **Palette "Riso Workshop"** (warm paper, ink, vermilion, violet, mustard). Risograph-style colour suits Excalidraw's hand-drawn line, reads creative and energetic, and is deliberately **not** Phlo's palette, as you asked. Tight roles (violet = "things you can use", vermilion = "maker energy / caution", mustard = the pause only) keep it disciplined instead of rainbow.
- **Frames, not one canvas:** twelve self-contained 16:9 frames in narration order, so you can jump cleanly and cut to live Claude between them. Numbered badges keep the order obvious in the zoomed-out view.
- **Anti-slop choices baked into the prompt:** 8px grid, generated by script for perfect consistency, fixed type scale, left-aligned text, icons drawn from shapes (no emoji), verbatim copy, British English, hyphens not em dashes.
- **Currency:** publish/share, AI-powered Artifacts, Live Artifacts, persistent memory and tool connections are all reflected, kept light so the runtime stays at five minutes.

## Resources to link under the video
- Anthropic - *What are Artifacts and how do I use them*: https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them
- Anthropic - *Prototype AI-powered apps with Claude Artifacts* (publish, share, iterate): https://claude.com/resources/tutorials/prototype-ai-powered-apps-with-claude-artifacts