# Brief - Day 10: design work with Claude

**Folder:** `videos/ai-training/10-design/`
**File:** `build_design.py` -> `claude-design.excalidraw`
**Slug:** `claude-design` (so: `claude-design-script.md`, `claude-design-prompt.md`,
`claude-design-resource-card.md`)
**Style:** Style B, per `.claude/skills/SKILL.md` and the repo `CLAUDE.md`
**Length:** 7 beats. The recorded script measures **~6 min 38** (950 spoken words at 150 wpm, plus ~18s where the cut-away takes longer to do than to say). Hard cap 8, target 4 to 6 - see Runtime budget.
**Curriculum ref:** **Day 10** of the AI training day-by-day series. **No Day 10 entry
exists in `Phlo_Mandatory_AI_Course_Curriculum.docx`** - the day series is newer than the
docx, and the entry that exists describes the module-2.12 Claude Design product
walkthrough this board replaces. Board and narration were authored from this brief.
**Reconcile both against the curriculum when a Day 10 entry exists.**
**Action:** ADAPT, then MOVE. The brief said to adapt the folder holding
`build_design.py`, which was `videos/ai-training/10-design/`; it was adapted there and then
moved here as Day 10 when the day-by-day series was confirmed as the destination.

## Where it sits in the series

**Day 10 is the advanced beat.** By here a person can prompt (Day 3), hold context
(Day 4), write a procedure (Day 7) and supervise a long run (Day 8). What is left is
judgement. It sits **after Cowork deliberately**: the habit this board teaches - name the
test before you look - is the one that catches a *plausible* result, which is exactly what
a long unsupervised run produces.

**Day 9 is not built and nothing here depends on it.** Day 10 makes no callback to a day
between Cowork and this one, so the numbering can stay as it is.

Per the repo precedence rule, **a Day covers its topic in full**: this board does not
signpost the old module-2 walkthrough and must never be trimmed to a "see the other
video" pointer. There is no other video - `claude/12-design` *is* this one, moved.

## Why this video exists

**The advanced failure in design work is not a bad output, it is an acceptable one.
Generic passes review.** Everything on the board serves that one sentence.

**Ships:** one design, iterated three times, with each change named.
**Pause-and-try:** find the adjective in your last brief and replace it with a reference.

## Where it came from, and what changed

This board **moved here from `videos/ai-training/10-design/`** (module 2.12), the same move
Day 4, Day 7 and Day 8 each made out of `videos/claude/`. That series now has a **fourth
numbering gap, at 12** - a gap is not lost work.

It was a **nine-beat product walkthrough of Claude Design** (the Anthropic Labs
research preview): what it is, the design-system onboarding, start-from-anything inputs,
the export targets, three role flows, the preview caveat, a try-it close. That board
taught a **feature surface**.

It is now a **seven-beat board about the practice**. The reframe is settled by the demo
badge the brief specifies - "show in Claude desktop app" - and by the fact that not one
of the seven beats names a product, a plan tier or a model. So the board teaches design
*craft* with Claude and depends on nothing that can be renamed or re-tiered underneath it.

**Everything displaced is on `claude-design-resource-card.md`:** Labs / research-preview
status, the model and plan it runs on, design-system onboarding from a codebase and
design files, the four starting points, PPTX / Canva export, handing a feature flow to
Claude Code and the designer / PM / founder flows. That card is a **deliverable, not an
afterthought** - do not re-inflate the board with it.

### Two judgement calls worth recording

**1. The data caution moved onto the board rather than onto the card.** The old beat 8
carried the only on-screen data-handling rule ("confidential designs, patient-facing
material, or a private codebase"). The seven-beat brief has no slot for it. It now sits
on **beat 7**, in red, beside the human pass - because this is a mandatory course for a
regulated pharmacy and that is the only data rule a viewer sees on screen. This is the
same call Day 7 made when its six-beat cut had no slot for the red Skill caution. **Do
not quietly drop it in a later edit.**

**2. Beat 6 carries its own catch.** The shared constraint is "how this capability fails
silently **and how you would catch it**". The brief specified the failure (three
presentable, interchangeable outputs) and the chip, but not the catch. The catch on the
board is: **name what the design has to get right before you look at it**, write it as
one falsifiable sentence, then hold each output against it. All three outputs then fail
the same test, having passed the eye test. Failure without a catch is a diagnosis with no
test, and this beat is the Best Catch feeder, so the catch is the half that has to
travel.

## The seven beats

| # | Accent | Heading | What is drawn |
|---|---|---|---|
| 1 | orange | blank page to worth-reacting-to | A blank page beside a 90-second draft, with three margin critiques. The value is something to argue with, not something to ship. |
| 2 | violet | reference beats adjectives | "clean and modern" struck through against a taped-up reference. Struck adjectives above, pasteable things below. Caption: *show it the thing you like*. |
| 3 | blue | structure versus polish | The **same content twice** - grey boxes in the right order, and the same polished blocks in the wrong order. Polish on bad structure is a redraw. |
| 4 | teal | iterate by talking to it | A greyed settings panel against the correction said in plain language. |
| 5 | indigo | in units, not wholesale | One design forking two ways: change one named element (everything else survives) or start again (the card that was working is gone). Chip: *regenerate is not iterate*. |
| 6 | red | presentable is not correct | **Adversarial.** Three interchangeable outputs, all "looks fine", then the named criterion, then all three fail it. Chip: *you will accept this if you are in a hurry*. |
| 7 | green | human pass for brand-final | The three named iterations, the human gate (Claude drafts, a person passes it, it is brand-final), the red data rule, the demo badge, the close chip. |

**Pan order:** left to right, beats 1 to 7, one slot at a time. Documented in the build
script docstring.

**Accent cycle:** orange / violet / blue / teal / indigo / red / green - no repeats at
all on a seven-beat board, so none adjacent.

**Demo badge:** beat 7 only - `show in Claude desktop app: one design, three targeted
iterations`, with `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` in the script.

## Runtime budget

Budgeted in seconds first, beat count second - then **measured against the written
script, which is the step that matters.** Beats are not uniform: 2, 5 and 6 are the hero
beats; 1, 4 and 7 run short.

| section | words | on the clock |
|---|---|---|
| hook | 31 | 12s |
| why this matters | 92 | 37s |
| beat 1 · blank page to worth-reacting-to | 72 | 29s |
| beat 2 · reference beats adjectives | 104 | 42s |
| beat 3 · structure versus polish | 78 | 31s |
| beat 4 · iterate by talking to it | 72 | 29s |
| beat 5 · in units, not wholesale | 82 | 33s |
| **beat 6 · presentable is not correct** | **169** | **68s** |
| beat 7 · human pass for brand-final (incl. ~18s cut-away doing time) | 131 | 70s |
| pause-and-try | 46 | 18s |
| close | 73 | 29s |
| **total** | **950** | **~6 min 38** |

**Re-measure if you rewrite the narration.** The first draft of the script ran **1,520
words - over 10 minutes, past the 8-minute hard cap** - because the per-beat second
budget was never checked back against the written prose. To re-measure:

```bash
awk '/^## On-screen|^## Recording/{stop=1} stop{next}
     /^## [0-9]/{if(s)printf "%-44s %4d w ~%3ds\n",substr(s,4,40),w,int(w/2.5); s=$0; w=0; next}
     /^(>|`\[|\[|---|- |[0-9]\. )/{next} s{w+=NF; t+=NF}
     END{printf "%-44s %4d w ~%3ds\n",substr(s,4,40),w,int(w/2.5); \
         printf "\nTOTAL %d words = %d:%02d\n",t,int(t/2.5)/60,int(t/2.5)%60}' \
  videos/ai-training/10-design/claude-design-script.md
```

Hard cap 8 minutes, target 4 to 6. This runs ~38s over target and 1 min 22 under the cap, deliberately: the prose is already tight, so the route to target is the shorter cut, not thinner teaching.
**If it needs a shorter cut: beats 3 and 4 are the droppable pair** - nothing later
depends on either, and the board still lands its argument (draft → named reference → one
unit at a time → presentable is not correct → human pass). That removes 60s and takes it to ~5 min 40, inside target. **Beat 6 is the one to protect** - it is the longest section on purpose and
everything else was trimmed to pay for it.

## The worked example

One generic landing page for an internal tool runs through beats 1, 4, 5 and 7 - the
draft you can argue with, the correction said in words, that one correction applied to
one element and the three named iterations you ship. Everyday business, never
Phlo-specific, no patient or clinical detail, fictional content throughout.

The three named changes are pinned in `NAMED_CHANGES` and the beat-6 criterion in
`CRITERION`, both at the top of the build script. **Change the example and all four beats
have to move together.**

## How it is built

One flowing hand-drawn board, generated by `build_design.py`, which imports the shared
engine (`from excalidraw_kit import *`) and holds only the composition: the beat scaffold
(`OX` / `WID` / `ACCENT` / `beat_head`) and this board's bespoke illustrations. Never
hand-place elements in the `.excalidraw`; change the build script and regenerate. Never
edit `excalidraw_kit.py`.

```bash
python3 videos/ai-training/10-design/build_design.py          # rebuild this board
/usr/bin/python3 preview.py videos/ai-training/10-design/claude-design.excalidraw out.png
/usr/bin/python3 preview.py <scene> out.png XMIN XMAX    # close-up on one beat
python3 build_all.py                                     # rebuild all + Style-B guard
```

`preview.py` needs `/usr/bin/python3` - Pillow is on the system interpreter, not
Homebrew's. Beat *n* frames at `XMIN = (n-1)*2000 - 100`, `XMAX = (n-1)*2000 + 1300`.

`random.seed(121207)` keeps re-runs byte-identical.

### Bespoke illustrations (one-offs - they stay in the build, never in the kit)

- `mockup(..., shuffled=, cards=)` - the polished screen. `shuffled=True` puts the same
  blocks in the wrong order (beat 3's right half, beat 5's regenerate); `cards=0` drops
  the card row so beat 5 can show the regenerate losing the element that was working.
- `wireframe()` - the same screen in grey boxes. Two cards, deliberately matching
  `mockup()`, so beat 3 really is the same content twice.
- `struck()` - the kit has no strikethrough. Text plus a line across it, at **0.44** of
  the line box: with `lineHeight 1.4` the glyphs sit high in their box, so a line at the
  geometric middle crosses the descenders and reads as an underline that slipped.
- `reference_frame()` - a pasted reference, **taped** at both top corners. A paperclip
  was drawn first and rejected: at this scale it rasterised as a stray rectangle.
- `settings_panel()` - sliders, a dropdown and a hex field, all grey, because it is the
  thing you are *not* reaching for.
- `human_gate()` - the human-in-loop marker on beat 7. It does **not** use the kit's
  `person()`, which is sized for a crowd of tiny figures and reads as a paper dart when
  it has to stand alone at hero size. This marker is safety-bearing (SKILL.md requires
  the human decision point to be unmistakable), so it gets a bespoke head-and-shoulders,
  the same reasoning behind Day 3's `person_big()`.

## Validation record

`finish()` reported **0 text-overflow and 0 text/text collision warnings**, so there is
nothing to justify. `python3 build_all.py` runs **BUILD OK | GUARD PASS** across all
sixteen scenes in the repo.

Previewed whole-board plus a close-up x-window on all seven beats. Five things the
rasteriser caught and the build now fixes:

1. The strike on "clean and modern" sat on the descenders - factor 0.52 → **0.44**.
2. The paperclip on the reference read as a stray rectangle - replaced with **tape**.
3. An unlabelled dashed annotation arrow on beat 3 read as a stray mark - **removed**.
4. `wireframe()` drew three cards against `mockup()`'s two, undercutting "the same
   content, twice" - **two cards now**.
5. The kit's `person()` on beat 7 read as a paper dart - replaced with `human_gate()`.

Also tightened: the beat 2 and 4 stickies were bottom-heavy against their text, the beat
6 criterion band was top-heavy and the beat 5 ring spilled off its card onto the hero.

**Note on the rasteriser:** `preview.py` ignores element `angle`, so the rotation jitter
on notes, chips and the beat 2 tape does not show in the PNGs. It is in the scene and
will show in Excalidraw. Beat 6's three outputs are the deliberate exception - **no
jitter and one neutral grey**, because the sameness *is* the point: a tilt or a colour
each would read as three real options rather than three interchangeable ones.

## Constraints this board is held to

- No Excalidraw `frame` elements (a literal frame is a hard `build_all.py` guard
  failure), no boxes, no connector spine, no inter-beat arrows, no colour-band washes,
  white background. Beats are separated by whitespace only - **the whitespace is the
  camera**.
- Uniform slots, `WID = 1200`, content ~1120 x ~980, `GAP = 800`.
- All text hand-drawn (`fontFamily 1` / `HAND`), `roughness 1`, `lineHeight 1.4`. No
  typed sans or mono anywhere. Body and explanation text stays ink or grey; accents are
  for headings, labels, shapes and fills.
- Headings via the kit's `heading()`. No step-number circle, no highlighter sweep, no
  sparkles.
- Examples generic, not Phlo-specific. No Phlo branding or logo, no patient or clinical
  specifics. Phlo-native material appears only in the live cut-away at the demo badge.
- Fictional identifiers only. Any clinical or dispensing flow drawn anywhere shows the
  human verification gate: AI drafts, a human approves, the record updates.
- Product proper nouns exact: Claude, Artifact, Project, Skill, MCP, Connector, Cowork,
  Claude Desktop, Claude Tag, Dispatch.
- British English, hyphens not em dashes, no Oxford commas.

## Source note - READ BEFORE RECORDING

`Phlo_Mandatory_AI_Course_Curriculum.docx` is the stated source of truth for script
blocks and is **not in this repo**. There is **no Day 10 entry**, and the
module-2.12 entry that exists describes the **Claude Design product walkthrough this
board replaces** rather than the design-practice video it now is.

The narration in `claude-design-script.md` was therefore written from this brief.
**Reconcile it against the curriculum before recording** - particularly the hook, the
pause-and-try and the resource list. The script carries the same note at the top.
