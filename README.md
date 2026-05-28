# Phlo Learn Videos — bundle

Everything needed to produce animated explainer videos for Phlo's AI Ops Learn series.

## What's in this bundle

```
phlo-learn/
├── .claude/skills/phlo-learn-videos/
│   ├── SKILL.md                              # The Phlo skill — visual conventions, vocabulary, safety rules
│   └── example-prompts/
│       ├── 01-how-claude-reads-emails.md
│       ├── 02-what-is-mcp.md
│       ├── 03-how-granola-captures-notes.md
│       ├── 04-how-beacon-prepares-interviews.md
│       └── 05-humans-in-ai-workflows.md
├── scripts/
│   ├── start-excalimate.sh                   # Just starts the Excalimate server
│   └── make-learn-video.sh                   # Full setup: server + canvas + Claude Code
├── videos/                                   # Generated MP4s land here
└── README.md                                 # this file
```

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

## Recording a Learn video — the workflow

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
- Open one of the example prompts in `example-prompts/`
- Copy the prompt block (between the triple backticks)
- Paste into Claude Code
- Watch the diagram appear and animate in the Excalimate canvas tab
- Loom records the canvas as it builds, with your face cam + narration

When you're done:
```bash
./scripts/make-learn-video.sh --stop
```

This shuts down the Excalimate server cleanly.

## Tips for good Learn videos

**Pre-write the prompt.** The example prompts in `example-prompts/` are full-fat — they include narration scripts and rationale. For new topics, copy one as a template and adapt. The prompt itself is effectively the script — every element you ask Claude to draw is something you'll narrate.

**60 / 90 / 180 seconds — pick before you start.** Longer doesn't mean better. The skill plans element count based on the length you specify; an under-planned 180s video drags. Most Learn topics are well-served by 90s.

**Loom on the canvas, not on the Claude Code window.** Record the Excalimate browser tab (or fullscreen the canvas with `F`). Your audience doesn't need to see the prompt being typed — they need to see the diagram build.

**Sanity-check the safety guardrails** before publishing the first three videos. Have someone from clinical safety watch them. The skill enforces the rules but a human pair of eyes catches edge cases.

**Park unfinished videos in `videos/drafts/`** (create it if needed). Anything in `videos/` proper is treated as "ready to share."

## Troubleshooting

- **`make-learn-video.sh` says port 3001 is in use** — Excalimate is probably already running from a previous session. Either reuse it (open `app.excalimate.com` and click Live), or kill it: `./scripts/make-learn-video.sh --stop`.
- **The canvas shows "disconnected"** — click Reconnect in the Excalimate UI. SSE connections drop occasionally.
- **Diagrams aren't using Phlo brand colours** — you haven't replaced the placeholder HEX values in `SKILL.md`. Check that file.
- **Diagrams look generic** — confirm the skill is loaded by asking Claude in the session: "What skills do you have available?" The list should include `phlo-learn-videos`. If it doesn't, you launched `claude` from the wrong directory.
- **MP4 export fails** — Excalimate exports via WebCodecs, which needs Chrome or Edge. Open `app.excalimate.com` in Chrome, not Safari or Firefox.
- **Windows users** — the scripts are written for Mac/Linux. On Windows, use WSL (Windows Subsystem for Linux) or adapt to PowerShell — the `npx @excalimate/mcp-server` command works the same; only the wrapper script needs translation.

## Maintaining the bundle

When you add new example prompts, follow the existing pattern:
- Numbered filename: `06-topic-slug.md`
- Header with target length, audience, goal
- The prompt itself in a fenced code block
- Rationale ("Why this video matters")
- Narration script

The narration script is doing real work for the production process — the person recording the Loom may not be the person who wrote the prompt. The script keeps the two roles aligned.

## Files to share with the wider team

When onboarding someone else to produce Learn videos:
- This README
- The `SKILL.md` (so they can read the visual conventions)
- One or two example prompt files
- A 5-minute Loom of you actually producing a video end-to-end with the bundle

That last one is the highest-leverage onboarding artefact. Make it the first Learn video you produce after this bundle is set up.
