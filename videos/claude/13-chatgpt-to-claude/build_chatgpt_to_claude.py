#!/usr/bin/env python3
"""Build chatgpt-to-claude.excalidraw - ONE flowing, illustrated explainer for the
"Switching from ChatGPT to Claude" training video (Phlo AI Ops Learn, module 2.13).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, no
frames, white canvas, the hand font, lively palette. Composition + a few one-off
illustrations (a labelled set-up stack, a left->right mapping row, a GPT->Project
split) live here.

This is a MIGRATION guide: how to move everything worth keeping out of ChatGPT and
into Claude without rebuilding from scratch. The signature beat is 2 (the
translation map - every ChatGPT feature has a Claude equivalent). The shape is the
house "power then control": the how-to beats sit in the middle, then beat 8 is the
honest "what doesn't move 1:1" list, and beat 9 is the load-bearing safety teaching
- migration is a FILTER, not a bulk copy (don't propagate sensitive history).

Run:  python3 videos/claude/13-chatgpt-to-claude/build_chatgpt_to_claude.py
      python3 preview.py videos/claude/13-chatgpt-to-claude/chatgpt-to-claude.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(131313)

N = 9
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: GREEN,
          6: INDIGO, 7: YELLOW, 8: RED, 9: VIOLET}
OX = {}
_c = 0
for _i in range(1, N + 1):
    OX[_i] = _c
    _c += WID[_i] + GAP
TOTAL_W = _c
HEAD_Y = 60


def beat_head(i, title, sub=None):
    ox = OX[i]
    heading(ox, HEAD_Y, title, color=ACCENT[i], sub=sub)
    return ox


# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS
# ----------------------------------------------------------------------------
def folder(x, y, w=96, h=70, accent=YELLOW, abg=YELLOW_BG):
    rect(x, y + 14, w, h, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="fold")
    rect(x, y, w * 0.5, 22, stroke=INK, bg=abg, sw=2, rough=1, rounded=True, prefix="foldtab")


def file_icon(x, y, w=58, h=74, accent=BLUE, abg=BLUE_BG):
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="fic")
    rect(x, y, w, 14, stroke="transparent", bg=abg, sw=1, rough=1, rounded=True, prefix="fich")
    for k in range(3):
        line(x + 10, y + 30 + k * 14, [[0, 0], [w - 22, 0]], stroke=GREY, sw=2)


def tick(x, y, color=GREEN, s=30):
    line(x, y, [[0, s * 0.5], [s * 0.42, s], [s, 0]], stroke=color, sw=5, rough=1, prefix="tick")


def cross(x, y, color=RED, s=22):
    line(x, y, [[0, 0], [s, s]], stroke=color, sw=4, rough=1, prefix="x1")
    line(x, y, [[0, s], [s, 0]], stroke=color, sw=4, rough=1, prefix="x2")


def map_row(ox, y, left, right, lacc, racc):
    """One translation-table row: a ChatGPT chip -> arrow -> a Claude chip.
    Right chips share a fixed left edge so the arrows line up into a column."""
    chip(ox + 40, y, left, fill=WHITE, text_color=lacc, border=lacc, size=BODY, angle=jit(0.6))
    arrow(ox + 600, y + 26, [[0, 0], [96, 0]], stroke=GREY, sw=3, rough=1)
    chip(ox + 712, y, right, fill=TINT.get(racc, VIOLET_T), text_color=INK, border=racc,
         size=BODY, angle=jit(0.6))


def card(x, y, w, h, accent, abg, title, lines, ts=H3):
    """A soft accent card with a heading and a few body lines."""
    rect(x, y, w, h, stroke=accent, bg=abg, sw=2, rough=1, rounded=True,
         fill="solid", opacity=40, angle=jit(0.7))
    text(x + 28, y + 22, title, size=ts, color=accent)
    for k, ln in enumerate(lines):
        text(x + 28, y + 22 + ts * LINE_H + 14 + k * (BODY * LINE_H + 8), ln, size=BODY, color=INK)


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "ChatGPT  ->  Claude", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "switching over without starting over", size=H2, color=VIOLET)

# ============================================================================
# BEAT 1 - HOOK: switching, not starting over
# ============================================================================
ox = beat_head(1, "You're switching, not starting over",
               "Almost everything you set up in ChatGPT has a\nhome in Claude. You move it across - you don't rebuild it.")
# left: a labelled "your ChatGPT set-up" stack
sx, sy = ox + 40, 380
sticky(sx, sy, 380, 300, GREY, angle=jit(1.2))
text(sx + 30, sy + 24, "your ChatGPT set-up", size=BODY, color=WHITE)
for k, item in enumerate(["instructions", "memory", "custom GPTs", "saved chats"]):
    text(sx + 40, sy + 84 + k * 50, "- " + item, size=BODY, color=WHITE)
arrow(sx + 410, sy + 150, [[0, 0], [120, 0]], stroke=ORANGE, sw=6, rough=1)
claude_face(sx + 640, sy + 150, r=58, color=ORANGE)
text_centered(sx + 640, sy + 230, "it all has a place here", size=SMALL, color=ORANGE)
text(ox + 40, sy + 360, "a couple of hours, mostly copy-and-paste - no technical work", size=BODY, color=GREYD)

# ============================================================================
# BEAT 2 - THE TRANSLATION MAP  (signature)
# ============================================================================
ox = beat_head(2, "Same ideas, new names",
               "Every ChatGPT feature has a Claude equivalent.\nLearn the words and the move is mostly mechanical.")
text(ox + 60, 300, "in ChatGPT", size=SMALL, color=GREY)
text(ox + 760, 300, "in Claude", size=SMALL, color=VIOLET)
rows = [
    ("Custom instructions", "Profile preferences", GREYD, BLUE),
    ("Memory", "Memory (built-in)", GREYD, TEAL),
    ("Projects (folders)", "Projects", GREYD, VIOLET),
    ("Custom GPTs", "Projects + Skills", GREYD, INDIGO),
    ("Plugins / Actions", "Connectors (MCP)", GREYD, ORANGE),
    ("Tasks", "Scheduled tasks", GREYD, GREEN),
]
for k, (l, r, la, ra) in enumerate(rows):
    map_row(ox, 348 + k * 86, l, r, la, ra)
text(ox + 40, 348 + len(rows) * 86 + 16,
     "the full table is in the migration playbook - this is the shape of it", size=SMALL, color=GREYD)

# ============================================================================
# BEAT 3 - INVENTORY: gather what you've got
# ============================================================================
ox = beat_head(3, "First, gather what you've got",
               "Before you move anything, list what's actually worth\nkeeping. Most of a clean switch is this step.")
items = [
    ("Custom instructions", "your global 'how to answer me' text", BLUE, BLUE_BG),
    ("Saved memory", "the facts ChatGPT has learned about you", TEAL, TEAL_BG),
    ("Custom GPTs", "each one's name, instructions and files", INDIGO, INDIGO_BG),
    ("Projects / folders", "grouped chats with shared files", VIOLET, VIOLET_BG),
    ("The chats you reuse", "the handful you actually go back to", ORANGE, ORANGE_BG),
]
iy = 340
for k, (t, cap, acc, abg) in enumerate(items):
    yy = iy + k * 104
    sticky(ox + 40, yy, 1080, 88, abg, angle=jit(0.8))
    ellipse(ox + 66, yy + 26, 36, 36, stroke=acc, bg=WHITE, sw=3)
    text_centered(ox + 84, yy + 30, str(k + 1), size=H3, color=acc)
    text(ox + 130, yy + 16, t, size=H3, color=acc)
    text(ox + 520, yy + 24, cap, size=BODY, color=INK)

# ============================================================================
# BEAT 4 - EXPORT YOUR CHATGPT DATA
# ============================================================================
ox = beat_head(4, "Export your ChatGPT data",
               "One official button. It arrives by email as a zip -\nyour chats as a data file plus a readable web page.")
# the click-path as chips
px = ox + 50
for k, step in enumerate(["Settings", "Data Controls", "Export data"]):
    w, h = chip(px, 330, step, fill=WHITE, text_color=BLUE, border=BLUE, size=BODY)
    if k < 2:
        arrow(px + w + 6, 330 + h / 2, [[0, 0], [40, 0]], stroke=BLUE, sw=3)
    px += w + 56
text(ox + 50, 410, "you get an email link - the zip has conversations.json + a chat.html you can read", size=BODY, color=GREYD)
# the important caveat - what it does NOT include
ny = 480
rect(ox + 40, ny, 1080, 250, stroke=RED, bg=RED_BG, sw=2, rough=1, rounded=True,
     fill="solid", opacity=30, angle=jit(-0.6))
text(ox + 76, ny + 22, "What the export does NOT include", size=H3, color=RED)
for k, ln in enumerate(["your Memory (the saved facts) - those live in a separate place",
                        "each Custom GPT's instructions and knowledge files",
                        "so copy those two by hand - the next two beats show how"]):
    cross(ox + 84, ny + 84 + k * 50, color=RED, s=20)
    text(ox + 124, ny + 80 + k * 50, ln, size=BODY, color=INK)

# ============================================================================
# BEAT 5 - INSTRUCTIONS + MEMORY ACROSS
# ============================================================================
ox = beat_head(5, "Bring your instructions and memory across",
               "Two quick wins that make Claude feel like home\nfrom the first message.")
card(ox + 40, 330, 520, 300, BLUE, BLUE_BG, "Custom instructions",
     ["Copy your ChatGPT custom", "instructions into Claude's", "Profile preferences", "(Settings -> your profile).",
      "Always on, every new chat."])
card(ox + 600, 330, 520, 300, TEAL, TEAL_BG, "Memory",
     ["Ask ChatGPT: 'summarise", "everything you know about me.'", "Paste that into Claude.",
      "Claude's own Memory then", "builds as you work - on by default."])
demo_badge(ox + 40, 660, "show in Claude:  pasting preferences, then the memory summary")

# ============================================================================
# BEAT 6 - CUSTOM GPTs BECOME PROJECTS
# ============================================================================
ox = beat_head(6, "Custom GPTs become Projects",
               "One Project per GPT. Its three parts map straight\nacross - nothing is lost in translation.")
# left: a GPT card
gx, gy = ox + 60, 360
rect(gx, gy, 360, 320, stroke=GREYD, bg=FAINT, sw=2, rough=1, rounded=True, angle=jit(-0.8))
text(gx + 28, gy + 22, "a Custom GPT", size=H3, color=GREYD)
for k, part in enumerate(["name", "instructions", "knowledge files"]):
    text(gx + 40, gy + 96 + k * 56, "- " + part, size=BODY, color=INK)
arrow(gx + 380, gy + 160, [[0, 0], [130, 0]], stroke=INDIGO, sw=6, rough=1)
# right: a Project taking the three parts
px2 = gx + 560
rows6 = [("name", "-> Project name", INDIGO),
         ("instructions", "-> project instructions", VIOLET),
         ("knowledge files", "-> project knowledge", BLUE)]
for k, (a, b, acc) in enumerate(rows6):
    yy = gy + 30 + k * 96
    sticky(px2, yy, 470, 78, TINT.get(acc, VIOLET_T), angle=jit(0.8))
    text(px2 + 24, yy + 22, b, size=H3, color=acc)
text(ox + 60, gy + 360, "repeatable 'how it should behave' becomes a Skill - that's the next beat", size=BODY, color=GREYD)

# ============================================================================
# BEAT 7 - PROMPTS -> SKILLS, TOOLS -> CONNECTORS
# ============================================================================
ox = beat_head(7, "Repeat prompts -> Skills. Tools -> Connectors.",
               "The two things people forget to move: the prompts you\nkept re-pasting, and the apps you had wired up.")
card(ox + 40, 340, 520, 300, YELLOW, YELLOW_BG, "Saved / repeat prompts",
     ["The prompt you paste every", "week becomes a Skill -", "write it once, Claude reaches",
      "for it when it fits."])
card(ox + 600, 340, 520, 300, ORANGE, ORANGE_BG, "Plugins / GPT Actions",
     ["The tools a GPT could call", "reconnect as Connectors", "(MCP) - calendar, email,",
      "drive, chat and more."])

# ============================================================================
# BEAT 8 - WHAT DOESN'T MOVE 1:1  (honest gaps)
# ============================================================================
ox = beat_head(8, "What doesn't move 1-to-1",
               "A short, honest list - and where to go instead.\nMost things map; a few genuinely differ.")
gaps = [
    ("Native image generation", "Claude doesn't make images. Use a", "dedicated image tool; Claude Design", "for on-brand UI and deck visuals.", RED, RED_BG),
    ("Real-time voice", "Claude has voice in the mobile app,", "but it's lighter than ChatGPT's", "real-time voice mode.", ORANGE, ORANGE_BG),
    ("The GPT Store", "No like-for-like marketplace. The", "extensibility story is the Skills", "Directory + Connectors + partner Skills.", INDIGO, INDIGO_BG),
]
for k, (t, l1, l2, l3, acc, abg) in enumerate(gaps):
    yy = 320 + k * 190
    rect(ox + 40, yy, 1080, 170, stroke=acc, bg=abg, sw=2, rough=1, rounded=True,
         fill="solid", opacity=32, angle=jit(0.5))
    text(ox + 76, yy + 22, t, size=H3, color=acc)
    text(ox + 76, yy + 72, l1 + "\n" + l2 + "\n" + l3, size=BODY, color=INK)

# ============================================================================
# BEAT 9 - SAFETY + CLOSE: move smart, not everything
# ============================================================================
ox = beat_head(9, "Move smart, not everything",
               "A switch is a filter, not a bulk copy. This is the\none part you can't skip.")
# the safety teaching - red caution card
rect(ox + 40, 320, 1080, 250, stroke=RED, bg=RED_BG, sw=3, rough=1, rounded=True,
     fill="solid", opacity=30, angle=jit(-0.5))
diamond(ox + 80, 268, 56, 56, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 108, 280, "!", size=H2, color=RED)
text(ox + 80, 340, "Review and leave behind", size=H3, color=RED)
for k, ln in enumerate(["don't bulk-load old chats into a Project - you'd carry old mistakes with them",
                        "nothing confidential or patient-identifiable goes into projects, skills or exports",
                        "keep examples generic - the method travels, the sensitive data does not"]):
    text(ox + 80, 400 + k * 50, "- " + ln, size=BODY, color=INK, width=1000)
# the try-it close
sticky(ox + 40, 612, 700, 150, VIOLET_BG, angle=jit(1.0))
text(ox + 76, 638, "This week", size=H3, color=VIOLET)
text(ox + 76, 696, "move ONE Custom GPT into a Project,\nand paste your instructions into preferences", size=BODY, color=INK)
arrow(ox + 760, 686, [[0, 0], [70, 0]], stroke=VIOLET, sw=4)
claude_face(ox + 900, 686, r=48, color=VIOLET)
text(ox + 60, 800, "Docs: Claude - Intro to Projects, Understanding Claude's personalization features",
     size=SMALL, color=VIOLET)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatgpt-to-claude.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
