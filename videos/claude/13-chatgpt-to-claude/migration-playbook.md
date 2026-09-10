# ChatGPT -> Claude migration playbook

The exhaustive, do-it-alongside reference for **Video 2.13 - "ChatGPT -> Claude: switching over without starting over."**
The video is the overview; this is the thing to keep open in a second window while you actually move across.

- **Time:** ~1-2 hours for a typical setup, longer if you have many Custom GPTs.
- **Skill needed:** none - it's almost entirely copy-and-paste.
- **Plans:** most steps work on free Claude; **Projects, project instructions and Skills need a paid plan** (Pro and above). Scheduled tasks and some Connectors are paid too.
- **British English, generic examples only.** See [Safety & governance](#7-safety--governance) before you move anything sensitive - it is not optional for Phlo.

---

## 1. The complete mapping table

Every ChatGPT concept and where it lives in Claude. The board (beat 2) shows the headline six; this is the full set.

| In ChatGPT | In Claude | Notes |
|---|---|---|
| **Custom instructions** (global "how to answer me") | **Profile preferences** | Settings -> your profile. Always on, every chat. |
| **Memory** (saved facts about you) | **Memory** (built-in) | On by default; learns as you work. Seed it once from ChatGPT (Step 5). |
| **Projects / folders** (grouped chats + shared files + instructions) | **Projects** | The *direct* 1:1. Project instructions + a project knowledge base. |
| **Custom GPTs** (a packaged assistant) | **Project + Skill (+ Connector)** | Splits up - see Step 6. Instructions+knowledge -> Project; repeatable behaviour -> Skill; Actions -> Connector. |
| **GPT Knowledge files** | **Project knowledge base** | Upload the same files into the Project. |
| **GPT Instructions** | **Project instructions** | Paste the text straight in. |
| **GPT Actions / Plugins** | **Connectors (MCP)** | Reconnect the underlying app as a Connector. |
| **Saved / re-pasted prompts** | **Skills** | Write the repeated prompt once as a Skill (Step 8). See video 2.4. |
| **Tasks** (scheduled prompts) | **Scheduled tasks** | Recreate the schedule. See video 2.5. |
| **Advanced Data Analysis / Code Interpreter** | **Analysis tool + Artifacts** | Upload data and ask; charts/tools come back as Artifacts. See video 2.3. |
| **Canvas** (side-by-side editing) | **Artifacts** | Editable documents/code in a side panel. |
| **Web browsing** | **Web search** | Built in; Claude searches and cites mid-answer. |
| **File uploads in a chat** | **File uploads in a chat** | Same - drag files into the message. |
| **GPT Store / community GPTs** | **Skills Directory + Connectors + partner Skills** | No single marketplace; extensibility is spread across these. |
| **DALL-E image generation** | *(no native equivalent)* | Use a dedicated image tool; **Claude Design** for on-brand UI/deck visuals (video 2.12). |
| **Real-time Voice mode** | **Voice (mobile app)** | Lighter than ChatGPT's real-time voice. |
| **Desktop app working across your files/apps** | **Claude Cowork** | Agentic desktop work (video 2.11). |
| **Conversation history** | *(export only - no direct import)* | Export from ChatGPT; bring across *selectively* (Step 11), don't bulk-load. |

---

## 2. Step 0 - Inventory what's worth keeping

Open a scratch doc and list, from ChatGPT:

- [ ] **Custom instructions** - the global text (Settings -> Personalization -> Custom instructions).
- [ ] **Memory** - skim Settings -> Personalization -> Memory to see what it's stored.
- [ ] **Each Custom GPT** - name, full instructions, and the list of uploaded knowledge files. (You'll need the files themselves too.)
- [ ] **Projects / folders** - which ones, and the shared files/instructions in each.
- [ ] **Saved or repeated prompts** - the ones you paste again and again.
- [ ] **Tasks** - any scheduled prompts you rely on.
- [ ] **Connected tools** - plugins or GPT Actions you actually use.
- [ ] **The handful of chats you reuse** - not all of them; the ones you genuinely return to.

> Most of a clean switch is this step. If it's not on the list, you won't miss it.

---

## 3. Step 1 - Export your ChatGPT data

1. ChatGPT -> **Settings -> Data Controls -> Export data -> Confirm export**.
2. You'll get an **email with a download link** (can take minutes, occasionally up to ~24 hours; OpenAI quote up to 7 days). The link expires - download promptly.
3. The zip contains **`conversations.json`** (full history with timestamps/metadata) and **`chat.html`** (a readable version you can open in a browser).

**What the export does NOT include - copy these by hand:**
- Your **Memory** (the saved facts) - separate system (Step 3).
- Each **Custom GPT's instructions and knowledge files** - copy the text, re-download the files (Step 5).

> The export is a backup of *chats*, not your whole set-up. Don't assume the zip is everything.

---

## 4. Step 2 - Extract memory + custom instructions (manual)

These don't come out in the export, so pull them with a prompt **inside ChatGPT**, then copy the output.

**Extraction prompt - paste into ChatGPT:**
```
Summarise everything you know about me, as a single block I can copy into another assistant.
Include:
1. My custom instructions (how I want answers formatted and toned).
2. Everything in your saved memory about me - my role, preferences, ongoing projects, working style.
Write it as plain, portable notes. Don't add anything you don't actually have.
```

Copy the result into your scratch doc. Also copy your **Custom instructions** verbatim from **Settings -> Personalization -> Custom instructions** (both boxes: "what to know about you" and "how to respond").

---

## 5. Step 3 - Set up Claude's foundations

### 5a. Profile preferences (= ChatGPT custom instructions)
1. Claude -> **profile icon (lower-left) -> Settings**.
2. Find **"What preferences should Claude consider in responses?"** (Profile preferences).
3. Paste your custom-instructions text. Trim ChatGPT-specific phrasing. **Save.**
4. It's now always on, every new conversation - you never paste it again.

### 5b. Seed memory (= ChatGPT memory)
1. Claude's **Memory** is on by default (Settings -> ... -> Memory to confirm / control it).
2. Start a chat and paste the summary block from Step 2 with:
   `Here's a profile of how I work and what I'm working on - keep this in mind going forward.`
3. From here Claude's memory grows automatically as you work. You can review/edit/turn it off in Settings, and use **Temporary Chat** for one-off chats you don't want remembered.

---

## 6. Step 4 - Recreate your assistants

### 6a. Custom GPTs -> Projects (+ Skills, + Connectors)
For **each** Custom GPT:
1. Claude -> **Projects -> Create Project**. Name it after the GPT.
2. Paste the GPT's **instructions** into the Project's **instructions** field.
3. Upload the GPT's **knowledge files** into the Project's **knowledge base**.
4. If the GPT had a repeatable *way of doing a task* (a fixed format/process), capture that as a **Skill** instead of cramming it into instructions (see 6c).
5. If the GPT used **Actions** to call another app, set that up as a **Connector** (6d).

### 6b. ChatGPT Projects / folders -> Claude Projects
The *direct* equivalent. **Create a Project**, paste the folder's shared instructions, upload its shared files, and carry on your chats inside it. (Don't bulk-import the old chats - start fresh in the Project; reference key past chats selectively per Step 8 in the video / Step 9 here.)

### 6c. Saved / repeat prompts -> Skills
The prompt you re-paste every week becomes a **Skill** - write it once, Claude reaches for it when it fits.
1. Claude -> **Settings -> Skills** (or **Customize -> Skills -> + -> Browse skills**).
2. Create a custom Skill: a clear **name**, a **specific description** (this is the trigger - be precise), and the steps in plain English.
3. Tip: use the built-in **skill-creator** Skill to help write it. (Skills need **code execution** enabled in settings.)
4. See **video 2.4 (Skills)** for the full how-to.

### 6d. Plugins / GPT Actions -> Connectors (MCP)
1. Claude -> **Settings -> Connectors**.
2. Add the connector for each app you used (calendar, email, drive, chat, etc.) and authorise it.
3. The tool fires when Claude needs it - same capability, different plumbing.
4. See **video 2.6 (Connectors & MCP)**.

### 6e. Tasks -> Scheduled tasks
Recreate each scheduled prompt as a Claude **Scheduled task** (a prompt that runs on a schedule). See **video 2.5 (Scheduled tasks)**.

---

## 7. Step 5 - Bring across conversation history (selectively)

There is **no direct import** of ChatGPT chats into Claude. Don't try to bulk-load `conversations.json` into a Project.

For the **few** chats you genuinely reuse:
1. Open the chat in `chat.html` (or in ChatGPT).
2. **Review it** - is anything in it sensitive? If so, leave it behind or redact.
3. Copy the useful conclusion/context into the relevant Claude **Project** as a note or knowledge file - not the whole raw transcript.

> Reuse the *output and context*, not the *log*. The history is a reference, not cargo.

---

## 8. What doesn't transfer 1-to-1 (and where to go instead)

| Gap | What to do |
|---|---|
| **Native image generation** (DALL-E) | Use a dedicated image tool. For on-brand UI mockups and deck visuals, use **Claude Design** (video 2.12). |
| **Real-time voice mode** | Claude has voice in the **mobile app**, but it's lighter. Keep ChatGPT only if real-time voice is essential to you. |
| **GPT Store / community marketplace** | No single store. Discover capability via the **Skills Directory**, **Connectors**, and **partner Skills**. |
| **Shared/published Custom GPTs** | Share a **Project** with your team instead (paid plans), or publish a **Skill**. |
| **Exact chat history in-app** | Export + selective reference (Step 5). No live import. |

---

## 9. Safety & governance (read before moving anything)

**The core rule: a switch is a filter, not a bulk copy.** Export-and-reimport is the moment to *leave things behind*, not to propagate them.

- **Don't bulk-load old chats** into a Project - you'd carry old errors and any sensitive content straight across.
- **Nothing confidential or patient-identifiable** goes into projects, project knowledge, Skills, or anything you export/share. Skills and shared Projects are designed to be seen widely - treat them like a published document.
- **Keep examples generic.** The *method* travels; the *data* does not. Use invented identifiers (`Patient_001`, `J. Doe`) if you ever need a placeholder.
- **Review each Custom GPT's knowledge files** before re-uploading - did the original contain anything sensitive? If so, don't carry it over.
- **Delete the ChatGPT export zip** from your machine once you've finished - it's a full copy of your history sitting in your Downloads folder.
- If in doubt about whether something can move, **ask before you move it** - not after.

---

## 10. Verification checklist

- [ ] Profile preferences set and saved (Claude answers in your style without being asked).
- [ ] Memory seeded; Claude recalls your role/preferences in a fresh chat.
- [ ] One Project created per Custom GPT - instructions pasted, knowledge files uploaded.
- [ ] ChatGPT Projects/folders recreated as Claude Projects.
- [ ] Repeat prompts captured as Skills (and they trigger when expected).
- [ ] Connectors reconnected and authorised; a test call works.
- [ ] Scheduled tasks recreated.
- [ ] Only the chats you actually reuse have been referenced across - nothing bulk-loaded.
- [ ] No confidential/patient data in any project, skill, or export; export zip deleted.

---

## 11. Resources

- Claude - *Intro to Projects*: https://support.claude.com/en/articles/9945648-intro-to-projects
- Claude - *What are projects?*: https://support.claude.com/en/articles/9517075-what-are-projects
- Claude - *How can I create and manage projects?*: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude - *Understanding Claude's personalization features*: https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- Claude - *What are skills?*: https://support.claude.com/en/articles/12512176-what-are-skills
- Claude - *Use skills in Claude*: https://support.claude.com/en/articles/12512180-use-skills-in-claude
- OpenAI - *Projects in ChatGPT*: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Help Center - exporting your data (Settings -> Data Controls -> Export data)
- Internal: videos 2.2 (Projects), 2.3 (Artifacts), 2.4 (Skills), 2.5 (Scheduled tasks), 2.6 (Connectors & MCP), 2.11 (Cowork), 2.12 (Design).

*Product UIs change - exact menu labels may shift. If a path has moved, the concept and order of steps still hold.*
