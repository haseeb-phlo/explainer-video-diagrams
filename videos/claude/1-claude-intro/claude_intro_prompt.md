GOAL
Produce ONE file: `claude_intro.excalidraw` - a valid Excalidraw scene (schema version 2) for the ~4-minute "Claude: the interface, properly" training video (Phlo AI training, module 2, video 1), shown beat-by-beat and talked over in Loom. The single required deliverable is the .excalidraw file.

METHOD (do it this way - it is what keeps the result clean and on-style)
Write a THIN Python build script `build_claude_interface.py` that imports the shared Style B engine and composes the scene - do NOT hand-place raw JSON, and do NOT re-implement helpers.

```python
import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
import random
from excalidraw_kit import *
random.seed(40404)   # deterministic - re-runs produce an identical file
# ... compose the scene with the helpers below ...
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude_intro.excalidraw")
finish(out, MAXW, TOTAL_W)   # validates (palette, no frames, overflow, collisions) then writes + reloads
```

The engine (`excalidraw_kit.py`, repo root) owns the palette, element factory, fun primitives, reusable illustrations and the validate/write tail. Your script holds only the composition: the per-video beat scaffold plus any bespoke one-off illustration (here, the Claude.ai window). Preview without opening the app:
`python3 ../../../preview.py claude_intro.excalidraw out.png [XMIN XMAX]`

STYLE B - NON-NEGOTIABLES (house style; see CLAUDE.md + .claude/skills/SKILL.md)
- ONE flowing, illustrated, hand-drawn journey, left to right. NO frames, NO bordered slides. Beats are separated by whitespace and a connector spine, never by rectangles.
- White canvas (`viewBackgroundColor #ffffff`).
- ALL text hand-drawn in Excalifont (`fontFamily 5` = the kit's `HAND`), `roughness 1` on everything. No typed sans/mono.
- Lively palette, colour-coded per beat. Heavy colour-blocking (highlighter sweeps, pastel sticky notes) + scribbled annotations (underlines, circled words, freehand arrows, sparkles) do the work; a charming primitive illustration (the Claude.ai window) carries the hero beat; light rotation jitter on notes/chips.
- No emoji - draw any icon from primitives (the kit has `pause_icon`, `sparkles`, warning triangles via `line`, etc.).
- British English. Hyphens "-", never em dashes. Use the verbatim copy below; do not "improve" it.
- Vocabulary: Claude / Opus / Sonnet / Haiku / MCP are proper nouns; "Patient" not "user/customer"; "Phlo" not "we/us".

PALETTE & TYPE (constants exported by the kit - never introduce a colour outside PALETTE)
- Neutrals: WHITE, INK, GREYD, GREY, FAINT.
- Beat colours, each with a matching pastel `_BG`: VIOLET, ORANGE, GREEN, BLUE, RED, TEAL, YELLOW, INDIGO.
- Type scale (px): HERO 96 · H1 48 · H2 34 · H3 28 · BODY 22 · LABEL 20 · SMALL 17. Font: HAND (5) throughout.

HELPERS available from the kit (use these; don't redefine)
rect, ellipse, line, arrow, text, text_centered, text_w; highlighter, sticky, chip, scribble_underline,
circle_around, sparkle, sparkles, pause_icon, num_badge, jit; finish(out, max_w, total_w).

LAYOUT - beat scaffold (wide gaps so a single beat frames cleanly on a 14" laptop)
- `GAP = 1800`. Four beats keyed 1-4: `WID = {1:3120, 2:2600, 3:2000, 4:2300}`. Per-beat accent: `ACCENT = {1:VIOLET, 2:BLUE, 3:YELLOW, 4:GREEN}` with matching `ABG`. Lay beats out left-to-right: `OX[i]` accumulates `WID[i] + GAP`; `TOTAL_W` is the running total; `MAXW = max(WID.values()) + 200`.
- A `head(ox, title, accent, abg)` helper draws each beat heading: a highlighter sweep behind a HAND H1 title with a scribbled underline. The five PARTS carry the number badges, so headings have no step number.

BOARD TITLE (above beat 1, around y=-300)
- HERO INK: "The interface, properly"  (+ a VIOLET `sparkles` to its right)
- H2 VIOLET: "five things on screen most people never touch"
- H3 GREYD: "- and they're where the productivity is"
- SMALL GREY: "Phlo AI training  -  about 4 minutes"

BEAT 1 - "One window. Five parts."  (accent VIOLET)
Bespoke illustration `claude_window_full(x, y, w, h)`: a rounded white Claude.ai window (~1500x420), thin top bar with three grey dots, and inside it the five real parts so every callout arrow lands on something:
  - a left sidebar (VIOLET_BG tint, a few white rows) -> Projects;
  - a central chat column (grey "message" bars) -> Conversations;
  - a small TEAL "Sonnet v" model chip top-right -> Model picker;
  - a BLUE-edged "Artifact" side panel on the right -> Artifacts;
  - a bottom input bar with a GREEN paperclip glyph -> File uploads.
  It returns anchor points for those five targets.
Five numbered callouts (a jittered `sticky` + `num_badge` + H3 title + SMALL body, with a coloured `arrow` to the matching anchor). Verbatim copy:
  1. Conversations (ORANGE) - "Where most people live. Useful,\nbut volatile - context doesn't\ncarry between chats."
  2. Projects (VIOLET) - "The multiplier. Persistent\ninstructions, files and memory\nacross every chat inside it.\n(Video 2.2)"
  3. Artifacts (BLUE) - "When Claude builds a document\nor tool, not just text. Opens a\nside panel - persistent, editable."
  4. File uploads (GREEN) - "PDFs, images, spreadsheets, code.\nClaude reads them. The most\nunderused feature."
  5. Model picker (TEAL) - "Match the model to the task."
SAFETY CAUTION (Phlo, regulated pharmacy) - directly under the File uploads callout, draw a small RED warning triangle (a `line` filled RED_BG) with a "!" and a RED `chip`: "Never upload patient-identifiable data". This guardrail is required, not decorative.

BEAT 2 - "Pick the model deliberately"  (accent BLUE)
Three jittered `sticky` cards side by side, each with a HAND title, a SMALL subhead, a small primitive illustration, and a BODY description. Models are current as of today - do not change the versions:
  - Opus (INDIGO) - "Claude Opus 4.8" - "Deep reasoning, long-form\nwriting, complex analysis.\nSlowest, deepest."   illustration: a stacked weight.
  - Sonnet (GREEN) - "Claude Sonnet 4.6" - "Balanced speed and quality.\nMost day-to-day work."   add a GREEN "DEFAULT" chip.   illustration: a bright star (`sparkle`).
  - Haiku (YELLOW) - "Claude Haiku 4.5" - "Fast and light.\nQuick lookups, simple drafts."   illustration: motion lines + a zippy dot.
Under the cards:
  - GREYD BODY: "Heavier models think longer and use more of your allowance.  Lighter ones are faster."
  - a "faster -> deeper" spectrum: the label "faster", then chips Haiku (YELLOW) -> Sonnet (GREEN) -> Opus (INDIGO) joined by small grey arrows, then "deeper".
  - GREYD BODY: "Switch any time - even mid-conversation."

BEAT 3 - "Pause here, and try it"  (accent YELLOW)
A `pause_icon` + a YELLOW_BG `highlighter` sweep behind H3 INK: "Open Claude. Switch to a model that\nisn't your default. Run one prompt."
A row of three YELLOW-outlined chips: "try Opus", "or Haiku", "notice the difference". A YELLOW `sparkles`. GREYD BODY: "60 seconds - then carry on."

BEAT 4 - "Five features. Four minutes."  (accent GREEN)
- Recap: five chips in beat colours - "Conversations" (ORANGE), "Projects" (VIOLET), "Artifacts" (BLUE), "File uploads" (GREEN), "Model picker" (TEAL).
- H3 INK: "Next: Projects - the one that compounds for years." with a VIOLET `circle_around` "Projects".
- Roadmap (signpost only, planned not shipped): SMALL GREY "Later in this module:" then faint white/FAINT-outline chips "Skills", "Scheduled tasks", "Connectors (MCP)", "Cowork", then SMALL GREY "+ more".  (Confirm this slate against the course curriculum before recording.)
- A `sparkles` + VIOLET SMALL: "Docs: Claude Help Centre - support.claude.com"
- Footer SMALL GREY: "Phlo AI training  -  the interface"

CONNECTOR SPINE (makes it ONE picture, not "boxes minus the borders")
Across each gap, draw a wavy hand-drawn `arrow` from the end of beat i to the start of beat i+1, in the NEXT beat's accent colour. Add one faint dashed FAINT baseline `line` running the full width beneath the beats.

ACCEPTANCE CHECKS (`finish()` enforces these before it writes)
- Valid Excalidraw v2 JSON; `appState.viewBackgroundColor` is WHITE.
- Zero frames (Style B). No off-palette colours. No text overflow or text/text collisions (collisions print as warnings - resolve them, aim for 0).
- All ids unique. Print the final element count, total width, and collisions at the end.
