# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Production tooling for the **Phlo Mandatory AI Course** — short animated explainer videos in Phlo's "AI Ops Learn" series, watched by all staff (clinical, ops, engineering, design, commercial, support). It is **not** an application: there is nothing to deploy, no test suite, no lint step. Each "build" produces an animated diagram that gets screen-recorded (Loom) with face-cam + narration and uploaded to AI Ops Learn.

Phlo is a regulated UK digital pharmacy. The safety guardrails in the skill (below) are non-negotiable, not stylistic.

## Build & record workflow (current)

**Excalimate — the animation tool this repo was originally built around — is no longer used.** It's broken, and the team records differently now: a single hand-drawn **static** Excalidraw scene that you pan and zoom through on screen while narrating. No MCP server, no MP4 export, no keyframes.

For each video:

1. **Generate the scene with a Python script.** Each video folder has a thin `build*.py` that imports the shared engine (`from excalidraw_kit import *`), defines its scene + beat scaffold, and calls `finish(out, max_w, total_w)` to validate + write. The engine — palette, element factory, fun primitives, reusable illustrations, the validate/write tail — lives once in the repo-root `excalidraw_kit.py`; each `build*.py` holds only the composition (scene + scaffold) and any bespoke one-off illustrations. A deterministic `random.seed` keeps re-runs identical. Don't hand-place raw elements. Canonical example: `videos/claude/3-artefacts/build_excalidraw.py`.
   ```bash
   python3 videos/claude/3-artefacts/build_excalidraw.py   # build one video (finds the kit via a sys.path walk-up)
   python3 build_all.py                                    # rebuild EVERY video, then run the Style-B guard
   ```
   `finish()` self-checks before writing: palette discipline, no stray frames, text-overflow, and text/text collisions (printed as warnings). `build_all.py` rebuilds all videos and runs the **Style-B guard**, which hard-fails on the Style A signature (frames, or typed non-hand fonts) so the editorial style can never silently return; off-palette colours are warnings.

2. **Eyeball it with the PIL preview.** There's no Excalidraw CLI, so the repo-root `preview.py` rasterises a scene to a PNG — approximate (flat fills, macOS hand-font stand-ins for Excalifont) but enough to check composition, colour, overlap and text overflow without opening the app.
   ```bash
   python3 preview.py videos/claude/3-artefacts/2-3-artifacts.excalidraw out.png            # whole board
   python3 preview.py videos/claude/3-artefacts/2-3-artifacts.excalidraw out.png XMIN XMAX  # close-up x-window
   ```

3. **Record in Loom.** Open the `.excalidraw` at excalidraw.com (or the desktop app), full-screen the canvas, and pan/zoom beat-by-beat, left to right, while narrating. The beats are spaced with wide gaps (the `GAP` constant) precisely so you can frame one beat at a time on a 14" laptop without neighbours peeking in — the whitespace *is* the camera.

## Design system (current house style)

The style is **one flowing, illustrated, hand-drawn journey** — modelled on `videos/ai-foundations/1-what-is-ai/llm_explainer.excalidraw` (the preferred reference) and pushed further toward "fun and visual". The canonical build is `videos/claude/3-artefacts/`. Rules:

- **No frames, no boxes.** One continuous left-to-right canvas, not a row of bordered slides. Beats are separated by whitespace + a connector spine, never by rectangles.
- **White background** (`viewBackgroundColor: #ffffff`).
- **All text hand-drawn** in Excalifont (`fontFamily: 5`), `roughness: 1` on everything. No typed sans/mono — the hand-drawn line is the whole point.
- **Lively Excalidraw palette**, colour-coded per beat: violet / orange / green / blue / red / teal / yellow / indigo strokes, each with a matching pastel fill. This deliberately replaces the old restrained "Riso Workshop" four-colour palette, which read as flat and boring.
- **Fun applied in dose order:** heavy colour-blocking (highlighter sweeps, pastel sticky notes) + scribbled annotations (underlines, circled words, freehand arrows, sparkles, strike-throughs) do the heavy lifting; charming primitive illustrations (sketched Claude face, chat-left/Artifact-panel-right window, colour-coded object doodles) on hero beats; light rotation jitter on notes/chips. Prefer hand-drawn icons over emoji.
- **A load-bearing connector spine** — wavy hand-drawn arrows across the gaps — threads the beats so the whole thing reads as one picture, not "boxes minus the borders."

Keep British English, hyphens not em-dashes, fictional identifiers only, and the SKILL.md vocabulary (Claude / Granola / Beacon / Patient are proper nouns).

## Legacy Excalimate pipelines (kept for reference, not used)

Earlier videos were authored by driving Excalimate. These are retained as historical reference but are **not** the current workflow:

1. **Live MCP build (`build.mjs`)** — a Node script that pushed elements + keyframes + camera frames live onto the Excalimate canvas over HTTP. Example: `videos/ai-foundations/2-ai-benefits-and-cons/build.mjs`.
2. **Compile-from-files (`scripts/compile_excalimate.py`)** — compiled a static `.excalidraw` + a `.excalimate.json` animation plan into a `.checkpoint.json` for the Excalimate UI. Example trio: `videos/ai-foundations/1-what-is-ai/llm_explainer.{excalidraw,excalimate.json,checkpoint.json}`.

The launcher scripts `scripts/make-learn-video.sh` and `scripts/start-excalimate.sh` start the `@excalimate/mcp-server` MCP and belong to these legacy pipelines only.

**The shared engine lives in the repo-root `excalidraw_kit.py`; build scripts import it.** This replaced the older "each build is self-contained and embeds its own helpers" convention — the engine was duplicated across videos and copies drifted (it's how a couple of off-style files once crept in). Now: the *look* (palette, primitives, illustrations, validate/write) is centralised in the kit; each video's `build*.py` keeps only its *composition* (scene + the per-video beat scaffold: `OX`/`WID`/`ACCENT`, `beat_head`, the connector spine) plus any bespoke one-off illustrations. When adding a new video, copy the closest existing `build*.py` as a scene template — it already imports the kit. A change to the kit re-styles every video on next `build_all.py`; the design is intended to be stable, so kit edits are rare and deliberate.

## File layout

```
excalidraw_kit.py             # shared Style B engine: palette, factory, primitives, illustrations, validate/finish
build_all.py                  # rebuild every video + run the Style-B guard
preview.py                    # PIL rasteriser for eyeballing a scene (takes a scene path + optional x-window)
videos/<series>/<NN-slug>/    # one folder per video; thin build*.py + .excalidraw + plan/script live together
.claude/skills/SKILL.md       # the phlo-learn-videos skill (visual + safety conventions)
scripts/                      # session launchers + compile_excalimate.py
```

Series seen so far: `ai-foundations/` (Module 1 concepts), `claude/` (Module 2 Claude walkthrough), and a stubbed `copilot/`. Each video folder also tends to hold a narration/voiceover script (`*.md` or `*-script`) and an `animation-plan.md` documenting the build so it can be rebuilt or re-exported by hand. Many `NN-slug` folders are **empty placeholders** for planned-but-unbuilt videos (e.g. `ai-foundations/3-context-windows/`, `claude/4-skills/` through `claude/9-claude-word/`, `claude/cowork/`) — an empty folder means "not started", not "lost work".

## Non-negotiable conventions (from `.claude/skills/SKILL.md`)

Read `.claude/skills/SKILL.md` in full before authoring a diagram. The hard rules:

- **Brand colours are placeholders.** The HEX block in `SKILL.md` and the palette constants at the top of each `build.mjs`/`build_excalidraw.py` are placeholder values, **not** real Phlo brand colours, until someone swaps in the design-system hex codes. Don't assume the on-screen palette is final.
- **Safety (regulated pharmacy):** no real patient identifiers (use `Patient_001`, `J. Doe`, `NHS_TEST_123`); always draw the human verification gate on any clinical/dispensing/records workflow; AI never writes to patient records directly (AI drafts → human approves → record updates); label MHRA/GPhC/CQC steps; no UI screenshots — diagrams are abstractions.
- **Vocabulary is fixed:** "Phlo" not "we/us"; "Patient" not "user/customer"; "Claude"/"Granola"/"Beacon"/"MCP"/"Claude Code" are proper nouns with exact capitalisation.
- **Pacing is now manual.** With static scenes recorded by panning, "animation" means the camera move you perform live in Loom — reveal each beat by panning to it, hold ~3s of narration per beat, left-to-right. The SKILL.md "Animation defaults" (stagger, `drawProgress`, keyframes, MP4 export) describe the **legacy Excalimate** flow only and don't apply to static builds.

## Notes / known drift

- The skill lives at `.claude/skills/SKILL.md` (skill name is still `phlo-learn-videos`) and work is organised under `videos/<series>/<NN-slug>/`. README and SKILL.md have both been brought in line with this and with the static/flowing workflow.
- `Phlo_Mandatory_AI_Course_Curriculum.docx` is the course's source of truth for every video's script blocks, but it is **not** checked into this repo — ask for it before authoring content.
- **Ownership, to stop drift recurring:** `.claude/skills/SKILL.md` owns the drawing rules, safety guardrails, and vocabulary; `README.md` owns the human production workflow; this file is the operating map and cross-references the other two rather than restating them. SKILL.md uses the lively non-brand Excalidraw palette deliberately — there is no "replace the brand hex" step.
- `scripts/compile_excalimate.py` (legacy) hardcodes `llm_explainer.*` paths relative to repo root.
- **Module 2 Claude videos in active build** use Style B `build_*.py` scripts that live next to their video (output filename is named in the folder's `*_prompt`): `videos/claude/1-claude-intro/build_claude_interface.py` → `claude-interface-properly.excalidraw`; `videos/claude/2-projects/build_projects.py` → `phlo-2.2-claude-projects.excalidraw`. Both write output via `os.path.dirname(__file__)` (lands in-folder) and reference the shared rasteriser as `../3-artefacts/preview.py`. The Projects video was **converted from a rejected frame-based "Style A" deck** (10 fixed `1920x1080` frames, purple/lilac palette); that old generator (`build_projects_2_2.py`) has been deleted — do not reintroduce a frame-based build.
- `videos/claude/1-claude-intro/` has a single canonical scene, `claude_intro.excalidraw`, generated by `build_claude_interface.py`. (The script's docstring + `claude_intro_prompt.md` still say `claude-interface-properly.excalidraw`; the live `out =` target is `claude_intro.excalidraw` — trust the code. Regenerate from the script; don't keep a second hand-named copy.)
- Several `*_prompt`/`*_prompt.md` files (e.g. `1-claude-intro/claude_intro_prompt.md`) still describe the **old editorial Style A** (fontFamily 2, five `1600x1000` frames, purple brand palette). The shipped build scripts are Style B; trust the `build_*.py` + script over the prompt file when they disagree.
```
