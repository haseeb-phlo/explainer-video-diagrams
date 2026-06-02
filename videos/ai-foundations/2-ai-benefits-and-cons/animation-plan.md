# Phlo AI Training - Video 1.3 · Animation Plan
**"What AI is good at, what it's bad at"**

Built **live** against the Excalimate MCP server (`localhost:3001`, v0.4.1). The scene + full timeline already exist in Excalimate - this file documents the build so it can be re-exported, tweaked, or rebuilt by hand.

- **Scene checkpoint:** `phlo_v1_3_final` (Excalimate → load checkpoint)
- **Source of truth / rebuild script:** `build.mjs` (this folder) - with Excalimate live: `node build.mjs scene1`, then `rest`, `verify`, `finalize`, `dump <file>`
- **Static `.excalidraw`:** `phlo-ai-1.3.excalidraw` (this folder) - fully-assembled final state, opens in any Excalidraw editor.

## Canvas & camera
- **Aspect ratio:** 16:9. Camera width **1700** scene-units (height ≈ 956). Camera centre Y = **470**.
- **Layout:** 7 scenes laid out left→right, centres at **x = 1000 + (n−1)·2400**. The camera holds on each scene then pans (`translateX`, `easeInOutCubic`, ~1.6 s) to the next at its narration cue.
- **Total timeline / clip:** 0 – **300 000 ms** (5:00). Reveals land on the cue; static holds fill the gaps where the presenter is still talking.
- **Verified:** at every scene's settled time, 100 % of that scene's elements are in-frame and no neighbouring scene bleeds in (S1 21, S2 34, S3 13, S4 17, S5 18, S6 22, S7 6 = 131 elements).

## Palette (assumption noted below)
Green `#2f9e44` · Amber `#f08c00` · Red `#e03131` · Ink `#1e1e1e` · Grey `#868e96` · Blue accent `#1971c2`.
Soft tints: green `#ebfbee`, amber `#fff9db`, red `#fff5f5`, paper `#f8f9fa`. Font: **Excalifont** (`fontFamily: 5`), high roughness.

> **Brand assumption:** the repo's UI theme is a monochrome neutral (oklch greys) with no distinctive brand green/amber, so the prompt's traffic-light palette was used as-is. Swap the six constants at the top of `build.mjs` if Phlo has official hex values.

## Reveal technique
`drawProgress` is **lines/arrows only**, so it's reserved for genuinely drawn marks: the Scene 1 underline, Scene 3 strike-throughs, Scene 5 tick/cross, Scene 6 row-lines + pointer arrow, Scene 7 underline. **All text reveals use staggered `opacity` fades** (handwriting-style "type out" in Scene 5 is opacity-staggered bullets). Individual reveals are 350–900 ms with `easeOut`/`easeInOut`.

---

## Scene-by-scene (times are absolute ms; +offset = scene start)

### Scene 1 - Hook: confidence ≠ accuracy · 0:00–0:30 (offset 0)
1. `+0.2s` Robot "Your AI intern" fades in (grouped).
2. `+1.2s` Both gauges (dials + labels + MAX/low marks) fade in.
3. `+1.7→3.4s` **Confidence** needle sweeps low-left → MAX and **locks** (`easeOutBack`), held pinned to end.
4. `+1.4s→` **Accuracy** needle jitters between low and mid (10 oscillating rotation keyframes, `easeInOut`).
5. `+4.0s` Caption "Brilliant, fast - and confidently wrong…" fades in.
6. `+6.5s` Takeaway "Confidence ≠ accuracy. Fluent ≠ correct." fades in.
7. `+7.4s` Amber underline **draws** under the takeaway (`drawProgress`, 1.1 s).

### Scene 2 - The map: three zones · 0:30–2:00 (offset 30 000)
- `+0.2s` Title.
- Lanes reveal left→right, **9 s apart** (GREEN ≈0:30, AMBER ≈0:39, RED ≈0:48):
  per lane → box fades → header → subtitle → rule **draws** → list items stagger in 0.5 s apart.
- GREEN "Let it run - glance & ship", AMBER "Verify before it leaves", RED "A qualified human must own it" (lists per the brief; grey italic-style notes inside Amber/Red).

### Scene 3 - Why it fails · 2:00–2:40 (offset 120 000)
1. `+0.3s` "It predicts **likely** text - not **true** text." fades in.
2. Three rows reveal **9 s apart** (≈2:04 / 2:13 / 2:22): icon → label → grey note, then a **red strike-through draws** across icon+label.
   - 🧮 not a calculator → counting, exact maths
   - 🗄️ not a live database → recent facts, niche proprietary knowledge
   - ⚙️ not a rule engine → deterministic logic, 100 % reliability

### Scene 4 - The unlock: grounding · 2:40–3:20 (offset 160 000)
1. `+0.3s` Headline "Bad at *remembering* your stuff / Good at *working with* what you give it."
2. `+1.6s` BEFORE box (🤷, "Don't know your Q3 policy / that email thread").
3. `+2.4s` AFTER box frame appears.
4. `+5.0s` Document fades in and **slides right** into the AFTER box (`translateX` 0→480, `easeInOutCubic`), then **fades out as it's "absorbed"** (+7.4→7.8s); arrow **draws** beneath.
5. `+7.6s` AFTER box flips to ✅ "drafts it accurately from your source."
6. `+9.0s` Safe-to-ground caption.
7. **`+12.0s` RED caveat banner fades up LAST and stays put** - no later opacity keyframe, so it never disappears. ("Grounding fixes recall. It does NOT move anything out of RED…")

### Scene 5 - Side-by-side demo · 3:20–4:00 (offset 200 000)
- `+1.2s` Both panels appear; `+1.8s` prompts; `+2.2s` rules draw.
- **LEFT (✅):** 3-bullet summary "types out" (opacity-staggered, +3.0/3.7/4.4s) → green **tick draws** (+6.0s) → "Glance & ship".
- **RIGHT (❌):** confident **wrong** dosing answer types out (+3.3s) + "(stated with total confidence)" → red **cross draws** (+6.5s) → **"Left wrong on purpose"** stamp rotates in (`easeOutBack`, +7.6s) and **stays** - no corrected version is ever shown (teaching point).

### Scene 6 - Your turn · 4:00–4:30 (offset 240 000)
- `+0.3s` Title "Pick 3 tasks you do every week." → `+1.2s` worksheet.
- `+2.0s→` three rows **draw** in (row-line + number), 0.7 s apart.
- `+4.5s→` column labels **Good fit / Maybe / Never** fade in; 9 tick-boxes stagger in.
- `+8.0s` arrow **draws**, pointing at the first empty box (prompt to pause).
- `+9.0s` "Keep this list - you'll reuse it in Module 5."

### Scene 7 - Close · 4:30–5:00 (offset 270 000)
1. `+0.5s` Big "The skill isn't *using* AI. It's *knowing when*."
2. `+1.6s` Amber underline **draws** under "knowing when".
3. `+3.5s` Accountability line "…a qualified human always owns the output. AI assists - it never decides, and it's never accountable."
4. `+6.0s` Resource card slides up (`translateY` 160→0, `easeOutCubic`) and settles: "Read more → Ethan Mollick, *One Useful Thing* (blog)."

---

## Camera pan schedule (`translateX` offset from x=1000)
| To scene | Pan window | Value |
|---|---|---|
| 2 | 28.4s → 30.0s | 2400 |
| 3 | 118.4s → 120.0s | 4800 |
| 4 | 158.4s → 160.0s | 7200 |
| 5 | 198.4s → 200.0s | 9600 |
| 6 | 238.4s → 240.0s | 12000 |
| 7 | 268.4s → 270.0s | 14400 |

All pans `easeInOutCubic`; camera holds between.

## Guardrails honoured
- RED zone (clinical / dosing / regulatory / post-failure apology) never framed as AI-safe; Scene 4 caveat banner persists to the end of the clip.
- Scene 5 wrong dosing answer left **uncorrected**, stamped "Left wrong on purpose".
- All placeholders are obviously fake (supplier emails, generic GLP-1-style dosing numbers) - no real patient data, names, or Phlo internal docs.
- Text kept large (20–64 px) and ≤ ~9 words/line.

## Exporting the three deliverables
Excalimate exposes **no MCP/HTTP export tool** - MP4 / animated-SVG / PNG are produced from the **Excalimate app UI**:
1. Open the project (it's live in the connected app, or open the share link below).
2. **MP4 1080p:** Export → Video → 1920×1080, full clip (0–300 000 ms). 16:9 already set.
3. **Animated SVG:** Export → Animated SVG (full clip).
4. **Static PNG + SVG cheat-sheet:** scrub to the end (or open `phlo-ai-1.3.excalidraw` in Excalidraw) → Export image → PNG and SVG of the assembled state.

**Share link (30-day, E2E-encrypted):**
`https://app.excalimate.com/#share=vvyEaRyo,uqm2TGkotiE5N6L6FX5CJOJ_s6v8LravCoNRGIvV0BQ`
