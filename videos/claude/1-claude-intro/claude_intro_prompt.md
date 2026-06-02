Create a single valid Excalidraw file named `claude-interface-properly.excalidraw` for a 4-minute internal training video at Phlo (a UK digital pharmacy). Output strictly valid Excalidraw JSON: { "type": "excalidraw", "version": 2, "source": "https://excalidraw.com", "elements": [...], "appState": { "viewBackgroundColor": "#FFFFFF", "gridSize": null }, "files": {} }. Every element needs a unique id, correct type, x/y, width/height, angle:0, strokeColor, backgroundColor, fillStyle:"solid", strokeWidth, strokeStyle:"solid", roughness:1, opacity:100, seed, version, versionNonce, isDeleted:false, boundElements, updated, link:null, locked:false. Text elements need fontSize, fontFamily, textAlign, verticalAlign, baseline, containerId, originalText. Arrows need points arrays and startBinding/endBinding. Validate the JSON parses before finishing.

DESIGN DIRECTION
- Clean, confident, editorial. NOT a sketchy doodle. Use roughness 0 or 1 max, generous whitespace, strong alignment to an 8px grid, clear hierarchy. This is mandatory training, so legibility beats decoration.
- Typography: fontFamily 2 (the clean Helvetica-style font) throughout for legibility on video. Title ~48px, frame headings ~30px, card titles ~22px, body ~16-18px. Never centre long body text; left-align body, centre only short titles.
- Phlo-aligned purple palette (these match Phlo's violet brand identity; if you have the exact brand-guide hex, substitute it):
  - Deep purple (primary): #4A1F7A
  - Brand purple (accent): #6B2FB5
  - Bright violet (highlight): #8B5CF6
  - Lavender tint (fills/backgrounds): #F3EEFB
  - Soft lavender (secondary fill): #E7DBF7
  - Ink (body text): #1E1B2E
  - Mid grey (secondary text): #6B6480
  - White: #FFFFFF
  - Use one restrained teal #0FB5A6 ONLY for the single "do this" highlight on the pause card.
- Rounded rectangles for all cards/containers. Consistent corner feel. Cards sit on white or lavender-tint backgrounds with the deep purple as the stroke and headings.
- Accessibility: keep text-on-background contrast at AA or better. No light grey text on lavender.

LAYOUT
Create FIVE Excalidraw "frame" elements laid out left to right in one row, each 1600 wide x 1000 tall, with a 400px horizontal gap between frames. Name each frame (frame name shows in Excalidraw). Keep ~120px internal padding inside every frame. Snap everything to the grid; align card edges.

FRAME 1 - name "01_Hook"
- Top-left small kicker in mid grey: "PHLO · AI TRAINING · 4 MIN"
- Large title in deep purple: "The Claude interface, properly"
- Subtitle in ink, left-aligned, max ~14 words per line: "Five things on screen most people never touch. They're where the productivity is."
- A thin brand-purple underline rule beneath the title.
- Bottom: five small lavender pills in a row, each with one word in deep purple: "Conversations"  "Projects"  "Artifacts"  "File uploads"  "Model picker". Even spacing, vertically centred text.

FRAME 2 - name "02_The_map" (the core diagram)
- Heading in deep purple: "One window. Five parts."
- Draw a stylised Claude.ai window: a large rounded rectangle (white fill, deep-purple stroke) occupying the centre. Inside, sketch a simple layout: a narrow left sidebar column (lavender tint), a wide central chat area (white) with two or three rounded "message" bars, a small model-picker chip at the top-right of the window, and a paperclip/upload glyph near a bottom input bar. A right-hand panel tab to suggest the Artifacts panel.
- Add FIVE numbered callout labels connected to the relevant part of the window with thin brand-purple arrows. Each callout is a small rounded card (soft lavender fill) with a deep-purple number badge, a bold card title, and one line of ink body:
  1. "Conversations" - "Where most people live. Useful, but volatile - context doesn't carry between chats."
  2. "Projects" - "The multiplier. Persistent instructions, files and memory across every chat inside it. (Video 2.2)"
  3. "Artifacts" - "When Claude builds a document or tool, not just text. Opens a side panel. Persistent and editable."
  4. "File uploads" - "PDFs, images, spreadsheets, code. Claude reads them. The most underused feature."
  5. "Model picker" - "Match the model to the task."
- Arrange callouts around the window without crossing arrows; keep arrows short and tidy.

FRAME 3 - name "03_Model_picker"
- Heading in deep purple: "Pick the model deliberately"
- Three equal cards side by side (white fill, deep-purple stroke, brand-purple title bar):
  - Card 1 "Opus" - small subhead "Claude Opus 4.8" - body: "Heavyweight. Deep reasoning, long-form writing, complex analysis. Slowest, deepest."
  - Card 2 "Sonnet" - small subhead "Claude Sonnet 4.6" - body: "The default. Balanced speed and quality. Most day-to-day work." Add a small "DEFAULT" tag in brand purple.
  - Card 3 "Haiku" - small subhead "Claude Haiku 4.5" - body: "Fast and light. Quick lookups, simple drafts."
- A full-width footer strip in lavender tint with deep-purple text: "Heavier models think longer and use more of your usage allowance. Lighter models are faster. Choose to fit the job."

FRAME 4 - name "04_Pause_and_try"
- Centre a single bold rounded card (lavender tint, teal #0FB5A6 stroke 3px to signal action).
- Eyebrow in teal: "PAUSE AND TRY"
- Big ink instruction, left-aligned: "Open Claude. Switch to a model that isn't your default. Run one prompt. Notice the difference."
- Small mid-grey note beneath: "60 seconds. Then carry on."

FRAME 5 - name "05_Close"
- Heading in deep purple: "Five features. Four minutes."
- Line in ink: "Next: Projects - the one that compounds for years."
- A resource card (white fill, brand-purple stroke): title "Resource" in brand purple, body in ink: "Claude Help Centre - support.claude.com"
- Bottom-right small mid-grey tag: "Phlo · AI training"

FINAL CHECKS
- Confirm valid JSON, all ids unique, all arrows bound or with explicit points, no overlapping text, consistent padding and alignment, AA contrast. Save as `claude-interface-properly.excalidraw`. Tell me the file path.