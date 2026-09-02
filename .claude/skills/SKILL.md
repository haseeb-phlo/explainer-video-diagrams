---
name: phlo-learn-videos
description: Generate illustrated explainer diagrams for Phlo's AI Ops Learn series. Use whenever creating short explainer video content about AI tools, AI concepts, or AI-augmented workflows intended for training Phlo staff (pharmacists, operations, engineering, design, commercial, customer support). Triggered by phrases like "Learn video", "explainer", "training diagram", "Phlo AI Ops", or any request to make a diagram for internal Phlo education.
---

# Phlo Learn Video Diagrams

You are producing the diagrams for short (≈3–7 minute) explainer videos in Phlo's AI Ops "Learn" series. These videos are watched by everyone at Phlo — clinical, ops, engineering, design, commercial, customer support. Default to plain-English labels over jargon. If you must use a technical term, also show a short plain-English gloss.

This skill owns the **drawing rules, safety guardrails, and vocabulary**. The human production workflow (record-in-Loom, handoff, course conventions) lives in `README.md`; the repo operating map for the agent lives in `CLAUDE.md`.

## How these videos are made now (read first)

A video is **one hand-drawn, frameless Excalidraw scene** that the presenter pans and zooms through on screen while narrating. It is generated programmatically by a per-video `build_excalidraw.py`, eyeballed with `preview.py`, then recorded in Loom. There is no animation engine, no keyframes, and no MP4 export — **the camera move is performed live by the presenter**. (The repo's old Excalimate animation pipeline is dead; ignore it.)

## Visual conventions — the house style

The style is **one flowing, illustrated, hand-drawn journey**, left to right — not a row of bordered slides. Canonical reference: `videos/claude/3-artefacts/`.

- **No frames, no boxes, no connector spine.** One continuous canvas; beats are separated by whitespace only. No wavy through-line, no inter-beat arrows, no baseline, and no colour-band washes behind beats — the white background stays white.
- **White background.** All text hand-drawn in the **Virgil hand font** (`fontFamily: 1`, the kit's `HAND`), `roughness: 1`, `lineHeight: 1.4`. No typed sans/mono.
- **Lively colour, coded per beat** — violet / orange / green / blue / red / teal / yellow / indigo strokes, each with a matching pastel fill and ultra-light tint. A deliberate house palette, **not** Phlo brand colours — do not "correct" it to brand hex. Colour comes from **vivid elements** (accent headings, saturated stickies, coloured illustrations), not background panels.
- **Prominent but unpolished headings** via the kit's `heading()`: a big hand title in the beat's accent colour with a hand-drawn underline. **No step-number circle, no highlighter sweep behind the title, and no decorative sparkles/twinkles anywhere** (they read as AI slop). Body/explanation text stays ink/grey for legibility.
- **Charming primitive illustrations** carry the visual interest on hero beats; light rotation jitter on notes/chips. Prefer hand-drawn icons over emoji.
- **Uniform beat dimensions:** every beat occupies the same slot — content ≈ 1120 × 980 (~1.15 : 1, the "Words left, a thing right" shape), `GAP = 800` — so each frames identically and fits a 14" laptop. Stack pairs vertically and grids into ~square layouts instead of spreading wide.
- **Live-demo cut-aways:** mark each cut to the live app with `demo_badge(x, y, "show in Claude desktop app: …")` on the board and `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` in the script.

### Safety-bearing visual markers (must survive the house style)

These three markers carry the regulatory semantics below — keep them legible in every diagram, drawn in the hand-drawn style:

- **AI / automated step** → mark with a dashed/sketchy outline (and an accent colour) so it reads as "done by AI", not by a person. (No sparkles — they're banned as decoration.)
- **Human-in-loop step** → mark with a person glyph / "👤"-equivalent hand-drawn figure or a solid checkmark gate, so the human decision point is unmistakable.
- **Regulated / clinical-safety step** → draw in **red** and label the regulator inline ("MHRA", "GPhC", or "CQC"). Never hide a regulated step inside a generic-coloured beat.

### Layout & legibility

- Left-to-right reading order. Roughly one beat per ~3s of narration; plan beat count to the target length.
- Keep critical content away from the extreme edges — Loom and embeds crop.
- Minimum text size large enough to read on a phone; these play on small screens.

## Pacing (manual, in Loom)

There is no timeline. "Animation" = the camera move the presenter performs while recording: reveal each beat by **panning to it**, hold for the narration, move left-to-right, and end framed on the final beat so it can be paused on. Plan the scene so panning beat-by-beat tells the story in order.

## Vocabulary (use these exact terms)

**Examples are GENERIC, not Phlo-specific.** Diagrams and scripts use everyday business scenarios (a customer reply, a budget calculator, a team tone guide, Support / Ops) and carry no Phlo branding/logo and no patient/clinical specifics — so a video is reusable. The pharmacy-specific terms below (Patient, Pharmacist, Repeat prescription, Granola, Beacon, AI Ops) apply ONLY if a video is genuinely about a Phlo clinical workflow; for the general Claude/AI-literacy videos, prefer the generic equivalents.

| Use | Avoid |
|---|---|
| your team / the team (generic) | naming Phlo in on-screen examples |
| customer (generic example) | patient, unless the video is a real clinical workflow |
| Pharmacist (clinical videos only) | unless precision needed, then "Responsible Pharmacist" or "PIC" |
| Claude | "the AI", "the model", "AI" alone |
| Granola | "the notes tool", "transcription" |
| Beacon | "discovery tool", "the pre-interview thing" |
| AI Ops | "the AI team", "AI rollout" |

Capitalisation matters — Claude, Granola, Beacon, MCP are all proper nouns. "Claude code" is wrong; "Claude Code" is right. British English; hyphens, not em-dashes.

## Safety guardrails (non-negotiable, Phlo is regulated)

These must hold for every diagram:

1. **No real patient identifiers.** Use obviously fictional placeholders: `Patient_001`, `J. Doe`, `NHS_TEST_123`, `acme.pharmacy@example.com`. Never plausible-looking real names.

2. **Always show the human verification gate** (the human-in-loop marker above) in any workflow that touches clinical decisions, dispensing, prescriptions, or patient records. Even a simplified diagram must not imply an AI makes unsupervised clinical decisions. If a workflow legitimately has no human gate (e.g. AI summarising internal Slack), that's fine — the rule is "show it when it exists".

3. **AI never writes directly to patient records.** Draw AI as drafting → human approves → record updated. Any arrow from an AI step to a data store must pass through a human-in-loop marker.

4. **Regulator visibility.** If a step is governed by MHRA, GPhC, or CQC, use the red regulated marker and name the regulator. Don't bury the regulatory layer in a generic beat.

5. **No screenshots of internal tools.** Diagrams are abstractions, not UI mockups. If asked for a UI-style diagram, push back and offer an abstracted version. (A stylised, obviously-hand-drawn "Claude window" illustration on a hero beat is fine — a faithful screenshot is not.)

## Output behaviour (what to do when asked for a Learn diagram)

When the user requests a Learn diagram, execute this sequence:

1. **Confirm the slug**: derive a kebab-case topic slug and its `videos/<series>/<NN-slug>/` folder (e.g. "Claude Projects", Day 4 of the AI training → `videos/ai-training/4-projects/`). State it in your response.
2. **Plan the beats**: list the beats in narration order before generating — one line each. This is the left-to-right journey.
3. **Generate the scene with a thin `build*.py`** in that folder that does `from excalidraw_kit import *` (the shared engine: palette, primitives, illustrations, `heading()`, `finish()`), then defines the scene + its per-video scaffold and calls `finish(out, max_w, total_w)`. Copy the closest existing build (canonical: `videos/claude/3-artefacts/`) as a template — the *look* is centralised in the kit; only the scene is per-video. Keep beats to the uniform ~1120×980 slot.
4. **Eyeball it with the repo-root `preview.py`** (rasterises to PNG; pass the scene path), then run `python3 build_all.py` — it rebuilds every video and runs the Style-B guard (hard-fails on frames / non-hand fonts / off-palette). Fix overflow and any collisions it warns about.
5. **Confirm** the output `.excalidraw` path and the beat count, so the user knows roughly how long the pan-through narration will run.

If the target length isn't given, ask once ("Roughly how long — 3, 5, or 7 minutes?") and plan the beat count accordingly (~1 beat per 3s of narration).

## When NOT to use this skill

- A diagram for engineering documentation (use a standard architecture-diagram approach, not this house style).
- A diagram for a customer-facing surface (different brand rules apply).
- A diagram for an external presentation to investors, regulators, or partners (those need design-team review, not skill output).
- Videos that aren't explainer diagrams at all — talking-head, screen-share demos, "watch me fail/prompt" — those are recorded directly, with no diagram. See `README.md` for which course videos are diagram-fit.
