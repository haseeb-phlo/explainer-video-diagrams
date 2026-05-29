---
name: phlo-learn-videos
description: Generate animated diagrams for Phlo AI Ops Learn series. Use whenever creating short explainer video content about AI tools, AI concepts, or AI-augmented workflows intended for training Phlo staff (pharmacists, operations, engineering, design, commercial, customer support). Triggered by phrases like "Learn video", "explainer", "training diagram", "Phlo AI Ops", or any request to make an animated diagram for internal Phlo education.
---

# Phlo Learn Video Diagrams

You are producing diagrams for short (60–180 second) animated explainer videos in Phlo's AI Ops "Learn" series. These videos run inside Phlo and are watched by everyone — clinical, ops, engineering, design, commercial, customer support. Default to plain-English labels over jargon. If you must use a technical term, also show a short plain-English gloss.

## CRITICAL — colours to replace before first use

These placeholder values keep the workflow working out of the box. **Replace them with the real Phlo brand HEX codes from the design system before publishing any video.**

```
PRIMARY      = #1E8E7A   (placeholder teal — replace with Phlo brand primary)
SECONDARY    = #0F3D3E   (placeholder deep teal — replace with Phlo brand secondary)
ACCENT       = #F4A261   (placeholder warm orange — replace with Phlo brand accent)
NEUTRAL_BG   = #FAFAF7   (off-white background)
NEUTRAL_INK  = #1A1A1A   (text colour, near-black not pure black)
REGULATED    = #C44545   (red — clinical/regulated step indicator, do not change)
SUCCESS      = #2E7D5B   (green for positive outcomes, only when needed)
```

## Visual conventions (apply these to every diagram)

Element types are recognisable at a glance because their shape + border tells you what they are:

- **Patient-facing surface** → rounded rectangle, PRIMARY fill, white text
- **Internal Phlo staff surface** → sharp rectangle, SECONDARY fill, white text
- **AI / automated step** → dashed border, NEUTRAL_BG fill, prefix label with sparkle marker `✦`
- **Human-in-loop step** → solid 2px black border, NEUTRAL_BG fill, small person glyph or "👤" before label
- **Regulated / clinical-safety step** → red (REGULATED) dashed border, label includes the relevant regulator: "MHRA", "GPhC", or "CQC"
- **Data store / record** → cylinder shape, SECONDARY fill
- **External system** (NHS, GP surgery, courier) → rectangle with double-line top, NEUTRAL_BG fill

Arrows:
- Always labelled with the **action verb** (e.g. "verifies", "drafts", "approves", "sends"). Never an unlabelled line.
- Forward flow → solid arrow
- Optional / conditional path → dashed arrow with the condition labelled mid-line
- Loop-back / iteration → curved arrow

Layout:
- Left-to-right reading order by default; top-to-bottom only if showing layered abstractions
- Max 7 visible elements at any one time (cognitive load limit for video)
- 16:9 canvas at 1920×1080; keep critical elements inside the centre 80% (avoid edges — Loom and embeds crop)
- Minimum text size: 24pt — videos play on phones, smaller text becomes unreadable

## Animation defaults

Every Learn video diagram is animated, not static:

- **Sequence reveal is mandatory** — never show the whole diagram from frame one
- **Stagger** between reveals: 600–800ms (matches calm narration pace)
- **Hold per element**: 3 seconds of narration per major element — plan element count around video length (60s ≈ 5 elements, 180s ≈ 12 elements broken into reveal groups)
- **Camera moves**: gently pan/zoom to centre the currently revealed element. Camera should never be jarring.
- **Final state**: hold the full diagram for 2 seconds at the end before clip ends, so it can be paused on
- **Easing**: `easeOutCubic` for reveals, `easeInOutQuad` for camera moves — avoid linear or bouncy easing

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

Capitalisation matters — Claude, Granola, Beacon, MCP are all proper nouns. "Claude code" is wrong; "Claude Code" is right.

## Safety guardrails (non-negotiable, Phlo is regulated)

These must hold for every diagram:

1. **No real patient identifiers.** Use obviously fictional placeholders: `Patient_001`, `J. Doe`, `NHS_TEST_123`, `acme.pharmacy@example.com`. Never plausible-looking names.

2. **Always show the human verification gate** in any workflow that touches clinical decisions, dispensing, prescriptions, or patient records. Even simplified diagrams must not imply an AI is making unsupervised clinical decisions. If a workflow legitimately has no human gate (e.g. an AI just summarising internal Slack), that's fine — the rule is "show it when it exists".

3. **AI never writes directly to patient records.** Draw AI as drafting → human approves → record updated. The arrow from AI to the data store must go through a human-in-loop node.

4. **Regulator visibility.** If a step is governed by MHRA, GPhC, or CQC, label it. Don't hide the regulatory layer behind generic boxes.

5. **No screenshots of internal tools.** Diagrams are abstractions, not UI mockups. If asked for a UI-style diagram, push back and offer an abstracted version instead.

## Output behaviour (what to do when asked for a Learn diagram)

When the user requests a Learn diagram, execute this sequence:

1. **Confirm the slug**: derive a kebab-case topic slug from the request (e.g. "How Claude reads emails" → `how-claude-reads-emails`). State the slug in your response.
2. **Plan the reveal sequence**: list the elements in narration order before generating. Brief 1-line description per element.
3. **Generate the static diagram** following the conventions above.
4. **Add sequence reveal animation** with 600–800ms stagger and the easing rules above.
5. **Add camera focus moves** to track the active element.
6. **Export as MP4** at 1920×1080.
7. **Save to** `~/phlo-learn/videos/[slug].mp4`.
8. **Confirm** the full file path in your response, plus the total duration of the animation, so the user knows whether it fits their target Loom length.

If the user has not specified a target video length, ask once: "What's the target length — 60s, 90s, or 180s?" Then plan element count accordingly.

## When NOT to use this skill

Don't apply these conventions if the user is asking for:
- A diagram for engineering documentation (use the standard mermaid/architecture-diagrams skill)
- A diagram for a customer-facing surface (different brand application rules)
- A diagram for an external presentation to investors, regulators, or partners (those need design team review, not skill output)
- A static screenshot to embed in a Confluence page (use the regular Excalidraw MCP, not Excalimate)
