# Day 3 - Prompting & CRISPE Framework
### Production pack: Excalidraw board + narration script + demo steps

**Format:** one flowing Excalidraw board (`prompting-crispe-framework.excalidraw`) you pan across left-to-right and talk over, cutting to the live Claude desktop app at four points · ~10:40 Loom · British English · invented, generic examples (no Phlo branding, no patient or clinical data) · current to today.

**How to use this pack**
- Open `prompting-crispe-framework.excalidraw` full-screen and frame **one beat at a time** - the whitespace gaps are the camera moves. Pan left-to-right. Beat origins are at x = 0, 2000, 4000 … 30000.
- `[BEAT n]` maps **1:1** to board beat *n*. `[CUT TO CLAUDE DESKTOP]` / `[BACK TO BOARD]` mark the cut-away inside the beat it belongs to. There are four, on beats 2, 9, 10 and 12.
- Loom chapters: **Hook** (beat 1), **The craft** (beats 2-8), **Your setup** (beats 9-12), **Pause and try** (beat 16 opening), **Close** (beat 16).

> The single most important teaching in this video is beat 13: **memory doesn't retire CRISPE, it splits it.** Three dials get set once in the background; three stay yours to say every time - and the dials you can no longer see are the ones that bite. Don't let beat 13 get rushed; it's the beat that makes the other fifteen cohere.

> **Length note.** At ~10:40 this is long for a mandatory video. The board splits cleanly at the beat 8 / beat 9 boundary - beats 1-8 are "how to ask", beats 9-16 are "set it up once" - if you'd rather ship two parts. No board change needed; just record two passes and stop the first at x ≈ 15000.

---

## Section 2 - Narration script (~10:40)

Voice: warm, plain, a colleague who has done this a lot and is handing over the shortcuts. Not evangelical - the framing is "this is a craft with about six moving parts, and half of them you only set once."

**[BEAT 1] 0:00 - 0:35 (Hook - vague in, vague out)**
"Here's the most common prompt in the building: *can you help with this customer reply?* And here's what's wrong with it - nothing, except that it doesn't say who it's for, what 'help' means, or what a good answer would look like. So Claude fills in the gaps itself, generically, and you rewrite what comes back. That's not Claude being bad at its job. That's a prompt with three pieces missing. Over the next few minutes I'll show you which pieces, how to spot which one is missing when an answer feels off, and - the important bit - which of them you never have to type again."

**[BEAT 2] 0:35 - 1:15 (The same ask, rebuilt) → [CUT TO CLAUDE DESKTOP]**
"Same request, rebuilt. Three sticky notes. One: *context* - our Support team answers refund requests all day. Two: *the real ask* - rewrite this reply so it's warm but firm, and under 120 words. Three: *one example* - here's one that reads well. That's it. That's the minimum viable prompt, and it takes about fifteen seconds longer than the vague one. Notice there's no magic phrasing in there, no 'you are an expert' preamble. It's just the three things a new colleague would need before they could do the job. Let me fix the vague one live."

**[CUT TO CLAUDE DESKTOP] 1:15 - 1:45 (Demo 1 - see Section 3)**
Paste the vague prompt, show the generic answer, then rebuild it with the three parts and show the difference.

**[BACK TO BOARD] [BEAT 3] 1:45 - 2:30 (CRISPE)**
"Those three pieces are part of a longer list, and the list has a name: CRISPE. Six dials - Context, what's going on. Role, who Claude is. Instructions, what to do. Style, how it should read. Parameters, length, format, limits. And Example, one that looks right. Now, the reason these are dials and not boxes: nobody fills in all six. You turn up the ones this particular ask needs and leave the rest alone. It's a diagnostic, not a form. One small thing - if you go looking, you'll find other expansions of CRISPE online, Capacity and Insight and Statement. Same acronym, different framework. These six are ours, and they're the ones the rest of this video uses."

**[BEAT 4] 2:30 - 3:05 (Fault-finder)**
"Here's where the six dials earn their keep. When an answer comes back wrong, you usually can't say why - it's just *off*. The dials let you name it. Tone's wrong? That's Style - say how it should read. Too long, or the wrong format? That's Parameters - say how long, what format. The shape is wrong, it's a wall of prose when you wanted a table? That's Example - show it one that looks right. Three symptoms, three dials. And then there's a fourth fault that isn't a dial at all: the facts about *you* are wrong. That one lives in memory, and we'll come back to it - but the headline is that the fault is almost never 'Claude got it wrong'. It's a dial you didn't set, or one that got set wrong behind your back."

**[BEAT 5] 3:05 - 3:40 (Tell it why)**
"Now four habits that make everything above work better, and the first one is the biggest. Give the reason, not just the rule. Compare these. 'Never use ellipses' - fine, it'll obey. Versus: 'this will be read aloud by a text-to-speech engine, so never use ellipses; it won't know how to pronounce them.' Same rule. But only the second one lets Claude work out the cases you didn't think to list - the dashes, the abbreviations, everything else that engine will mangle. Anthropic's own framing is that Claude is a brilliant new colleague on their first day: capable, and with no idea how anything here works. And the golden rule that falls out of that - show your prompt to a colleague with no context. If they'd be confused, Claude will be too."

**[BEAT 6] 3:40 - 4:10 (Show, don't just tell)**
"Second habit: examples. Of everything in this video, examples are the single most reliable way to steer what comes back - format, tone, structure. Three to five is the sweet spot. Make them relevant, so they mirror the job you actually do. Make them diverse, or Claude picks up a quirk that only existed in your one sample and repeats it forever. And structure them - wrap each one in `<example>` tags, which sounds technical but is literally just typing angle brackets around it. And if you've only got one good example: paste it in, ask Claude to write three more like it, and keep the ones that fit."

**[BEAT 7] 4:10 - 4:40 (Say what to do)**
"Third habit, and it's the one people get backwards. Say what to *do*, not what not to do. 'Do not use markdown' leaves Claude guessing what you wanted instead. 'Write in smoothly flowing prose paragraphs' tells it. 'Don't write so much' - versus 'give me a high-level summary unless I ask for the detail.' And the same lever works upwards: 'create a dashboard' gets you a dashboard, but 'create a dashboard, include as many relevant features and interactions as possible, go beyond the basics' gets you a much better one. If you want above-and-beyond, ask for it. One last thing here - your prompt's style rubs off. Drop the markdown out of your prompt and you'll get less of it back."

**[BEAT 8] 4:40 - 5:15 (Paste first, ask last)**
"Fourth habit, for when you're working with a long document or several of them. Put the documents at the top of your prompt and your question at the very end. Not the other way round. It measurably improves the answer on long, multi-document pastes - on a one-line ask it makes no difference, so don't overthink it. And then the bit that matters most for us: ask for the quotes first. *Quote the lines that answer this, then answer using only those quotes.* You get an answer you can check, instead of one you have to take on trust - and for anything that has to be right, checkable beats confident every single time."

**[BEAT 9] 5:15 - 5:45 (Set once, never repeat) → [CUT TO CLAUDE DESKTOP]**
"Right - that's the craft. Now the half you only do once. Two settings that carry across every chat, so you stop retyping the same instructions. *Styles* control how Claude writes back to you - plain, formal, brief, whatever suits. *Preferences* are standing notes it applies to every conversation: your role, British English, keep it short. Set them once and you never type them again. Let me show you where they live."

**[CUT TO CLAUDE DESKTOP] 5:45 - 6:05 (Demo 2 - see Section 3)**
Set a Style, then add a generic preferences block. Point out "always on, every new chat".

**[BACK TO BOARD] [BEAT 10] 6:05 - 6:35 (Projects hold the context) → [CUT TO CLAUDE DESKTOP]**
"Next level up: Projects. A Project is a folder of chats with three things attached. *Project instructions* - who you are, how you want replies, the rules for this particular work, applied to every chat inside it. *Project knowledge* - the files Claude should always have to hand, so you stop re-attaching the same spreadsheet. And its own memory, which we'll come to in a second. The practice that matters: one Project per piece of work. Support replies. Ops reporting. One launch. Clean and contained beats one giant chat that slowly drifts."

**[CUT TO CLAUDE DESKTOP] 6:35 - 6:55 (Demo 3 - see Section 3)**
Open a generic Project; show its instructions field and its knowledge files.

**[BACK TO BOARD] [BEAT 11] 6:55 - 7:30 (It remembers you now)**
"And now the thing that has genuinely changed how this works. Claude can carry context between chats. Two features. *Memory* holds your role, how you like replies, and what you're working on, and brings it into new conversations - and you can say 'remember this' to save something on purpose. *Chat search* means you can ask 'what did we discuss about the refund wording?' and it goes and finds the conversation instead of you scrolling. Every Project keeps its own separate memory, so project context stays in the project and doesn't leak into your other chats. In CRISPE terms: this is the Context dial, filled in for you - which frees the prompt up for the actual ask. One caveat: on a Team plan an owner switches memory on. If it isn't in your Settings, that's why, not because you've missed a button."

**[BEAT 12] 7:30 - 8:10 (You stay in charge of it) → [CUT TO CLAUDE DESKTOP]**
"Everything it remembers is visible, editable and deletable. Settings, Memory, Topics - read any topic, edit it, delete it. *Pause memory* keeps what's there and stops adding more. *Reset memory* deletes the lot, and that one is permanent. Worth knowing: deleting a chat does *not* delete the memories it made - those you delete here. And if you want a conversation that's never saved or remembered at all, that's the ghost icon, top right: incognito. Now the rule, and this is the one to actually remember. Health and the other sensitive topics are left out of memory by default. Leave that setting alone. No patient details, and nothing confidential, goes into a chat that memory can keep - because a memory outlives the conversation that made it. Let me show you the panel."

**[CUT TO CLAUDE DESKTOP] 8:10 - 8:30 (Demo 4 - see Section 3)**
Open Settings → Memory → Topics; read one, edit one, delete one. Show the incognito ghost icon.

**[BACK TO BOARD] [BEAT 13] 8:30 - 9:05 (So does CRISPE still matter?)**
"So if Claude remembers who I am, is the framework redundant? No - and this is the most useful idea in the video. Memory doesn't retire CRISPE. It splits it. Three dials get set once, in the background: Context, Role and Style now live in memory, your Project instructions and your Style settings. You genuinely stop typing them. The other three stay yours, every single time: Instructions - what you want doing. Parameters - how long, what format. Example - what right looks like. Memory can't know what you want *this* output to be. So half the framework gets automated, and the other half is all yours, which makes it more worth learning, not less. And the sting in the tail: the dial you can no longer see is the one that bites. If memory holds something wrong about you, every answer quietly inherits it and nothing in the output tells you why. That's the fourth fault from beat 4. 'A diagnostic, not a form' - more true now than it was. The framework stopped being a thing you type and became a thing you check."

**[BEAT 14] 9:05 - 9:40 (How the sharp end works)**
"What do the heaviest Claude users actually do? Almost none of it is clever wording. A new chat per topic - start fresh when the answers start drifting, because a long conversation buries your original instructions. One Project per piece of work, so contexts stay clean. End a session with a handoff note saved into the Project, rather than keeping one endless thread alive. Prune memory - read Topics now and then and delete what's gone stale. Ask for the outcome you want, not the steps to get there. And stop over-engineering the prompt: shorter usually wins. The number that makes that concrete - Anthropic removed over eighty per cent of Claude Code's system prompt for the newest models and measured no loss. Long prompts are not better prompts. Less scaffolding, more curation."

**[BEAT 15] 9:40 - 10:10 (Different models, different habits)**
"Quick one, because the model you pick changes what comes back. Claude Opus 5 - answers run long, and it already checks its own work, so ask for brief and *don't* tell it to double-check itself; that makes it worse, not better. Claude Sonnet 5 - length tracks the task, and it reads you very literally, so spell out the scope: 'every section, not just the first.' Claude Fable 5 and Mythos 5 are built to run on their own for a long time, so ask them to back progress claims with evidence. And Claude Opus 4.8 reasons rather than reaching for tools, so say when you want it to search. Fair warning: these habits move with every new model. Check the docs rather than trusting this beat in a year."

**[BEAT 16] 10:10 - 10:40 (Capture by voice + pause and try + close)**
"Last one, and it's the cheapest win here. Talking is faster than typing, and a rambling spoken prompt still beats a vague written one - because when you talk you naturally give the context and the reason, the two things you skip when typing. So capture by voice on your phone, then shape it at your desk. The fastest prompt is usually the one you said out loud. **So - pause here, and do one thing.** Take a prompt you typed this week that gave you a mediocre answer, and add the two pieces it was missing: the reason you're asking, and one example of what good looks like. That's the whole video in one habit. And then, when you've got two minutes, go and read what Claude already remembers about you - Settings, Memory, Topics. See you in the next one."

---

## Section 3 - On-screen demo steps

Everything below is invented, generic content. No Phlo branding, no patient or confidential material, at any point. Use a sample Project and generic text throughout.

### Demo 1 - fix the prompt live (~30s, beat 2)

1. New chat. Type the vague version: `Can you help with this customer reply?` and paste a short, invented customer message about a delayed order. Let it answer. Point at how generic it is.
2. New chat. Type the rebuilt version:
   `Our Support team answers refund requests all day. Rewrite this reply so it's warm but firm, and under 120 words. Here's one that reads well: "Thanks for flagging this - you're right that it took too long, and I've refunded it today."`
   Paste the same invented message.
3. Put the two answers side by side. The teaching point is the fifteen seconds of extra typing, not the wording.

### Demo 2 - set a Style and preferences (~20s, beat 9)

1. **Settings → your profile → preferences.** Paste a generic block: `Reply in British English. I work in operations. Be concise, lead with the answer.` Save. Say "always on, every new chat".
2. Show the **Style** picker in a chat and switch between two styles on the same short question, so the difference is visible rather than described.

### Demo 3 - a Project's instructions and knowledge (~20s, beat 10)

1. Open a sample Project (invent one: *Supplier queries*). Show **project instructions** - a few lines of generic standing context.
2. Show **project knowledge** - one or two generic reference files. Say the line: "stop re-attaching the same spreadsheet".
3. Do **not** create a Project containing anything real on camera.

### Demo 4 - Settings → Memory → Topics (~20s, beat 12)

1. **Settings → Memory → Topics.** Read one topic aloud (make sure the account has only generic, invented topics before recording).
2. Edit one, then delete one. Show that it's plain text you control.
3. Point out **Pause memory** and **Reset memory** without clicking Reset.
4. Show the **incognito ghost icon**, top right, and open one incognito chat.

> Pre-record check: the demo account's memory must contain nothing real. Review **Topics** before you hit record - this is the one demo in the series where the panel itself is the thing on screen.

---

## Section 4 - Design rationale

- **House Style B**, built by `build_excalidraw.py` (imports the shared `excalidraw_kit`); re-run to regenerate. 16 beats, `random.seed(30330)`, 432 elements, 0 frames, 0 text collisions, Style-B guard clean.
- **Shape: craft, then setup, then synthesis.** Beats 1-8 are the craft (what you type). Beats 9-12 are the setup (what you stop typing). Beat 13 is the synthesis that ties the two halves together, and it's the beat the whole board exists to deliver. Beats 14-16 are practice, models and the close.
- **Beat 4 pays off twice** - once immediately as the diagnostic, and again at beat 13 when its fourth row (the fault that isn't a dial) turns out to be the memory failure mode. That's deliberate; don't cut the fourth row.
- **Power then control**, the house shape, applied twice: beats 9-11 are the power of persistent context, beat 12 is the control and the rule. Same shape as the Cowork and Chrome boards.
- **Verified behaviour** (Anthropic docs + support articles, checked at build time):
  - Memory: **Settings → Memory**, topics visible under **Topics**; *Pause memory* keeps existing entries, *Reset memory* is permanent; deleting a conversation does **not** remove memories generated from it.
  - Memory is **on by default for Free, Pro and Max**, and **off by default for Team and Enterprise** - an owner enables it org-wide. Phlo is on a Team plan, which is why beat 11 says so.
  - Health, race, ethnicity, religion, politics and gender identity are **excluded from memory by default**; there is an opt-in setting. Claude never saves government IDs, criminal history, financial account numbers or immigration status.
  - Each **Project** has its own separate memory space. **Chat search** is Pro/Max/Team/Enterprise. **Incognito** (ghost icon) is on all plans, but on Team/Enterprise incognito chats still appear in data exports and follow retention policy.
  - Per-model habits are from the per-model prompting pages: Opus 5 (longer default responses, self-verifies, can widen scope), Sonnet 5 (length tracks task, literal instruction following), Fable 5 / Mythos 5 (long autonomous runs, ground progress claims), Opus 4.8 (favours reasoning over tool calls, strong default house style).
- **Deliberately excluded, because this audience uses the Claude app and not the API:** `effort`, adaptive thinking, `budget_tokens`, `max_tokens`, prefill migration, computer-use toolsets, code-review harnesses, subagent caps, LaTeX. Also left off on purpose: "ask me questions before you execute" (contradicts beat 15's Opus 5 row) and "XML tags are obsolete" (contradicts Anthropic's own reference, which still says to wrap examples in `<example>` tags - beat 6).
- **The CRISPE acronym collision is called out on the board** (beat 3, grey line). Canonical CRISPE expands to Capacity/Role, Insight, Statement, Personality, Experiment. Ours is Context, Role, Instructions, Style, Parameters, Example. Anyone who googles it after watching would otherwise think the training is wrong.
- **Safety teaching is memory-specific**, not the generic house rule: a memory outlives the conversation that created it, so the usual "don't paste patient data" line needs the extra clause that deleting the chat doesn't undo it.
- **No dedicated pause-and-try beat on the board** - the house convention (see `3-artefacts` beat 9) is a beat of its own. Here it's spoken over beat 16 instead, to avoid a seventeenth slot. Say the word if you'd rather it were on the board.

## Resources to link under the video
- Anthropic - *Prompting best practices*: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic - *Use Claude's chat search and memory to build on previous context*: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- Anthropic - *Understanding Claude's personalization features*: https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- Anthropic - *What are projects?*: https://support.claude.com/en/articles/9517075-what-are-projects
- Per-model prompting guides: *Prompting Claude Opus 5*, *Prompting Claude Sonnet 5*, *Prompting Claude Fable 5*, *Prompting Claude Opus 4.8* (all under platform.claude.com/docs/en/build-with-claude/prompt-engineering/)
