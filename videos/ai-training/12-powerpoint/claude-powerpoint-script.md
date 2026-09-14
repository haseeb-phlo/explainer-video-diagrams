# Day 12: Claude in Microsoft PowerPoint - narration script (Loom)

Board: `videos/ai-training/12-powerpoint/claude-powerpoint.excalidraw` (7 beats, one slot
each, `GAP = 800`). **Day 12** of the AI training series - it moved here from module 2.7.

> **Source note - read before recording.** `Phlo_Mandatory_AI_Course_Curriculum.docx` is
> the stated source of truth for script blocks and is **not in this repo**. There is **no
> Day 12 entry**, and the module-2.7 entry that does exist describes the Claude +
> PowerPoint **product walkthrough** this board replaces rather than the
> argument-construction video it now is. This narration was written from the brief in
> `claude-powerpoint-prompt.md`. **Reconcile it against the curriculum when a Day 12
> entry exists** - particularly the hook, the pause-and-try and the resource list.

> **What changed.** This was a nine-beat walkthrough of what Claude can do to a
> PowerPoint file. It is now a seven-beat argument about what a deck is *for*. The board
> names the tool in its title and its demo badge and nowhere else - no plan tier, no
> add-in, no file-size limit - so it stays true as the product moves. Everything that
> came off the board is on `claude-powerpoint-resource-card.md`.

> **Runtime, measured not asserted.** 844 spoken words = **5 min 37 at 150 wpm**, plus
> the ~15 seconds where the cut-away takes longer to *do* than to say: **~5 min 52**. Hard
> cap 8 minutes, target 4 to 6 - this sits inside target with 2 min 08 of headroom. The
> first draft measured 5 min 48 spoken and was trimmed to get here. Per-section word
> counts are in `claude-powerpoint-prompt.md`; **re-measure if you rewrite** - the command
> is there, and this repo's one recorded process lesson is that per-beat second budgets
> drift badly against written prose.

Cues:
- `[CAM]` - talking to camera, board not shared
- `[BOARD: beat N]` - share the Excalidraw board and pan to beat N
- `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` - the live cut-away, marked on the board
  with an orange demo badge on beat 7

Beat numbers match the build script's slot numbers and the sections below run in board
order, so you only ever pan **left to right**. Hold roughly 3 seconds of whitespace
between beats - the gap is the transition.

**If you need a shorter cut:** beats 4 and 5 are the droppable pair - nothing later
depends on either, and the argument still lands (tidy but empty → outline first →
headlines state positions → the plausible deck → build it live). That removes 55 measured
seconds and takes the video to **~4 min 57**.
**Beat 6 is the one to protect** - it is the whole reason this video exists, it is the
longest section on purpose, and everything else was trimmed to pay for it.

**Loom chapters:** Hook (0:00) · Why this matters (0:10) · Content (0:42) · Pause and try
(5:17) · Close (5:33). Beat 6 is the long one - 3:20 to 4:24.

---

## 0:00 - 0:10 · Hook [CAM]

Nobody said your last deck looked bad. That is not the same as saying it worked. The
failure here is a tidy deck that makes no argument.

## 0:10 - 0:42 · Why this one matters [CAM]

Most of us build a deck the same way: open the template, make slides, fill them in, and
the argument turns up around slide six - if at all. Claude will do all of that faster,
and it will format it better than you will.

That is the problem. Formatting is the part it is best at. Arguing is the part it will
skip unless you make it. So this one is not about slides. It is about making a case.

## 0:42 - 1:10 · It looks finished and says nothing [BOARD: beat 1]

Eight slides. Titles, bullets, a chart on every one. Nothing on there is wrong and
nothing on there needs fixing, which is exactly why it will sail through review.

Now go looking for the slide that says why any of it matters - the one that tells you
what to do about it. It is not there. It usually is not, because nobody was ever asked
for it.

**Formatted is not reasoned.**

## 1:10 - 1:42 · Structure first, slides second [BOARD: beat 2]

So do the structure first, in the chat, before anything gets designed.

Ask for an outline, not slides. Five lines here: unit cost rose nine per cent, two of
three suppliers missed SLA twice, absorbing it costs more by Q2, a re-tender takes eleven
weeks, and then the ask. That is the entire argument, and it took four minutes of typing.

Only *then* does it build the deck. **If the outline is wrong, every minute of design
after it is wasted.**

## 1:42 - 2:25 · One idea per slide, one line that carries it [BOARD: beat 3]

Then the bit that does most of the work: one idea to a slide, and one line that carries
it.

On the left, "Q3 results". That is a topic - a chapter heading. It commits to nothing,
and there is no way to disagree with it.

On the right, "margin fell because unit cost rose". Same slide, same chart. Now it is a
claim, and somebody can push back on it.

Do that to every headline. "Supplier review" becomes "two of three suppliers missed SLA
twice". "Next steps" becomes "re-tender now, or absorb it again". **If the headline could
be a chapter title, it is not doing any work.**

## 2:25 - 2:53 · Build it from a source [BOARD: beat 4]

And build it from a source, not from a sentence.

Give it the supplier report and last quarter's costs, and the outline that comes back is
grounded in those two files, line by line.

Ask it instead for "a deck about supplier costs" and you get the thing on the right:
plausible, generic, perfectly well made, and not about your numbers. **Feed it the
source, not a description of the source.**

## 2:53 - 3:20 · Design is not its strength [BOARD: beat 5]

An honest one. Design is not its strength.

It is good at the order things go in, one idea to a slide, the line that carries each
one, a first draft in minutes. What stays with you is the template, the brand colours,
and what "good" actually looks like here. It will follow a template you hand it. It will
not decide what your brand is. **Structure, not design.**

## 3:20 - 4:24 · The plausible deck [BOARD: beat 6]

Here is the failure you will not catch.

Three decks. Different structures, all well made, every one of them would pass a review.
Look at them and the only verdict available to you is "looks fine".

So stop looking. Read only the headlines, in order: Q3 results, Background, Our options,
Next steps. Four topics. That is not an argument, that is a table of contents - and it is
the same deck three times.

Here is the catch, and it goes *before* you build anything, not after. **Name the
decision you want, in one sentence.** Approve the re-tender of the packaging contract.
Write it down first, so that "looks fine" cannot be the verdict.

Now read those headlines again and ask whether a single one of them argues for that. Not
one does. All three decks fail the same test, having comfortably passed the eye test.

Claude will happily produce something nobody can disagree with. Nobody can agree with it
either.

## 4:24 - 5:17 · Outline to deck, live [BOARD: beat 7]

So: the outline first, agreed in the chat before a single slide exists. Then the deck
built from it, with every headline stating a position.

Let me do that live.

`[CUT TO CLAUDE DESKTOP]` - agree the outline in chat, then build the deck from it. Steps
are in the demo section below. ~15 seconds of doing.

`[BACK TO BOARD]`

One rule before it leaves your hands. Nothing confidential goes in a deck you are going
to send out, and do not build on a template or a file you do not trust - a file from
outside can carry instructions of its own.

**The argument is the deliverable.** The slides are just where it lives.

## 5:17 - 5:33 · Pause and try [CAM]

Pause here. Open the last deck you sent and rewrite three slide titles so each states a
claim rather than a topic. Three, not the whole deck. You will know within a minute
whether that deck ever had an argument in it.

## 5:33 - 5:47 · Close [CAM]

That is it. One deck, built from an outline you agreed first, with a headline on every
slide that takes a position. If you keep one thing from today: name the decision before
you build.

---

## On-screen demo steps

Everything below is invented, generic data. No patient information, no Phlo specifics, at
any point. The board marks this cut-away with the orange demo badge on **beat 7**.

### Demo - outline in chat, then the deck from it (~15s on camera)

1. In a new chat in **Claude Desktop**, paste a short block of plain notes - invent them
   on the spot, e.g. a fictional packaging-supplier review: unit cost up 9%, two of three
   suppliers missed SLA twice, a re-tender takes eleven weeks. Then type:
   > Before any slides: propose a five-line outline for a deck arguing that we should
   > re-tender the packaging contract. One claim per line, no topics.
2. Read the outline back on camera. Push on one line so they see it is negotiable:
   > Line 3 is a topic, not a claim. Rewrite it as a position.
3. Only now ask for the deck:
   > Build the deck from that outline. Every slide headline must state the position, not
   > name the topic.
4. Point at two headlines as it builds: "that is a claim, you can argue with that."

> Tip if the demo wobbles on camera: say the problem out loud in plain English ("slide
> four went back to being a topic") and ask again. Re-runs are cheap - keep talking.

## Recording notes

- Open the `.excalidraw` full-screen and frame **one beat at a time**; the whitespace
  between slots is the camera move. Pan strictly left to right.
- Beat 6 is the long hold. Do not rush the gap between "stop looking" and reading the
  headline strip - the pause is what makes the catch land.
- The red band on beat 7 is the only on-screen data rule in this video. Say it, do not
  skim it.
