GOAL
Produce ONE file: `3-artifacts.excalidraw` - a valid Excalidraw scene (schema version 2) for a training video shown frame-by-frame and talked over in Loom. The single required deliverable is the .excalidraw file. Do not output anything that is not needed to produce it.

METHOD (do it this way - it is what keeps the result clean, not sloppy)
Write a Python script `build_excalidraw.py` that builds the scene programmatically, then writes the JSON. Do NOT hand-place raw elements one by one. Implement a layout grid and a small set of reusable component builders so spacing, sizing and styling are identical everywhere. After writing the file, load it back, assert the JSON parses, and print the frame count and element count. Then stop.

NON-NEGOTIABLE QUALITY BAR ("no AI slop")
- One coherent design system, used consistently. Everything snaps to an 8px grid.
- Strict, small palette with fixed roles (below). Never introduce a colour outside it.
- Generous whitespace. Never crowd a frame. If a frame feels busy, remove content, do not shrink it.
- Left-aligned text blocks (not everything centred). Clear size hierarchy.
- No emoji. Draw any icon (play, pause, arrow, tick, dots) from primitive shapes.
- No lorem ipsum, no filler, no decorative shapes that mean nothing.
- British English in all on-canvas text. Use hyphens "-", never em dashes.
- Use the EXACT copy provided per frame. Do not rewrite or "improve" it.

EXCALIDRAW FILE SCHEMA (so the file is valid)
Top level:
{ "type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
  "elements": [ ... ], "appState": { "viewBackgroundColor": "#FBF7F0", "gridSize": null }, "files": {} }

Every element needs (at least): id (unique string), type, x, y, width, height, angle (0),
strokeColor, backgroundColor, fillStyle, strokeWidth, strokeStyle, roughness, opacity (100),
groupIds ([]), frameId (null OR the parent frame's id), roundness (null OR {"type":3} for rounded),
seed (random int), version (1), versionNonce (random int), isDeleted (false),
boundElements (null), updated (epoch ms), link (null), locked (false).

Type-specific:
- type "rectangle" | "ellipse" | "diamond" | "line" | "arrow" | "text" | "frame".
- text: add text, fontSize, fontFamily (1 = hand-drawn, 2 = normal sans, 3 = mono/code),
  textAlign ("left"|"center"|"right"), verticalAlign ("top"|"middle"|"bottom"),
  containerId (null), originalText (= text), lineHeight (1.25). For multi-line, put "\n" in text
  and size height ~= lines * fontSize * lineHeight. Set width wide enough that text does not wrap unexpectedly.
- arrow / line: add points (array of [x,y] RELATIVE to the element's x,y; start at [0,0]),
  startArrowhead (null), endArrowhead ("arrow" for arrows, null for lines), lastCommittedPoint (null).
  Set width/height to the bounding box of the points.
- frame: type "frame", plus name (string). Frames are transparent containers; child elements belong to a
  frame by setting their frameId to that frame's id. Place children using absolute canvas coordinates that
  fall inside the frame's rectangle.

Notes that prevent breakage:
- Place all text as standalone text elements positioned manually (do NOT bind text inside shapes as containers).
- Keep z-order by array order: push background shapes first, then content, then labels.
- enums: fillStyle "solid"|"hachure"; strokeStyle "solid"|"dashed"|"dotted"; roughness 0 (clean) |1 (hand-drawn).

DESIGN SYSTEM - "Riso Workshop" (define as constants)
Palette (hex, fixed roles):
  PAPER   = "#FBF7F0"   # canvas + frame background showing through
  INK     = "#1A1A2E"   # primary text, primary strokes
  GREY    = "#6B6B7B"   # secondary text, captions, number badges, neutral lines
  VERMIL  = "#FF5A36"   # HERO accent: title underlines, "build/maker" energy, play icon, the ONE caution card
  VIOLET  = "#6C4CE0"   # the "tool / app / interactive / artifact panel" colour. Anything you can USE.
  MUSTARD = "#FFC233"   # highlight only: the pause moment + one or two emphasis sweeps. Use sparingly.
  SAND    = "#F1E9DC"   # soft fill for neutral cards
  WHITE   = "#FFFFFF"   # fill for "screen / panel / object" shapes so they pop on paper
Colour discipline: ink + two accents (vermilion, violet) + one highlight (mustard) + neutrals. Nothing else.

Type scale (px): TITLE 46 · FRAME_TITLE 30 · SUBHEAD 22 · BODY 17 · SMALL 14.
Fonts: hand-drawn (1) for the board title, frame titles, labels, short annotations. Normal sans (2) for body
and any sentence longer than ~6 words (legibility). Mono (3) ONLY for things shown as a typed prompt or code.
Strokes: strokeWidth 2 default; 1 for fine detail. roughness 1 (hand-drawn feel) for everything EXCEPT
"screen / window / panel" rectangles, which use roughness 0 so they read crisp. fillStyle "solid" for cards
and objects; "hachure" allowed for the small accent burst behind a hero object and for a mustard highlight sweep.

CANVAS LAYOUT
- Board title text (hand-drawn, TITLE, INK) at x=120, y=-180:
  "ARTIFACTS - when Claude makes things, not just text"
  Subtitle (SMALL, GREY) directly under it: "Phlo AI training · module 2.3 · ~5 minutes"
- 12 frames in a SINGLE horizontal row. Each frame is 1600 wide x 900 tall. Horizontal gap 240px.
  Frame i (0-indexed) at x = i*(1600+240), y = 0. Set each frame's name to the strings listed below.
- Inside every frame, with frame padding 72px from the frame edges:
    * Frame title (hand-drawn, FRAME_TITLE, INK), top-left.
    * A short VERMIL underline (a line element, strokeWidth 3, ~180px long) just under the title.
    * A number badge top-right: small GREY text like "01 / 12", "02 / 12" ...
    * Then the frame content, laid out on the grid with plenty of air.

RECURRING COMPONENTS (build once, reuse)
- claude_window(x, y, w, h): a rounded WHITE rectangle (roughness 0, thin GREY border). A thin top bar with
  three small GREY dots top-left. Split internally: LEFT ~55% = "chat" (3-4 short GREY rounded bars = messages);
  RIGHT ~45% = the "Artifact panel" - a WHITE inner rounded rect with a VIOLET left edge (a 6px violet bar) and
  a small VIOLET label "Artifact" at its top. Optionally render a tiny object inside the panel (see objects).
- object_doc / object_calc / object_app / object_chart / object_diagram / object_filestack: small symbolic
  objects (~140x140) drawn from primitives, INK strokes with VIOLET or SAND accents:
    doc = page with 3 text lines; calc = grid of small squares + a display bar; app = window with a button;
    chart = 3 bars of different heights; diagram = 3 nodes joined by 2 lines; filestack = 3 offset pages.
- split_motif(x, y): a small "words -> thing" unit: a GREY chat bubble on the left, a VERMIL arrow pointing
  right, and one object on the right. This is the spine of the whole deck - reuse it.
- chip(x, y, label, font=mono_or_sans, fill): a small rounded pill for prompts / tags / version labels.
- play_icon / pause_icon: a VERMIL filled triangle / two VERMIL filled bars. Never an emoji.
- version_chips(x, y): three small chips "v1" "v2" "v3", the last one VIOLET-filled, joined by small arrows.

FRAMES - exact content (titles are the frame `name`; copy is verbatim)

01 / 12  name "1 - Hook"
  Title: "Claude doesn't just describe a tool. It builds you one."
  Subhead (GREY): "Five minutes on the feature that turns Claude from advisor into maker."
  Big split_motif centred-lower: chat bubble "build me a tool to..." -> VERMIL arrow -> object_calc,
  with a soft VERMIL hachure burst behind the calculator.

02 / 12  name "2 - What it is"
  Title: "What's an Artifact?"
  Body (sans, BODY): "Any output Claude makes in its own side panel - one you can edit, run and reuse,
  right next to the chat."
  A large claude_window on the right half, artifact panel clearly highlighted.
  Caption under the window (hand-drawn, SUBHEAD, VIOLET): "Words on the left. A thing you can use on the right."

03 / 12  name "3 - It can be almost anything"
  Title: "It can be almost anything"
  A tidy single row of six labelled objects with their captions (SMALL, GREY) beneath each:
    object_doc "One-pager"  ·  object_calc "Calculator / tool"  ·  object_app "Mini-app"  ·
    object_chart "Chart"  ·  object_diagram "Diagram"  ·  object_filestack "File to download:\nWord · PPT · Excel · PDF"
  Keep equal spacing on the grid.

04 / 12  name "4 - Two ways you get one"
  Title: "Two ways you'll get one"
  Two equal cards side by side (rounded, SAND fill):
    LEFT card header (hand-drawn, SUBHEAD, INK) "Appears on its own", body lines (sans, BODY):
      "long documents", "code", "tables and structured output", "anything you'll clearly reuse".
    RIGHT card header "Ask for one on purpose", then two mono chips (VIOLET text on WHITE):
      "Make me a one-page Artifact summarising X"
      "Build me a tool to calculate Y"

05 / 12  name "5 - Demo: one-pager"
  A large VERMIL play_icon, with hand-drawn TITLE next to it: "Over to Claude"
  Subhead (sans, BODY, INK): "Build a reusable one-pager, live - a meeting-prep template."
  Small GREY note: "Cut to the Claude window. Come back when it's built."

06 / 12  name "6 - It's clay, not stone"
  Title: "It's clay, not stone"
  A left-to-right loop of four chips joined by VERMIL arrows: "Build" -> "Edit on the spot" ->
  "Ask Claude to refine" -> "Roll back to any version".
  Below, version_chips (v1 v2 v3). Caption (sans, BODY): "Change it on the canvas yourself, or just tell
  Claude what to change. Every version is kept."

07 / 12  name "7 - Demo: working tool"
  A large VERMIL play_icon + hand-drawn TITLE "Over to Claude"
  Subhead (sans, BODY): "Build a working tool, live - a medication supply calculator."
  Small GREY note (mono): "quantity + tablets/day  ->  days of supply + reorder date"

08 / 12  name "8 - Build once, share with everyone"
  Title: "Build once. Share with everyone."
  Body (sans, BODY): "Publish an Artifact and send a link. Anyone with the link can use it - no Claude account
  needed to open it. A team-mate who has an account can make their own copy and adapt it; yours stays put."
  Three small shareable cards (rounded, WHITE, VIOLET top edge) in a row:
    "Patient Care:\nreply-template one-pager"  ·  "Anyone:\nmeeting-prep one-pager"  ·
    "Ops:\nreorder-date calculator"
  Small GREY caption: "Lives in your chat, your Project, and your Published tab. On Team you share inside the
  workspace; on any plan you can share a link."

09 / 12  name "9 - New, and worth knowing"
  Title: "The panel just got superpowers"
  Four chips (rounded, SAND), each with a one-line caption (SMALL, GREY) under it:
    "AI inside the Artifact" - "it can think, not just sit there"
    "Live Artifacts" - "data refreshes when you reopen it"
    "Remembers between visits" - "saves what you put in"
    "Connects to your tools" - "calendar, email, chat and more"
  Caption (hand-drawn, SUBHEAD, VIOLET): "Same five-minute skill. Much more range."

10 / 12  name "10 - One rule, one reality check"
  Title: "One rule, one reality check"
  CARD A (rounded, WHITE, VERMIL border, strokeWidth 2) header (hand-drawn, SUBHEAD, VERMIL) "The rule",
    body (sans, BODY, INK): "Publishing or connecting an Artifact changes who can see it. Keep anything
    patient-identifiable, and any logins or keys, out of anything you share or connect."
  CARD B (rounded, SAND) header (hand-drawn, SUBHEAD, INK) "When not to bother",
    body (sans, BODY): "A quick one-off answer doesn't need an Artifact. Reach for one when you'll reuse it,
    edit it, or hand it on."

11 / 12  name "11 - Pause and try"
  A wide MUSTARD hachure highlight sweep behind the title. pause_icon (two VERMIL bars) beside the title.
  Title (hand-drawn, TITLE): "Pause here, and try it"
  Body (sans, SUBHEAD, INK): "Ask Claude to make a one-page Artifact for something you do every week."
  Examples row (mono chips): "a status update"  ·  "a meeting-prep sheet"  ·  "a checklist"
  Closing line (sans, BODY, GREY): "See what it gives you. Then change one thing."

12 / 12  name "12 - Close"
  Title (hand-drawn, TITLE): "Artifacts turn Claude from advisor to maker."
  Subhead (sans, SUBHEAD, INK): "Once you start asking for them, you'll wonder how you worked without them."
  Resource line (sans, BODY, VIOLET): "Docs: Anthropic - What are Artifacts and how do I use them"
  Footer (SMALL, GREY): "Phlo AI training · module 2.3"

ACCEPTANCE CHECKS (verify before finishing)
- File opens as valid Excalidraw v2 JSON; appState.viewBackgroundColor is PAPER.
- Exactly 12 frames, named as above, in one horizontal row, evenly spaced.
- Only the palette colours appear. No emoji anywhere. No text wraps awkwardly or overflows its frame.
- Every frame has: title, vermilion underline, "NN / 12" badge, and breathing room (72px padding respected).
- Print "frames: 12, elements: <n>" at the end.