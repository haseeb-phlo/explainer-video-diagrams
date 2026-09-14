# Brief - Day 11: Claude Design, job by job

**Folder:** `videos/ai-training/11-design-workflows/`
**File:** `build_design_workflows.py` -> `claude-design-workflows.excalidraw`
**Slug:** `claude-design-workflows` (so: `claude-design-workflows-script.md`,
`claude-design-workflows-prompt.md`, `claude-design-workflows-resource-card.md`)
**Style:** Style B, per `.claude/skills/SKILL.md` and the repo `CLAUDE.md`
**Length:** 9 beats. The recorded script measures **~6 min 42** (967 spoken words at
150 wpm, plus ~15s where the cut-away takes longer to do than to say). Hard cap 8,
target 4 to 6 - see Runtime below.
**Curriculum ref:** **Day 11**. **No Day 11 entry exists in
`Phlo_Mandatory_AI_Course_Curriculum.docx`** - the day series is newer than the docx, as
with Day 10 and Day 13. **Reconcile board and narration against the curriculum when a
Day 11 entry exists.**

**Ships:** one job off the board, run end to end through the six-step loop.
**Pause-and-try:** pick the job you actually have this week, run the six steps, then ask
for the empty state before you send it anywhere.

## The numbering change this board caused

This board is new work and took slot **11**. To make room:

- `videos/ai-training/11-design-md/` moved to **`videos/ai-training/13-design-md/`**. It
  went 11 -> 12 first, to free slot 11; then 12 -> 13 when **Claude PowerPoint landed on
  Day 12** from another branch mid-flight. Every "Day 11" inside it became "Day 13".
- **Day 10's beat 2 pointer chip was regenerated** to read "write the reference down once:
  Day 13, design.md", and Day 10's script, prompt and Resource Card were updated to match.
  The replacement string is the same length and the seed is unchanged, so Day 10's scene
  diff is exactly those two strings - **nothing moved, and a recorded Day 10 does not need
  re-recording.**
- **Claude PowerPoint is Day 12**, at `videos/ai-training/12-powerpoint/` - that move
  landed on main independently and this branch merged it rather than duplicating it.
  **Day 13 reuses the number of the retired day 13**, whose Dispatch content went to
  Day 8 beat 8: the number is free, the old content is not coming back.

## Where it sits, and what kind of board it is

**This is topic coverage, not an argument.** Day 10 is the argument about judgement
(reference beats adjectives, presentable is not correct). Day 13 is the plumbing
(design.md, design system, template). **Day 11 walks the actual jobs**, in the order the
sources cover them, built on one repeatable six-step loop.

The brief was explicit: *ignore anything already covered in the earlier Claude Design
boards, cover those as a brief reminder, and cover everything new from wireframing
onwards.* **Beat 1 is that reminder and it is 20 seconds** - four Day 10 chips, a forward
chip to Day 13, and a chip sending full on-brand decks to Day 12, Claude PowerPoint. That is not a breach of the precedence rule ("each Day covers its topic in full"):
the rule governs a Day's **own** subject, and this board's subject starts at beat 2.
Day 10's own beat 2 pointer to Day 13 is the standing precedent for a forward chip.
**Beat 1 must never grow into a re-teach.**

## Sources, and the hierarchy between them

Three sources, and they are **not** equal:

1. a **third-party video transcript** supplied with the brief;
2. a **third-party published playbook** of workflows, supplied as a second resource;
3. **Anthropic's own documentation** - the Claude Design announcement, *Get started with
   Claude Design*, *Set up your design system in Claude Design*, the *Claude Design admin
   guide for Team and Enterprise plans*, the product page, and the Claude Academy
   prototypes/UX and presentations tutorials.

**(3) outranks (1) and (2).** Where a third-party source asserts product surface the docs
do not carry, it goes on the Resource Card, attributed, never on the board. Both
third-party sources were **distilled in our own words** - no prompt templates, tables or
passages were carried across.

### What was taken, and where it landed

| From the sources | Where it landed |
|---|---|
| the six-step framework every workflow runs: prep input, start simple, review, refine global then local then global, ask Claude to review, export | **beat 2** - the spine, and the only numbered thing on the board |
| inline comments for targeted changes, chat for structural shifts | beat 2, as the "match the channel" row |
| a requirements document becomes clickable wireframes; it asks questions before it builds | beat 3 |
| prototyping live inside a meeting, so you leave with the prototype rather than the notes | beat 3 chip - not its own beat |
| handoff bundle: the design files, the conversation and a written brief, with a prompt for Claude Code | beat 4 |
| view / comment / edit share levels (docs) | beat 4 |
| the "does not look AI-generated" method: give it references, generate several directions, take the strongest parts of each, then build | **beat 5** - drawn UNNUMBERED, see below |
| "ask for two or three variations before committing" | beat 5, same idea |
| one input to one-pagers, roadmaps, landing pages, social templates | beat 6 |
| it renders with code, not an image model; you upload real images | beat 6, as the durable limit |
| motion graphics generated from a video transcript, edited in plain English | beat 7 |
| there is no native export for those - you screen-record the playback | beat 7 caveat, phrased as a mechanism |
| "ask Claude to review before exporting" - readability, hierarchy, contrast, accessibility | beat 8 setup |
| Academy: check empty, error and loading states and different data volumes; flag edge cases explicitly rather than relying on automatic detection | **beat 8, the catch** |
| the when-to-use-what comparison: production code, pixel-perfect design, final polish, full explainer videos | beat 9 |
| plans, beta status, the model, generation times, design-system setup detail, connectors, known issues | **Resource Card only** - version-specific |

### What was deliberately left out

- **Every plan, model and button.** Same filter as Day 13: the board names none of them,
  which is why it does not date. **Fix the card, not the board.**
- **"Go to another vendor's model for images."** That is one source's answer to the image
  limit. For a regulated pharmacy the routing decision belongs to the AI Use Policy, not
  to a training board, so beat 6 says "a real one, or one from a tool you are allowed to
  use" and names no third-party model.
- **Two claims still unverified** - a downloadable 3D-object file for a 3D printer, and a
  gallery of named templates on the home screen. Neither appears in Anthropic's
  documentation and the second source does not mention either. They are on the Resource
  Card, marked.

### One claim the second source resolved

The video transcript showed generated animations being **downloaded as an MP4**. The
playbook states plainly that there is **no native export** and that screen recording is
the workaround. **Treat the MP4 download claim as false.** The board carries the durable
half - *it plays in the browser, so you capture it off the screen* - which stays true even
if an export button ships; if one does, that is the line to revisit.

### Two facts the docs check corrected

1. **Claude Design is default ON for Team plans** and default off for Enterprise, with
   admins toggling it under Organization settings > Capabilities. **Phlo is on Team**, so
   this board does **not** use the Day 3 / Day 8 hedge ("you may not see this yet") - that
   hedge exists because memory and Cowork are off by default on Team. The honest line is
   "on unless an admin turned it off", and it is on the card.
2. **There is no separate Claude Design usage allowance.** It draws from the same pool as
   chat, Claude Code and Cowork. "It used to have its own meter" is history, not current
   behaviour.

## The beats

| # | accent | beat | what it carries |
|---|---|---|---|
| 1 | orange | you already have the habits | the brief reminder: four Day 10 chips, two forward chips. **20 seconds** |
| 2 | violet | the loop, six steps | the spine. **The only numbered process on the board** |
| 3 | blue | a spec in, wireframes out | it asks questions first; answer them. + prototype live in the meeting |
| 4 | teal | hand it to whoever builds it | the package: designs, conversation, written brief. View / comment / edit |
| 5 | indigo | explore before you commit | references, three directions, the best parts of each. **Unnumbered** |
| 6 | orange | one input, many outputs | short beat + the durable limit: it draws with code |
| 7 | yellow | motion graphics for video | transcript in, graphics out. **Fastest-dating line on the board** |
| 8 | **red** | **it checks its own work** | **adversarial: the failure AND the catch.** Demo badge |
| 9 | green | where it stops, and who owns it | four jobs that belong elsewhere, the human pass, the data rule |

Orange repeats on 1 and 6 and that is allowed - never on adjacent beats. **Green = the
human pass** is held constant across Day 10, Day 11 and Day 13 so the rule reads as the
same rule wherever a viewer meets it. There is deliberately **no second object-colour
system** here: Day 13 owns blue = design.md, green = design system, teal = template, and
beat 1 draws those three as neutral chips rather than re-using semantics out of context.

## One numbered process per board

The six-step loop is beat 2. **Beat 5's habit is a sequence in the source and is drawn
unnumbered on purpose** - two competing "the steps are" claims on one board is a
legibility failure, and what travels from beat 5 is the habit (explore three, then
combine), not the count. Do not number it in a later edit.

## The adversarial beat, written out

**The failure:** step 5 of the loop tells you to ask Claude to review its own work, and it
does that genuinely well - readability, hierarchy, contrast, accessibility. A second check
also runs that you never see, where it holds its output against your design system and
corrects it before you look. Both are worth having. **Neither is a second opinion**,
because it reviewed the screen it drew using the data it invented: three rows, three short
names, everything fits, because it chose what had to fit.

**The catch, as one falsifiable sentence:**

> *"show me this with no requests at all, one that was refused and forty rows - one name
> sixty characters long."*

Empty, refused and far too many. That is Anthropic's own design-review guidance (empty,
error and loading states, and data volumes; flag edge cases explicitly) written in the
shape Day 10's beat 6 established: a sentence you can hold the output against and answer
yes or no. **This beat is the Best Catch feeder, and the demo badge sits here** because
this is the payload - it is also fast and repeatable on camera, unlike a generation.

## The worked example

**One internal holiday-request tool**, carried across beats 2, 3, 4 and 8. Everyday
business, no Phlo branding, no patient or clinical detail. Beat 8's three states are
exactly the states beat 3's wireframe never drew, so the two beats are one story: the
shape you agreed, and the shape you never checked. **Change the tool and all four beats
move together** - it is pinned in `TOOL` and `CATCH` at the top of the build script.

## The safety call

Beat 9 carries the **only on-screen data-handling rule** on this board - a shared design is
a shared file; nothing confidential goes in; anything touching records keeps the human
gate. Same call Day 7 made with its Skill caution and Day 10 made with its beat 7 rule:
the beat count had no spare slot, but a mandatory course for a regulated pharmacy does not
push its data rule to a card.

## Runtime

Budgeted in **words** first this time, because budgeting in seconds is how Day 10 and the
first draft of this board both overran - then measured.

| section | words | on the clock |
|---|---|---|
| hook | 29 | 12s |
| why this matters | 54 | 22s |
| beat 1 · you already have the habits | 54 | 22s |
| beat 2 · the loop, six steps | 106 | 42s |
| beat 3 · a spec in, wireframes out | 90 | 36s |
| beat 4 · hand it to whoever builds it | 74 | 30s |
| beat 5 · explore before you commit | 93 | 37s |
| beat 6 · one input, many outputs | 76 | 30s |
| beat 7 · motion graphics for video | 84 | 34s |
| beat 8 · it checks its own work | 149 | 60s (+15s cut-away) |
| beat 9 · where it stops, and who owns it | 93 | 37s |
| pause and try | 32 | 13s |
| close | 33 | 13s |
| **total** | **967** | **~6 min 42** |

**The first draft measured 1,031 words / 6 min 52** and was trimmed. **Re-measure if you
rewrite:**

```bash
awk '/^## On-screen|^## Recording/{stop=1} stop{next}
     /^## [0-9]/{if(s)printf "%-44s %4d w ~%3ds\n",substr(s,4,40),w,int(w/2.5); s=$0; w=0; next}
     /^(>|`\[|\[|---|- |[0-9]\. )/{next} s{w+=NF; t+=NF}
     END{printf "%-44s %4d w ~%3ds\n",substr(s,4,40),w,int(w/2.5); \
         printf "\nTOTAL %d words = %d:%02d\n",t,int(t/2.5)/60,int(t/2.5)%60}' \
  videos/ai-training/11-design-workflows/claude-design-workflows-script.md
```

**Shorter cut: beats 4 and 6 are the droppable pair** - nothing later depends on either.
That removes ~60s and lands at **~5 min 42**. **Beat 8 is the one to protect.**

## Build and check

```bash
python3 videos/ai-training/11-design-workflows/build_design_workflows.py
/usr/bin/python3 preview.py videos/ai-training/11-design-workflows/claude-design-workflows.excalidraw out.png
/usr/bin/python3 preview.py <scene> out.png XMIN XMAX   # close-up on one beat
python3 build_all.py            # rebuild all + Style-B guard
```

`preview.py` needs the **system** Python (`/usr/bin/python3`) - Pillow is not installed
for Homebrew's interpreter. Beat *i* occupies x from `(i-1)*2000` to `(i-1)*2000 + 1200`.

**Last run:** 367 elements, 0 frames, 18000px wide, **0 collisions**; `build_all.py`
BUILD OK, GUARD PASS across every scene in the repo.

---

## The brief this board was built from

> Create an Excalidraw presentation similar to the ones already created, using the
> transcript from the YouTube video attached, but ignore anything already covered in the
> first Claude Design Excalidraw files. Cover those as a brief reminder, but cover all of
> the new things from wireframing onwards. Look at the Anthropic docs regarding all of
> these different aspects. Make sure everything is relevant and the latest information.

> Follow-up: create a new folder for the transcript of the video, and cover those exact
> topics in the format they have been covered. A second resource was supplied listing the
> topics to cover.

### Shared constraints, applied verbatim

**Build.** All changes go into a thin `build*.py` that does `from excalidraw_kit import *`,
defines the scene and beat scaffold (`OX` / `WID` / `ACCENT` / `beat_head`), and calls
`finish(out, max_w, total_w)`. Never hand-place elements in the `.excalidraw`. Never edit
`excalidraw_kit.py`. Copy `videos/claude/3-artefacts/build_excalidraw.py` as the scene
template. Set a deterministic `random.seed` (here: `110911`). Document the left-to-right
pan order in the module docstring.

**Beat count.** No fixed number - the board carries the beats its content needs. Runtime is
the real constraint: hard cap 8 minutes, target 4 to 6. Beats are not uniform (beat 8 runs
60s, beat 1 runs 22s). Budget in seconds, then check the beat count follows. One beat per
board is adversarial - how this capability fails silently and how you would catch it.
Always red. This is the Best Catch feeder.

**Style (Style B - the guard hard-fails on Style A).** No Excalidraw frame elements. No
boxes, no connector spine, no inter-beat arrows, no colour-band washes. White background.
Beats separated by whitespace only - the whitespace is the camera. Uniform slots, content
~1120 x 980, `GAP = 800`. All text in the Virgil hand font (fontFamily 1 / `HAND`),
roughness 1, lineHeight 1.4. Headings via the kit's `heading()` - no step-number circle, no
highlighter sweep, no sparkles. Body and explanation text stays ink or grey. Light rotation
jitter on notes and chips. Hand-drawn icons over emoji. Accents cycle violet / orange /
green / blue / red / teal / yellow / indigo; an accent may repeat on a longer board but
never on adjacent beats.

**Content.** Examples generic, not Phlo-specific. No Phlo branding or logo, no patient or
clinical specifics. Everyday business scenarios only; Phlo-native material appears only in
the live cut-away at the demo badge. Fictional identifiers only. Any clinical or dispensing
flow drawn anywhere must show the human verification gate: AI drafts, a human approves, the
record updates. Product proper nouns exact: Claude, Artifact, Project, Skill, MCP,
Connector, Cowork, Claude Desktop, Claude Tag, Dispatch. British English, hyphens not
em dashes, no Oxford commas.

**Demo cut-aways.** Marked with `demo_badge(x, y, "show in Claude desktop app: ...")` and
`[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` in the script.

**Deliverables.** (1) `build*.py` with the pan order in the docstring. (2) the regenerated
`.excalidraw`. (3) `preview.py` on the whole board plus a close-up per beat, with every
overflow and collision warning resolved or justified. (4) `build_all.py` clean against the
Style-B guard. (5) the `<slug>-script.md` narration - hook 10s, why 30s, content,
pause-and-try, close 15s. (6) this `<slug>-prompt.md`. (7) a Resource Card built with
everything displaced from the board.

**Curriculum.** `Phlo_Mandatory_AI_Course_Curriculum.docx` is the stated source of truth
for script blocks and is not in the repo. It was asked for; **there is no Day 11 entry**,
and the Day 10 / Day 13 precedent was used instead - a source note at the top of the script
and a "before publishing" header on the card.
