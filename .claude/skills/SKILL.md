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

- **No frames, no boxes.** One continuous canvas. Beats are separated by whitespace and a **connector spine** (a wavy hand-drawn arrow threading the beats), never by rectangles.
- **White background.** All text hand-drawn in **Excalifont** (`fontFamily: 5`), `roughness: 1` on everything. No typed sans/mono.
- **Lively colour, coded per beat** — violet / orange / green / blue / red / teal / yellow / indigo strokes, each with a matching pastel fill. This is a deliberate house palette, **not** Phlo brand colours — do not "correct" it to brand hex.
- **Fun in dose order:** heavy colour-blocking (highlighter sweeps, pastel sticky notes) + scribbled annotations (underlines, circled words, freehand arrows, sparkles, strike-throughs) do the heavy lifting; charming primitive illustrations on hero beats; light rotation jitter on notes/chips. Prefer hand-drawn icons over emoji.
- **Wide gaps between beats** (the `GAP` constant) so a single beat frames cleanly on a 14" laptop while recording — the whitespace is the camera.

### Safety-bearing visual markers (must survive the house style)

These three markers carry the regulatory semantics below — keep them legible in every diagram, drawn in the hand-drawn style:

- **AI / automated step** → mark with a sparkle `✦` and a dashed/sketchy outline so it reads as "done by AI", not by a person.
- **Human-in-loop step** → mark with a person glyph / "👤"-equivalent hand-drawn figure or a solid checkmark gate, so the human decision point is unmistakable.
- **Regulated / clinical-safety step** → draw in **red** and label the regulator inline ("MHRA", "GPhC", or "CQC"). Never hide a regulated step inside a generic-coloured beat.

### Layout & legibility

- Left-to-right reading order. Roughly one beat per ~3s of narration; plan beat count to the target length.
- Keep critical content away from the extreme edges — Loom and embeds crop.
- Minimum text size large enough to read on a phone; these play on small screens.

## Pacing (manual, in Loom)

There is no timeline. "Animation" = the camera move the presenter performs while recording: reveal each beat by **panning to it**, hold for the narration, move left-to-right, and end framed on the final beat so it can be paused on. Plan the scene so panning beat-by-beat tells the story in order.

## Vocabulary (use these exact terms)

| Use | Avoid |
|---|---|
| Phlo | "we", "the company", "us" |
| Patient | user, customer, end-user |
| Pharmacist | unless precision needed, then "Responsible Pharmacist" or "PIC" |
| Repeat prescription | refill, re-order |
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

1. **Confirm the slug**: derive a kebab-case topic slug and its `videos/<series>/<NN-slug>/` folder (e.g. "Claude Projects", module 2.2 → `videos/claude/2-projects/`). State it in your response.
2. **Plan the beats**: list the beats in narration order before generating — one line each. This is the left-to-right journey.
3. **Generate the scene with a self-contained `build_excalidraw.py`** in that folder, following the house style above. Copy the closest existing build script (canonical: `videos/claude/3-artefacts/`) and adapt — each script embeds its own helpers + palette; nothing is shared.
4. **Eyeball it with `preview.py`** (rasterises to PNG). Fix palette drift, text overflow, and any caption/caption collisions it warns about.
5. **Confirm** the output `.excalidraw` path and the beat count, so the user knows roughly how long the pan-through narration will run.

If the target length isn't given, ask once ("Roughly how long — 3, 5, or 7 minutes?") and plan the beat count accordingly (~1 beat per 3s of narration).

## When NOT to use this skill

- A diagram for engineering documentation (use a standard architecture-diagram approach, not this house style).
- A diagram for a customer-facing surface (different brand rules apply).
- A diagram for an external presentation to investors, regulators, or partners (those need design-team review, not skill output).
- Videos that aren't explainer diagrams at all — talking-head, screen-share demos, "watch me fail/prompt" — those are recorded directly, with no diagram. See `README.md` for which course videos are diagram-fit.
