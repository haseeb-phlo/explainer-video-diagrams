# Day 8: Cowork - narration script (~7 min 30, Loom)

Board: `videos/ai-training/8-cowork/claude-cowork.excalidraw` (9 beats, one slot each, `GAP = 800`).

> **Source note.** There is no Day 8 entry in `Phlo_Mandatory_AI_Course_Curriculum.docx`
> to lift the script blocks from - the day-by-day series is newer than the docx, and the
> Dispatch day this one absorbs has been retired. This narration was written from the
> Day 8 brief in `claude-cowork-prompt.md`. **Reconcile it against the curriculum when a
> Day 8 entry exists**, particularly the hook, the pause-and-try and the resource list.

> **Two claims on this board date faster than anything else in the repo** - the plan
> availability on beats 7 and 8. Re-check both against Claude before you record. See
> "Facts to re-check before recording" at the bottom.

Cues:
- `[CAM]` - talking to camera, board not shared
- `[BOARD: beat N]` - share the Excalidraw board and pan to beat N
- `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` - the live cut-away, marked on the board
  with an orange demo badge on beat 4

Beat numbers match the build script's slot numbers and the sections below run in board
order, so you only ever pan **left to right**. Hold roughly 3 seconds of whitespace
between beats - the gap is the transition.

**If you need a shorter cut:** beats 7 and 8 are the droppable pair - the built-in
browser and Dispatch are both product surface, and nothing after them depends on either.
That takes the video to about 6 minutes 20.

**Loom chapters:** Hook (0:00) · Content (0:42) · Pause and try (6:56) · Close (7:16)

---

## 0:00 - 0:12 · Hook [CAM]

Everything in this course so far has been a conversation. You ask, Claude answers, you
look at it, you ask again. Today is the first time you hand over a shift and walk away.
That changes what your job is while it runs.

## 0:12 - 0:42 · Why this one matters [CAM]

Cowork is the expensive rung on the ladder. Not expensive in money - expensive in what
it costs you when it goes wrong, because it goes wrong quietly and at the end.

In chat you supervise turn by turn, so a mistake surfaces immediately and costs you one
correction. In a run, nobody is watching turn three, so a mistake at turn three arrives
an hour later baked into everything after it. Same model, same intelligence, completely
different supervision job. That is the whole of today.

## 0:42 - 1:22 · A conversation versus a shift [BOARD: beat 1]

Left-hand side, chat. You ask for a reply to be reworded. A draft comes back. You say
shorter and warmer. A better draft comes back. Four turns, four ticks - you read every
one of them. That is what makes chat safe: you are the checkpoint, every single turn.

Right-hand side, Cowork. One brief: reconcile these two lists and write up the gaps. And
then nine steps.

Now be honest about the next bit, because everybody does it. You watch step one. You
watch step two. Somewhere around step three you think "this is going fine", and you go
and do something else. That is not laziness, that is the entire point of handing work
over - if you watched all nine you would have been quicker doing it yourself.

So the supervision has to move. It cannot be per turn any more. It has to go into the
brief at the start and into the checkpoints in the middle.

## 1:22 - 2:02 · The brief is the whole job [BOARD: beat 2]

Top row: a thin brief. "Tidy up the reports." Watch the steps - they start on the line
and they wander off it, further each time, because every step has to guess a bit more
than the last one. And you find out at the very end, when a document arrives that is
not what you meant.

Bottom row: same work, specified. The folder, the columns, what to skip, when to stop
and ask me. Four sentences. The steps stay on the line, and what comes back is something
you can actually check.

Here is the thing to take away. In chat, the brief is an opening move - you correct on
the next turn. In a run there is no next turn. The brief is the only steering you get,
so it has to carry the whole job.

## 2:02 - 2:40 · What a brief must name [BOARD: beat 3]

Four things. Name them, or Claude will name them for you, nine times over, on its own,
while you are not looking.

One, the inputs. Which folder, which files, and which list wins when the two of them
disagree.

Two, the output shape. One page. A table with these four columns, in this order. If you
do not say, you get whatever it felt like.

Three, what a gap means. A file is missing - do you skip it and list it at the end, or
do you stop? Say it. Never leave "guess the number" as an available option.

Four, when to stop and ask. Anything that changes a number. Anything that leaves the
folder.

That is four sentences. It is the difference between a run you can check and a run you
end up doing again yourself.

## 2:40 - 3:10 · Checkpoints, applied [BOARD: beat 4]

You met these three stops on the autonomy ladder. Here they are against real files.

One, before the first write. It has read everything, it understands the job, and it is
about to change a file. That is the moment.

Two, at the join. When the branches come back together and become one answer - and we
will see why that matters in two beats' time.

Three, before it leaves the folder. The output is about to go to a person, a channel or
a system. Anything that leaves is a stop.

Cowork has a setting for this. Manual means it pauses and asks. Auto means it keeps
going. Skip means nothing checks its actions at all - do not use Skip for anything that
matters. And name the stops in the brief before the run starts, not after it has
surprised you.

Let me show you one.

## [CUT TO CLAUDE DESKTOP] 3:10 - 3:50 · Demo (see "On-screen demo steps")

Run a real multi-file task in **Manual**, and stop it at the first checkpoint.

## [BACK TO BOARD] 3:50 - 4:26 · It splits the work [BOARD: beat 5]

One more thing that makes a run different from a chat: it does not do the steps in a
line. It splits them.

One brief becomes several workers running at the same time - sub-agents, each with its
own context. One reads the folder. One checks the numbers. One drafts the write-up. One
goes looking for what is missing. Then it all comes back to the join, and the join is
what you get.

Which tells you where to put your attention. You review the join, not each branch. The
branches are the fast part. The join is where the mistakes meet.

## 4:26 - 5:08 · Long runs hide their mistakes [BOARD: beat 6]

Now the beat I would most like you to remember.

Step two makes one wrong assumption. Nothing crashes. Nothing goes red. Step three takes
step two's answer and does perfectly correct work on it. So does four. So does five. All
the way to nine.

Read that line: each step is right, given the one before it. Every individual step
passes. The output is internally consistent. It is also wrong, and has been since step
two.

So look at what actually arrives. It reads well - tick. It adds up - tick. It has been
wrong since step two, and neither of the first two ticks would ever have caught that.
This is the failure mode of long runs, and it is not a failure of intelligence. A better
model makes a more convincing version of the same document.

The fix is a checkpoint at step two. That is it. That is why the last three beats have
all been about the same thing.

## 5:08 - 5:44 · It has its own browser [BOARD: beat 7]

Something practical. When a step in the run needs a website, Claude does not stop and
ask you to go and get it. A browser opens in the side panel and it works the page
itself - reads it, fills the form, clicks the button. No extension, no setup, and
nothing shared from your own browser unless you choose to share it. It asks before it
acts on a new site.

Two things to hold onto. A web page can carry instructions written at Claude rather than
at you, and Claude is reading that page. And anything you sign it into stays available
to it in later runs - so do not sign it into anything you would not hand someone the
keys to.

And to head off the question: computer use, where Claude clicks around your actual
screen, is a wider and separate thing. It is in beta, it is Pro and Max only, and it is
not on Team or Enterprise. Different feature, not today's lesson.

## 5:44 - 6:20 · Start it from your phone [BOARD: beat 8]

This one is called Dispatch. You send the brief from your phone - "sort the invoices
folder" - the run happens on your desktop, and the answer comes back to your phone. It
is one conversation, synced across both, not two separate chats.

Two honest caveats, because they change whether this is useful to you. It runs on your
own machine, not in a cloud - so the desktop has to be awake with Claude Desktop open
while it works. And it is a limited beta on Pro and Max, so you may well not see it on a
Team plan yet.

The reason it is on this board anyway is the bit at the end: it pings you when it wants
a yes. That is a checkpoint arriving on your phone. Same discipline, smaller screen.

## 6:20 - 6:56 · What belongs here [BOARD: beat 9]

So what actually belongs in Cowork?

Hand it over when it is many files, and the real work is the moving between them. When
it is repeatable, because you will run it again next month. And when it survives a
second pass - run it twice, get the same answer.

Keep it in chat when you cannot check it. If you cannot verify the output, you cannot
hand it over - you are just choosing not to look. And keep it in chat if it is
patient-facing without a gate. Anything touching prescriptions, dispensing or patient
records keeps the human gate: Claude drafts, a person approves, then the record updates.
That is not negotiable, and a long unattended run is exactly the wrong shape for it.

The test is not "can Claude do it". The test is "can I check it when it comes back".

## 6:56 - 7:16 · Pause and try [BOARD: beat 9, hold]

Pause here.

Write the brief for one task you would actually hand over. Then read it back and find
the sentence doing no work - the one that sounds professional and tells Claude nothing.
Delete it, and replace it with one of the four from beat three. Usually it is "when to
stop and ask", because that is the one nobody writes.

## 7:16 - 7:31 · Close [CAM]

What you are shipping today: one multi-step task handed to Cowork, with its checkpoints
named before it runs. Not after.

Chat you supervise turn by turn. A run you supervise twice - once in the brief, and once
at the stops you chose. Get those two right and the rest of it genuinely does work while
you are somewhere else. Resource Card below. See you tomorrow.

---

## On-screen demo steps

Everything below is invented, generic content in a **dedicated demo folder**. No patient
information, no Phlo systems, no real confidential files, at any point.

### Demo - a multi-file task, stopped at the first checkpoint (~40s)

1. Beforehand: make a throwaway folder (e.g. `~/cowork-demo`) with four or five short
   invented files - fictional weekly notes from different teams, and one deliberately
   missing a figure so a checkpoint has something to fire on.
2. In the **Claude desktop app**, start a Cowork task and give it access to **just that
   folder**. Narrate: "scoped to one folder, nothing else."
3. Set the permission mode to **Manual** on camera. This is the point of the demo - say
   out loud that Manual means it pauses and asks.
4. Give it a brief that names all four things from beat 3, out loud as you type:
   `Read every file in this folder and produce one combined summary as a table with
   Team, Theme, Decision and Open question. If a file is missing a figure, skip it and
   list it at the end - do not estimate. Stop and ask me before you write anything to
   disk.`
5. Let it run. **Stop at the first approval prompt** and read it on camera: "here is the
   checkpoint - this is the bit I actually do."
6. Approve it, let it finish, then read the output before saying anything about it.
   Switch back to the board.

> Keep it to the scoped demo folder with invented content - the scoping *is* half the
> safety message and Manual mode is the other half. Never grant whole-disk access, and
> never demo on real confidential files.

---

## Facts to re-check before recording

These date fastest. Re-check them in this order, and again at each 90-day refresh.

| Beat | Claim on the board | Source |
|---|---|---|
| 4 | Permission modes are **Manual / Auto / Skip** | Get started with Claude Cowork |
| 7 | Built-in browser: Pro, Max, Team, Enterprise where enabled. On by default on Team as it rolls out; an Owner controls it at **Organization settings → Cowork → Built-in browser** | Use the built-in browser in Claude Cowork; Set up browser use for Team and Enterprise |
| 7 | Computer use is **beta, Pro and Max only, not Team or Enterprise** | Let Claude use your computer in Cowork |
| 8 | Dispatch is a **limited beta on Pro and Max**, runs **on your desktop** (awake, Claude Desktop open), one synced conversation | Assign tasks from anywhere in Claude Cowork |

The brief this board was built from described computer use as a "research preview" and
said Dispatch work continues "on the desktop or in the cloud". Both were corrected
against the docs above - see `claude-cowork-prompt.md`. If you re-record from the brief
rather than from this script, do not let either claim back in.
