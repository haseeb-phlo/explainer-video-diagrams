# Video 2.13 - ChatGPT -> Claude: switching over without starting over
### Production pack: Excalidraw board + narration script + demo steps

**Format:** one flowing Excalidraw board (`chatgpt-to-claude.excalidraw`) you pan across left-to-right and talk over, cutting to live Claude between beats · ~5:30 Loom · British English · invented, generic examples (no Phlo branding, no patient or clinical data) · current to today.

**How to use this pack**
- Open `chatgpt-to-claude.excalidraw` full-screen and frame **one beat at a time** - the whitespace gaps are the camera moves. Pan left-to-right, ~3-4s of narration per beat.
- `[BEAT n]` maps **1:1** to board beat *n*. `[CUT TO CLAUDE]` / `[BACK TO BOARD]` mark the cut-away inside the beat it belongs to.
- The board is the **conceptual overview**. The companion `migration-playbook.md` is the **exhaustive step-by-step** - tell viewers it's linked below the video and is the thing to keep open in a second window while they actually do the move.

> The single most important teaching in this video is beat 9: **a switch is a filter, not a bulk copy.** For a regulated pharmacy, "review and leave behind" is the load-bearing safety point - don't let it get rushed at the end.

---

## Section 2 - Narration script (~5:30)

Voice: warm, plain, a colleague who's already done the move and is saving you the faff. Reassuring - the headline is "you won't lose anything".

**[BEAT 1] 0:00 - 0:30 (Hook - switching, not starting over)**
"If you're moving from ChatGPT to Claude, here's the good news up front: you're switching, not starting over. Almost everything you set up in ChatGPT - your instructions, the things it remembers about you, your custom GPTs, the chats you go back to - has a home in Claude. You move it across; you don't rebuild it from nothing. It's about a couple of hours, and it's mostly copy-and-paste - no technical work. Let me show you exactly what goes where."

**[BEAT 2] 0:30 - 1:10 (The translation map - signature)**
"The whole trick is learning the new names, because every ChatGPT feature has a Claude equivalent. Your *custom instructions* become Claude's *profile preferences*. *Memory* is *memory* - Claude has it built in. ChatGPT *Projects*, the folders of chats, become Claude *Projects*. A *custom GPT* splits into a *Project* plus a *Skill*. *Plugins and Actions* reconnect as *Connectors*. And *Tasks* - scheduled prompts - become Claude's *scheduled tasks*. Learn those six pairs and the move is mostly mechanical. The full table's in the playbook linked below - this is the shape of it."

**[BEAT 3] 1:10 - 1:50 (Inventory - gather first)**
"Before you move a single thing, make a quick list of what's actually worth keeping. Honestly, most of a clean switch is this step. Five things to gather: one, your custom instructions - that global 'how to answer me' text. Two, your saved memory - the facts ChatGPT has learned about you. Three, each custom GPT - its name, its instructions, and any files you uploaded to it. Four, your projects or folders - grouped chats with shared files. And five, the handful of chats you genuinely go back to. Not all of them - the ones you reuse."

**[BEAT 4] 1:50 - 2:35 (Export your ChatGPT data)**
"Now, the export. In ChatGPT: Settings, then Data Controls, then Export data. You'll get an email with a link to a zip file - your chats as a data file, plus a readable web page. But - and this matters - the export does *not* include two things. It doesn't include your Memory, those saved facts; they live in a separate place. And it doesn't include each custom GPT's instructions and knowledge files. So you copy those two by hand - which is exactly what the next two beats show. Don't assume the zip is everything; it isn't."

**[BEAT 5] 2:35 - 3:20 (Instructions + memory across) → [CUT TO CLAUDE]**
"Two quick wins that make Claude feel like home from the first message. First, custom instructions. Copy the text from ChatGPT and paste it into Claude's profile preferences - that's Settings, then your profile. It's always on, every new chat. Second, memory. Here's a neat trick: ask ChatGPT to 'summarise everything you know about me', then paste that summary into Claude. From there Claude's own memory builds as you work - it's on by default. Let me do both quickly."

**[CUT TO CLAUDE] 3:20 - 3:50 (Demo - see Section 3)**
Paste a sample preferences block into Profile preferences; paste a sample "what you know about me" summary into a chat. Generic content only.

**[BACK TO BOARD] [BEAT 6] 3:50 - 4:25 (Custom GPTs become Projects)**
"Custom GPTs are the part people worry about, and they're the easiest. One Project per GPT, and its three parts map straight across. The GPT's name becomes the Project name. Its instructions become the project instructions. Its knowledge files become the project knowledge. That's it - nothing's lost in translation. The one extra bit: if your GPT had a repeatable *way it should behave* - a format it always followed - that's better as a Skill, which is the next beat."

**[BEAT 7] 4:25 - 4:55 (Prompts -> Skills, tools -> Connectors)**
"Two things people forget to move. First, the prompts you kept re-pasting - that weekly report prompt, the same summary instruction. Write it once as a Skill, and Claude reaches for it when it fits, instead of you pasting it again and again. Second, the tools you had wired up - plugins, or GPT Actions calling other apps. Those reconnect as Connectors: calendar, email, drive, chat and more. Same capability, different plumbing."

**[BEAT 8] 4:55 - 5:20 (What doesn't move 1:1 - honest gaps)**
"Let me be straight about the few things that *don't* map one-to-one. Claude doesn't generate images, so for that you'll use a dedicated image tool - and Claude Design for on-brand UI and deck visuals. Claude has voice in the mobile app, but it's lighter than ChatGPT's real-time voice. And there's no like-for-like GPT Store; instead the extensibility comes from the Skills Directory, Connectors, and partner Skills. Everything else has a clean equivalent."

**[BEAT 9] 5:20 - 5:30 (Move smart, not everything - safety + close)**
"Last thing, and it's the one part you can't skip: a switch is a filter, not a bulk copy. Don't dump your old chats wholesale into a Project - you'd carry old mistakes across with them. Nothing confidential or patient-identifiable goes into projects, skills or exports, and keep your examples generic: the method travels, the sensitive data does not. So this week, do one thing - move a single custom GPT into a Project and paste your instructions into preferences. Full step-by-step is in the playbook below. That's the move - see you in the next one."

---

## Section 3 - On-screen demo steps

Everything below is invented, generic content. No Phlo branding, no patient or confidential material, at any point. Use a throwaway/sample ChatGPT account or generic text - do **not** export or paste a real account's history on camera.

### Demo - instructions + memory across (~30s)

1. In **Claude**, open **Settings -> your profile -> Profile preferences**. Paste a generic preferences block, e.g.
   `Reply in British English. Be concise and direct. I work in operations; prefer bullet points and a short summary first.`
   Save, and point out "always on, every new chat".
2. In **ChatGPT** (sample account), type: `Summarise everything you know about me from memory and custom instructions, as a single block I can copy.` Show the output.
3. Back in **Claude**, paste that summary into a new chat with: `Here's a profile of how I work - keep this in mind going forward.` Note that Claude's memory then builds automatically.
4. (Optional) Show **Projects -> Create Project**, name it after a sample GPT, paste sample instructions into project instructions, and drag in a generic reference file as project knowledge.

> Keep every input invented and generic. The teaching point is "copy across, don't rebuild" - so do the paste live rather than just describing it.

---

## Section 4 - Design rationale

- **House Style B**, built by `build_chatgpt_to_claude.py` (imports the shared `excalidraw_kit`); re-run to regenerate. 9 beats, `random.seed(131313)`.
- **The signature beat is 2 (the translation map)** - "every ChatGPT feature has a Claude equivalent" is the whole reassurance of the video, so the deck leans on it. The middle beats (3-7) are the mechanical how-to; beat 8 is the honest gaps; beat 9 is the safety + try-it close. This is the house **"power then control"** shape (the bulk of the move, then the filter rule last).
- **Two ChatGPT sources, deliberately distinguished** (a common mix-up): ChatGPT **Projects (folders)** are the *direct* 1:1 with Claude **Projects**; a **Custom GPT** splits across Claude - instructions + knowledge -> a **Project**, the repeatable behaviour -> a **Skill**, any Actions -> a **Connector**. Beats 2 and 6 keep these separate.
- **Verified behaviour** (current Anthropic/Claude + OpenAI docs, checked at build time):
  - ChatGPT export: **Settings -> Data Controls -> Export data**, arrives by email as a zip (`conversations.json` + `chat.html`); the export **excludes** Memory and per-GPT instructions/knowledge - those are copied manually.
  - Claude custom instructions = **Profile preferences** (Settings -> profile), always-on.
  - Claude **Memory** is built-in and on by default (rolled out to all plans, March 2026); seed it with a ChatGPT "summarise what you know about me" block.
  - Claude **Projects** = project instructions + project knowledge base; **Skills** = reusable how-to; **Connectors (MCP)** = external tools; **Scheduled tasks** = recurring prompts (see video 2.5).
  - Honest gaps: **no native image generation**; **lighter real-time voice** than ChatGPT; **no GPT-Store equivalent** - extensibility via Skills Directory + Connectors + partner Skills.
- **Safety teaching is migration-specific**, not just the generic house rule: export-and-reimport is a *filter* moment. Staff may have pasted sensitive material into ChatGPT historically; bulk-loading `conversations.json` into a Project would propagate it. The beat teaches "review and leave behind" - load-bearing for a regulated pharmacy.

## Resources to link under the video
- Companion **`migration-playbook.md`** in this folder - the exhaustive step-by-step + full mapping table.
- Claude - *Intro to Projects*: https://support.claude.com/en/articles/9945648-intro-to-projects
- Claude - *What are projects?*: https://support.claude.com/en/articles/9517075-what-are-projects
- Claude - *Understanding Claude's personalization features*: https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- Claude - *What are skills?*: https://support.claude.com/en/articles/12512176-what-are-skills
- OpenAI - *Projects in ChatGPT*: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Help Center - exporting your data (Settings -> Data Controls -> Export data)
