Build me a single, presentation-ready Excalidraw file for a training video.
Output: one valid file named `phlo-2.2-claude-projects.excalidraw` in the current directory.

HOW TO BUILD IT (reliability matters)
- Do NOT hand-write the JSON. Write a small Python (or Node) generator script that
  constructs the Excalidraw document programmatically, then run it to emit the file.
- Use a helper function that fills every required Excalidraw element field with sane
  defaults (id, x, y, width, height, angle:0, strokeColor, backgroundColor, fillStyle,
  strokeWidth, strokeStyle, roughness, opacity:100, groupIds:[], frameId, roundness,
  seed (random int), version:1, versionNonce (random int), isDeleted:false,
  boundElements:[], updated (epoch ms), link:null, locked:false). Text elements also
  need: text, fontSize, fontFamily, textAlign, verticalAlign, containerId:null,
  originalText, lineHeight:1.25. Frame elements need type:"frame" and name.
- Top level: { type:"excalidraw", version:2, source:"https://excalidraw.com",
  elements:[...], appState:{ gridSize:20, viewBackgroundColor:"#FFFFFF" }, files:{} }.
- After writing, VALIDATE: load the file back with json.load, assert it parses, assert
  every element has a unique id, and print a one-line summary (frame count, element count).
  Fix and re-run until it validates cleanly.

CANVAS LAYOUT
- 10 frames, each exactly 1920 x 1080 (16:9, fills a Loom screen share).
- Lay frames left to right in a single horizontal strip: frame N at x = N*2100, y = 0.
  This makes left-to-right presentation order obvious.
- Name frames "01 Title", "02 The tax", "03 Anatomy", "04 The shift",
  "05 Three Projects", "06 The maths", "07 Multiplier", "08 Build-along",
  "09 Pause", "10 Close".
- Generous margins (>=120px), clear top-to-bottom hierarchy, plenty of whitespace.
  Never crowd a frame. One idea per frame.

PHLO PALETTE (use these only - swap hex here if official values differ)
- Primary purple (titles, key shapes):      #5B2D90
- Bright accent purple (highlights, arrows): #7C3AED
- Lilac fill (soft card backgrounds):        #F1ECFA
- Ink (body text):                           #1E1B2E
- White:                                     #FFFFFF
- Muted green (positive / "after" / ticks):  #2BA98E
- Muted coral (problem / "before" only):     #E2705F
Use purple as the lead. Coral and green are accents only, used once or twice each.

TYPOGRAPHY & STYLE (clean, professional, no "AI slop")
- Use the clean sans font (fontFamily 2) for ALL text - legibility first.
- Sizes: frame title ~40px bold-feel, section labels ~26px, body ~20px, captions ~16px.
- roughness:1 on shapes for a light hand-drawn warmth; roughness:0 is too cold, 2 too messy.
- Rounded rectangles for all cards/containers (roundness type 3).
- Consistent card style across frames: lilac fill, purple 2px stroke, generous padding.
- British English everywhere. Replace any em dash with " - ". No clichés, no filler,
  no decorative emoji, no stock-icon clutter. Restrained and tidy.

FRAME CONTENT (exact copy - use verbatim)

01 Title
- Top-left small wordmark: "Phlo"  (purple)
- Centre title (large): "Claude Projects"
- Subtitle: "The multiplier - set up once, use forever"
- Pill/tag under subtitle: "AI at Phlo  ·  Module 2.2  ·  7 min"
- Bottom-left footer: "AI Ops  ·  Mandatory training"

02 The tax
- Title: "The tax you pay every morning"
- Visual: a small Claude chat icon on the left. To its right, five identical sticky-note
  cards in a row labelled Mon, Tue, Wed, Thu, Fri. Each note reads:
  "Who I am · my role · Phlo's tone · the do-not-say list..."
- Below: a clock glyph + "~10 min a day" → arrow → "≈ 1 hour a week. Every week."
  (use coral for the cost figures)
- Caption (bottom): "Re-explaining yourself is invisible work. It adds up."

03 Anatomy
- Title: "What a Project actually is"
- One large rounded container labelled "PROJECT" (purple stroke) holding three cards:
  Card 1 - "Custom instructions"  body: "Your standing brief: role, Phlo's voice, what to avoid."
  Card 2 - "Knowledge files"      body: "Reference material Claude reads before every reply."
  Card 3 - "Conversations"        body: "Every chat here shares the two above - automatically."
- Caption: "One persistent space. Context lives here, not in your clipboard."

04 The shift
- Title: "The shift"
- Left block (coral accents), label "BEFORE": "Paste context every time" with three
  small repeated/messy note shapes.
- A bold purple arrow pointing right across the centre.
- Right block (green accents), label "AFTER": "Context is permanent" with one clean
  Project card and a green tick.
- Caption: "Write the brief once. Claude applies it every time."

05 Three Projects
- Title: "Three Projects you could build this week"
- Three equal cards side by side:
  A) "Patient comms drafting"
     In it: Phlo tone guide · examples of great replies · the do-not-say list
     Who: Patient Care + Pharmacy
  B) "Engineering PR review"
     In it: coding standards · common review patterns · Phlo style guide
     Who: Engineering
  C) "Weekly board prep"
     In it: board memo format · the last four memos · the questions the board cares about
     Who: Leadership

06 The maths
- Title: "The maths"
- Left, small: "Setup:  20 minutes.  Once."
- Right, large (green): "Saving:  hours every week - for as long as you do the job."
- A simple seesaw/scale tipping hard toward the saving side.
- Caption: "The best twenty minutes you'll spend this month."

07 Multiplier
- Title: "Why it's a multiplier"
- One person glyph labelled "Builds the Project once" on the left.
- A purple arrow fanning out to a row of four teammate glyphs labelled "The whole team uses it".
- Sub-line: "One person builds Patient Comms. The clinical team drafts in Phlo's voice from day one."
- Small note (ink, smaller): "Sharing is available on Team and Enterprise plans."

08 Build-along
- Title: "Let's build one - live"
- Three numbered checklist rows (large, simple):
  1  Name it, and set who can see it
  2  Write the custom instructions
  3  Add two or three reference files, then chat
- Keep this frame deliberately plain - it sits behind the screen-share.

09 Pause
- Centre: large "PAUSE" with a simple pause-bars glyph (bright purple).
- Line 1: "Think of one task you repeat."
- Line 2: "Open claude.ai/projects and create it now - even empty."
- Line 3: "Fill it as you watch the rest of this module."

10 Close
- Title: "One Project. Twenty minutes."
- Line: "Use it once a day for a month. Then tell me Projects didn't change how you work."
- Resources card (lilac):
   "Anthropic Help Centre - 'How can I create and manage projects' (support.claude.com)"
   "AI Ops Learn → Prompt Library - Phlo's shared Projects"
- Bottom-right footer: "Phlo  ·  AI Ops"

Finish by printing the validation summary and the output file path.