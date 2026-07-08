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

2. **Eyeball it with the PIL preview.** There's no Excalidraw CLI, so the repo-root `preview.py` rasterises a scene to a PNG — approximate (flat fills, macOS hand-font stand-ins for the Virgil hand font) but enough to check composition, colour, overlap and text overflow without opening the app.
   ```bash
   python3 preview.py videos/claude/3-artefacts/3-artifacts.excalidraw out.png            # whole board
   python3 preview.py videos/claude/3-artefacts/3-artifacts.excalidraw out.png XMIN XMAX  # close-up x-window
   ```

3. **Record in Loom.** Open the `.excalidraw` at excalidraw.com (or the desktop app), full-screen the canvas, and pan/zoom beat-by-beat, left to right, while narrating. The beats are spaced with wide gaps (the `GAP` constant) precisely so you can frame one beat at a time on a 14" laptop without neighbours peeking in — the whitespace *is* the camera.

## Design system (current house style)

The style is **one flowing, illustrated, hand-drawn journey** — modelled on `videos/ai-foundations/1-what-is-ai/llm_explainer.excalidraw` (the preferred reference). The canonical build is `videos/claude/3-artefacts/`. Rules:

- **No frames, no boxes.** Beats are separated by whitespace only. **No connector spine / no inter-beat arrows / no baseline** — beats read as one picture through consistent shape and rhythm, not a wavy through-line (removed: it read as clutter).
- **White background** (`viewBackgroundColor: #ffffff`). **No colour-band washes behind beats** — the background stays white; colour comes from the *elements*.
- **All text hand-drawn** in the Virgil hand font (`fontFamily: 1`, the kit's `HAND`), `roughness: 1`, `lineHeight: 1.4` (roomy). No typed sans/mono.
- **Lively Excalidraw palette**, colour-coded per beat: violet / orange / green / blue / red / teal / yellow / indigo strokes, each with a matching pastel fill and an ultra-light tint. Colour comes from **vivid elements** — accent headings, saturated sticky notes, coloured illustrations — not from background panels.
- **Prominent but unpolished headings.** A big hand title in the beat's accent colour with a lively hand-drawn underline. **No step-number circle, no highlighter sweep behind the title, and no decorative sparkles/twinkles anywhere** (they read as AI slop). Use the kit's `heading()`.
- **Charming primitive illustrations** (sketched Claude face, chat-left/Artifact-panel-right window, colour-coded object doodles) carry visual interest on hero beats; light rotation jitter on notes/chips. Prefer hand-drawn icons over emoji.
- **Uniform beat dimensions.** Every beat occupies the SAME slot — content ≈ 1120 wide × 980 tall (~1.15 : 1, the shape of the "Words left, a thing right" beat), `GAP = 800` between slots — so each beat frames identically and fits a 14" MacBook screen when you pan to it. Stack side-by-side pairs vertically and grids into ~square layouts rather than spreading wide; an inherently-wide flow/diagram beat may run a little wider, within reason. Body/explanation text stays ink/grey for legibility; accents are for headings, labels, shapes and fills.
- **Live-demo cut-aways.** Where the presenter drops out to the live Claude desktop app, mark it on the board with a `demo_badge(x, y, "show in Claude desktop app: …")`, and use `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` cues in the matching script. The flowing per-beat layout supports cutting away and returning to the same beat with no structural change.

Keep British English, hyphens not em-dashes, and fictional identifiers only. **Examples must be generic, not Phlo-specific** — no Phlo branding/logo, and no patient/clinical specifics. Use everyday business scenarios (a customer reply, a budget calculator, a team tone guide, Support / Ops) so a video is reusable. Product proper nouns stay exact: Claude, Artifact, Project, Skill, MCP, Connector, Cowork, Claude Desktop. (This supersedes SKILL.md's older "use *Patient*" vocabulary rule.)

## Legacy Excalimate pipelines (kept for reference, not used)

Earlier videos were authored by driving Excalimate. These are retained as historical reference but are **not** the current workflow:

1. **Live MCP build (`build.mjs`)** — a Node script that pushed elements + keyframes + camera frames live onto the Excalimate canvas over HTTP. Example: `videos/ai-foundations/2-ai-benefits-and-cons/build.mjs`.
2. **Compile-from-files (`scripts/compile_excalimate.py`)** — compiled a static `.excalidraw` + a `.excalimate.json` animation plan into a `.checkpoint.json` for the Excalimate UI. Example trio: `videos/ai-foundations/1-what-is-ai/llm_explainer.{excalidraw,excalimate.json,checkpoint.json}`.

The launcher scripts `scripts/make-learn-video.sh` and `scripts/start-excalimate.sh` start the `@excalimate/mcp-server` MCP and belong to these legacy pipelines only.

**The shared engine lives in the repo-root `excalidraw_kit.py`; build scripts import it.** This replaced the older "each build is self-contained and embeds its own helpers" convention — the engine was duplicated across videos and copies drifted (it's how a couple of off-style files once crept in). Now: the *look* (palette, primitives, illustrations, validate/write) is centralised in the kit; each video's `build*.py` keeps only its *composition* (scene + the per-video beat scaffold: `OX`/`WID`/`ACCENT`, `beat_head`) plus any bespoke one-off illustrations. When adding a new video, copy the closest existing `build*.py` as a scene template — it already imports the kit. A change to the kit re-styles every video on next `build_all.py`; the design is intended to be stable, so kit edits are rare and deliberate.

## File layout

```
excalidraw_kit.py             # shared Style B engine: palette, factory, primitives, illustrations, validate/finish
build_all.py                  # rebuild every video + run the Style-B guard
preview.py                    # PIL rasteriser for eyeballing a scene (takes a scene path + optional x-window)
videos/<series>/<NN-slug>/    # one folder per video; thin build*.py + .excalidraw + plan/script live together
.claude/skills/SKILL.md       # the phlo-learn-videos skill (visual + safety conventions)
scripts/                      # session launchers + compile_excalimate.py
```

Series seen so far: `ai-foundations/` (Module 1 concepts), `claude/` (Module 2 Claude walkthrough), and a stubbed `copilot/`. Each video folder also tends to hold a narration/voiceover script (`*.md` or `*-script`) and an `animation-plan.md` documenting the build so it can be rebuilt or re-exported by hand. As of 2026-06-04 **all twelve `claude/` videos (1-12) have a Style-B `build*.py` + `.excalidraw`**; the two built `ai-foundations/` videos have Style-B-guard-clean `.excalidraw` scenes but no `build*.py` (they were authored by hand / via the legacy pipelines); the only remaining **empty placeholder** is `ai-foundations/3-context-windows/` — an empty folder means "not started", not "lost work".

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
- `scripts/compile_excalimate.py` (legacy) hardcodes the `llm_explainer.*` paths under `videos/ai-foundations/1-what-is-ai/`.
- **All twelve Module 2 Claude videos are built** with Style B `build_*.py` scripts that live next to their video and write output via `os.path.dirname(__file__)` (lands in-folder): `1-claude-intro/build_claude_interface.py` → `claude_intro.excalidraw`; `2-projects/build_projects.py` → `phlo-2.2-claude-projects.excalidraw`; `3-artefacts/build_excalidraw.py`, then `build_skills_training.py`, `build_scheduled_tasks.py`, `build_connectors_mcp.py`, `build_powerpoint.py`, `build_excel.py`, `build_word.py`, `build_web_extension.py`, `build_cowork.py`, `build_design.py`. The Projects video was **converted from a rejected frame-based "Style A" deck** (10 fixed `1920x1080` frames, purple/lilac palette); that old generator (`build_projects_2_2.py`) has been deleted — do not reintroduce a frame-based build.
- `videos/claude/1-claude-intro/` has a single canonical scene, `claude_intro.excalidraw`, generated by `build_claude_interface.py`. Regenerate from the script; don't keep a second hand-named copy.
- Several `*_prompt`/`*_prompt.md` files (e.g. `1-claude-intro/claude_intro_prompt.md`) still describe the **old editorial Style A** (fontFamily 2, five `1600x1000` frames, purple brand palette). The shipped build scripts are Style B; trust the `build_*.py` + script over the prompt file when they disagree.
```
