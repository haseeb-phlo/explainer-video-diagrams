# Day 17 - That's the course - narration script

**Board:** `videos/ai-training/17-recap/claude-training-recap.excalidraw` (built by `build_recap.py`) · **9 beats**
**Audience: everyone.** This is the one board in the series written for the whole company again, deliberately - Day 15 was the specialist one.

**Measured: 981 words = ~6 min 32 board** (no cut-away; hard cap 8:00).

Re-measure after every edit. This repo's recorded lesson is that per-beat budgets drift by up to 2x, and it has bitten on Day 10, Day 14 and Day 15:

```bash
awk '/^## Narrat/,/^## Recording/' claude-training-recap-script.md | grep -vE '^(#|>|\*\*|\[|-)' | wc -w
```

> **No demo cut-away, deliberately.** Every other Day has one; this video teaches nothing new, so there is nothing to demonstrate. The actionable beat is 8, and those are things the viewer does afterwards.

---

## Narration

> **Voice:** warm, unhurried, and genuinely pleased. This is the one video in the series where you are not teaching - you are closing. Do not rush the congratulation and do not undercut it with a joke.

### [BEAT 1] 0:00 - 0:45 · green · *you got to the end*

"That's the course.

Eleven videos: prompting, Projects, Skills, Cowork, three on design, and four on the documents you already work in. You watched all of them.

That is not nothing. This was a mandatory course about a tool that changes every few months, and you sat through the awkward part - the one where you change how you work, rather than watch somebody else do it.

So, well done. Genuinely.

The next six minutes are the whole thing compressed: what you covered, the one idea underneath all of it, and three things to do this week."

### [BEAT 2] 0:45 - 1:40 · red · *one failure, eleven times*

"Here is the thing nobody says out loud until the end.

Every day of this course was pointed at the same failure. Not eleven risks - one risk, eleven costumes. A tidy deck that argues nothing. A clean layout that says nothing. A plausible figure where every cell checks out. A fluent rewrite that drops the clause you needed.

None of those are bad outputs, and that is the point. Nobody here was going to ship something obviously broken - you would have caught it. What gets through is well-made, plausible and empty, and it gets through because review checks whether it looks right. It does look right.

So one move sits underneath all eleven days: name what it has to get right, before you look at it. Everything else is a version of that sentence."

### [BEAT 3] 1:40 - 2:15 · violet · *the foundations*

"Days three and four were the foundations, and they pay you back daily.

Day three: prompting, and CRISPE - Context, Role, Instructions, Style, Parameters, Example. The short version: name the thing you want. 'Don't do X' just leaves it guessing.

Day four: Projects. Write the brief once, and every chat after it starts briefed instead of you retyping the background.

Day three teaches one good prompt. Day four is how you stop typing it again tomorrow. If nothing else survives, let it be those two."

### [BEAT 4] 2:15 - 2:50 · blue · *making it repeatable*

"Days seven and eight took that further.

Day seven: Skills. Procedure, not context. Write the steps down once, then - the bit people skip - test the Skill on a known input, where you already know the answer.

Day eight: Cowork. The brief is the whole job, because you are not in the room while it runs. Name the checkpoints before the run starts, not after it surprises you.

The order was deliberate: a Skill is what you should have written before handing the job to Cowork."

### [BEAT 5] 2:50 - 3:30 · teal · *the design days*

"Then three days on design.

Day ten was the argument: generic passes review. An acceptable design is more dangerous than a bad one, because a bad one gets sent back.

Day eleven was the work - one six-step loop, and the catch that it will happily review its own screen using data it invented. So make it draw the states it never drew: empty, refused, forty rows with a sixty-character name.

Day thirteen was the plumbing: three files before you prompt, and everything compounds - including the rule you got wrong."

### [BEAT 6] 3:30 - 4:10 · indigo · *the documents you already have*

"And three days on the files you actually open.

Day twelve, PowerPoint: structure first, slides second, and one line per slide that states a position rather than a topic.

Day fourteen, Word and PowerPoint: review as a diff. Revise, do not rewrite - a rewrite is fluent and it quietly drops the clause you needed.

Day fifteen, Excel, for the modellers: every row can be right and the answer still wrong. Reconcile a second, independent way.

And day sixteen, Outlook - the only one where the output leaves the building. A bad clause costs you a rewrite; an email that agrees to something costs you the thing it agreed to. So read only the sentences that commit you: a date, a number, an obligation.

Same failure, four surfaces - and all four pass a review that looks at the surface."

### [BEAT 7] 4:10 - 5:00 · orange · *your eleven catches*

"So here is the whole course on one page. One sentence from each day. If you screenshot anything today, screenshot this.

Name the thing you want. Write the brief once, in a Project. Test it on a known input. Name the checkpoints before the run. Name what it has to get right, first.

Make it draw the states it never drew. Read only the headlines, in order. Re-render a reference design after each change. Read the change as a diff. Reconcile a second, independent way. Read only the sentences that commit you.

Eleven catches, one shape: you decide what good looks like before you look at what it made. Afterwards is too late - afterwards you are just reacting to something plausible."

### [BEAT 8] 5:00 - 5:45 · yellow · *what to do this week*

"Three things you can do this week. Not all three - pick the one that matches your week.

One: build one Project for the job you do most. Twenty minutes, and day four walks you through it.

Two: take the explanation you have typed four times this month and turn it into one Skill. Then test it on a known input and see what it left out.

Three: take something you already shipped, name the test it should have passed, and run that test on it. That is the whole course in five minutes, and it is the one that changes people's minds.

If you only do one, do the first."

### [BEAT 9] 5:45 - 6:15 · green · *and after that*

"What good looks like in ninety days is modest. You stop retyping context, because it lives in a Project. You name the test before you look at the output. And 'it looks fine' stops counting as a review.

And you still sign it off. Claude drafts, a person approves, the record updates. That did not change here and it is not going to.

One last rule, and it outlives everything else here: no patient data, no confidential data, and nothing you would not put in an email to somebody outside Phlo. That holds whichever tool you are using.

Eleven days. One habit. Name the test before you look.

Thanks for sticking with it."

---

## Recording notes

- **No cut-away.** Board only, start to finish. Pan left to right, one beat at a time.
- **Beat 1 is the congratulation - slow down.** It is the only warm beat in the series and the temptation is to rush it to get to the content. Do not.
- **Beat 7 is the screenshot.** Hold on it a beat longer than feels natural, and say so on camera ("screenshot this one"). Frame it so all ten rows are in shot - it is the one slot that is 1600 wide.
- **Beat 9's red rule is the last thing anyone hears about data handling in this course.** Read it as written; do not ad-lib around it.
- If a day gets rebuilt **or a new one lands**, beats 3 to 7, this script and the card all need the change. This board was built as Day 16 and renumbered to 17 mid-build when Claude in Outlook shipped - and had to absorb it. **Check `videos/ai-training/` against the board before recording.** The catches on beat 7 are quoted from the day boards, not paraphrased.

## Ships

Nothing to ship. The viewer picks one of the three items on beat 8.

## Pause-and-try

Beat 8, item one: build one Project for the job you do most. Twenty minutes.
