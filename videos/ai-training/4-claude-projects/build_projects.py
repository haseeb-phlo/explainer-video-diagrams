#!/usr/bin/env python3
"""Build claude-projects.excalidraw - ONE flowing, illustrated explainer for
DAY 4 of the Phlo AI training: "Claude Projects" (~12 min).

Day 4 follows Day 3 (Prompting & CRISPE Framework): Day 3 is how to write one
good prompt, Day 4 is how to stop writing the same one every morning. The board
was originally the module-2.2 Claude walkthrough and moved here when the
day-by-day training became the authoritative series.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames, NO
boxes, white canvas, everything in the hand font (fontFamily 1), roughness 1, a
lively colour-coded Excalidraw palette, big colour-blocking, scribbled annotations
and charming primitive illustrations. The look lives in the shared excalidraw_kit;
this file holds only the composition. Converted from the old 10-frame editorial
"Style A" deck of the same name.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time, ~20-40s each):

     1  RED     The tax you pay every morning
     2  ORANGE  Every chat starts from zero        <- cold chat
     3  GREEN   Every chat starts briefed          <- briefed chat  [CUT TO CLAUDE DESKTOP]
     4  VIOLET  What a Project actually is
     5  BLUE    The shift
     6  VIOLET  The instructions field             <- the highest-leverage square inch
     7  INDIGO  Write it like you mean it          <- how to write the instructions
     8  GREEN   Three Projects you could build this week
     9  ORANGE  The maths
    10  BLUE    What you get on your plan          <- plans, the five-Project cap, retrieval
    11  TEAL    Why it's a multiplier
    12  VIOLET  Sharing, and who can do what       <- view / edit, and who can see it
    13  INDIGO  Let's build one - live             [CUT TO CLAUDE DESKTOP]
    14  YELLOW  Pause here, and try it
    15  BLUE    Slow vs live                       <- signposts Connectors and MCP
    16  VIOLET  One Project. Twenty minutes.       (closing chip, lower-left)

Beats 2, 3, 6 and 15 were added in the first extension; 7, 10 and 12 in the
second, which folded in the Claude Projects help-centre article (plans, the
five-Project cap, retrieval, sharing permissions) and the instruction-writing
discipline from Claude Code's memory docs. Beats 1, 4, 5, 8, 9, 11, 13, 14 and
16 are the original nine, unchanged and in their original order.

Run:  python3 build_projects.py
      python3 ../../../preview.py claude-projects.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(22022)

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD
# ----------------------------------------------------------------------------
# Wide gaps so a single beat can be framed on a 14" laptop without neighbours
# peeking in - the empty space IS the zoom-to-one-beat affordance. Every beat
# uses the SAME slot (~1120 wide x ~980 tall content, ~1.15 : 1) so framing is
# identical and fits a 14" MacBook screen. No two neighbouring beats share an
# accent, so a pan always lands on a fresh colour.
GAP = 800
N_BEATS = 16
WID = {i: 1200 for i in range(1, N_BEATS + 1)}
ACCENT = {1: RED, 2: ORANGE, 3: GREEN, 4: VIOLET, 5: BLUE, 6: VIOLET, 7: INDIGO,
          8: GREEN, 9: ORANGE, 10: BLUE, 11: TEAL, 12: VIOLET, 13: INDIGO,
          14: YELLOW, 15: BLUE, 16: VIOLET}
OX, _c = {}, 0
for _i in range(1, N_BEATS + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60

def beat_head(i, title, sub=None):
    # QUIET heading: kit heading() draws a prominent hand title in the beat's
    # accent colour + a hand underline. No step circle, no highlighter sweep.
    heading(OX[i], HEAD_Y, title, color=ACCENT[i], sub=sub)
    return OX[i]

# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS  (bespoke to this board - the kit owns the rest)
# ----------------------------------------------------------------------------
def chat_window(x, y, w, h):
    """A plain chat window: title bar with three dots, empty thread below.
    (Not the kit's claude_window - that one carries an Artifact panel.)"""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="chatw")
    line(x, y + 44, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 18 + k * 18, y + 16, 10, 10, stroke=GREY, bg=GREY, sw=1)

def context_note(x, y, w=300, h=112, accent=ORANGE, abg=ORANGE_BG, angle=None):
    """The pasted brief - a small note doodle. Every part carries the SAME angle
    so a rotated paste stays a paste and not a pile of loose parts."""
    a = jit(3.0) if angle is None else angle
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, angle=a, prefix="ctx")
    rect(x, y, w, 30, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True, angle=a, prefix="ctxh")
    text(x + 16, y + 4, "team tone guide", size=SMALL, color=accent, angle=a)
    for k, f in enumerate((0.84, 0.62, 0.74)):
        rect(x + 16, y + 48 + k * 20, (w - 32) * f, 10, stroke="transparent", bg=FAINT,
             sw=1, rough=1, rounded=True, angle=a, prefix="ctxl")

def folder(x, y, w=300, h=200, accent=GREEN, abg=GREEN_BG, papers=True):
    """A closed Project folder - tabbed, filled in the beat accent, with a few
    papers peeking over the top edge. `papers=False` for the small ones that are
    counted rather than read."""
    rect(x, y, w * 0.5, 24, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="foldtab")
    for k in range(3 if papers else 0):
        rect(x + w * 0.5 + k * 44, y - 4, 40, 44, stroke=INK, bg=WHITE, sw=2, rough=1,
             rounded=True, prefix="foldpaper")
    rect(x, y + 16, w, h, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="fold")

def open_folder(x, y, w, h, abg=VIOLET_T):
    """The same folder opened out flat: tabbed back panel + a shallow front lip,
    so its contents can be laid out and read."""
    rect(x, y - 30, w * 0.3, 34, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="ofoldtab")
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="ofold")
    rect(x, y + h - 44, w, 44, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="ofoldlip")

def pipe(x, y, w=160, h=60, accent=BLUE, abg=BLUE_BG):
    """A short length of pipe: flanged ends, a dashed flow running through it."""
    rect(x + 22, y, w - 44, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=False, prefix="pipe")
    rect(x, y - 10, 22, h + 20, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="pipef")
    rect(x + w - 22, y - 10, 22, h + 20, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="pipef")
    arrow(x - 30, y + h / 2, [[0, 0], [w + 60, 0]], stroke=accent, sw=3, rough=1, dashed=True)

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude Projects", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4, "the multiplier - set up once, use forever", size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - THE TAX YOU PAY EVERY MORNING
# ============================================================================
ox = beat_head(1, "The tax you pay every morning")
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
dw, dgap, dy = 192, 26, 320
for k, d in enumerate(days):
    dx = ox + 40 + k * (dw + dgap)
    sticky(dx, dy, dw, 200, RED_BG, angle=jit(1.6))
    text(dx + 22, dy + 18, d, size=BODY, color=RED)
    text(dx + 22, dy + 64, "Who I am -\nmy role -\nhouse tone -\ndo-not-say\nlist ...", size=SMALL, color=INK)
    arrow(dx + dw / 2, dy + 200, [[0, 0], [0, 32]], stroke=RED, sw=2, rough=1)
text(ox + 40, dy + 248, "the same brief, re-pasted every single morning", size=SMALL, color=GREYD)
clock(ox + 110, 700, 46, RED)
text(ox + 180, 676, "~10 min a day", size=H3, color=INK)
text(ox + 180, 726, "= about 1 hour a week. Every week.", size=H3, color=RED)
text(ox + 40, 830, "Re-explaining yourself is invisible work. It adds up.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 2 - EVERY CHAT STARTS FROM ZERO  (the cold chat)
# ============================================================================
ox = beat_head(2, "Every chat starts from zero")
cwx, cwy, cww, cwh = ox + 40, 300, 700, 566
chat_window(cwx, cwy, cww, cwh)
# explicit, visibly-different angles - a paste you can see is a re-paste
asks = [("Mon - draft a reply", 0.048), ("Wed - rewrite an update", -0.030),
        ("Fri - draft a reply", 0.022)]
ty = cwy + 66
for ask, pang in asks:
    context_note(cwx + 30, ty, 300, 112, ORANGE, ORANGE_BG, angle=pang)
    rect(cwx + 372, ty + 34, 296, 46, stroke="transparent", bg=FAINT, sw=1, rough=1,
         rounded=True, prefix="msg")
    text(cwx + 392, ty + 44, ask, size=SMALL, color=GREYD)
    ty += 172
text(ox + 40, 900, "the same context, re-pasted into every new thread", size=BODY, color=GREYD)
claude_face(ox + 940, 440, r=46, color=ORANGE)
text_centered(ox + 940, 530, "no memory of\nyesterday's brief", size=SMALL, color=GREYD)
text(ox + 806, 660, "So you paste the\nsame tone guide\nagain. And again.", size=H3, color=ORANGE)

# ============================================================================
# BEAT 3 - EVERY CHAT STARTS BRIEFED  (the briefed chat)
# ============================================================================
ox = beat_head(3, "Every chat starts briefed")
folder(ox + 60, 350, 300, 200, GREEN, GREEN_BG)
text(ox + 60, 600, "Project:  Customer replies", size=H3, color=GREEN)
text(ox + 60, 654, "team tone guide\nexample replies\nthe do-not-say list", size=SMALL, color=GREYD)
arrow(ox + 384, 466, [[0, 0], [126, 0]], stroke=GREEN, sw=5, rough=1)
text(ox + 396, 406, "written once", size=SMALL, color=GREEN)
chat_window(ox + 540, 320, 580, 470)
rect(ox + 572, 396, 380, 48, stroke="transparent", bg=FAINT, sw=1, rough=1, rounded=True, prefix="msg")
text(ox + 592, 406, "draft a reply - order late", size=SMALL, color=GREYD)
rect(ox + 572, 476, 500, 186, stroke=GREEN, bg=GREEN_BG, sw=2, rough=1, rounded=True,
     fill="solid", opacity=40)
text(ox + 598, 506, "warm, clear, on-brand -\nfirst time, and every\ntime after that.", size=BODY, color=INK)
text(ox + 598, 692, "nothing pasted", size=SMALL, color=GREEN)
text(ox + 60, 830, "one Project, one arrow - a fresh chat is briefed before you type.", size=BODY, color=GREYD)
demo_badge(ox + 60, 886, "show in Claude desktop app: build the Project live")

# ============================================================================
# BEAT 4 - WHAT A PROJECT ACTUALLY IS
# ============================================================================
ox = beat_head(4, "What a Project actually is")
cont_x, cont_y, cont_w, cont_h = ox + 40, 300, 1080, 560
rect(cont_x, cont_y, cont_w, cont_h, stroke=VIOLET, bg=VIOLET_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=22, angle=jit(0.8))
text(cont_x + 28, cont_y + 18, "ONE PROJECT", size=H3, color=VIOLET)
parts = [("Custom instructions", "Your standing brief: role,\nyour house voice, what to avoid.", obj_doc, VIOLET, VIOLET_BG),
         ("Knowledge files", "Reference docs Claude reads\nbefore every reply.", obj_files, BLUE, BLUE_BG),
         ("Conversations", "Every chat here shares the\ntwo above - automatically.", None, GREEN, GREEN_BG)]
pw = (cont_w - 80) / 3
for k, (ttl, body, illus, acc, abg) in enumerate(parts):
    px = cont_x + 20 + k * (pw + 10)
    sticky(px, cont_y + 70, pw - 10, cont_h - 200, WHITE, angle=jit(0.8))
    rect(px, cont_y + 70, pw - 10, cont_h - 200, stroke=acc, bg="transparent", sw=2, rough=1, rounded=True)
    text(px + 22, cont_y + 92, ttl, size=LABEL, color=acc)
    if illus:
        illus(px + 24, cont_y + 150, acc, abg)
    else:
        for m in range(3):
            rect(px + 24, cont_y + 150 + m * 34, pw - 90, 24, stroke="transparent", bg=FAINT, sw=1, rounded=True, prefix="msg")
    text(px + 22, cont_y + 304, body, size=SMALL, color=INK)
text(cont_x + 20, cont_y + cont_h + 24, "One persistent space. Context lives here,\nnot in your clipboard.", size=H3, color=VIOLET)

# ============================================================================
# BEAT 5 - THE SHIFT (before -> after)
# ============================================================================
ox = beat_head(5, "The shift")
# BEFORE - top
bx, by = ox + 60, 300
text(bx, by - 36, "BEFORE", size=H3, color=RED)
for k in range(3):
    sticky(bx + k * 26, by + k * 22, 300, 86, FAINT, angle=jit(2.0))
text(bx + 56, by + 26, "context ...\ncontext ...", size=SMALL, color=GREYD)
arrow(bx + 360, by + 50, [[0, 0], [260, 0]], stroke=RED, sw=3, rough=1)
claude_face(bx + 700, by + 56, r=42, color=RED)
text(bx + 666, by + 130, "paste it all, every time", size=SMALL, color=RED)
# arrow down to AFTER
arrow(bx + 180, by + 200, [[0, 0], [0, 120]], stroke=BLUE, sw=6, rough=1)
text(bx + 220, by + 240, "write it once", size=BODY, color=BLUE)
# AFTER - below
ay = by + 340
text(bx, ay - 36, "AFTER", size=H3, color=BLUE)
rect(bx, ay, 360, 260, stroke=BLUE, bg=BLUE_BG, sw=3, rough=1, rounded=True, fill="solid", opacity=30, angle=jit(-1.0))
text(bx + 110, ay + 22, "Project", size=H2, color=BLUE)
text(bx + 40, ay + 100, "the brief lives here\nand never moves", size=SMALL, color=INK)
claude_face(bx + 700, ay + 90, r=42, color=BLUE)
text(bx + 660, ay + 170, "context is permanent", size=SMALL, color=BLUE)
text(ox + 40, ay + 290, "Write the brief once.\nClaude applies it every time.", size=H3, color=BLUE)

# ============================================================================
# BEAT 6 - THE INSTRUCTIONS FIELD  (the folder, opened out)
# ============================================================================
ox = beat_head(6, "The instructions field")
open_folder(ox + 40, 336, 1080, 520, VIOLET_T)
# the one thing in the folder that is not reference material: saturated, and far
# bigger than everything around it. The size and the fill do the work - no glow,
# no highlighter sweep, no sparkles.
ia = jit(1.5)
sticky(ox + 80, 386, 470, 360, VIOLET, angle=ia)
text(ox + 112, 416, "Custom instructions", size=H3, color=WHITE, angle=ia)
text(ox + 112, 484, "who you are\nyour house voice\nwhat never to say\nBritish English", size=BODY, color=WHITE, angle=ia)
# the rest of the folder: small, neutral, ink-and-grey reference doodles
refs = [("tone guide", 620, 396), ("example replies", 860, 396),
        ("do-not-say list", 620, 560), ("past conversations", 860, 560)]
for lab, rx, ry in refs:
    file_icon(ox + rx, ry, 66, 84, abg=FAINT)
    text(ox + rx, ry + 96, lab, size=SMALL, color=GREYD)
text(ox + 620, 706, "everything else is reference.\nThis is the part that changes\nevery answer you get.", size=SMALL, color=GREYD)
text(ox + 40, 886, "the highest-leverage square inch", size=H3, color=INK)

# ============================================================================
# BEAT 7 - WRITE IT LIKE YOU MEAN IT  (how to write the instructions)
# ============================================================================
# Distilled from Claude Code's memory docs (code.claude.com/docs/en/memory):
# only the part that changes what a PERSON TYPES - specific over vague, short,
# structured, no contradictions, write down what you would otherwise re-explain.
# The developer machinery (.claude/rules/, claudeMdExcludes, /memory, auto
# memory settings) is deliberately off the board; this audience uses the app.
ox = beat_head(7, "Write it like you mean it")
py7 = 300
pairs7 = [("be professional", "warm, plain English, no jargon,\nunder 120 words"),
          ("follow our format", "greeting, answer, next step,\nsign-off - in that order")]
for vague, precise in pairs7:
    xmark(ox + 46, py7 + 10, RED, s=22, sw=4)
    text(ox + 96, py7, '"' + vague + '"', size=BODY, color=GREYD)
    arrow(ox + 420, py7 + 20, [[0, 0], [90, 0]], stroke=INDIGO, sw=3, rough=1)
    tick(ox + 550, py7 + 2, GREEN)
    text(ox + 600, py7, '"' + precise + '"', size=BODY, color=INK)
    py7 += 150
ry7 = 610
for r7 in ["Specific beats vague - write what you could check.",
           "Short beats long - it is read before every answer.",
           "Structure it: headings and bullets, not a paragraph.",
           "Two rules that contradict each other get picked at random.",
           "Re-explained it twice? It belongs in here."]:
    check_item(ox + 46, ry7, r7, accent=INDIGO)
    ry7 += 52
chip(ox + 46, 890, "in Claude Code the same job is a CLAUDE.md file",
     fill=INDIGO_BG, text_color=INK, border=INDIGO)
text(ox + 46, 960, "you write the rules; Claude keeps its own notes alongside them",
     size=SMALL, color=GREY)

# ============================================================================
# BEAT 8 - THREE PROJECTS YOU COULD BUILD THIS WEEK
# ============================================================================
ox = beat_head(8, "Three Projects you could build this week")
projects = [
    ("A", "Customer reply drafting", "Support and Ops",
     "your tone guide - examples of\ngreat replies - the do-not-say list", GREEN, GREEN_BG, True),
    ("B", "Engineering PR review", "Engineering",
     "coding standards - common review\npatterns - the team style guide", BLUE, BLUE_BG, False),
    ("C", "Weekly board prep", "Leadership",
     "board memo format - the last four\nmemos - what the board cares about", ORANGE, ORANGE_BG, False),
]
cw, ch, cgap, cy0 = 1070, 235, 16, 285
for k, (letter, ttl, who, files, acc, abg, gate) in enumerate(projects):
    cy = cy0 + k * (ch + cgap)
    sticky(ox + 40, cy, cw, ch, abg, angle=jit(0.8))
    ellipse(ox + 64, cy + 24, 50, 50, stroke=acc, bg=acc, sw=2)
    text_centered(ox + 89, cy + 35, letter, size=H2, color=WHITE)
    text(ox + 132, cy + 32, ttl, size=H3, color=acc)
    text(ox + 132, cy + 92, "Who: " + who, size=BODY, color=INK)
    # right half: knowledge files
    text(ox + 600, cy + 28, "Knowledge:", size=SMALL, color=GREYD)
    text(ox + 600, cy + 64, files, size=SMALL, color=INK)
    if gate:
        rect(ox + 132, cy + 150, 420, 64, stroke=RED, bg=RED_BG, sw=2, rough=1, rounded=True, fill="solid", opacity=30)
        text(ox + 150, cy + 164, "Drafts only - a person checks\nand sends. Never auto-sent.", size=SMALL, color=RED)

# ============================================================================
# BEAT 9 - THE MATHS
# ============================================================================
ox = beat_head(9, "The maths")
base = 700
line(ox + 60, base, [[0, 0], [560, 0]], stroke=INK, sw=2)
# setup bar (small) vs saving bar (big)
rect(ox + 120, base - 90, 150, 90, stroke=INK, bg=ORANGE, sw=2, rough=1, rounded=False)
text_centered(ox + 195, base + 14, "Setup", size=SMALL, color=GREYD)
text_centered(ox + 195, base - 130, "20 min\nonce", size=SMALL, color=ORANGE)
rect(ox + 360, base - 360, 150, 360, stroke=INK, bg=GREEN, sw=2, rough=1, rounded=False)
text_centered(ox + 435, base + 14, "Saving", size=SMALL, color=GREYD)
text_centered(ox + 435, base - 400, "hours\nevery week", size=SMALL, color=GREEN)
text(ox + 700, base - 320, "Setup:  20 minutes.\nOnce.", size=H3, color=ORANGE)
text(ox + 700, base - 180, "Saving:  hours every\nweek - for as long as\nyou do the job.", size=H3, color=GREEN)
# under the bars
highlighter(ox + 56, base + 70, 940, 60, ORANGE_BG, angle=0.0)
text(ox + 70, base + 82, "The best twenty minutes you'll spend this month.", size=BODY, color=INK)

# ============================================================================
# BEAT 10 - WHAT YOU GET ON YOUR PLAN
# ============================================================================
# Figures from the Claude Projects help-centre article: Projects are on every
# plan, free is capped at five, paid plans are uncapped and fall back to
# retrieval (up to 10x capacity) when a knowledge base outgrows the context.
ox = beat_head(10, "What you get on your plan")
text(ox + 40, 296, "Free", size=H2, color=GREYD)
for k in range(5):
    folder(ox + 44 + k * 116, 362, 96, 62, GREYD, FAINT, papers=False)
text(ox + 44, 456, "Projects are on every plan, including free - five of them, and that is the cap.",
     size=BODY, color=INK)
line(ox + 40, 536, [[0, 0], [1040, 0]], stroke=FAINT, sw=2, dashed=True)
text(ox + 40, 576, "Pro, Max, Team and Enterprise", size=H2, color=BLUE)
for k in range(6):
    folder(ox + 44 + k * 116, 642, 96, 62, BLUE, BLUE_BG, papers=False)
text(ox + 748, 656, "...", size=H2, color=BLUE)
text(ox + 44, 736, "As many as you like. And as a knowledge base gets close to the context\n"
                   "limit, Claude switches to retrieval on its own - up to 10 times the\n"
                   "capacity, with the same answer quality.", size=BODY, color=INK)
chip(ox + 44, 880, "retrieval is a paid-plan feature", fill=BLUE_BG, text_color=INK, border=BLUE)

# ============================================================================
# BEAT 11 - WHY IT'S A MULTIPLIER
# ============================================================================
ox = beat_head(11, "Why it's a multiplier")
sx, sy = ox + 120, 460
claude_face(sx, sy, r=48, color=TEAL)
text_centered(sx, sy + 80, "builds the\nProject once", size=SMALL, color=GREYD)
fan_x = sx + 460
for k in range(4):
    py = sy - 150 + k * 110
    arrow(sx + 70, sy, [[0, 0], [fan_x - sx - 110, py - sy + 30]], stroke=GREY, sw=2, rough=1)
    person(fan_x + 40, py + 30, TEAL)
text(fan_x + 110, sy - 130, "the whole\nteam uses it", size=H3, color=TEAL)
text(ox + 40, 800, "One person builds Customer Replies. The support team\ndrafts in the house voice from day one.", size=BODY, color=INK)
text(ox + 40, 900, "Sharing is available on Team and Enterprise plans.", size=SMALL, color=GREY)

# ============================================================================
# BEAT 12 - SHARING, AND WHO CAN DO WHAT
# ============================================================================
# The mechanics behind beat 11's fan-out, per the help-centre article: two
# permission levels, three ways to share, and the admin switch that can turn
# organisation-wide sharing off.
ox = beat_head(12, "Sharing, and who can do what")
# what each level can actually do - ticks and crosses, not prose
levels = [(40, "Can view", jit(1.0),
           [(True, "read what is in it"), (True, "chat in it"), (False, "change it")]),
          (600, "Can edit", jit(-1.0),
           [(True, "everything above"), (True, "change the instructions"),
            (True, "add and remove files")])]
for lx, ttl, la, rows in levels:
    sticky(ox + lx, 300, 520, 280, VIOLET_BG, angle=la)
    text(ox + lx + 36, 326, ttl, size=H2, color=VIOLET)
    yy = 396
    for allowed, lab in rows:
        if allowed:
            tick(ox + lx + 42, yy - 2, GREEN, s=22, sw=4)
        else:
            xmark(ox + lx + 44, yy, RED, s=18, sw=4)
        text(ox + lx + 86, yy - 6, lab, size=BODY, color=INK)
        yy += 52
text(ox + 40, 636, "Share it with one person, add people in bulk, or make it visible to the\n"
                   "whole organisation.", size=BODY, color=INK)
ry12 = 746
for r12 in ['They get an email, and find it under "Shared with me".',
            "Team and Enterprise plans only.",
            "An admin can switch organisation-wide sharing off."]:
    check_item(ox + 40, ry12, r12, accent=VIOLET)
    ry12 += 58

# ============================================================================
# BEAT 13 - LET'S BUILD ONE, LIVE
# ============================================================================
ox = beat_head(13, "Let's build one - live")
steps = ["Name it, and set who can see it",
         "Write the custom instructions",
         "Add two or three reference files, then chat"]
for k, s in enumerate(steps):
    sy = 320 + k * 150
    num_circle(ox + 50, sy, k + 1, INDIGO, d=64)
    sticky(ox + 140, sy, 940, 96, INDIGO_BG, angle=jit(0.8))
    text(ox + 176, sy + 28, s, size=H3, color=INK)
demo_badge(ox + 140, 320 + 3 * 150 + 10, "show in Claude desktop app:  building a Customer Replies Project")

# ============================================================================
# BEAT 14 - PAUSE HERE, AND TRY IT
# ============================================================================
ox = beat_head(14, "Pause here, and try it")
pause_icon(ox + 40, 322, 80, color=YELLOW)
lines14 = ["Think of one task you repeat.",
           "Open claude.ai/projects and create it\nnow - even empty.",
           "Fill it as you watch the rest of\nthis module."]
yy = 332
for s in lines14:
    text(ox + 170, yy, s, size=H3, color=INK)
    yy += text_h(s, H3) + 28
text(ox + 170, yy + 8, "two minutes - then carry on.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 15 - SLOW VS LIVE  (two halves, stacked)
# ============================================================================
ox = beat_head(15, "Slow vs live")
# TOP half - the slow-changing stuff, which is exactly what a Project holds
obj_files(ox + 80, 340, BLUE, BLUE_BG)
text(ox + 320, 350, "slow-changing lives here", size=H3, color=BLUE)
text(ox + 320, 412, "the tone guide, the templates, the standards -\nthings that change monthly, not hourly.", size=BODY, color=GREYD)
text(ox + 320, 508, "Drop them into the Project once.", size=BODY, color=INK)
line(ox + 60, 620, [[0, 0], [1000, 0]], stroke=FAINT, sw=2, dashed=True)
# BOTTOM half - live data, which is a different tool's job
pipe(ox + 110, 730, 160, 60, BLUE, BLUE_BG)
text(ox + 320, 700, "live data comes next: Connectors and MCP", size=H3, color=BLUE)
text(ox + 320, 762, "stock levels, tickets, today's numbers -\nstale the moment you paste them.", size=BODY, color=GREYD)
text(ox + 320, 858, "That is a Connector's job, not a Project's.", size=BODY, color=INK)

# ============================================================================
# BEAT 16 - ONE PROJECT, TWENTY MINUTES (close)
# ============================================================================
ox = beat_head(16, "One Project. Twenty minutes.")
highlighter(ox + 36, 318, 620, 64, VIOLET_BG, angle=0.0)
text(ox + 50, 330, "Use it once a day for a month.", size=H3, color=INK)
text(ox + 50, 410, "Then tell me Projects didn't\nchange how you work.", size=H3, color=VIOLET)
text(ox + 40, 540, "Resources", size=H3, color=VIOLET)
text(ox + 60, 606, "Anthropic Help Centre - 'How can I create and\nmanage projects' (support.claude.com)", size=SMALL, color=VIOLET)
text(ox + 60, 700, "AI Ops Learn - Prompt Library - the team's\nshared Projects", size=SMALL, color=VIOLET)
text(ox + 60, 782, "Engineers - the same idea in Claude Code:\ncode.claude.com/docs/en/memory", size=SMALL, color=VIOLET)
# the one line to leave them with, as a chip in the beat's own accent
chip(ox + 40, 860, "third paste of the week = it wants a Project",
     fill=VIOLET_BG, text_color=INK, border=VIOLET)

# No connector spine and no branding footer: beats read as one picture through
# layout + consistent rhythm (the ai-foundations natural-flow look), not arrows.

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-projects.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
