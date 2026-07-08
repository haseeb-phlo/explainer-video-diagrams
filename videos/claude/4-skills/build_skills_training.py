#!/usr/bin/env python3
"""Build skills.excalidraw - ONE flowing, illustrated explainer
for the "Claude Skills" training video (AI literacy series).

Style B (the house style): a single hand-drawn journey that reads left-to-right -
NO frames, NO boxed slides, white canvas, everything in the hand font (fontFamily 1),
roughness 1, a lively colour-coded Excalidraw palette, colour blocking, scribbled
annotations and charming primitive illustrations. The eleven sections are eleven
WIDE-GAP beats: you frame one beat at a time and pan left-to-right while narrating -
the whitespace IS the camera. Modelled on the canonical videos/claude/3-artefacts
build; the look lives in the shared excalidraw_kit.

Run:  python3 videos/claude/4-skills/build_skills_training.py
      python3 preview.py videos/claude/4-skills/skills.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(40411)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - eleven beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
GAP = 800
# every beat uses the SAME slot, shaped ~1.15:1 (content ~1120 wide x ~980 tall,
# heading at y60 counted in) so framing is identical on a 14" laptop. Content
# fills the slot; it never spreads wider than ox+1120 or below y~1050.
WID = dict.fromkeys(range(1, 12), 1200)
ACCENT = {1: VIOLET, 2: BLUE, 3: ORANGE, 4: GREEN, 5: TEAL, 6: INDIGO,
          7: VIOLET, 8: ORANGE, 9: GREEN, 10: RED, 11: YELLOW}
OX = {}
_c = 0
for _i in range(1, 12):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60

def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude Skills", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "teaching Claude how your team works", size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - HOOK: a Skill is modular know-how, bundled
# ============================================================================
ox = beat_head(1, "Reusable know-how, built once",
               "Bundles of instructions Claude snaps in only when a task needs them.")
# three loose pieces -> bundled into one Skill, stacked to fill the square slot
by = 380
for k, (c, cbg) in enumerate([(VIOLET, VIOLET_BG), (ORANGE, ORANGE_BG), (GREEN, GREEN_BG)]):
    bx = ox + 80 + k * 220
    rect(bx, by, 150, 150, stroke=c, bg=cbg, sw=3, rough=1, rounded=True, angle=jit(2.0))
arrow(ox + 80 + 290, by + 230, [[0, 0], [0, 130]], stroke=VIOLET, sw=5, rough=1)
fbx = ox + 80
fby = by + 400
rect(fbx, fby - 16, 150, 30, stroke=VIOLET, bg=VIOLET_BG, sw=2, rough=1, rounded=True)
rect(fbx, fby + 12, 660, 200, stroke=VIOLET, bg=VIOLET_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=45)
text(fbx + 40, fby + 56, "a Skill", size=H1, color=VIOLET)
text(fbx + 40, fby + 140,
     "instructions, examples and scripts - bundled and reusable",
     size=SMALL, color=GREY)
chip(ox + 80, fby + 270, "Mandatory AI literacy training  -  10-15 min",
     fill=VIOLET_BG, text_color=VIOLET, border=VIOLET, size=LABEL)

# ============================================================================
# BEAT 2 - WHAT IS A SKILL  (the folder)
# ============================================================================
ox = beat_head(2, "What is a Skill?",
               "A folder of instructions, scripts and resources Claude loads only when a task needs it.")
# the folder card (left), what's in it (right) - then the three chips below
rect(ox + 60, 360, 150, 30, stroke=BLUE, bg=BLUE_BG, sw=2, rough=1, rounded=True)
rect(ox + 60, 388, 480, 320, stroke=BLUE, bg=BLUE_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=45)
text(ox + 96, 440, "SKILL", size=H1, color=BLUE)
text(ox + 96, 540, "a recipe card Claude\nreaches for at the\nright moment",
     size=BODY, color=GREYD)
ix = ox + 620
for k, lab in enumerate(["Instructions", "Examples", "Scripts (optional)"]):
    chip(ix, 410 + k * 110, lab, fill=WHITE, text_color=BLUE, border=BLUE, size=BODY)
text(ox + 60, 800, "Claude opens it only when the task matches the description.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 3 - WHY THEY MATTER  (without vs with)
# ============================================================================
ox = beat_head(3, "Why they matter")
# without (top) -> with (bottom), stacked to fill the square slot
lw, lh, ly = 1080, 280, 300
sticky(ox + 40, ly, lw, lh, FAINT, angle=jit(1.4))
text(ox + 80, ly + 28, "Without Skills", size=H3, color=GREYD)
for k, s in enumerate(["re-explain the same thing every time",
                       "inconsistent results",
                       "knowledge stuck in people's heads"]):
    text(ox + 80, ly + 96 + k * 56, "- " + s, size=BODY, color=INK)
ry = ly + lh + 120
arrow(ox + 80, ly + lh + 16, [[0, 0], [0, 86]], stroke=GREEN, sw=6, rough=1)
sticky(ox + 40, ry, lw, lh, GREEN_BG, angle=jit(-1.3))
text(ox + 80, ry + 28, "With Skills", size=H3, color=GREEN)
for k, s in enumerate(["write it once",
                       "same result every time",
                       "shared across the team"]):
    text(ox + 80, ry + 96 + k * 56, "- " + s, size=BODY, color=INK)

# ============================================================================
# BEAT 4 - HOW IT WORKS  (progressive disclosure)
# ============================================================================
ox = beat_head(4, "How it works: only what's needed loads",
               "You give Claude a task; it loads just the relevant Skill - nothing else.")
steps4 = [("You ask", "you give Claude a task"),
          ("Claude scans", "reviews the available Skills and picks only the relevant one(s)"),
          ("Claude applies", "loads those instructions and follows them")]
cw4, ch4, cy4 = 1080, 180, 320
for k, (head4, body4) in enumerate(steps4):
    cy = cy4 + k * (ch4 + 70)
    sticky(ox + 40, cy, cw4, ch4, GREEN_BG, angle=jit(1.2))
    num_badge(ox + 68, cy + 26, k + 1, GREEN)
    text(ox + 136, cy + 32, head4, size=H3, color=GREEN)
    text(ox + 80, cy + 100, body4, size=BODY, color=INK)
    if k < 2:
        arrow(ox + 100, cy + ch4 + 8, [[0, 0], [0, 56]], stroke=GREEN, sw=5, rough=1)
text(ox + 40, cy4 + 3 * (ch4 + 70) + 8,
     "Only relevant Skills load, so the context window stays clear and fast.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 5 - ANATOMY  (SKILL.md)
# ============================================================================
ox = beat_head(5, "What's inside a Skill")
fx5, fy5, fw5, fh5 = ox + 40, 320, 1080, 350
rect(fx5, fy5, fw5, fh5, stroke=TEAL, bg=WHITE, sw=3, rough=1, rounded=True)
rect(fx5, fy5, fw5, 50, stroke="transparent", bg=TEAL_BG, sw=1, rough=1, rounded=True)
text(fx5 + 30, fy5 + 12, "SKILL.md", size=H3, color=TEAL)
text(fx5 + 36, fy5 + 90, "name: team-report-format", size=BODY, color=INK)
text(fx5 + 36, fy5 + 150, "description: when to use it (the trigger)", size=BODY, color=INK)
scribble_underline(fx5 + 36, fy5 + 188, text_w("description: when to use it (the trigger)", BODY), VIOLET)
text(fx5 + 36, fy5 + 232, "--- instructions, in plain Markdown ---", size=BODY, color=GREY)
arrow(fx5 + 220, fy5 + fh5 + 6, [[0, 0], [-60, 56]], stroke=VIOLET, sw=3, rough=1)
text(fx5 + 36, fy5 + fh5 + 66,
     "the description is how Claude knows when to use it - make it specific",
     size=SMALL, color=VIOLET)
# optional extras - chips below the card
cy5 = fy5 + fh5 + 130
cx5 = ox + 40
for lab in ["scripts/", "resources/"]:
    w, h = chip(cx5, cy5, lab, fill=WHITE, text_color=TEAL, border=TEAL, size=BODY)
    cx5 += w + 50
text(cx5 + 20, cy5 + 8, "optional extras for advanced Skills", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 6 - FOUR TYPES
# ============================================================================
ox = beat_head(6, "Four types of Skills")
types6 = [("Anthropic Skills", "built in - Word, Excel,\nPowerPoint, PDF creation", BLUE),
          ("Custom Skills", "built by you or your team\nfor your own workflows", VIOLET),
          ("Organisation Skills", "pushed to everyone by\nadmins, automatically", GREEN),
          ("Partner Skills", "from the Skills directory -\nNotion, Figma, Atlassian", ORANGE)]
cw6, chx6 = 520, 250
gx6, gy6 = ox + 40, 320
for k, (head6, body6, acc6) in enumerate(types6):
    cx = gx6 + (k % 2) * (cw6 + 40)
    cy = gy6 + (k // 2) * (chx6 + 70)
    sticky(cx, cy, cw6, chx6, INDIGO_BG, angle=jit(1.1))
    text(cx + 36, cy + 30, head6, size=H3, color=acc6)
    text(cx + 36, cy + 110, body6, size=BODY, color=INK)

# ============================================================================
# BEAT 7 - SKILLS VS OTHER FEATURES  (hand-drawn comparison, no boxed table)
# ============================================================================
ox = beat_head(7, "Skills vs other Claude features",
               "They stack - a Skill can tell Claude how to use an MCP connector well.")
# one row per feature: chip on the left, then what / when stacked under it so the
# whole comparison fits ~1080 wide and fills the square slot
rows7 = [("Skills", "how to do a task", "loads only when relevant", VIOLET),
         ("Projects", "background knowledge", "always, in that project", BLUE),
         ("MCP / Connectors", "access to tools & data", "when you call the tool", TEAL),
         ("Custom instructions", "your general preferences", "always, everywhere", ORANGE)]
ACC_BG = {VIOLET: VIOLET_BG, BLUE: BLUE_BG, TEAL: TEAL_BG, ORANGE: ORANGE_BG}
ry7 = 320
for feat, what, when, acc in rows7:
    line(ox + 40, ry7 - 14, [[0, 0], [1060, 0]], stroke=FAINT, sw=1)
    chip(ox + 40, ry7, feat, fill=ACC_BG[acc], text_color=acc, border=acc, size=LABEL)
    text(ox + 560, ry7 + 4, what, size=BODY, color=INK)
    text(ox + 560, ry7 + 44, when, size=SMALL, color=GREYD)
    ry7 += 160

# ============================================================================
# BEAT 8 - USING A SKILL
# ============================================================================
ox = beat_head(8, "Finding and turning on Skills",
               "Needs code execution enabled in settings.")
steps8 = ["Open Customize in your account",
          "Skills  ->  '+'  ->  Browse skills",
          "Enable what you need - org Skills appear automatically"]
for k, s in enumerate(steps8):
    yy = 360 + k * 150
    num_circle(ox + 40, yy, k + 1, ORANGE)
    text(ox + 130, yy + 8, s, size=H3, color=INK)
demo_badge(ox + 40, 360 + 3 * 150 + 30,
           "show in Claude desktop app:  browse and enable a Skill")

# ============================================================================
# BEAT 9 - CREATE YOUR OWN
# ============================================================================
ox = beat_head(9, "Make your own - no coding needed")
# the four steps, wrapped onto two rows so they fit the square slot
flow9 = ["spot a repeated task", "write the steps in plain English",
         "add a clear description", "save & share"]
fx9, fy9 = ox + 40, 360
row_x0 = fx9
for k, lab in enumerate(flow9):
    w, h = chip(fx9, fy9, lab, fill=GREEN_BG, text_color=INK, border=GREEN, size=BODY)
    if k == 1:  # wrap to row two after the second chip
        arrow(fx9 + w / 2, fy9 + h + 6, [[0, 0], [0, 64]], stroke=GREEN, sw=4)
        fx9 = row_x0
        fy9 += h + 130
    elif k < len(flow9) - 1:
        arrow(fx9 + w + 12, fy9 + h / 2, [[0, 0], [56, 0]], stroke=GREEN, sw=4)
        fx9 += w + 80
sticky(ox + 40, 700, 1080, 150, YELLOW_BG, angle=jit(1.3))
text(ox + 80, 740, "tip: ask Claude's skill-creator Skill\nto help you build it",
     size=BODY, color=INK)

# ============================================================================
# BEAT 10 - BEST PRACTICE / GOVERNANCE  (do vs avoid)
# ============================================================================
ox = beat_head(10, "Do this, avoid this")
# Do (top) over Avoid (bottom), stacked to fill the square slot
text(ox + 40, 310, "Do", size=H2, color=GREEN)
for k, s in enumerate(["keep descriptions specific", "one Skill = one job",
                       "reuse approved Skills"]):
    yy = 390 + k * 70
    rect(ox + 40, yy, 26, 26, stroke=GREEN, bg=GREEN, sw=2, rough=1, rounded=True)
    text(ox + 90, yy - 2, s, size=BODY, color=INK)
ay10 = 640
text(ox + 40, ay10, "Avoid", size=H2, color=RED)
avoid10 = ["vague descriptions", "cramming many jobs into one Skill"]
for k, s in enumerate(avoid10):
    yy = ay10 + 80 + k * 70
    rect(ox + 40, yy, 26, 26, stroke=RED, bg=RED, sw=2, rough=1, rounded=True)
    text(ox + 90, yy - 2, s, size=BODY, color=INK)
# the safety point - emphasised with a red caution + highlighter
py10 = ay10 + 80 + 2 * 70 + 10
highlighter(ox + 26, py10 - 10, 1080, 96, RED_BG, angle=0.0)
diamond(ox + 40, py10 - 4, 40, 40, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 60, py10 + 2, "!", size=H3, color=RED)
text(ox + 104, py10 - 2,
     "never put confidential or sensitive data in\na Skill file - they're shared",
     size=BODY, color=RED)

# ============================================================================
# BEAT 11 - RECAP + NEXT STEPS
# ============================================================================
ox = beat_head(11, "Recap")
for k, s in enumerate(["Skills = reusable how-to knowledge",
                       "they load only when needed",
                       "four types: built-in, custom, org, partner",
                       "anyone can make one"]):
    text(ox + 60, 340 + k * 90, "- " + s, size=H3, color=INK)
highlighter(ox + 40, 760, 1080, 100, YELLOW_BG, angle=0.0)
text(ox + 76, 784, "Next: browse the Skills directory and\nenable one this week",
     size=H3, color=INK)

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit; hard-fails on frames / off-palette)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
