# Resource Card - Day 10: design work with Claude

Paste this into the AI Ops Learn Resource Card for Day 10, alongside the Loom.

> **Three things to do before publishing this card.**
> 1. **There is no Day 10 entry in `Phlo_Mandatory_AI_Course_Curriculum.docx`**, and the
>    module-2.12 entry that exists describes the older Claude Design *product
>    walkthrough* rather than the design-practice video this now is - so the "Resources
>    linked from this video" list could not be lifted from it. The links below are
>    **named, not pasted** - put the current URLs in and check each one resolves before
>    the card goes live.
> 2. Everything under "The detail that did not fit on the board" is **product surface
>    that dates fast** - a research preview, its model and three plan rules. Re-check it
>    all against Claude before publishing, and again at each 90-day refresh.
> 3. The board deliberately names **no product, plan or model**, which is why it will
>    still be true when this card has gone stale. Keep it that way: if something here
>    changes, fix the card, not the board.

---

## What you are shipping today

**One design, iterated three times, with each change named.** That is the whole
assignment. Not a finished page - a draft plus three named corrections, so you can see
what changed and why.

**Pause-and-try:** find the adjective in your last brief and replace it with a reference.
Not a better adjective. A screenshot, a link, a page you already like.

## The one sentence to take away

**The advanced failure in design work is not a bad output. It is an acceptable one.**
Generic passes review. Nothing on the board matters more than that.

## The seven things from the video

1. **Blank page to worth-reacting-to.** The win is not a design you can ship, it is a
   design you can argue with. A draft you disagree with tells you what you actually
   wanted; a blank page tells you nothing.
2. **Reference beats adjectives.** "Clean and modern" is a phrase you both think you
   understand. Show it the thing you like - a screenshot, a link, last year's deck.
3. **Structure versus polish.** Settle the order of things while they are still cheap to
   move. Polish laid over the wrong structure is the most expensive work you can do.
4. **Iterate by talking to it.** You already know what is wrong with it. Say that, in the
   words you would use to a colleague - not by hunting for a control.
5. **In units, not wholesale.** Change one named element at a time. **Regenerate is not
   iterate**: a fresh roll of the dice can lose the parts you had already won.
6. **Presentable is not correct.** Three outputs can all look fine, be completely
   interchangeable and none of them be right. **Name what it has to get right before you
   look at it** - one sentence you can hold the output against. You will accept a
   presentable-but-wrong design if you are in a hurry.
7. **Human pass for brand-final.** Claude gets you a strong draft, fast. A person owns
   what actually goes out.

## The catch, written out

Beat 6 is the one to practise, because it is the failure you will not notice.

**Before** you generate anything, write one sentence naming what the design has to get
right. It must be **falsifiable by looking at the output**:

- Good: *"a first-time reader can see the price without scrolling"*
- Good: *"the one thing we want them to click is the most prominent thing on the page"*
- Useless: *"it looks professional"*, *"it feels on-brand"*, *"it's clean"*

Then hold each output against that sentence and answer yes or no. An output that looks
fine and fails the sentence is a **fail**, not a starting point. Three outputs that all
fail the same sentence are telling you the brief was wrong, not that you need a fourth.

## The safety rule, repeated

**Nothing confidential goes in.** No unapproved designs, no private codebase, nothing
patient-facing.

- Everything you put in a prompt or upload as a reference is content you are handing to a
  tool. Treat it the way you would treat a shared folder.
- Fictional placeholders only in any example: `Patient_001`, `J. Doe`, `NHS_TEST_123`,
  `acme.pharmacy@example.com`.
- **A design is never brand-final because Claude produced it.** A person does the last
  pass and owns what ships - and for anything patient-facing that pass is not optional.
- Any flow that touches prescriptions, dispensing or patient records keeps the human
  gate: **Claude drafts, a person approves, then the record is updated.**
- Check the Phlo AI Use Policy before anything made this way goes in front of a patient.

---

## The detail that did not fit on the board

The board was cut from nine product beats to seven practice beats. This is the product
surface that came off it. **All of it dates faster than anything on the board -
re-check before you rely on it.**

### Claude Design, the product

- An **Anthropic Labs research preview** - newer and rougher than the rest of the tools in
  this series. It has rough edges and it changes.
- Ran on a **current top-tier Claude model**, on the **Pro plan and above**, at the time
  the earlier version of this video was written. **Verify the model and the plan
  requirement before quoting either** - both have moved since.
- A design *partner*: you work with Claude to make polished visual things - designs,
  interactive prototypes, on-brand decks, one-pagers.

### Its signature: it learns your house style

A one-time onboarding where Claude reads your codebase and your design files and builds a
**design system** - your colours, type and components. Every project after that uses them
automatically, so output is on-brand by default rather than by copy-paste. This is the
thing a generic image generator cannot do.

**Do not point it at a real Phlo codebase or at confidential design files** - on camera
or otherwise - without approval. Use a generic or sample style.

### Where a design can start

- A text prompt.
- Uploaded images and documents (DOCX, PPTX, XLSX).
- Your codebase.
- Elements captured off a live website, so a prototype looks like the real product rather
  than a template.

### What you can get out

- **Interactive prototypes** you can share and user-test - no code review, no pull
  requests.
- **Feature flows** you sketch and then hand to Claude Code to build.
- **On-brand decks** exported to PPTX, or sent to Canva.
- **One-pagers** that make an idea look finished.

### Three flows, one per job

| Who | From | To |
|---|---|---|
| Designers | a static mockup | an interactive prototype to user-test |
| Product managers | a sketched feature flow | handed to Claude Code |
| Founders and account execs | a rough outline | a complete, on-brand deck |

**Every one of these is still governed by beats 6 and 7.** A prototype that looks
finished is exactly the artefact this video warns you about: presentable is not correct,
and nothing goes out without the human pass.

---

## Resources to link under the video

Paste the current URLs and check each resolves - and re-check that the first two still
describe a shipping product before linking them.

- Anthropic - *Introducing Claude Design by Anthropic Labs* (announcement)
- Claude support - *Get started with Claude Design*
- The Phlo AI Use Policy (internal)
- The board itself: `videos/ai-training/10-design/claude-design.excalidraw` - open it
  full-screen and pan beat to beat if you want the argument without the narration

## Related videos in the course

- **2.3 Artifacts** - where Claude makes a thing rather than describing one. Beat 1 here
  is the design-shaped version of that.
- **Day 12 - design.md** - the depth pass on the pointer in beat 2. Beat 2 says "show it
  the thing you like"; Day 12 writes that reference down as a file, builds a design system
  from it, and makes every later correction carry forward. **Watch Day 10 first, then
  Day 12.**
- **Day 8 - Cowork** - Day 10 sits after it on purpose. "Name the test before you look"
  is what catches a plausible result, and a long unsupervised run is where plausible
  results come from.
- **Day 3 - Prompting and CRISPE** - beat 2 of this board is the Example dial, applied to
  visual work: a reference *is* the example.
- **Day 7 - Skills** - if you find yourself typing the same three design corrections every
  week, they belong in a Skill.
