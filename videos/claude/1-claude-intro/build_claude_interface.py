#!/usr/bin/env python3
"""Build claude_intro.excalidraw - ONE flowing, illustrated explainer for the
"Claude, properly" training video (Phlo AI training, Module 2, video 1, ~5 min).

This intro is the MAP for the whole Claude module. It teaches the six core
surfaces that have NO dedicated video of their own - the things you need on
day one:
  Conversations . Model picker (incl. effort + thinking) . File uploads .
  Web search . Research . Voice
plus the first-time SETUP basics (none of which have their own video): how to
access Claude (web / desktop / mobile, work-account sign-in - a line in the
opening) and a "Set it up once" Settings beat (Instructions for Claude /
profile, Memory, and Appearance & language - theme, dyslexic-friendly font,
language, notifications). Data/privacy is NOT a card: on Phlo's Team plan,
training on customer content is barred by contract, so there is no per-user
data toggle to manage - just a one-line mention. The hard no-confidential-data
rule stays on the File-uploads beat. It then SIGNPOSTS the rest of the module (Projects, Artifacts, Skills,
Scheduled tasks, Connectors/MCP, Cowork, and Claude for PowerPoint / Excel /
Word / Chrome / Design), each of which gets its own video. It deliberately does
NOT spend a headline beat on Projects or Artifacts (videos 2 and 3), and does
NOT cover Styles at all: as of June 2026 Claude is retiring Styles into Skills
(the Concise/Formal/Explanatory defaults are being discontinued; custom styles
convert to skills under Customize > Skills), and Skills has its own video (4),
so Styles is left to that video rather than taught or signposted here.

Interface facts checked against the Claude Help Centre (support.claude.com),
June 2026:
  - Voice mode is a beta feature on the WEB app (Claude.ai) and mobile - a
    sound-wave icon in the lower-right of the chat window. (Not the desktop app.)
  - Web search and Research live in the composer's "+ / Search and tools" area
    at the bottom-left of the input box. Research is multi-step, runs in the
    background, and needs web search switched on.
  - The model picker sits along the BOTTOM of the composer (not top-right), so
    the hero window draws it as the first pill in that bottom row. The same model
    menu holds the Effort setting (five levels Low/Medium/High/Extra/Max - High
    is the default; Opus & Sonnet only, not Haiku) and a separate Extended-
    thinking switch, enabled for complex tasks.

Style B (house style): a single hand-drawn journey, left-to-right, NO frames,
NO boxes, white canvas, everything in the Virgil hand font (fontFamily 1),
roughness 1. A lively Excalidraw palette colour-coded per beat. Modelled on
videos/claude/3-artefacts/. Imports the shared engine; this file holds only the
composition (scene + beat scaffold) and the bespoke Claude.ai window.

Run:  python3 build_claude_interface.py
      python3 ../../../preview.py claude_intro.excalidraw out.png [XMIN XMAX]
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(40404)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# PER-FEATURE COLOURS - each surface gets one distinct, on-palette accent reused
# on its badge / heading / chips / illustration. The first six are the featured
# essentials; C_SKILLS just colours the "Skills" pill shown in the hero composer
# (Skills is a real menu item with its own video - not taught here).
# ----------------------------------------------------------------------------
C_CONV, C_MODEL, C_FILES, C_WEB, C_RES, C_VOICE, C_SKILLS = \
    ORANGE, INDIGO, GREEN, TEAL, BLUE, YELLOW, VIOLET

# ----------------------------------------------------------------------------
# THE HERO ILLUSTRATION - a Claude.ai web window with the real surfaces drawn
# where they actually live, each labelled. The beat-1 agenda list below it
# teaches the names; the window just shows WHERE each one is.
# ----------------------------------------------------------------------------
def tool_btn(x, y, label, color):
    """A small composer tool pill (Files / Web / Research / Skills)."""
    w = text_w(label, SMALL) + 26
    rect(x, y, w, 34, stroke=color, bg=WHITE, sw=2, rough=1, rounded=True, prefix="tbtn")
    text(x + 13, y + 8, label, size=SMALL, color=color)
    return w

def voice_wave(cx, cy, color, scale=1.0):
    """A little sound-wave glyph - Claude's voice-mode icon."""
    for k, hh in enumerate((10, 20, 30, 20, 10)):
        hh *= scale
        line(cx + k * 8 * scale, cy - hh / 2, [[0, 0], [0, hh]], stroke=color, sw=3, rough=1, prefix="wave")

def claude_window_full(x, y, w, h):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="cwin")
    line(x, y + 44, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 20 + k * 20, y + 16, 11, 11, stroke=GREY, bg=GREY, sw=1)
    # 1) left sidebar -> Conversations (chats list)
    sb_x, sb_w = x + 18, 236
    sb_y, sb_h = y + 56, h - 74
    rect(sb_x, sb_y, sb_w, sb_h, stroke="transparent", bg=ORANGE_BG, sw=1, rough=1,
         rounded=True, fill="solid", opacity=40, prefix="side")
    for k in range(5):
        rect(sb_x + 18, sb_y + 22 + k * 50, sb_w - 36, 28, stroke="transparent", bg=WHITE,
             sw=1, rough=1, rounded=True, prefix="srow")
    text(sb_x + 18, sb_y + sb_h - 30, "your chats", size=SMALL, color=GREY)
    # central chat column -> the conversation
    cx = sb_x + sb_w + 40
    cw = 520
    my = y + 78
    for f in (1.0, 0.7, 0.92, 0.6):
        rect(cx, my, cw * f, 30, stroke="transparent", bg=FAINT, sw=1, rough=1,
             rounded=True, prefix="msg")
        my += 46
    # composer (input bar) at the bottom - on Claude.ai the model picker AND the
    # tools all live along the bottom of this box (verified, June 2026).
    ib_x = cx
    ib_y = y + h - 96
    ib_w = (x + w - 26) - ib_x
    rect(ib_x, ib_y, ib_w, 80, stroke=GREY, bg=WHITE, sw=2, rough=1, rounded=True, prefix="input")
    text(ib_x + 14, ib_y + 8, "ask anything...", size=SMALL, color=GREY)
    # bottom row, left -> right: model picker, then the "+ / Search and tools" pills
    bx = ib_x + 14
    by = ib_y + 38
    bx += tool_btn(bx, by, "Sonnet v", C_MODEL) + 10   # 2) Model picker
    bx += tool_btn(bx, by, "Files", C_FILES) + 10      # 3) File uploads
    bx += tool_btn(bx, by, "Web", C_WEB) + 10          # 4) Web search
    bx += tool_btn(bx, by, "Research", C_RES) + 10     # 5) Research
    tool_btn(bx, by, "Skills", C_SKILLS)               # Skills - real menu item, its own video (4)
    # 6) voice + send, on the right of the composer
    voice_wave(ib_x + ib_w - 84, by + 17, C_VOICE)
    ellipse(ib_x + ib_w - 38, by, 26, 26, stroke=GREYD, bg=GREYD, sw=2)

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - uniform slots + wide gaps so each beat frames cleanly on a
# 14" laptop. Eight beats, left to right.
# ----------------------------------------------------------------------------
N = 10
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
# Beats 3 and 4 are both the model picker (family, then effort), so they share
# the model accent. 5 files, 6 web/research, 7 voice, 8 settings (set-up-once),
# 9 pause, 10 recap.
ACCENT = {1: VIOLET, 2: C_CONV, 3: C_MODEL, 4: C_MODEL, 5: C_FILES,
          6: C_WEB, 7: C_VOICE, 8: INDIGO, 9: BLUE, 10: VIOLET}
OX, _c = {}, 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c

HEAD_Y = 60

def head(ox, title, accent, sub=None):
    """QUIET heading: kit heading() draws a prominent hand title in the beat's
    accent colour + a lively hand underline. No step circle, no highlighter sweep,
    no scribble of its own."""
    heading(ox, HEAD_Y, title, color=accent, sub=sub)

# ----------------------------------------------------------------------------
# Small shared illustrations for the teaching beats
# ----------------------------------------------------------------------------
def illus_search(cx, cy, accent):       # magnifier over a globe -> live web
    ellipse(cx - 30, cy - 30, 58, 58, stroke=accent, bg="transparent", sw=4, rough=1)
    line(cx - 1, cy - 30, [[0, 0], [0, 58]], stroke=accent, sw=2, rough=1)
    line(cx - 30, cy - 1, [[0, 0], [58, 0]], stroke=accent, sw=2, rough=1)
    line(cx + 22, cy + 22, [[0, 0], [26, 26]], stroke=accent, sw=5, rough=1)

def illus_research(cx, cy, accent):     # cross-referenced sources: docs linked by lines
    nodes = [(cx - 46, cy - 34), (cx + 18, cy - 44), (cx - 4, cy + 22)]
    line(cx - 28, cy - 16, [[0, 0], [56, -12]], stroke=accent, sw=2, rough=1)   # links
    line(cx - 28, cy - 16, [[0, 0], [30, 50]], stroke=accent, sw=2, rough=1)
    line(cx + 36, cy - 26, [[0, 0], [-22, 60]], stroke=accent, sw=2, rough=1)
    for nx, ny in nodes:
        rect(nx, ny, 38, 48, stroke=INK, bg=BLUE_BG, sw=2, rough=1, rounded=True, prefix="src")
        line(nx + 8, ny + 14, [[0, 0], [22, 0]], stroke=GREY, sw=2)
        line(nx + 8, ny + 28, [[0, 0], [22, 0]], stroke=GREY, sw=2)

def illus_think(cx, cy, accent):        # ascending "thinking longer" dots
    for dx, dy, r in [(-34, 24, 8), (-8, 4, 12), (24, -20, 18)]:
        ellipse(cx + dx - r, cy + dy - r, 2 * r, 2 * r, stroke=accent, bg=accent, sw=2, rough=1)

def illus_memory(cx, cy, accent):       # a bookmark - context kept / remembered
    line(cx - 22, cy - 38, [[0, 0], [44, 0], [44, 74], [22, 52], [0, 74], [0, 0]],
         stroke=accent, sw=3, rough=1, bg=WHITE, fill="solid", prefix="bmk")
    line(cx - 8, cy - 20, [[0, 0], [16, 0]], stroke=accent, sw=2, rough=1)
    line(cx - 8, cy - 4, [[0, 0], [16, 0]], stroke=accent, sw=2, rough=1)

def illus_appearance(cx, cy, accent):   # theme + fonts: an 'Aa' and a little sun
    text(cx - 50, cy - 34, "Aa", size=H1, color=accent)
    scx, scy = cx + 34, cy + 4
    ellipse(scx - 13, scy - 13, 26, 26, stroke=accent, bg=accent, sw=2, rough=1)
    for sx, sy, ex, ey in [(0, -24, 0, -16), (0, 16, 0, 24), (-24, 0, -16, 0), (16, 0, 24, 0)]:
        line(scx + sx, scy + sy, [[0, 0], [ex - sx, ey - sy]], stroke=accent, sw=2, rough=1)

# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude, properly", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "what's actually on screen - beyond the chat box", size=H2, color=VIOLET)
text(OX[1] + 6, -300 + HERO * LINE_H + 4 + H2 * LINE_H + 8,
     "- and where the productivity hides", size=H3, color=GREYD)
text(OX[1] + 6, -300 + HERO * LINE_H + 4 + H2 * LINE_H + 8 + H3 * LINE_H + 8,
     "Phlo AI training  -  about 6 minutes", size=SMALL, color=GREY)

# ============================================================================
# BEAT 1 - THE MAP: one window, six things worth knowing
# ============================================================================
ox = OX[1]
head(ox, "One window. More than a chat box.", ACCENT[1])
text(ox + 50, 190,
     "On the web, a desktop app and mobile - sign in with your work account.  (Shown here: the web app.)",
     size=SMALL, color=GREY)
win_x, win_y, win_w, win_h = ox + 50, 250, 1100, 420
claude_window_full(win_x, win_y, win_w, win_h)

# Agenda: the six featured surfaces, numbered, in two columns under the window.
agenda = [
    ("Conversations", C_CONV), ("Model picker", C_MODEL),
    ("File uploads", C_FILES), ("Web search", C_WEB),
    ("Research", C_RES), ("Voice", C_VOICE),
]
text(ox + 70, win_y + win_h + 36, "Six things worth knowing - we'll take each:",
     size=BODY, color=GREYD)
ay0 = win_y + win_h + 96
for k, (name, acc) in enumerate(agenda):
    col = k // 3
    row = k % 3
    ax = ox + 90 + col * 560
    ay = ay0 + row * 66
    num_badge(ax, ay, k + 1, acc, d=40)
    text(ax + 54, ay + 4, name, size=H3, color=acc)

# ============================================================================
# BEAT 2 - CONVERSATIONS: useful, but volatile
# ============================================================================
ox = OX[2]
head(ox, "Conversations: useful, but volatile", ACCENT[2])

def chat_bubble(x, y, w, h, accent, abg, filled=True):
    rect(x, y, w, h, stroke=accent, bg=abg, sw=2, rough=1, rounded=True, fill="solid",
         opacity=55, prefix="bub")
    if filled:
        for k in range(3):
            line(x + 22, y + 30 + k * 26, [[0, 0], [w - 64, 0]], stroke=GREY, sw=2)
    else:
        text(x + 22, y + h / 2 - 16, "starts blank", size=SMALL, color=GREY)

chat_bubble(ox + 60, 290, 360, 200, C_CONV, ORANGE_BG, filled=True)
text(ox + 60, 506, "Chat A", size=SMALL, color=GREYD)
chat_bubble(ox + 760, 290, 360, 200, C_CONV, ORANGE_BG, filled=False)
text(ox + 760, 506, "Chat B", size=SMALL, color=GREYD)
arrow(ox + 430, 380, [[0, 0], [320, 0]], stroke=RED, sw=3, rough=1, dashed=True)
# a red cross on the arrow - context does NOT carry across
line(ox + 580, 360, [[0, 0], [28, 28]], stroke=RED, sw=4, rough=1)
line(ox + 608, 360, [[0, 0], [-28, 28]], stroke=RED, sw=4, rough=1)
text(ox + 470, 410, "context doesn't carry", size=SMALL, color=RED)
text(ox + 60, 580,
     "Every chat is its own bubble. Brilliant for one-off\nquestions. But unless you're inside a Project, Claude\ndoesn't carry your instructions or files from one chat\nto the next.",
     size=BODY, color=INK)
sticky(ox + 60, 820, 720, 86, VIOLET_BG, angle=jit(1.0))
text(ox + 84, 846, "Projects fix this - persistent context across chats.",
     size=BODY, color=VIOLET)
chip(ox + 800, 832, "video 2", fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)

# ============================================================================
# BEAT 3 - PICK THE MODEL DELIBERATELY  (no dedicated video -> taught in full)
# ============================================================================
ox = OX[3]
head(ox, "Pick the model deliberately", ACCENT[3])

def opus_illus(cx, cy, accent):     # heavy: a stacked weight
    rect(cx - 60, cy + 40, 120, 24, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)
    rect(cx - 42, cy + 18, 84, 24, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)
    rect(cx - 24, cy - 4, 48, 24, stroke=INK, bg=accent, sw=2, rough=1, rounded=True)

def sonnet_illus(cx, cy, accent):   # balanced: a little balance scale
    line(cx, cy - 8, [[0, 0], [0, 50]], stroke=accent, sw=3, rough=1)
    line(cx - 44, cy, [[0, 0], [88, 0]], stroke=accent, sw=3, rough=1)
    line(cx, cy + 50, [[0, 0], [-24, 0], [24, 0]], stroke=accent, sw=3, rough=1)
    ellipse(cx - 58, cy + 6, 28, 16, stroke=accent, bg=accent, sw=2, rough=1)
    ellipse(cx + 30, cy + 6, 28, 16, stroke=accent, bg=accent, sw=2, rough=1)

def haiku_illus(cx, cy, accent):    # light + fast: motion lines + a zippy dot
    for k, ln in enumerate((100, 76, 52)):
        line(cx - 50, cy + 8 + k * 20, [[0, 0], [ln, 0]], stroke=accent, sw=4, rough=1)
    ellipse(cx + 56, cy + 20, 14, 14, stroke=accent, bg=accent, sw=2)

cards = [
    ("Opus", "Claude Opus 4.8", "Deep reasoning, long-form writing,\ncomplex analysis. Slowest, deepest.",
     INDIGO, INDIGO_BG, opus_illus, None),
    ("Sonnet", "Claude Sonnet 4.6", "Balanced speed and quality.\nMost day-to-day work.",
     GREEN, GREEN_BG, sonnet_illus, "DEFAULT"),
    ("Haiku", "Claude Haiku 4.5", "Fast and light.\nQuick lookups, simple drafts.",
     YELLOW, YELLOW_BG, haiku_illus, None),
]
cw, cy0, ch, cvg = 1100, 250, 200, 20
for k, (name, sub, body, acc, abg, illus, tag) in enumerate(cards):
    cy = cy0 + k * (ch + cvg)
    sticky(ox + 30, cy, cw, ch, abg, angle=jit(1.0))
    text(ox + 70, cy + 24, name, size=H2, color=acc)
    text(ox + 70, cy + 80, sub, size=SMALL, color=GREYD)
    if tag:
        chip(ox + 70, cy + 130, tag, fill=acc, text_color=WHITE, border=acc, size=SMALL)
    illus(ox + cw - 220, cy + 90, acc)
    text(ox + cw - 480, cy + 24, body, size=BODY, color=INK)
fy = cy0 + 3 * (ch + cvg) + 12
text(ox + 30, fy, "Heavier models think longer and use more of your\nallowance.  Lighter ones are faster.",
     size=BODY, color=GREYD)
gy = fy + 96
gx = ox + 30
text(gx, gy + 10, "faster", size=SMALL, color=GREY)
gx += 120
for lab, acc, abg in [("Haiku", YELLOW, YELLOW_BG), ("Sonnet", GREEN, GREEN_BG), ("Opus", INDIGO, INDIGO_BG)]:
    w, h = chip(gx, gy, lab, fill=abg, text_color=acc, border=acc, size=SMALL)
    gx += w
    arrow(gx + 6, gy + h / 2, [[0, 0], [36, 0]], stroke=GREY, sw=3)
    gx += 48
text(gx + 6, gy + 10, "deeper", size=SMALL, color=GREY)
text(ox + 30, gy + 70, "Switch any time - even mid-conversation.", size=BODY, color=GREYD)

# ============================================================================
# BEAT 4 - DIAL THE EFFORT (+ thinking) - still inside the model picker.
# Effort levels Low/Medium/High/Max live in the model menu (Opus & Sonnet only,
# not Haiku); thinking is a SEPARATE switch in the same menu (verified, 2026).
# ============================================================================
ox = OX[4]
head(ox, "Dial the effort", ACCENT[4], sub="in the same model menu")
text(ox + 40, 268, "Tell Claude how hard to work on a task - it's right\nnext to the model name, in the model menu.",
     size=BODY, color=INK)
# effort ladder: Low -> Medium -> High (default) -> Extra -> Max
ey = 420
ex = ox + 40
text(ex, ey + 12, "lighter", size=SMALL, color=GREY)
ex += 124
for lab, isdef in [("Low", False), ("Medium", False), ("High", True), ("Extra", False), ("Max", False)]:
    w, h = chip(ex, ey, lab, fill=(INDIGO_BG if isdef else WHITE),
                text_color=INDIGO, border=INDIGO, size=SMALL, angle=0.0)
    if isdef:
        text(ex + 2, ey + h + 8, "default", size=SMALL, color=INDIGO)
    ex += w
    arrow(ex + 6, ey + h / 2, [[0, 0], [30, 0]], stroke=GREY, sw=3)
    ex += 42
text(ex + 6, ey + 12, "deeper", size=SMALL, color=GREY)
text(ox + 40, ey + 130,
     "More effort = better answers, but slower and more of\nyour usage allowance. Start at High; step up to Extra\nor Max for hard, long-running work.",
     size=BODY, color=GREYD)
chip(ox + 40, ey + 270, "Effort is on Opus & Sonnet (not Haiku)",
     fill=INDIGO_BG, text_color=INDIGO, border=INDIGO, size=SMALL, angle=0.0)
# Extended thinking - a SEPARATE switch in the same menu (not the tools row).
sticky(ox + 30, ey + 350, 1100, 200, BLUE_BG, angle=jit(0.8))
text(ox + 70, ey + 372, "Extended thinking", size=H2, color=BLUE)
text(ox + 70, ey + 430,
     "A separate switch in the same menu. Enable it for\ncomplex tasks - you'll see Claude reason step by step\nbefore it answers.",
     size=BODY, color=INK)
illus_think(ox + 1100 - 120, ey + 440, BLUE)

# ============================================================================
# BEAT 5 - GIVE CLAUDE YOUR FILES  (+ the non-negotiable safety guardrail)
# ============================================================================
ox = OX[5]
head(ox, "Give Claude your files", ACCENT[5])
obj_files(ox + 60, 300, C_FILES, GREEN_BG)
# a green paperclip beside the stack
line(ox + 200, 300, [[0, 0], [0, 36], [22, 36], [22, 8], [10, 8], [10, 28]],
     stroke=C_FILES, sw=4, rough=1, prefix="clip")
text(ox + 300, 300,
     "PDFs, images, spreadsheets, code - Claude\nreads them and answers from the document\nitself. The most underused feature.",
     size=BODY, color=INK)
fx = ox + 300
for lab in ["PDFs", "images", "spreadsheets", "code"]:
    w, h = chip(fx, 470, lab, fill=GREEN_BG, text_color=C_FILES, border=C_FILES, size=SMALL)
    fx += w + 22
# SAFETY guardrail (regulated pharmacy) - required, not decorative.
wy = 640
line(ox + 60, wy + 40, [[0, 0], [22, -40], [44, 0], [0, 0]],
     stroke=RED, sw=3, rough=1, bg=RED_BG, fill="solid", prefix="warn")
text(ox + 76, wy + 6, "!", size=H2, color=RED)
chip(ox + 130, wy, "Never upload confidential data", fill=RED_BG, text_color=RED,
     border=RED, size=H3, angle=0.0)
text(ox + 60, wy + 110,
     "Regulated pharmacy: keep anything with patient or personal\ndetail out. Use non-sensitive material only - policies, rotas,\ntemplates, public docs.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 6 - REACH BEYOND ITS TRAINING DATA  (web search + research)
# ============================================================================
ox = OX[6]
head(ox, "Reach beyond its training", ACCENT[6])

def feat_card(y, h, accent, abg, title, body, illus):
    sticky(ox + 30, y, 1100, h, abg, angle=jit(0.9))
    text(ox + 70, y + 22, title, size=H2, color=accent)
    text(ox + 70, y + 80, body, size=BODY, color=INK)
    illus(ox + 1100 - 130, y + h / 2, accent)

feat_card(300, 220, C_WEB, TEAL_BG, "Web search",
          "Searches the live web and cites its sources -\ncurrent answers, not just its training data.", illus_search)
feat_card(560, 240, C_RES, BLUE_BG, "Research",
          "A deeper, multi-step dig: searches, reads and\ncross-refs many sources, then writes it up.\nRuns in the background.", illus_research)
text(ox + 30, 850, "Find these under the  +  /  Search and tools  in the composer.",
     size=BODY, color=GREYD)
text(ox + 30, 898, "Research needs web search switched on.", size=SMALL, color=GREY)

# ============================================================================
# BEAT 7 - TALK TO IT  (Voice - the sixth featured essential)
# ============================================================================
ox = OX[7]
head(ox, "Talk to it - speak, don't type", ACCENT[7])
sticky(ox + 30, 290, 1100, 300, YELLOW_BG, angle=jit(0.7))
text(ox + 70, 320, "Voice", size=H2, color=C_VOICE)
text(ox + 70, 384,
     "Speak instead of type. Tap the sound-wave icon in\nthe chat window and just talk - Claude listens, then\nanswers. On the web app and mobile (in beta).",
     size=BODY, color=INK)
voice_wave(ox + 1100 - 170, 470, C_VOICE, scale=2.0)
text(ox + 70, 660, "Good for thinking out loud, or when your hands are busy.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 8 - SET IT UP ONCE  (Settings: personalisation, memory, data/privacy).
# First-time setup wins with no video of their own; the data/privacy card also
# reinforces the no-confidential-data rule (regulated pharmacy).
# ============================================================================
ox = OX[8]
head(ox, "Set it up once", ACCENT[8], sub="in Settings")
# 1) Instructions for Claude (personalisation / profile)
sticky(ox + 30, 270, 1100, 200, VIOLET_BG, angle=jit(0.8))
text(ox + 70, 292, "Instructions for Claude", size=H2, color=VIOLET)
text(ox + 70, 352,
     "In Settings, under your profile. Tell Claude your role\nand how you like replies - it applies to every chat, so\nyou don't repeat yourself each time.",
     size=BODY, color=INK)
# profile-card glyph (clearer than a stick person at this size)
pcx, pcy = ox + 1100 - 200, 320
rect(pcx, pcy, 120, 92, stroke=VIOLET, bg=WHITE, sw=2, rough=1, rounded=True)
ellipse(pcx + 16, pcy + 18, 28, 28, stroke=VIOLET, bg=VIOLET_BG, sw=2)
line(pcx + 56, pcy + 24, [[0, 0], [44, 0]], stroke=VIOLET, sw=3, rough=1)
line(pcx + 56, pcy + 42, [[0, 0], [38, 0]], stroke=GREY, sw=2, rough=1)
line(pcx + 16, pcy + 66, [[0, 0], [84, 0]], stroke=GREY, sw=2, rough=1)
# 2) Memory
sticky(ox + 30, 490, 1100, 200, TEAL_BG, angle=jit(0.8))
text(ox + 70, 512, "Memory", size=H2, color=TEAL)
text(ox + 70, 572,
     "Claude can remember useful context across your chats.\nView, edit or delete what it keeps - any time, in Settings.",
     size=BODY, color=INK)
illus_memory(ox + 1100 - 120, 590, TEAL)
# 3) Appearance & language (theme, dyslexic-friendly font, language, notifications)
sticky(ox + 30, 710, 1100, 200, ORANGE_BG, angle=jit(0.8))
text(ox + 70, 732, "Appearance & language", size=H2, color=ORANGE)
text(ox + 70, 792,
     "Light or dark theme, a dyslexic-friendly font, and your\nlanguage - set it comfortable to read. Notifications live\nhere too, for when long tasks finish.",
     size=BODY, color=INK)
illus_appearance(ox + 1100 - 130, 800, ORANGE)
# Data/privacy is org-managed on a Team plan, not a per-user setting - a brief
# mention, not a card. The hard upload rule lives on the File-uploads beat.
text(ox + 40, 940,
     "On our Team plan, your chats aren't used to train Claude - that's contractual, not a setting you manage.",
     size=SMALL, color=GREYD)
text(ox + 40, 974, "Usage limits reset over time; heavier models and effort use them faster.",
     size=SMALL, color=GREY)

# ============================================================================
# BEAT 9 - PAUSE HERE, AND TRY IT
# ============================================================================
ox = OX[9]
head(ox, "Pause here, and try it", ACCENT[9])
pause_icon(ox + 40, 322, 76, color=BLUE)
highlighter(ox + 150, 312, 980, 150, BLUE_BG, angle=0.0)
text(ox + 174, 330, "Open Claude. Switch off your default model,\nturn on web search, and run one prompt.",
     size=H3, color=INK)
ex_x = ox + 60
for lab in ["switch the model", "turn on web search", "notice the difference"]:
    w, h = chip(ex_x, 560, lab, fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
    ex_x += w + 36
text(ox + 60, 700, "60 seconds - then carry on.", size=BODY, color=GREYD)
demo_badge(ox + 60, 820, "show in Claude:  the composer tools + model picker")

# ============================================================================
# BEAT 10 - THAT'S THE CORE. HERE'S THE REST.  (recap + module signpost)
# ============================================================================
ox = OX[10]
head(ox, "That's the core. Here's the rest.", ACCENT[10])
text(ox + 40, 250, "The six you've just met:", size=BODY, color=GREYD)
recap = [("Conversations", C_CONV), ("Model picker", C_MODEL), ("File uploads", C_FILES),
         ("Web search", C_WEB), ("Research", C_RES), ("Voice", C_VOICE)]
ry = 310
rx = ox + 40
for lab, acc in recap:
    w, h = chip(rx, ry, lab, fill=TINT.get(acc, VIOLET_T), text_color=acc, border=acc, size=SMALL)
    rx += w + 20
    if rx > ox + 1000:
        rx = ox + 40
        ry += h + 22
text(ox + 40, ry + 70, "And once, in Settings: your instructions, memory and appearance.",
     size=SMALL, color=GREYD)
# signpost the rest of the module - each has its own video
sy = ry + 170
text(ox + 40, sy, "The rest of this module - each gets its own video:", size=BODY, color=GREYD)
mx, mrow = ox + 40, sy + 56
for lab in ["Projects", "Artifacts", "Skills", "Scheduled tasks", "Connectors (MCP)", "Cowork"]:
    w, h = chip(mx, mrow, lab, fill=WHITE, text_color=GREYD, border=FAINT, size=SMALL)
    mx += w + 20
    if mx > ox + 1040:
        mx = ox + 40
        mrow += h + 20
text(ox + 40, mrow + 60, "...and Claude for PowerPoint, Excel, Word, Chrome & Design.",
     size=SMALL, color=GREY)
# next up
ny = mrow + 140
text(ox + 40, ny, "Next: Projects - the one that compounds for years.", size=H3, color=INK)
circle_around(ox + 40 + text_w("Next: ", H3) - 6, ny - 6, text_w("Projects", H3) + 24,
              H3 * LINE_H + 16, VIOLET, sw=3)
text(ox + 40, ny + 90, "Docs: Claude Help Centre - support.claude.com", size=SMALL, color=VIOLET)

# Beats read as one picture through consistent layout + rhythm - no connector
# spine, no boxes, no branding footer (Style B).

# ----------------------------------------------------------------------------
# WRITE + VALIDATE  (shared excalidraw_kit)
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude_intro.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
