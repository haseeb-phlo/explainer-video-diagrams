# Phlo Mandatory AI Course — Excalimate video production bundle

Everything needed to produce the animated explainer videos that make up the **Phlo Mandatory AI Course** in AI Ops Learn.

This bundle is the production tooling. The course content itself lives in `Phlo_Mandatory_AI_Course_Curriculum.docx` (the source of truth for every video) and the platform spec lives in `Claude_Code_Prompt_Learn_Page.md` (the AI Ops Learn extension that hosts the finished videos).

## What's in this bundle

```
phlo-learn/
├── .claude/skills/phlo-learn-videos/
│   ├── SKILL.md                              # Phlo visual conventions, vocabulary, safety rules
│   └── example-prompts/
│       ├── 01-how-claude-reads-emails.md
│       ├── 02-what-is-mcp.md
│       ├── 03-how-granola-captures-notes.md
│       ├── 04-how-beacon-prepares-interviews.md
│       └── 05-humans-in-ai-workflows.md
├── scripts/
│   ├── start-excalimate.sh                   # Just starts the Excalimate server
│   └── make-learn-video.sh                   # Full setup: server + canvas + Claude Code
├── videos/                                   # Finished MP4s land here
│   └── drafts/                               # Work-in-progress; create if missing
└── README.md                                 # this file
```

## What this bundle is for

The Mandatory AI Course is 5 modules, ~34 videos, ~6 hours of content. Not every video is an Excalimate animation — some are talking-head (the CEO video 1.1), some are screen-share demos (most of Module 2's Claude walkthrough, all of Module 4's tool demos), some are deliberately rough (the "Watch me fail" 3.6).

**Use Excalimate for the explainer-style videos** — the conceptual ones where a moving diagram beats a screen recording. Specifically:

| Course video | Why Excalimate fits |
|---|---|
| 1.2 — What an LLM actually is | The autocomplete-mechanism animation is the whole point. |
| 1.3 — What AI is good at, bad at | A visual "good vs bad" map lands faster than slides. |
| 1.4 — Hallucinations and verification | Animated "plausible vs true" walkthrough. |
| 1.7 — When AI gets it wrong: response playbook | 4-step flow visualised. |
| 3.2 — The CRISP framework | Building up the framework letter by letter, animated. |
| 4.1 — AI Ops, what it is and why | System diagram of how AI Ops fits into Phlo. |
| 4.9 — Choosing the right tool in 30 seconds | The decision tree — perfect Excalimate content. |
| 5.5 — Anti-AI: where this should make things slower | Conceptual map of "where the human time is the point." |

**Don't use Excalimate for** the screen-share videos (most of Module 2 and Module 4), the talking-head videos (1.1 CEO, the "Watch me fail" 3.6, the "Watch me prompt" 3.3), or the demo-heavy videos (the live Project build in 2.2, the failure library walkthrough in 4.5). Loom + screen recording + face cam handles those better.

## First-time setup

1. **Drop this folder somewhere stable**, e.g. `~/phlo-learn`.

2. **Replace the placeholder colours** in `.claude/skills/phlo-learn-videos/SKILL.md`. Open the file, find the colour block near the top, and swap the placeholder HEX values for the real Phlo brand HEX codes from the design system. The placeholders work out of the box but won't match Phlo branding until you do this.

3. **Verify prerequisites**:
   ```bash
   node --version       # v18 or higher
   claude --version     # Claude Code CLI must be installed
   ```
   If Node is missing: `brew install node` (Mac) or download from nodejs.org.
   If Claude Code is missing: `npm install -g @anthropic-ai/claude-code`.

4. **Confirm scripts are executable**:
   ```bash
   chmod +x scripts/*.sh
   ```

5. **Read the curriculum document.** Before producing any video, read its full entry in `Phlo_Mandatory_AI_Course_Curriculum.docx`. Each video has its "why this exists," hook, key points, on-screen demo flow, pause-and-try moments, close line, and resources. **The curriculum entry is your script.** Don't free-style; the videos are designed to slot together.

## Recording a Mandatory AI Course video — the workflow

From this directory, one command:

```bash
./scripts/make-learn-video.sh
```

This will:
1. Check Node + Claude Code are installed
2. Start the Excalimate MCP server on `localhost:3001` in the background
3. Register the MCP with Claude Code (only on first run)
4. Open `app.excalimate.com` in your default browser — click the **Live** button there
5. Launch Claude Code in this project directory so the skill loads automatically

Then in the Claude Code session:
- Open the relevant prompt in `example-prompts/` (or write a new one — see "Writing a new prompt" below)
- Copy the prompt block (between the triple backticks)
- Paste into Claude Code
- Watch the diagram appear and animate in the Excalimate canvas tab
- Loom records the canvas as it builds, with your face cam + narration

When you're done:
```bash
./scripts/make-learn-video.sh --stop
```

## Production conventions for the Mandatory AI Course

Every video in the course follows the same structural rules. These are tighter than generic Learn videos — please honour them.

| Convention | Rule |
|---|---|
| **Length** | Hard cap 8 min. Target 3–5. The course's longest video is 3.3 (10 min) and that's deliberate. Past 5 min, completion drops sharply. |
| **Structure** | Hook (10s) → Why (30s) → Content/Demo (2–6 min) → Pause-and-try → Close (15s). Match the curriculum entry's blocks. |
| **Naming** | Filename and Loom title: `[Module].[NN] — Title`. E.g. `1.2 — What an LLM actually is`. Slug version for AI Ops: `1-2-what-an-llm-actually-is`. |
| **Captions** | **Mandatory.** Hand-corrected, not just auto-generated. Pharmacists watch with sound off at lunch. |
| **Chapters** | Loom chapters at hook / content / pause-and-try / close. Lets people skim and re-watch. |
| **Pause-and-try moments** | If the curriculum entry has pause-and-try moments listed, include them. They're the Type 1 micro-exercises that distinguish this course from passive video courses. |
| **Resources** | Each video has a Resource Card in AI Ops linking the resources from its curriculum entry. Produce the card alongside the video. |
| **Phlo-native demos** | When the video shows examples (real or simulated), use anonymised Phlo content, not stock examples. Generic demos feel like LinkedIn Learning. |
| **Refresh stamp** | The last-reviewed date is shown on-screen in the final 2 seconds. Tool-specific videos refresh every 90 days. |

## Recording priority order

The course launches on a drip-and-iterate schedule. Record in this order so the course can ship in stages:

1. **1.1 — Why this matters now (CEO/leadership talking head)** — single most important video in the whole course. Not Excalimate. Schedule this first.
2. **Module 1 in full (1.2–1.7)** — the policy and judgement videos must ship before anyone uses AI on patient data. Excalimate fits 1.2, 1.3, 1.4, 1.7. Talking-head/screen-share for 1.5 and 1.6.
3. **Module 2 (2.1–2.6)** — Claude walkthrough. Mostly screen-share, not Excalimate.
4. **Module 3** — record 3.3 (Watch me prompt) and 3.6 (Watch me fail) with proper production time. 3.2 (CRISP) is the natural Excalimate fit in this module.
5. **Module 4** — mostly screen-share for AI Ops, Copilot, and the wider stack. 4.1 and 4.9 are Excalimate fits.
6. **Module 5** — short module. 5.5 (Anti-AI) is the Excalimate fit.

The CEO video is the trigger for going live company-wide. Don't release the rest until 1.1 is recorded.

## Writing a new prompt (for course videos not yet in `example-prompts/`)

The existing example prompts in `example-prompts/` are generic Learn topics. For a Mandatory AI Course video, write a new prompt following the same pattern but driven by the curriculum entry.

Template:

```markdown
# [Module].[NN] — [Title]

**Target length:** [3-5 minutes typically; see curriculum]
**Audience:** Every Phlo employee (mandatory course)
**Goal:** [Copy from "Why this video exists" in the curriculum]
**Curriculum reference:** Module X.Y in `Phlo_Mandatory_AI_Course_Curriculum.docx`

## The prompt

```
[The Excalimate prompt — what to draw, how to animate, what the narrator will be saying over each beat. Lift the key points and on-screen demo flow from the curriculum entry verbatim. Each visual element should correspond to a narration moment.]
```

## Why this video matters

[2-3 sentences. Lifted from the "Why this video exists" in the curriculum.]

## Narration script

[Full narration, broken into beats matching the animation. Include the hook, the pause-and-try moments, and the close line — all from the curriculum entry.]

## Resources linked from this video

[From the curriculum entry's "Resources linked from this video" section.]
```

Save as `06-NN-topic-slug.md` (continuing the numbering past the existing 1–5 examples).

The narration script is doing real work for the production process — the person recording the Loom may not be the person who wrote the prompt. The script keeps the two roles aligned, and ensures the on-screen animation, the narration, and the curriculum stay consistent.

## Tips for good Mandatory AI Course videos

**Pre-write the prompt from the curriculum entry.** Each curriculum entry has the script blocks (hook, points, demo flow, pauses, close) already broken out. Lift them in order — don't reinvent the structure.

**Pick the length from the curriculum, not from feel.** The curriculum specifies each video's duration. An under-planned 5-minute video drags; an over-planned 3-minute video feels rushed. Match the duration to the curriculum.

**Loom on the canvas, not on the Claude Code window.** Record the Excalimate browser tab (or fullscreen the canvas with `F`). Your audience doesn't need to see the prompt being typed — they need to see the diagram build.

**Honour the pause-and-try moments.** When the curriculum entry says "pause and try" at a specific beat, the narration must explicitly tell the viewer to pause and try the action. Don't skip this even if it feels awkward — it's the Type 1 micro-exercise that makes the course retention-heavy.

**Show the policy when it's relevant.** Videos 1.5, 1.6, 4.6, and 5.5 reference the Phlo AI Use Policy. Show the policy one-pager on-screen at the relevant moment. Don't just mention it.

**Sanity-check the safety guardrails** before publishing Module 1 and any clinical demo. Have someone from clinical safety watch them. The skill enforces visual rules but a human pair of eyes catches content edge cases — particularly around PHI, dosing, regulated comms.

**Park unfinished videos in `videos/drafts/`** (create it if needed). Anything in `videos/` proper is treated as "ready to ship to AI Ops Learn."

## After recording: handoff to AI Ops Learn

When a video is ready:

1. **Upload to Loom** with the title in the format `[Module].[NN] — [Title]`.
2. **Hand-correct the captions.** Auto-captions aren't enough.
3. **Add Loom chapters** at hook / content / pause-and-try / close.
4. **Update the AI Ops Learn record** for that video: change `is_published` to true, paste the Loom URL, set `published_at`, set `last_reviewed_at` to today.
5. **Verify the Resource Card** linked from the video has the resources from the curriculum entry.
6. **Test the page** with a colleague who hasn't seen it. Specifically: do the pause-and-try moments work? Are the resources right? Does the next-video CTA fire?
7. **Announce in #ai-at-phlo** with one sentence on what shipped and one sentence on what changes for the team.

## Troubleshooting

- **`make-learn-video.sh` says port 3001 is in use** — Excalimate is probably already running from a previous session. Either reuse it (open `app.excalimate.com` and click Live), or kill it: `./scripts/make-learn-video.sh --stop`.
- **The canvas shows "disconnected"** — click Reconnect in the Excalimate UI. SSE connections drop occasionally.
- **Diagrams aren't using Phlo brand colours** — you haven't replaced the placeholder HEX values in `SKILL.md`. Check that file.
- **Diagrams look generic** — confirm the skill is loaded by asking Claude in the session: "What skills do you have available?" The list should include `phlo-learn-videos`. If it doesn't, you launched `claude` from the wrong directory.
- **MP4 export fails** — Excalimate exports via WebCodecs, which needs Chrome or Edge. Open `app.excalimate.com` in Chrome, not Safari or Firefox.
- **The animation runs ahead of the narration** — pause the Excalimate replay between beats while recording. The diagram is built once, then re-played for the Loom take; you control the pacing on replay.
- **Windows users** — the scripts are written for Mac/Linux. On Windows, use WSL (Windows Subsystem for Linux) or adapt to PowerShell — the `npx @excalimate/mcp-server` command works the same; only the wrapper script needs translation.

## Maintaining the bundle

When you add new example prompts, follow the existing pattern:

- Numbered filename: `06-NN-topic-slug.md` (or higher).
- For Mandatory AI Course videos specifically, the `NN` should match the course numbering (e.g. `06-1-2-what-an-llm-actually-is.md`).
- Header with target length, audience, goal, **curriculum reference**.
- The prompt itself in a fenced code block.
- Rationale ("Why this video matters") lifted from the curriculum.
- Narration script lifted from the curriculum's points, demo flow, pauses, and close.

When a course video gets updated (tool changes, policy changes, the 90-day refresh), update the prompt file alongside the new recording. Old prompt files for retired videos move to `example-prompts/_retired/` — the Dead Video List is public, and the retired prompts are useful context for what changed and why.

## Files to share when onboarding a new producer

When bringing someone else into Mandatory AI Course production:

1. This README.
2. `Phlo_Mandatory_AI_Course_Curriculum.docx` — the source of truth for every video's content.
3. The `SKILL.md` (so they can read the visual conventions).
4. Two example prompts — one Excalimate-fit course video (e.g. 1.2 once written), one generic Learn topic from the existing examples.
5. A 5-minute Loom of you actually producing a Mandatory AI Course video end-to-end with the bundle.

That last one is the highest-leverage onboarding artefact. Make it the first thing you record after this bundle is set up. Recording yourself building 1.2 (What an LLM actually is) doubles as the onboarding video and as the first piece of course content.

## Related documents

- `Phlo_Mandatory_AI_Course_Curriculum.docx` — the full curriculum, every video's script blocks, exercises, and resources. **Source of truth.**
- `Claude_Code_Prompt_Learn_Page.md` — the AI Ops Learn platform extension spec. Where the finished videos live.
- The Phlo AI Use Policy one-pager — referenced from videos 1.5, 1.6, 4.6, 5.5.
- The #ai-at-phlo Slack channel — where each shipped video gets announced.