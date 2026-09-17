#!/usr/bin/env python3
"""Build claude-outlook.excalidraw - ONE flowing, illustrated explainer for
DAY 16 of the Phlo AI training: "Claude in Microsoft Outlook"
(~5 min 10 board, + a 10s hold and a ~30s cut-away = ~5 min 50. Hard cap 8).

WHAT THIS BOARD IS - the CLOSE of the Microsoft block
-----------------------------------------------------
This is the fourth and last of the Microsoft-app videos, and it carries the
closing beat for all four. Beat 7 is not this video's payoff, it is the BLOCK's
payoff, landing once, here: one conversation touching the document, the sheet,
the deck and the reply. It therefore assumes the other three exist. If this is
ever recorded first, beat 7 needs re-cutting, not re-writing - see
`claude-outlook-prompt.md`.

Slug: `videos/ai-training/16-outlook/` - DAY 16, the next free number in the
day-by-day series (Day 15 is Excel).

THIS IS NOT A MOVE in the sense Days 4, 7, 8, 10, 12 and 15 are, and a future
reader should not treat it as one. It was first authored on 2026-09-17 into
`videos/claude/14-claude-outlook/`, which is the path the brief wrote, and
relocated here the same day BEFORE it was ever committed. Nothing was left
behind, no `claude/` folder was retired, and the `claude/` numbering is
untouched - 14 is still free there. The brief called this the close of "all
four days" while writing the path into `videos/claude/`; the "days" half turned
out to be the accurate one.

WHY THIS DAY EXISTS, AND WHY IT IS LAST
----------------------------------------
It is the only one of the four where THE OUTPUT LEAVES THE BUILDING, and the
only one still in beta. Word, Excel and PowerPoint all fail inwards: a bad
clause, a wrong average, a deck that argues nothing. Those cost you a rewrite.
An email that agrees to something costs you the thing it agreed to. That is the
whole reason the adversarial beat here is about COMMITMENT rather than quality -
the draft on beat 6 is genuinely well written, and that is the problem.

ONE WORKED EXAMPLE RUNS THE BOARD, and it is DELIBERATELY the same generic
packaging-supplier re-tender that Day 14 uses for the document and the deck.
That is what makes beat 7 land: by the time a viewer reaches the closing beat
they have already seen this contract edited in Word and argued in PowerPoint, so
"one conversation, four apps" is a fact about a job they recognise rather than a
diagram. Nothing here is Phlo-specific, there is no patient or clinical detail,
and every name, date and figure is invented.

  THE CONTINUITY IS THE SCENARIO, NOT THE FIGURES, and that is deliberate. Day
  14 pins a 9% Q3 unit-cost rise and a renewal-notice clause; this board pins a
  4p unit-cost rise and a cutover date. They describe different things in the
  same story, so DO NOT "reconcile" the numbers across the two boards - making
  them match would assert a relationship that does not exist.

  THERE IS EXACTLY ONE NUMBER ON THIS BOARD, 4p, and it is said twice in the
  same unit (beat 6's draft absorbs it, beat 7's ask reports it). An earlier
  draft also put a "4% uplift" in beat 3's thread, which meant a viewer heard
  "four per cent" and then "four pence" two beats apart and took one for a
  misstatement of the other - ON THE ADVERSARIAL BEAT, whose whole instruction
  is to read the numbers rather than the tone. Day 14's docstring records the
  same failure class ("an earlier draft used the SAME condition on both, which
  quietly wrecked beat 10"). Keep beat 3's thread figure-free.

  CHANGE THE EXAMPLE AND BEATS 3, 4, 6 AND 7 ALL MOVE TOGETHER.

The supplier asks to push the cutover two weeks, to the 26th. On beat 4 YOU
decide the answer is no, and choose only the register. On beat 6 a draft quietly
decides yes - to the date, to the price, and to a liability nobody authorised.
That flip is intentional and the narration names it. It is not a contradiction:
beat 4 is you making a decision, beat 6 is a draft making one for you.

BEAT 2 IS BUILT TO BE PATCHED, NOT RE-RECORDED
-----------------------------------------------
Claude for Outlook is in beta today. When that changes, beat 2 is the ONLY beat
that needs rebuilding, and it is visually self-contained so the rest of the
board is untouched. The mechanism:
  * the beta fact lives in ONE module-level constant, BETA_LINE, and appears
    nowhere else on the board;
  * NO OTHER BEAT names beta, a plan or a tier. Plan tiers are card-only, which
    is the "name the tool, never the tier" line Day 12, Day 14 and Day 15 all
    draw - here it has the extra job of keeping the patch to one string;
  * keep the replacement SAME LENGTH OR SHORTER so nothing reflows. That is the
    `ai-foundations/1-what-is-ai` fix and the Day 10 beat-2 regeneration, both
    of which held their layout by holding their string length.

GREEN = THE HUMAN PASS, and on this board it is on BEAT 2. Held constant from
Day 10, Day 11, Day 13, Day 14 and Day 15. It sits inside a VIOLET beat on
purpose: this is the first gate in the repo where the thing being gated leaves
the organisation, so it is drawn at hero size in green rather than tinted to its
beat. It uses the bespoke human_gate(), not the kit's person(), which is sized
for a crowd of tiny figures and reads as a paper dart standing alone - the same
call Day 10, Day 12 and Day 14 each made.
  BEAT 7's GREEN IS AN ACCENT, NOT THE MARKER. The scaffold gives beat 7 green
  because it is the closing beat; there is no second human gate drawn on it.
  Day 15's beat 8 records the identical distinction.

THE RED DATA CAUTION IS ON BEAT 5, NOT THE CLOSING BEAT, and that is a
deliberate departure from Days 7, 10, 12, 14 and 15, which all park it on the
last beat. Here beat 5 IS the data beat - scope, other people's words, things
sent in confidence - so the rule belongs where the subject is. It is drawn in
RED on an INDIGO beat so it still reads as the regulated-course caution rather
than as more scope material. The board keeps it GENERIC, as the brief instructs:
the specifics (audit logging, retention, Graph scopes, the beta recommended-use
list) are on `claude-outlook-resource-card.md`.

BEAT 6 IS THE ONE WIDE SLOT (1600, not 1200). It carries the artefact, the
three commitments pulled out of it, AND the catch - three columns' worth.
Widened rather than made taller: on a 16:10 laptop HEIGHT binds framing, so
1600x980 frames more comfortably than 1200 running 250px past its slot. Day 14's
beat 10 and Day 15's beat 6 record the identical call.
  NOTHING ON THE DRAFT IS BADLY WRITTEN. Do not "improve" beat 6 by adding a
  clumsy sentence, a typo or a wrong fact - the absence of one is the lesson,
  the same rule Day 15's beat 6 states about its sheet. Red appears on the
  heading, on the "read it once" prompt, on the three commitment labels and on
  the catch strip, and NOWHERE on the draft itself.

VERIFIED AGAINST ANTHROPIC'S LIVE DOCS on 2026-09-17
-----------------------------------------------------
Primary source: claude.com/docs/office-agents/outlook (the support-centre URL
support.claude.com/en/articles/14855664 301s to it - the same URL rot Day 12 and
Day 15 each found). Full read on `claude-outlook-resource-card.md`. What the docs back
directly, beat by beat:
  * Beat 1's triage split - the docs' own three groups: "what needs you, what
    Claude can handle, and what is noise".
  * Beat 2 wholesale - "currently in beta", "landed unsent in Outlook's compose
    pane", and the load-bearing one: "Claude never sends mail or invites on its
    own. The add-in does not request the `Mail.Send` permission."
  * Beat 3 - thread summarisation "with per-email citations", and selecting a
    citation opens that message in Outlook.
  * Beat 4 - "Tone is learned from your sent folder". The board's claim is
    narrower and safer than the docs': that REGISTER IS YOURS TO CHOOSE.
  * Beat 5 - the open item via Office.js, mailbox-wide reach via Microsoft
    Graph, `.docx`/`.xlsx` attachments read inline, and the beta caution against
    "Mailboxes containing privileged or regulated data without appropriate
    organizational controls". The Graph scopes stay OFF the board.
  * Beat 6 - "Review every draft and inbox action before accepting it" and
    "Maintain human oversight for anything leaving your organization".
  * Beat 7 - "Claude for Outlook shares context with Claude for Excel,
    PowerPoint, and Word, so Claude can work across your open Office apps in a
    single conversation."
The board names NO plan, NO tier and NO model, so only BETA_LINE dates. Model
availability dates fastest of all and is card-only.

PAN ORDER (left to right - the whitespace between slots IS the camera; frame one
beat at a time, and hold the silence on 6):

     1  ORANGE  the inbox is not a document
     2  VIOLET  it drafts, you send        <- status beat, 20s, PATCHABLE
     3  BLUE    the thread is the brief
     4  TEAL    tone is most of the job
     5  INDIGO  know what it can see       <- red data caution lives here
     6  RED     the reply that commits you <- ADVERSARIAL. HERO. 1600 wide.
     7  GREEN   one conversation, four apps <- [CUT TO CLAUDE DESKTOP], block close

RUNTIME (budgeted in seconds, then MEASURED against the written narration - the
measuring is the step that matters; this repo has THREE recorded instances of
per-beat budgets drifting by up to 2x against written prose, on Day 10, Day 14
and Day 15). 7 beats at ~5 min means the script must land near 700-750 spoken
words at 150 wpm, plus ~30s of cut-away where the doing takes longer than the
saying. The measuring command is in the script's header. MEASURE BEFORE DONE.

Scene template: Day 14's build_word_powerpoint.py - the most recent
Microsoft-apps board and the closest existing sibling, by way of the canonical
videos/claude/3-artefacts/build_excalidraw.py. Its doc_page, human_gate, _strike
and dashed_box one-offs are RE-DECLARED here rather than imported: bespoke
illustrations belong to the build that needs them and never to the kit. (The
brief names "the adapted build_word.py" as the template; no adapted Word build
exists in this repo or on any branch - see `claude-outlook-prompt.md`.)

Run:  python3 videos/ai-training/16-outlook/build_outlook.py
      /usr/bin/python3 preview.py videos/ai-training/16-outlook/claude-outlook.excalidraw out.png
      /usr/bin/python3 preview.py <scene> out.png XMIN XMAX   # close-up on one beat
      python3 build_all.py            # rebuild all + Style-B guard
      (preview.py needs the SYSTEM interpreter - Pillow is not on Homebrew's.)
"""
import os
import sys

_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d) and not os.path.exists(os.path.join(_d, "excalidraw_kit.py")):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)

import random
from excalidraw_kit import *

random.seed(141017)  # deterministic - re-runs produce identical files

# ----------------------------------------------------------------------------
# BEAT SCAFFOLD - seven beats, wide gaps so one frames cleanly on a 14" laptop
# ----------------------------------------------------------------------------
N = 7
GAP = 800
# every beat uses the SAME slot, shaped ~1.15:1 (content ~1120 wide x ~980 tall,
# the heading at y60 counted in) so framing is identical on a 14" laptop.
WID = {i: 1200 for i in range(1, N + 1)}
# Beat 6 is the ONE exception the house rule allows. It carries the draft, the
# three commitments lifted out of it AND the catch - three columns. Widened
# rather than made taller: HEIGHT binds framing on a 16:10 laptop, so 1600 x 980
# frames better than 1200 running past its slot. Day 14's beat 10 and Day 15's
# beat 6 record the identical decision. Do not solve this by making it taller.
WID[6] = 1600
ACCENT = {1: ORANGE, 2: VIOLET, 3: BLUE, 4: TEAL, 5: INDIGO, 6: RED, 7: GREEN}
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
# THE ONE PATCHABLE FACT. Beat 2 and nowhere else. Same length or shorter on
# replacement, or the beat reflows. See the docstring.
# ----------------------------------------------------------------------------
BETA_LINE = ("Claude for Outlook is in beta, and it drafts only.\n"
             "It has no permission to send.")

# ----------------------------------------------------------------------------
# THE WORKED EXAMPLE - a generic packaging-supplier re-tender, shared on purpose
# with Day 14 so the block's closing beat lands on a job the viewer recognises.
# Everyday business, never Phlo-specific, invented throughout.
# CHANGE IT AND BEATS 3, 4, 6 AND 7 ALL MOVE TOGETHER.
# ----------------------------------------------------------------------------
# Beat 3: the thread, oldest at the top. The background you were about to
# re-type is already in it.
THREAD = [
    ("supplier", "revised schedule for the cutover"),
    ("you", "checking this against the agreement"),
    ("procurement", "the price review was signed off in June"),
    ("supplier", "can we push the cutover to the 26th?"),
]
# Figure-free, like THREAD above - 4p is the board's ONLY number. See the
# docstring: this sticky is struck through, but struck text is still read.
PREAMBLE = ("\"As you know, back in June we\n"
            "agreed the price review with the\n"
            "current supplier, and the cutover\n"
            "was set for the 12th, so before...\"")

# Beat 4: four replies, ONE answer. The opener carries the register; the rest is
# identical in substance. The answer here is NO - which beat 6 then reverses.
REGISTERS = [
    ("warm", "Really sorry -",
     "the 26th does not work our end.\nCan we talk through the knock-ons?"),
    ("neutral", "We are not able",
     "to move the cutover. The 12th\nstands, as agreed in June."),
    ("firm", "The date is fixed.",
     "Any change goes back through\nthe contract owner."),
    ("on the record", "We are unable to agree",
     "a change to the cutover date.\nOur position is unchanged."),
]

# Beat 6: the draft. It is warm, well judged, correctly pitched and short. There
# is NOTHING wrong with the writing. Do not add a flaw.
ASK = "\"friendly reply, agree where we\ncan, keep it short\""
DRAFT_LINES = ("Thanks for the revised schedule -\n"
               "that all works our end. Happy to hold\n"
               "the current volumes to the 26th, and\n"
               "we can absorb the 4p uplift this\n"
               "quarter while the re-tender runs.\n"
               "Anything that slips beyond that sits\n"
               "with us.")
# The three sentences that are not yours to give. Phrase, then what it is.
COMMITMENTS = [
    ("hold the current volumes to the 26th", "a date"),
    ("absorb the 4p uplift this quarter", "a price"),
    ("anything that slips sits with us", "a liability"),
]

# Beat 7: the one conversation, and the four things it touches.
CROSS_ASK = ("\"unit cost is 4p higher than the model says - update it,\n"
             "redo the cost slide, then draft the note to the supplier\"")
APPS = [
    ("doc", "the agreement", BLUE, BLUE_BG),
    ("sheet", "the model", TEAL, TEAL_BG),
    ("deck", "the cost slide", YELLOW, YELLOW_BG),
    ("mail", "the reply", VIOLET, VIOLET_BG),
]


# ----------------------------------------------------------------------------
# BESPOKE ILLUSTRATIONS for this board (one-offs stay here, never in the kit)
# ----------------------------------------------------------------------------
def _strike(x, y, s, size, color, sw=4):
    """A hand line through text. The kit has no strikethrough, so this is a
    one-off - and it sits at 0.44 of the line box, not 0.5: with lineHeight 1.4
    the glyphs sit high in their box, so a line at the geometric middle crosses
    the descenders and reads as an underline that slipped. (Day 10, Day 12 and
    Day 14 all record this; rediscovering it cost a preview round there.)"""
    w = text_w(s, size)
    line(x - 8, y + size * LINE_H * 0.44, [[0, 0], [w + 16, 0]], stroke=color,
         sw=sw, rough=1, prefix="strike")


def mail_card(x, y, w, h, accent=GREYD, abg=FAINT, lines=2, avatar=True,
              seal=False, subject=True, unread=False):
    """One email in a list: avatar, a sender rule, a subject bar, body rules.

    Deliberately carries no text of its own - the callers that need words put
    them beside it. A pile of six of these with three invented sender names on
    them would read as a screenshot, which the skill forbids."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="mail")
    if avatar:
        ellipse(x + 14, y + 14, 28, 28, stroke=accent, bg=abg, sw=2, rough=1, prefix="mav")
    tx = x + (54 if avatar else 16)
    line(tx, y + 22, [[0, 0], [0.30 * w, 0]], stroke=GREYD, sw=3)
    if subject:
        rect(tx, y + 36, 0.46 * w, 12, stroke="transparent", bg=abg, sw=1, rough=1,
             rounded=True, prefix="msub")
    for k in range(lines):
        line(x + 16, y + 62 + k * 20, [[0, 0], [(0.78 if k % 2 == 0 else 0.56) * w, 0]],
             stroke=GREY, sw=2)
    if unread:
        ellipse(x - 18, y + h / 2 - 8, 14, 14, stroke=accent, bg=accent, sw=2, prefix="munr")
    if seal:
        # a small wax-seal mark: a ring with a cross-hatch, drawn in the accent
        ellipse(x + w - 54, y + h - 50, 34, 34, stroke=accent, bg=abg, sw=3, rough=2, prefix="mseal")
        line(x + w - 46, y + h - 42, [[0, 0], [18, 18]], stroke=accent, sw=2, prefix="msealx")
        line(x + w - 28, y + h - 42, [[0, 0], [-18, 18]], stroke=accent, sw=2, prefix="msealx")


def compose_pane(x, y, w, h, body=None, accent=VIOLET, abg=VIOLET_BG,
                 size=BODY, send=None, to_label=True):
    """Outlook's compose pane: a To: rule, the drafted body, and a Send control.

    `send` is the colour of the Send button, or None to draw no button at all.
    Beat 2 draws it GREEN and outside the pane, because the whole point is that
    pressing it is not part of the drafting."""
    rect(x, y, w, h, stroke=accent, bg=WHITE, sw=2, rough=1, rounded=True, prefix="comp")
    rect(x, y, w, 10, stroke="transparent", bg=accent, sw=1, rough=1, rounded=True, prefix="compb")
    if to_label:
        text(x + 22, y + 24, "To:", size=SMALL, color=GREY)
        line(x + 72, y + 40, [[0, 0], [0.5 * w, 0]], stroke=FAINT, sw=3)
    by = y + (66 if to_label else 26)
    if body is not None:
        text(x + 22, by, body, size=size, color=INK)
    if send is not None:
        button(x + w - 170, y + h - 82, "Send", send, w=140, h=58, filled=False)


def mail_stack(x, y, w, h, n=3, accent=GREYD, abg=FAINT, step=12):
    """A small pile of unread mail - n cards offset behind one another."""
    for k in range(n - 1):
        off = (n - 1 - k) * step
        rect(x + off, y + off, w, h, stroke=GREYD, bg=WHITE, sw=2, rough=1,
             rounded=True, prefix="mstk")
    mail_card(x, y, w, h, accent=accent, abg=abg, lines=2)


def sheet_grid(x, y, w, h, accent=TEAL, abg=TEAL_BG, cols=4, rows=4, mark=None):
    """A tiny spreadsheet: a header row and a grid, with one cell optionally
    inked in the accent - the figure that changed."""
    cw, ch = w / cols, h / rows
    for c in range(cols):
        rect(x + c * cw, y, cw, ch, stroke=GREYD, bg=abg, sw=1, rough=1,
             rounded=False, prefix="shh")
    for r in range(1, rows):
        for c in range(cols):
            filled = (mark is not None and (r, c) == mark)
            rect(x + c * cw, y + r * ch, cw, ch, stroke=GREYD,
                 bg=(accent if filled else WHITE), sw=1, rough=1, rounded=False,
                 prefix="shc")


def mini_slide(x, y, w, h, accent=YELLOW, abg=YELLOW_BG, bullets=2):
    """A single slide: title bar, a bullet or two, a small bar chart."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="msl")
    rect(x + 0.10 * w, y + 0.13 * h, 0.5 * w, 0.10 * h, stroke="transparent",
         bg=accent, sw=1, rough=1, rounded=True, prefix="msltt")
    for k in range(bullets):
        ly = y + 0.38 * h + k * 0.15 * h
        ellipse(x + 0.10 * w, ly, 7, 7, stroke=accent, bg=accent, sw=1, prefix="mslb")
        line(x + 0.10 * w + 18, ly + 3, [[0, 0], [0.36 * w, 0]], stroke=GREY, sw=2)
    base = y + h - 0.14 * h
    for k, hh in enumerate([0.20, 0.34, 0.26, 0.44]):
        bh = hh * h
        rect(x + 0.60 * w + k * 0.085 * w, base - bh, 0.05 * w, bh, stroke=INK,
             bg=abg, sw=1, rough=1, rounded=False, prefix="mslbar")


def app_card(x, y, w, h, kind, accent, abg):
    """One of beat 7's four artefacts, drawn as a small app window. Four kinds,
    one frame, so the row reads as four views of the SAME conversation rather
    than four products."""
    rect(x, y, w, h, stroke=INK, bg=WHITE, sw=2, rough=1, rounded=True, prefix="acard")
    line(x, y + 32, [[0, 0], [w, 0]], stroke=GREY, sw=1)
    for k in range(3):
        ellipse(x + 14 + k * 15, y + 11, 9, 9, stroke=GREY, bg=GREY, sw=1, prefix="adot")
    ix, iy, iw, ih = x + 20, y + 54, w - 40, h - 78
    if kind == "doc":
        rect(ix, iy, 0.5 * iw, 12, stroke="transparent", bg=accent, sw=1, rough=1,
             rounded=True, prefix="adt")
        for k in range(6):
            line(ix, iy + 34 + k * 20, [[0, 0], [(0.92 if k % 3 else 0.62) * iw, 0]],
                 stroke=GREY, sw=2)
    elif kind == "sheet":
        sheet_grid(ix, iy, iw, ih * 0.82, accent=accent, abg=abg, mark=(2, 2))
    elif kind == "deck":
        mini_slide(ix, iy, iw, ih * 0.84, accent=accent, abg=abg)
    else:
        mail_card(ix, iy, iw, ih * 0.86, accent=accent, abg=abg, lines=3, avatar=False)


def human_gate(cx, cy, color=GREEN, abg=GREEN_BG, s=1.0):
    """The human marker: a head plus rounded shoulders, filled.

    GREEN, not the beat's accent - green = the human pass is held constant from
    Day 10, Day 11, Day 13, Day 14 and Day 15, and this marker is safety-bearing
    in a mandatory course for a regulated pharmacy. It does not use the kit's
    person(), which is sized for a crowd of tiny figures and reads as a paper
    dart when it has to stand alone at hero size."""
    r = 26 * s
    ellipse(cx - r, cy - 62 * s, 2 * r, 2 * r, stroke=color, bg=WHITE, sw=3,
            rough=1, prefix="hghead")
    line(cx - 50 * s, cy + 46 * s,
         [[0, 0], [0, -22 * s], [18 * s, -50 * s], [82 * s, -50 * s],
          [100 * s, -22 * s], [100 * s, 0]],
         stroke=color, sw=3, rough=1, bg=abg, fill="solid", prefix="hgbody")


# ============================================================================
# BOARD TITLE
# ============================================================================
text(OX[1], -400, "Claude in\nMicrosoft Outlook", size=HERO, color=INK)
text(OX[1] + 6, -400 + 2 * HERO * LINE_H + 10,
     "the only one of the four where the output leaves the building",
     size=H2, color=ORANGE)

# ============================================================================
# BEAT 1 - THE INBOX IS NOT A DOCUMENT   (two jobs, side by side)
# ============================================================================
ox = beat_head(1, "the inbox is not a document",
               "Two jobs live in here, and they are not the same job.\n"
               "One of them is deciding. The other is only wording.")
# -- left: triage, the deciding job
text(ox + 40, 292, "triage", size=H2, color=ORANGE)
text(ox + 40, 352, "deciding: what needs you, what it\ncan handle, what is noise",
     size=BODY, color=INK)
mail_stack(ox + 40, 480, 200, 120, n=3, accent=ORANGE, abg=ORANGE_BG)
text(ox + 40, 648, "unread", size=SMALL, color=GREY)  # clears the offset cards
arrow(ox + 262, 540, [[0, 0], [66, 0]], stroke=ORANGE, sw=4, rough=1)
for k, (lab, col) in enumerate([("needs you", ORANGE), ("it can draft", ORANGE),
                                ("noise", GREY)]):
    chip(ox + 348, 458 + k * 78, lab, fill=WHITE, text_color=col, border=col, size=SMALL)
# -- right: drafting, the wording job
text(ox + 660, 292, "drafting", size=H2, color=ORANGE)
text(ox + 660, 352, "wording: what to say,\nand how to say it", size=BODY, color=INK)
mail_card(ox + 660, 470, 250, 130, accent=ORANGE, abg=ORANGE_BG, lines=2)
arrow(ox + 780, 612, [[0, 0], [0, 52]], stroke=ORANGE, sw=4, rough=1)
compose_pane(ox + 660, 678, 330, 150, accent=ORANGE, abg=ORANGE_BG, to_label=True)
text(ox + 682, 744, "a draft reply, in your words", size=SMALL, color=GREYD)
# -- the misallocation
sticky(ox + 40, 856, 1120, 130, FAINT, angle=jit(0.7))
text(ox + 80, 884, "Most people ask it for the second when they need the first -\n"
                   "and then wonder why it only saved them ten minutes.",
     size=H3, color=GREYD)

# ============================================================================
# BEAT 2 - IT DRAFTS, YOU SEND   (status beat, 20s, PATCHABLE - see docstring)
# ============================================================================
ox = beat_head(2, "it drafts, you send")
compose_pane(ox + 40, 320, 430, 290, accent=VIOLET, abg=VIOLET_BG,
             body="a reply, written\nand waiting", size=BODY)
text(ox + 40, 626, "it writes the draft", size=SMALL, color=VIOLET)
arrow(ox + 492, 462, [[0, 0], [96, 0]], stroke=GREEN, sw=5, rough=1)
human_gate(ox + 664, 500, color=GREEN, abg=GREEN_BG)
text(ox + 592, 578, "you read it", size=SMALL, color=GREEN)
arrow(ox + 786, 462, [[0, 0], [96, 0]], stroke=GREEN, sw=5, rough=1)
button(ox + 910, 430, "Send", GREEN, w=200, h=72, filled=False)
text(ox + 910, 522, "you press Send", size=SMALL, color=GREEN)
# the ONE patchable fact on the board
text(ox + 40, 700, BETA_LINE, size=H3, color=INK)
chip(ox + 40, 812, "nothing leaves without you", fill=WHITE, text_color=VIOLET,
     border=VIOLET, size=LABEL)
text(ox + 40, 900, "Everything it writes waits for you in the compose pane.",
     size=BODY, color=GREYD)

# ============================================================================
# BEAT 3 - THE THREAD IS THE BRIEF
# ============================================================================
ox = beat_head(3, "the thread is the brief",
               "Everything you were about to re-explain is already sitting\n"
               "above the reply box. It has read all of it.")
text(ox + 40, 286, "the thread", size=SMALL, color=GREY)
for k, (who, subj) in enumerate(THREAD):
    cy = 318 + k * 96
    # lines=0, subject=False: the card's own body rules would strike straight
    # through the subject text, which reads as a deletion mark on a beat that
    # has nothing to do with deletions.
    mail_card(ox + 40 + k * 14, cy, 520 - k * 14, 84, accent=BLUE, abg=BLUE_BG,
              lines=0, subject=False)
    text(ox + 96 + k * 14, cy + 44, subj, size=SMALL, color=GREYD)
line(ox + 16, 318, [[0, 0], [0, 384]], stroke=BLUE, sw=4)
text(ox + 40, 716, "your reply", size=SMALL, color=BLUE)
compose_pane(ox + 40, 748, 520, 150, accent=BLUE, abg=BLUE_BG,
             body="\"reply agreeing the price,\nholding the date\"", size=SMALL)
# -- right: the preamble you do not need to type
text(ox + 640, 286, "what you were about to type", size=SMALL, color=GREY)
sticky(ox + 640, 318, 520, 220, FAINT, angle=jit(-1.1))
text(ox + 672, 344, PREAMBLE, size=SMALL, color=GREYD)
for k in range(4):
    _strike(ox + 672, 344 + k * SMALL * LINE_H, PREAMBLE.split("\n")[k], SMALL, BLUE, sw=3)
text(ox + 640, 566, "it is already above your reply", size=BODY, color=BLUE)
chip(ox + 640, 630, "what has been decided? what is still open?",
     fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)
text(ox + 640, 718, "every answer cites the email it came from -\n"
                    "click it and you land on the original.", size=SMALL, color=GREYD)
chip(ox + 40, 924, "stop explaining the background that is already in the thread",
     fill=WHITE, text_color=BLUE, border=BLUE, size=SMALL)

# ============================================================================
# BEAT 4 - TONE IS MOST OF THE JOB   (four registers, ONE answer, 2x2)
# ============================================================================
ox = beat_head(4, "tone is most of the job",
               "Four replies to one message. The answer is the same in all four.\n"
               "What changes is the register - and the register is the decision.")
text(ox + 40, 286, "they asked:", size=SMALL, color=GREY)
mail_card(ox + 40, 318, 1120, 112, accent=TEAL, abg=TEAL_BG, lines=0, subject=False)
text(ox + 112, 350, "\"Can we push the cutover two weeks, to the 26th?\"",
     size=BODY, color=INK)
for k, (reg, opener, rest) in enumerate(REGISTERS):
    cx = ox + 40 + (k % 2) * 580
    cy = 476 + (k // 2) * 212
    rect(cx, cy, 540, 188, stroke=GREYD, bg=WHITE, sw=2, rough=1, rounded=True,
         angle=jit(0.9), prefix="reg")
    text(cx + 26, cy + 18, reg, size=SMALL, color=GREY)
    text(cx + 26, cy + 56, opener, size=BODY, color=TEAL)
    text(cx + 26, cy + 96, rest, size=BODY, color=INK)
text(ox + 40, 924, "The content is identical. The register is the decision -\n"
                   "and it is the half it cannot make for you.", size=H3, color=INK)

# ============================================================================
# BEAT 5 - KNOW WHAT IT CAN SEE   (scope; the RED data caution lives here)
# ============================================================================
ox = beat_head(5, "know what it can see",
               "A mailbox is not your filing cabinet. Most of what is in it\n"
               "was written by somebody else, and sent to you in confidence.")
rect(ox + 40, 300, 620, 500, stroke=INDIGO, bg=INDIGO_T, sw=3, rough=1, rounded=True,
     fill="solid", prefix="mbox")
text(ox + 66, 318, "your mailbox", size=SMALL, color=INDIGO)
mail_card(ox + 70, 366, 200, 96, accent=INDIGO, abg=INDIGO_BG, lines=2)
text(ox + 300, 396, "words other people wrote", size=BODY, color=INK)
file_icon(ox + 76, 500, w=58, h=74, abg=INDIGO_BG)
file_icon(ox + 150, 500, w=58, h=74, abg=INDIGO_BG)
text(ox + 300, 526, "attachments you did not write", size=BODY, color=INK)
mail_card(ox + 70, 636, 200, 118, accent=INDIGO, abg=INDIGO_BG, lines=1, seal=True)
text(ox + 300, 676, "things sent in confidence", size=BODY, color=INK)
# -- right: how far it reaches
text(ox + 740, 300, "what it reaches", size=H3, color=INDIGO)
mail_card(ox + 740, 366, 130, 84, accent=INDIGO, abg=INDIGO_BG, lines=1, avatar=False)
text(ox + 896, 392, "the email you\nhave open", size=BODY, color=INK)
rect(ox + 740, 500, 130, 84, stroke=INDIGO, bg=INDIGO_BG, sw=2, rough=1, rounded=True,
     fill="solid", opacity=60, prefix="mbx2")
for k in range(3):
    line(ox + 756, 524 + k * 18, [[0, 0], [98, 0]], stroke=INDIGO, sw=2)
text(ox + 896, 512, "and, when you ask,\nthe rest of it", size=BODY, color=INK)
text(ox + 740, 620, "search, other threads,\nthe calendar, the attachments",
     size=SMALL, color=GREYD)
chip(ox + 40, 846, "check what your organisation's data agreement covers "
                   "before you point it at a mailbox",
     fill=WHITE, text_color=RED, border=RED, size=SMALL)
text(ox + 40, 936, "Email from outside is untrusted input - treat it as data, "
                   "never as instructions.", size=SMALL, color=RED)

# ============================================================================
# BEAT 6 - THE REPLY THAT COMMITS YOU   (ADVERSARIAL. HERO. 1600 wide.)
# ============================================================================
ox = beat_head(6, "the reply that commits you",
               "Nothing here is badly written. That is the problem: review reads\n"
               "for tone, and the tone is exactly right.")
# -- column A: what you asked for, and what came back
text(ox + 40, 286, "what you asked for", size=SMALL, color=GREY)
sticky(ox + 40, 318, 520, 112, FAINT, angle=jit(1.3))
text(ox + 72, 340, ASK, size=BODY, color=GREYD)
# GREYD, not RED: the draft itself carries no red anywhere. Red is on the
# heading, the prompt below, the three labels and the catch strip - never on the
# artefact, or the beat gives its own answer away before the pause does.
compose_pane(ox + 40, 462, 520, 340, body=DRAFT_LINES, accent=GREYD, abg=FAINT,
             size=BODY, to_label=True)
text(ox + 40, 832, "Read it once. Would you have sent it?", size=H3, color=RED)
# -- column B: the three sentences that are not yours to give
text(ox + 620, 286, "what it actually promises", size=SMALL, color=RED)
for k, (phrase, kind) in enumerate(COMMITMENTS):
    cy = 350 + k * 150
    xmark(ox + 620, cy + 6, RED, s=22)
    text(ox + 668, cy, phrase, size=SMALL, color=INK)
    chip(ox + 668, cy + 40, kind, fill=WHITE, text_color=RED, border=RED, size=SMALL)
text(ox + 620, 800, "Three sentences. Not one of\nthem was yours to give.",
     size=H3, color=RED)
# -- column C: the catch
text(ox + 1120, 286, "the catch", size=SMALL, color=GREY)
text(ox + 1120, 330, "Read only the sentences that\ncontain a commitment - a date,\n"
                     "a number, an obligation.", size=BODY, color=INK)
text(ox + 1120, 476, "For each one, name who\nauthorised it.", size=BODY, color=INK)
text(ox + 1120, 580, "If you cannot name them,\nit does not go.", size=H3, color=RED)
text(ox + 1120, 700, "Tone is not the review.\nIt is what gets the draft\npast one.",
     size=BODY, color=GREYD)
chip(ox + 40, 936, "read it for what it promises, not for how it reads",
     fill=WHITE, text_color=RED, border=RED, size=LABEL)

# ============================================================================
# BEAT 7 - ONE CONVERSATION, FOUR APPS   (the BLOCK's close, landing once)
# ============================================================================
ox = beat_head(7, "one conversation, four apps",
               "The payoff for the whole block. One thread, four files,\n"
               "and nothing copied between them.")
text(ox + 40, 282, "one conversation", size=SMALL, color=GREY)
rect(ox + 40, 314, 1120, 140, stroke=GREEN, bg=GREEN_T, sw=2, rough=1, rounded=True,
     fill="solid", prefix="conv")
text(ox + 76, 350, CROSS_ASK, size=BODY, color=INK)
for k, (kind, label, acc, abg) in enumerate(APPS):
    cx = ox + 40 + k * 293
    app_card(cx, 496, 240, 214, kind, acc, abg)
    text(cx, 722, label, size=SMALL, color=acc)
    if kind == "mail":
        # NOT a second human gate - beat 2 owns that marker, and drawing another
        # here would dilute it. This is a status on the artefact, in neutral
        # grey, so beat 7 still says "unsent" when it is lifted out of the board
        # on its own and the closing line is not there to say it.
        text(cx + 22, 676, "draft - unsent", size=SMALL, color=GREYD)
    if k:
        arrow(cx - 46, 600, [[0, 0], [36, 0]], stroke=GREEN, sw=4, rough=1)
text(ox + 40, 782, "Change the figure once. The slide follows. The email\n"
                   "that reports it follows too.", size=H3, color=INK)
demo_badge(ox + 20, 880, "show in Claude desktop app: change a figure in Excel, "
                         "rebuild the slide, then draft the email that reports it")
text(ox + 40, 964, "One conversation. Four files. One rule that outlasts all four:\n"
                   "nothing leaves the building until you have read it.",
     size=H3, color=GREEN)

# ----------------------------------------------------------------------------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-outlook.excalidraw")
finish(out, max(WID.values()) + 200, TOTAL_W)
