#!/usr/bin/env python3
"""Build claude-word.excalidraw - ONE flowing, illustrated explainer for the
"Claude + Word" training video (Phlo AI Ops Learn, module 2.9).

House Style B (see excalidraw_kit): one hand-drawn left-to-right journey, no
frames, white canvas, the hand font, lively palette. This file holds only the
composition + a one-off document illustration.

Sibling to PowerPoint (2.7, decks) and Excel (2.8, formulas). To keep the trio
distinct, THIS one's angle is long-form prose: edits that land as TRACKED changes
on a selection (surrounding styles preserved), document Q&A with clickable
citations, and THEMATIC search (every passage on a theme, not keyword hits). Two
real capabilities: (1) "Create and edit files with Claude" - the chat builds a
genuine .docx, all plans; (2) "Claude for Word" - the add-in (Pro+).

Run:  python3 videos/claude/9-claude-word/build_word.py
      python3 preview.py videos/claude/9-claude-word/claude-word.excalidraw out.png
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(90910)

N = 9
GAP = 800
WID = {i: 1200 for i in range(1, N + 1)}
ACCENT = {1: BLUE, 2: VIOLET, 3: ORANGE, 4: GREEN, 5: TEAL,
          6: INDIGO, 7: YELLOW, 8: INDIGO, 9: BLUE}
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
def doc_page(x, y, w, h, accent=BLUE, abg=BLUE_BG, lines=7, tracked=False, cite=None):
    """A document page: title bar + paragraph lines. tracked=True adds a struck
    deletion + a coloured insertion + a margin change-bar. cite=row highlights a
    line as a citation target."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="doc")
    rect(x + 0.10 * w, y + 0.08 * h, 0.5 * w, 0.045 * h, stroke="transparent",
         bg=accent, sw=1, rough=1, rounded=True, prefix="dttl")
    for k in range(lines):
        ly = y + 0.22 * h + k * (0.62 * h / lines)
        ln_w = (0.78 if k % 3 else 0.58) * w
        line(x + 0.10 * w, ly, [[0, 0], [ln_w, 0]], stroke=GREY, sw=2)
    if cite is not None:
        ly = y + 0.22 * h + cite * (0.62 * h / lines)
        rect(x + 0.08 * w, ly - 8, 0.84 * w, 18, stroke="transparent", bg=abg,
             sw=1, rough=1, rounded=True, fill="solid", opacity=70, prefix="dcite")
    if tracked:
        ly = y + 0.22 * h + 2 * (0.62 * h / lines)
        line(x + 0.10 * w, ly, [[0, 0], [0.38 * w, 0]], stroke=RED, sw=3)        # deletion
        line(x + 0.50 * w, ly, [[0, 0], [0.26 * w, 0]], stroke=GREEN, sw=3)       # insertion
        rect(x + 0.93 * w, y + 0.2 * h, 0.03 * w, 0.3 * h, stroke=accent, bg=abg,
             sw=1, rough=1, rounded=True, prefix="dmar")


def tiny_doc(x, y):
    doc_page(x, y, 150, 180, accent=BLUE, abg=BLUE_BG, lines=7, tracked=True)


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -300, "Claude + Word", size=HERO, color=INK)
text(OX[1] + 6, -300 + HERO * LINE_H + 4,
     "an editor that works in the document, not around it", size=H2, color=BLUE)

# ============================================================================
# BEAT 1 - HOOK
# ============================================================================
ox = beat_head(1, "It edits like an editor",
               "no copy-paste shuttle - Claude's changes land\nas tracked edits, right in the document")
by = 360
bw, bh = 520, 130
sticky(ox + 40, by, bw, bh, GREY, angle=jit(1.5))
text(ox + 72, by + 34, "tighten this paragraph,\nkeep the meaning", size=BODY, color=WHITE)
line(ox + 90, by + bh, [[0, 0], [-18, 30], [22, -2]], stroke=GREY, sw=3)
arrow(ox + 40 + bw + 30, by + bh / 2, [[0, 0], [150, 0]], stroke=BLUE, sw=5, rough=1)
dx = ox + 40 + bw + 230
ellipse(dx - 40, by - 40, 300, 280, stroke=BLUE, bg=BLUE_BG, sw=2, rough=1, fill="solid", opacity=45)
doc_page(dx, by - 20, 220, 240, accent=BLUE, abg=BLUE_BG, lines=7, tracked=True)
text(dx - 10, by + 234, "accept or reject each change\n- you're always in control", size=SMALL, color=BLUE)

# ============================================================================
# BEAT 2 - A REAL DOCUMENT
# ============================================================================
ox = beat_head(2, "A real document, not a transcript",
               "Ask in the chat and Claude builds a genuine .docx -\n"
               "headings, lists and styles, ready to download.")
cw_x, cw_y, cw_w, cw_h = ox + 40, 330, 1080, 560
claude_window(cw_x, cw_y, cw_w, cw_h, tiny=tiny_doc)
text(cw_x, cw_y + cw_h + 24, "you ask in the chat", size=SMALL, color=GREY)
arrow(cw_x + cw_w * 0.74, cw_y + cw_h + 56, [[0, 0], [70, -60]], stroke=VIOLET, sw=3, rough=1)
text(cw_x + cw_w * 0.55, cw_y + cw_h + 60,
     "opens in Word or Google Docs -\nproperly formatted, not a wall of text", size=SMALL, color=VIOLET)
chx = cw_x
for lab in ["every plan", "web, desktop & mobile"]:
    w, _ = chip(chx, cw_y + cw_h + 110, lab, fill=WHITE, text_color=VIOLET, border=VIOLET, size=SMALL)
    chx += w + 30

# ============================================================================
# BEAT 3 - ASK THE DOCUMENT QUESTIONS
# ============================================================================
ox = beat_head(3, "Ask the document questions",
               "Answers cite the exact passage - and a click\njumps you straight to it.")
doc_page(ox + 60, 330, 300, 380, accent=ORANGE, abg=ORANGE_BG, lines=9, cite=4)
arrow(ox + 380, 520, [[0, 0], [110, 0]], stroke=ORANGE, sw=4)
sticky(ox + 510, 420, 540, 200, ORANGE_BG, angle=jit(1.2))
text(ox + 540, 446, "“clause 4 commits us to a\n30-day notice period - see\nthe highlighted passage”", size=BODY, color=INK)
text(ox + 540, 580, "click the citation -> it scrolls there", size=SMALL, color=ORANGE)
# thematic search note
chip(ox + 60, 740, "find every passage about data retention - meaning, not keyword",
     fill=WHITE, text_color=ORANGE, border=ORANGE, size=SMALL)

# ============================================================================
# BEAT 4 - IT EDITS ONLY WHAT YOU SELECT  (signature)
# ============================================================================
ox = beat_head(4, "It edits only what you select",
               "Highlight a passage, say what to change. Claude touches\n"
               "that and nothing else - styles and numbering survive.")
doc_page(ox + 60, 340, 320, 300, accent=GREEN, abg=GREEN_BG, lines=8, cite=3)
text(ox + 70, 656, "you select one passage...", size=SMALL, color=GREEN)
arrow(ox + 400, 480, [[0, 0], [110, 0]], stroke=GREEN, sw=4)
doc_page(ox + 530, 340, 320, 300, accent=GREEN, abg=GREEN_BG, lines=8, tracked=True)
text(ox + 540, 656, "...only that passage changes,\nas a tracked revision", size=SMALL, color=GREEN)
for k, lab in enumerate(["it preserves surrounding styles & numbering",
                         "suggested-edits mode -> changes land as tracked revisions"]):
    chip(ox + 60, 720 + k * 84, lab, fill=WHITE, text_color=GREEN, border=GREEN, size=SMALL)

# ============================================================================
# BEAT 5 - TWO PLACES IT WORKS
# ============================================================================
ox = beat_head(5, "Make one, or mark up your own",
               "Build a fresh .docx in the chat - or open the\nadd-in on a document you already have.")
# top: build a fresh .docx from the chat
sticky(ox + 40, 330, 1040, 200, TEAL_BG, angle=jit(-0.7))
text(ox + 76, 354, "From the chat", size=H3, color=TEAL)
text(ox + 76, 414, "describe it, and Claude builds a whole .docx from scratch", size=BODY, color=INK)
doc_page(ox + 830, 346, 150, 168, accent=TEAL, abg=TEAL_BG, lines=6)
# bottom: the add-in marks up the document you've got open
sticky(ox + 40, 560, 1040, 250, INDIGO_BG, angle=jit(0.7))
text(ox + 76, 584, "Inside Word", size=H3, color=INDIGO)
text(ox + 76, 644, "open the add-in on a document you've got open -\nits edits land as tracked changes", size=BODY, color=INK)
text(ox + 76, 752, "Pro and up · Add-ins menu", size=SMALL, color=GREYD)
doc_page(ox + 740, 576, 210, 220, accent=INDIGO, abg=INDIGO_BG, lines=7, tracked=True)
rect(ox + 960, 576, 70, 220, stroke=INDIGO, bg=INDIGO_BG, sw=2, rough=1, rounded=True, fill="solid", opacity=55)
text(ox + 966, 586, "Claude", size=SMALL, color=INDIGO)

# ============================================================================
# BEAT 6 - STEER IT
# ============================================================================
ox = beat_head(6, "Ask, and read the changes back",
               "You ask in plain English; the edits come back\ntracked, so you read them before they stick.")
asks = ["cut this by a third, keep the headings",
        "make the tone more formal",
        "find every mention of liability",
        "turn these notes into a one-page brief"]
for k, a in enumerate(asks):
    chip(ox + 60, 350 + k * 92, a, fill=WHITE, text_color=INDIGO, border=INDIGO, size=SMALL)
arrow(ox + 620, 470, [[0, 0], [70, 0]], stroke=INDIGO, sw=4)
doc_page(ox + 710, 340, 330, 360, accent=INDIGO, abg=INDIGO_BG, lines=9, tracked=True)
text(ox + 710, 716, "each change is a tracked revision - accept or reject it", size=SMALL, color=INDIGO)
demo_badge(ox + 60, 730, "show in Word:  select a paragraph, ask Claude to tighten it")

# ============================================================================
# BEAT 7 - WHERE IT EARNS ITS KEEP  (a vertical 'reach for it when' list)
# ============================================================================
ox = beat_head(7, "Reach for it when...")
jobs = [("A first draft", "a policy, brief or report to react to", BLUE, BLUE_BG),
        ("Tightening a long doc", "cut the waffle, keep the structure", GREEN, GREEN_BG),
        ("Reviewing for a theme", "every clause that touches one topic", ORANGE, ORANGE_BG),
        ("Filling a template", "in your house style and headings", VIOLET, VIOLET_BG)]
for k, (head, cap, acc, abg) in enumerate(jobs):
    yy = 340 + k * 124
    doc_page(ox + 60, yy, 74, 96, accent=acc, abg=abg, lines=4)
    text(ox + 178, yy + 14, head, size=H3, color=acc)
    text(ox + 178, yy + 64, cap, size=BODY, color=INK)

# ============================================================================
# BEAT 8 - SAFETY  (a tracked doc with Accept / Reject, not a caution box)
# ============================================================================
ox = beat_head(8, "Read every change before you accept")
doc_page(ox + 60, 330, 360, 360, accent=INDIGO, abg=INDIGO_BG, lines=9, tracked=True)
rect(ox + 60, 716, 170, 58, stroke=GREEN, bg=GREEN_BG, sw=2, rough=1, rounded=True)
tick(ox + 84, 732, color=GREEN, s=22)
text(ox + 120, 730, "Accept", size=BODY, color=GREEN)
rect(ox + 250, 716, 170, 58, stroke=RED, bg=RED_BG, sw=2, rough=1, rounded=True)
xmark(ox + 276, 732, color=RED, s=20)
text(ox + 312, 730, "Reject", size=BODY, color=RED)
nx = ox + 560
rect(nx, 330, 520, 160, stroke=INDIGO, bg=INDIGO_T, sw=2, rough=1, rounded=True)
text(nx + 32, 354, "Go change by change", size=H3, color=INDIGO)
text(nx + 32, 412, "read each tracked edit - don't bulk-accept,\nespecially legal, client-facing or regulated", size=BODY, color=INK)
rect(nx, 530, 520, 160, stroke=GREYD, bg=FAINT, sw=2, rough=1, rounded=True)
text(nx + 32, 554, "Trust the source", size=H3, color=GREYD)
text(nx + 32, 612, "don't open documents you don't trust - a\nbooby-trapped doc can hijack the request", size=BODY, color=INK)

# ============================================================================
# BEAT 9 - TRY / CLOSE  (a long doc shrinking to a shorter one)
# ============================================================================
ox = beat_head(9, "Take a long doc, ask for a third less")
doc_page(ox + 60, 340, 300, 380, accent=BLUE, abg=BLUE_BG, lines=12)
arrow(ox + 390, 530, [[0, 0], [110, 0]], stroke=BLUE, sw=4)
doc_page(ox + 530, 380, 240, 300, accent=BLUE, abg=BLUE_BG, lines=7)
text(ox + 540, 696, "shorter, and tracked", size=SMALL, color=BLUE)
ex_x = ox + 60
for lab in ["a process note", "a long email", "a draft policy"]:
    w, h = chip(ex_x, 756, lab, fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
    ex_x += w + 32
text(ox + 60, 820, "read the tracked changes, then accept the ones you like", size=BODY, color=GREYD)
text(ox + 40, 868, "Claude works in the document - you keep the final word on the words.",
     size=H3, color=INK)
text(ox + 60, 940, "Docs: Claude - Create and edit files, and Use Claude for Word", size=SMALL, color=VIOLET)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-word.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
