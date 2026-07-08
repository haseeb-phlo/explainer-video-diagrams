#!/usr/bin/env python3
"""Build scheduled_tasks.excalidraw - ONE flowing, illustrated explainer for
the "Claude Scheduled Tasks" training video (Phlo AI training, module 2.5, Cowork).

Design: a single hand-drawn journey that reads left-to-right - NO frames, NO
boxes, white canvas, everything in the hand font, roughness 1. A lively
Excalidraw palette, colour-coded per beat, with colour blocking, scribbled
annotations and charming primitive illustrations. Modelled on the canonical
videos/claude/3-artefacts build (the Style-B house style).

The eleven beats carry the full content of the original eleven-frame brief
(title, what-it-is, prerequisites, how-it-runs, the awake-and-open caveat, two
ways to create, the form, managing tasks, Phlo use cases, safe use, recap) -
the information is unchanged; only the corporate-deck styling is dropped in
favour of the project's current Style B.

Run:  python3 build_scheduled_tasks.py   # writes the file, reloads it, asserts, prints counts
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(50250)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD  (copied from the canonical 3-artefacts build)
# ----------------------------------------------------------------------------
GAP = 800  # wide gaps so one beat frames cleanly on a 14" laptop while panning
# every beat uses the SAME slot, shaped like the reference's "Words left, a thing
# right" beat (~1120 wide x ~980 tall content, ~1.15 : 1) so framing is identical
# and fits a 14" MacBook screen. Content fills the slot; never spreads wider/taller.
WID = dict.fromkeys(range(1, 12), 1200)
ACCENT = {1: VIOLET, 2: ORANGE, 3: BLUE, 4: GREEN, 5: RED, 6: TEAL,
          7: INDIGO, 8: VIOLET, 9: YELLOW, 10: GREEN, 11: ORANGE}
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

# ----------------------------------------------------------------------------
# LOCAL ONE-OFF ILLUSTRATIONS  (bespoke to this video, kept out of the kit)
# ----------------------------------------------------------------------------
def node(x, y, label, accent, abg, w=760, h=66, text_color=INK):
    rect(x, y, w, h, stroke=accent, bg=abg, sw=2, rough=1, rounded=True, prefix="node")
    text_centered(x + w / 2, y + h / 2 - BODY * 0.6, label, size=BODY, color=text_color)

# ============================================================================
# BEAT 1 - TITLE
# ============================================================================
ox = OX[1]
clock(ox + 120, 360, 78, VIOLET)
text(ox + 250, 300, "Scheduled Tasks", size=HERO, color=VIOLET)
text(ox + 256, 300 + HERO * LINE_H + 6, "putting your repeat work on autopilot", size=H2, color=GREYD)
text(ox + 256, 300 + HERO * LINE_H + 70, "A team guide - Cowork on Claude Desktop", size=BODY, color=GREY)

# ============================================================================
# BEAT 2 - WHAT IT IS
# ============================================================================
ox = beat_head(2, "What is a scheduled task?")
text(ox + 40, 300, "You describe a job once. Claude runs it for you\n"
                   "on a schedule, and delivers the finished result.", size=H2, color=INK)
# before / after
bx, by, bw, bh = ox + 40, 470, 480, 380
sticky(bx, by, bw, bh, ORANGE_T, angle=jit(1.4))
text(bx + 36, by + 26, "Before", size=H3, color=GREYD)
for k, item in enumerate(["open Claude", "re-type the prompt", "wait",
                          "copy the result", "every single time"]):
    text(bx + 52, by + 96 + k * 48, "- " + item, size=BODY, color=INK)
arrow(bx + bw + 24, by + bh / 2, [[0, 0], [96, 0]], stroke=ORANGE, sw=5, rough=1)
ax, aw = bx + bw + 148, 440
sticky(ax, by, aw, bh, ORANGE, angle=jit(-1.2))
text(ax + 36, by + 26, "After", size=H3, color=WHITE)
for k, item in enumerate(["set it once", "it runs on its own",
                          "the result is\nwaiting for you"]):
    text(ax + 52, by + 96 + k * 64, "- " + item, size=BODY, color=WHITE)

# ============================================================================
# BEAT 3 - PREREQUISITES
# ============================================================================
ox = beat_head(3, "What you need first")
prereqs = [
    "The Claude Desktop app (not the browser)",
    "A paid plan: Pro, Max, Team or Enterprise",
    "Cowork enabled (your admin controls this on Team / Enterprise)",
    "Your work tools connected: Slack, Outlook, Atlassian,\nBeacon, Xero and so on",
]
py = 320
for s in prereqs:
    check_item(ox + 50, py, s, color=INK, accent=BLUE)
    py += 90 + (40 if "\n" in s else 0)
text(ox + 50, py + 10, "Scheduled tasks live inside Cowork, in the Desktop app only.",
     size=SMALL, color=GREY)

# ============================================================================
# BEAT 4 - HOW IT RUNS
# ============================================================================
ox = beat_head(4, "How a task actually runs")
steps = ["You write the prompt once", "You pick a cadence",
         "Claude opens its own session", "It uses your connectors, skills and plugins",
         "It delivers the output for you to review"]
nx, nw = ox + 60, 760
ny = 300
for k, s in enumerate(steps):
    node(nx, ny, s, GREEN, GREEN_T)
    if k < len(steps) - 1:
        arrow(nx + nw / 2, ny + 66, [[0, 0], [0, 40]], stroke=GREEN, sw=4)
    if k == 2:  # caption beside the middle node
        text(nx + nw + 40, ny + 6, "Each run is its own\nfresh Cowork session.", size=SMALL, color=GREY)
    ny += 110

# ============================================================================
# BEAT 5 - THE BIG CAVEAT  (red caution, the load-bearing safety point)
# ============================================================================
ox = beat_head(5, "The one rule everyone forgets")
diamond(ox + 40, 290, 60, 60, stroke=RED, bg=RED_BG, sw=3)
text_centered(ox + 70, 302, "!", size=H2, color=RED)
highlighter(ox + 120, 296, 980, 150, RED_BG, angle=0.0)
text(ox + 140, 312, "A task only runs while your computer is awake\n"
                    "AND the Desktop app is open.", size=H2, color=INK)
# timeline: closed -> skipped -> auto re-run
ty = 560
states = [("Laptop closed\nat run time", RED, RED_T),
          ("Task is skipped", RED, RED_T),
          ("It runs automatically when\nyou next open the app", GREEN, GREEN_T)]
tx = ox + 40
widths = [300, 280, 400]
for k, ((lab, acc, abg), w) in enumerate(zip(states, widths, strict=True)):
    node(tx, ty, lab, acc, abg, w=w, h=120)
    if k < len(states) - 1:
        arrow(tx + w + 6, ty + 60, [[0, 0], [24, 0]], stroke=GREYD, sw=4)
    tx += w + 36
text(ox + 40, ty + 170, "You get a notification on the re-run. Skipped runs show in the task history.",
     size=SMALL, color=GREY)

# ============================================================================
# BEAT 6 - TWO WAYS TO CREATE
# ============================================================================
ox = beat_head(6, "Two ways to create one")
cw, chh = 1080, 250
# A - from a chat
sticky(ox + 40, 300, cw, chh, TEAL_T, angle=jit(1.2))
text(ox + 76, 326, "A.  From a chat", size=H3, color=TEAL)
text(ox + 92, 396, "start or open a task  ->  type /schedule  ->\n"
                   "answer Claude's questions  ->  click Schedule", size=BODY, color=INK)
# B - from the Scheduled page
sticky(ox + 40, 300 + chh + 44, cw, chh, TEAL_BG, angle=jit(-1.1))
text(ox + 76, 326 + chh + 44, "B.  From the Scheduled page", size=H3, color=TEAL)
text(ox + 92, 396 + chh + 44, "click Scheduled in the sidebar  ->  click + New task  ->\n"
                              "fill the form  ->  Save", size=BODY, color=INK)
text(ox + 40, 300 + 2 * chh + 110, "Same result. Use whichever you prefer.", size=SMALL, color=GREY)
demo_badge(ox + 40, 300 + 2 * chh + 150, "show in Claude desktop app:  type /schedule in a chat")

# ============================================================================
# BEAT 7 - THE FORM, ANNOTATED
# ============================================================================
ox = beat_head(7, "What the form asks for")
mx, my, mw = ox + 40, 300, 980
fields = [
    ("Task name", "short and memorable"),
    ("Description", "what it does, in one line"),
    ("Prompt", "the instructions; type / to add plugins or skills"),
    ("Frequency", "hourly, daily, weekly, weekdays, or manual"),
    ("Model", "optional"),
    ("Folder", "optional, where Claude works"),
]
mh = 70 + len(fields) * 80 + 24
rect(mx, my, mw, mh, stroke=INDIGO, bg=INDIGO_T, sw=2, rough=1, rounded=True, prefix="modal")
text(mx + 30, my + 22, "Create task", size=H3, color=INDIGO)
ry = my + 88
for label, hint in fields:
    rect(mx + 26, ry, mw - 52, 60, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True, prefix="pill")
    text(mx + 52, ry + 16, label, size=LABEL, color=INK)
    text(mx + 350, ry + 18, hint, size=SMALL, color=GREY)
    ry += 80

# ============================================================================
# BEAT 8 - MANAGING TASKS
# ============================================================================
ox = beat_head(8, "Staying in control")
ctrls = ["Run now", "Pause", "Resume", "Edit", "View history", "Delete"]
bx0, by0, bw0, bh0 = ox + 50, 320, 300, 66
for k, lab in enumerate(ctrls):
    cxk = bx0 + (k % 3) * (bw0 + 40)
    cyk = by0 + (k // 3) * (bh0 + 36)
    button(cxk, cyk, lab, VIOLET, w=bw0, h=bh0)
text(ox + 50, by0 + 2 * (bh0 + 36) + 24,
     "Find all of this under Scheduled in the left sidebar, with upcoming and past runs.",
     size=SMALL, color=GREY)

# ============================================================================
# BEAT 9 - EVERYDAY USE CASES  (single-column rows)
# ============================================================================
ox = beat_head(9, "Everyday use cases")
cases = [
    ("Support and Ops", "8am weekday briefing of overnight Slack and flagged Outlook emails, urgent first."),
    ("Delivery & logistics", "Weekly summary of operational status pulled from Jira or Asana."),
    ("Data & analytics", "Weekly Beacon metrics digest, drafted for you to check before sharing."),
    ("Finance", "Start-of-month Xero snapshot of spend and outstanding items."),
    ("Marketing", "Weekly tracker of competitor moves and sector news."),
    ("Everyone", "Friday tidy-up of a shared project folder."),
]
cardw, cardh = 1100, 110
gx, gy = ox + 40, 300
for k, (head, body) in enumerate(cases):
    cyk = gy + k * (cardh + 12)
    sticky(gx, cyk, cardw, cardh, YELLOW_T, angle=jit(1.0))
    text(gx + 34, cyk + 20, head, size=H3, color=VIOLET)
    text(gx + 34, cyk + 72, body, size=BODY, color=GREYD)

# ============================================================================
# BEAT 10 - SAFE AND SENSIBLE
# ============================================================================
ox = beat_head(10, "Doing this safely")
safes = [
    "Keep confidential data out of prompts unless you are\nin an approved, sanctioned workspace",
    "Always review the output before you act on it or send it on",
    "Name tasks clearly so the team knows what is running",
    "Pause or delete tasks you no longer need",
]
py = 320
for s in safes:
    check_item(ox + 50, py, s, color=INK, accent=GREEN)
    py += 84 + (40 if "\n" in s else 0)
text(ox + 50, py + 10, "If in doubt, ask before you automate.", size=SMALL, color=GREY)

# ============================================================================
# BEAT 11 - RECAP AND NEXT STEP
# ============================================================================
ox = beat_head(11, "Your first task this week")
recap = [
    "Scheduled tasks = set it once, Claude runs it",
    "Desktop app open and awake, or it waits",
    "Start small and review the result",
]
py = 320
for s in recap:
    check_item(ox + 50, py, s, color=INK, accent=ORANGE)
    py += 80
# call-to-action band
band_y = 640
rect(ox + 40, band_y, WID[11] - 80, 110, stroke=ORANGE, bg=ORANGE, sw=2, rough=1, rounded=True, prefix="cta")
text_centered(ox + 40 + (WID[11] - 80) / 2, band_y + 32,
              "Pick one repetitive job. Schedule it this week.", size=H3, color=WHITE)
text(ox + 40, band_y + 140, "Questions? Post in #ai-ops.", size=SMALL, color=GREY)

# ----------------------------------------------------------------------------
# WRITE + VALIDATE
# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scheduled_tasks.excalidraw")
MAXW = max(WID.values()) + 200
finish(out, MAXW, TOTAL_W)
