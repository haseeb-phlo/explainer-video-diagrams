# Claude Projects - narration script (~12 minutes, Loom)

Board: `phlo-2.2-claude-projects.excalidraw` (16 beats, one slot each, `GAP = 800`).

Beats 10 and 12 are the plan / sharing mechanics. If you need a shorter cut for
an all-staff audience, those two are the ones to drop - nothing later depends on
them.

Cues:
- `[CAM]` - talking to camera, board not shared
- `[BOARD: beat N]` - share the Excalidraw board and pan to beat N
- `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` - the live cut-aways, marked on the
  board with an orange demo badge

Beat numbers match the build script's slot numbers, and the sections below run in
board order, so you only ever pan **left to right**. Hold roughly 3 seconds of
whitespace between beats - the gap is the transition.

---

## 0:00 - 0:12 · Hook [CAM]

If you're still pasting the same instructions into Claude every morning, this video
saves you about an hour a week for the rest of your career. Set up once, use forever.
Let me show you Projects.

## 0:12 - 0:55 · The problem [BOARD: beat 1 - The tax you pay every morning]

Here's the thing nobody clocks. Every time you open a fresh chat, you re-explain
yourself. Who you are, your role, how your team sounds, the things you never say. Then
you ask your actual question. That's maybe ten minutes a day of just setting the scene -
and you do it again tomorrow, and the day after. Call it an hour a week, every week,
forever. It's invisible, so it never lands on a to-do list. Projects delete that hour.

## 0:55 - 1:35 · Every chat starts from zero [BOARD: beat 2]

Look at what's actually happening in the chat window. Monday, you paste in the team tone
guide, then ask for a reply. Wednesday, new chat, you paste the same tone guide in again,
then ask for a rewrite. Friday, same thing. Three pastes of the identical document, and
they're not even tidy - it's whatever survived the clipboard that morning.

That's not Claude being forgetful. A new chat genuinely starts from zero every time; it
has no memory of yesterday's brief. So the context you need lives in your clipboard,
and it gets re-typed, re-found and re-pasted for as long as you keep working this way.

## 1:35 - 2:45 · Every chat starts briefed [BOARD: beat 3]

Now the same week with a Project. The tone guide, the example replies, the do-not-say
list - they go into the Project once. One arrow. From then on, every fresh chat you
start inside that Project is already briefed before you type a word.

Same ask - "draft a reply, order's late" - and what comes back is warm, clear and on
brand the first time, and every time after that. Nothing pasted.

`[CUT TO CLAUDE DESKTOP]` - demo badge: *show in Claude desktop app: build the Project live*

Let me show you how little there is to this. New Project, name it "Customer replies".
Custom instructions - the standing brief. Two or three files dropped in. That's the whole
setup, and I've done it in under a minute. Now watch: brand-new chat, inside the Project,
and it already sounds right.

`[BACK TO BOARD]`

That's the entire idea. Everything after this is detail.

## 2:45 - 3:30 · What a Project is [BOARD: beat 4]

A Project is a permanent space in Claude built from three parts. First, custom
instructions - your standing brief. Your role, your house voice, what to avoid. Written
once. Second, knowledge files - reference material Claude reads before it answers
anything: a style guide, examples, a template. And third, the conversations themselves.
Here's the part that matters: every chat you start inside the Project automatically
inherits the instructions and the files. You never paste them again. The context lives in
the Project, not in your clipboard.

## 3:30 - 4:00 · The shift [BOARD: beat 5]

So the whole shift is this. Before: paste context every time, hope you remembered all of
it. After: context is permanent, applied to every chat without you lifting a finger. You
write the brief once, and Claude uses it every single time.

## 4:00 - 4:45 · The instructions field [BOARD: beat 6]

If you only get one thing right, get this one right. Open the Project out and most of
what's inside is reference material - the tone guide, the examples, the do-not-say list,
the past conversations. Useful, but passive.

The custom instructions field is different. It's the part Claude reads before every
single answer, so it shapes all of them. It is, by a distance, the highest-leverage
square inch in the whole product. Four lines in there - who you are, your house voice,
what never to say, British English - will do more for your output than another ten files.
Spend your twenty minutes here.

## 4:45 - 5:35 · Write it like you mean it [BOARD: beat 7]

So how do you write four good lines? The same way you would write anything someone has
to act on: make it checkable. "Be professional" is not an instruction - nobody can tell
whether it was followed. "Warm, plain English, no jargon, under 120 words" is. "Follow
our format" tells Claude nothing; "greeting, answer, next step, sign-off, in that order"
tells it everything.

Four rules and you are done. Specific beats vague - write what you could check. Short
beats long, because this is read before every single answer. Give it structure, headings
and bullets, not one long paragraph. And keep it consistent: two rules that contradict
each other means Claude picks one at random, and you will never work out why.

The trigger for adding a line is simple - if you have re-explained something twice, it
belongs in the instructions.

And for the engineers watching: this is exactly the job a CLAUDE.md file does in Claude
Code. You write the standing rules, Claude keeps its own notes alongside them, and the
same discipline applies - specific, short, no contradictions. Link is at the end.

## 5:35 - 6:30 · Three examples [BOARD: beat 8]

What does that look like on your team? Three real examples. One - "customer reply
drafting": your house tone guide, a set of genuinely good replies, and the do-not-say
list; Support and Ops live in it. Two - "Engineering PR review": our coding standards,
the review patterns that come up again and again, and the team style guide. Three -
"Weekly board prep": the board memo format, the last four memos so the structure stays
consistent, and the questions the board actually cares about. Different teams, same
pattern - the context that makes the work good, captured once.

Note the red bar on the first one: Claude drafts, a person checks and sends. Nothing goes
out on its own.

## 6:30 - 7:00 · The maths [BOARD: beat 9]

Quick maths. Setup is about twenty minutes, once. The saving is hours a week, for as long
as you do the job. That's the best twenty minutes you'll spend this month.

## 7:00 - 7:45 · What you get on your plan [BOARD: beat 10]

Two practical questions before you go and build one.

First, do you have this? Yes. Projects are on every plan, including free - free accounts
just cap out at five of them. On Pro, Max, Team and Enterprise, make as many as you like.

Second, how much can you put in one? More than you think. As a knowledge base gets close
to the context limit, Claude switches to retrieval on its own - pulling in the relevant
parts rather than everything - which stretches capacity by up to ten times while keeping
the answers as good. That happens automatically, on paid plans; you don't configure
anything. So don't ration your files.

## 7:45 - 8:10 · Why it's a multiplier [BOARD: beat 11]

And it gets better, because Projects are shareable. One person builds Customer Replies
properly, and the whole support team drafts in your house voice from day one - nobody
else has to figure it out. That's why this is a multiplier and not just a personal
tidy-up. Sharing's available on our Team and Enterprise plans.

## 8:10 - 8:55 · Sharing, and who can do what [BOARD: beat 12]

Worth knowing how that actually works, because you get to choose. There are two levels.
"Can view" means someone can read what's in the Project and chat in it, but not change
it - that's what you want for most of the team. "Can edit" means they can rewrite the
instructions and add or remove files - keep that to the one or two people who own it.

You can share with one person, add people in bulk, or make it visible to the whole
organisation. Whoever you share with gets an email and finds it under "Shared with me".
Two caveats: sharing is Team and Enterprise only, and an admin can switch
organisation-wide sharing off, so if you can't see that option, that's why.

## 8:55 - 10:15 · Build one, properly [BOARD: beat 13]

Three steps, and you've seen them all already. Name it and set who can see it. Write the
custom instructions. Add two or three reference files, then chat.

`[CUT TO CLAUDE DESKTOP]` - demo badge: *show in Claude desktop app: building a Customer
Replies Project*

Back in the app, and this time slowly. I go to claude.ai/projects, click New Project, and
name it. Notice Claude can't see the name or description - that's just for us. If you're
on our Team plan you'll also choose who can see it; I'll set this so the support team can
use it.

Now the custom instructions - the standing brief. Something like: "You help the support
team draft replies to customers. Use our house tone: warm, clear, human, never cold. Keep
replies short. Never give advice that should come from a specialist - flag it instead.
Use British English." That's the bit you'd otherwise type every morning.

Then knowledge files, on the right. I'll add our tone guide, a handful of example replies
we're proud of, and the do-not-say list. One sensible habit: keep these examples
anonymised - no confidential detail in the files.

Now I just chat. "Draft a reply to a customer asking why their order is delayed." And look
- it already sounds like your team, because the brief and the examples are doing the work.
Here's the magic: I'll open a brand-new chat inside the same Project and ask something
completely different. Same voice, same rules, no pasting. That's the unlock.

`[BACK TO BOARD]`

## 10:15 - 10:40 · Pause and try [BOARD: beat 14]

Your turn. Pause the video right here. Think of one task you repeat - drafting, reviewing,
summarising, anything. Open claude.ai/projects and create it now, even if it's empty. Then
fill it in as you watch the rest of this module. Go.

## 10:40 - 11:15 · Slow vs live [BOARD: beat 15]

One thing to be clear about, so you don't get disappointed. A Project holds slow-changing
material: the tone guide, the templates, the standards - things that change monthly, not
hourly. Drop those in once and forget about them.

What it doesn't hold is live data. Stock levels, tickets, today's numbers - anything like
that is stale the moment you paste it. That's a Connector's job, not a Project's, and
it's the next video in this module. Projects give Claude your standards; Connectors give
it today's numbers.

## 11:15 - 11:40 · Resources [BOARD: beat 16]

Three things to take away. Anthropic's Help Centre has a short guide - search "How can I
create and manage projects" on support.claude.com. In the AI training series, the Prompt
Library holds the team's shared Projects, so check there before you build from scratch -
someone may have started yours already. And if you write code, the same idea in Claude
Code is documented at code.claude.com/docs/en/memory.

And the rule of thumb that's on the board: third paste of the week, it wants a Project.

## 11:40 - 11:55 · Close [CAM]

One Project. Twenty minutes. Use it once a day for a month. Then tell me Projects didn't
change how you work.
