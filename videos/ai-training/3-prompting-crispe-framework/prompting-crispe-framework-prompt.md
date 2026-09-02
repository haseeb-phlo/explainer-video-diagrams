# Day 3 - Prompting & CRISPE Framework - what the board covers

Companion to `prompting-crispe-framework-script.md`. This is the coverage spec: what is on the board, what is deliberately off it, and what a viewer should be able to do afterwards. Regenerate the board with:

```bash
python3 videos/ai-training/3-prompting-crispe-framework/build_excalidraw.py
python3 preview.py videos/ai-training/3-prompting-crispe-framework/prompting-crispe-framework.excalidraw out.png [XMIN XMAX]
```

## Status against the master prompt set

`Phlo_Excalidraw_Prompts_v2_Style_B.docx` specs Module 3 as **six beats** in `videos/claude/13-prompting-crispe/`. Both are now superseded:

- **Folder:** the board lives at `videos/ai-training/3-prompting-crispe-framework/`. `videos/claude/13-` is occupied by the ChatGPT→Claude video, and `videos/ai-training/` is the authoritative series (see CLAUDE.md).
- **Scope:** the six docx beats are all present and unchanged (they are beats 1, 2, 3, 4, 9 and 16). Beats 5-8 and 10-15 were added afterwards from Anthropic's prompting docs, the memory support article, and the current context-engineering material.
- **Known overlap with the docx, accepted deliberately:** Module 6 ("Research, memory and files") specs a memory pair with a notebook, a magnifier and an incognito window - the same three ideas and illustrations as beats 11-12 here. Day 3 owns memory at depth; **Module 6 should be re-scoped to "Research and files"** when it is built. Module 4 (Projects) and Module 10 (reverse prompting) have lighter conceptual overlaps with beats 10 and 4/7 respectively.

## What a viewer can do afterwards

1. Name the three pieces a weak prompt is missing, and add them in about fifteen seconds.
2. Diagnose a bad answer by symptom → dial, rather than re-rolling the prompt blindly.
3. Give the reason behind a rule, not just the rule.
4. Use three to five examples, and structure them.
5. Order a long, multi-document prompt correctly, and ask for quotes so the answer is checkable.
6. Set a Style and preferences once, and know when work deserves its own Project.
7. Find, edit, pause and delete what Claude remembers - and know what must never go in.
8. Explain why memory makes CRISPE more useful rather than redundant.

## Beat-by-beat coverage

| # | Accent | Beat | Covers | Source |
|---|---|---|---|---|
| 1 | orange | Vague in, vague out | the one-line vague prompt on a crumpled note; what's missing | docx M3 |
| 2 | green | The same ask, rebuilt | context / the real ask / one example; "minimum viable prompt" **[demo]** | docx M3 |
| 3 | violet | CRISPE | six dials, 3×2, each with a one-line gloss; "a diagnostic, not a form"; the acronym-collision caveat | docx M3 |
| 4 | blue | Fault-finder | wrong tone→Style, wrong length→Parameters, wrong shape→Example, **plus** facts-about-you-wrong→Memory | docx M3 + memory article |
| 5 | indigo | Tell it why | rule vs rule-with-reason (the text-to-speech example); brilliant-new-colleague; the golden rule | prompting best practices |
| 6 | green | Show, don't just tell | examples as the most reliable steer; 3-5; relevant / diverse / structured; `<example>` tags; ask Claude for more | prompting best practices |
| 7 | red | Say what to do | three less/more-effective pairs; ask for above-and-beyond explicitly; prompt style rubs off | prompting best practices |
| 8 | blue | Paste first, ask last | documents top, question last on long multi-doc pastes; quote-grounding for checkable answers | prompting best practices |
| 9 | teal | Set once, never repeat | Styles and preferences **[demo]** | docx M3 |
| 10 | orange | Projects hold the context | project instructions, project knowledge, own memory; one Project per piece of work **[demo]** | projects docs |
| 11 | indigo | It remembers you now | Memory, chat search, per-Project memory; the Team-plan default-off caveat | memory article |
| 12 | red | You stay in charge of it | Settings→Memory→Topics; Pause vs Reset; deletion caveat; incognito; **the rule** **[demo]** | memory article |
| 13 | violet | So does CRISPE still matter? | three dials automated vs three still yours; the invisible-dial failure mode | synthesis |
| 14 | teal | How the sharp end works | new chat per topic, one Project per job, handoff notes, prune memory, outcome not steps, stop over-engineering; the 80% system-prompt cut | context-engineering material |
| 15 | indigo | Different models, different habits | Claude Opus 5, Sonnet 5, Fable 5 / Mythos 5, Opus 4.8; "check the docs" | per-model prompting pages |
| 16 | yellow | Capture by voice | phone → squiggle → desk; pause-and-try; close | docx M3 |

Four demo badges: beats 2, 9, 10, 12.

## Deliberately not covered

- **API-only material**, because the audience uses the Claude app: `effort`, adaptive thinking, `budget_tokens`, `max_tokens`, prefilled responses, computer-use toolsets, code-review harnesses, subagent caps, LaTeX output.
- **"Ask me questions before you execute"** - popular in power-user write-ups, but it contradicts beat 15's Claude Opus 5 guidance (don't invite extra checking-in).
- **"XML tags are obsolete"** - one 2026 blog claims it; Anthropic's own reference still says to wrap examples in `<example>` tags, which is what beat 6 teaches. Where the two disagree, the platform reference wins.
- **A bare "30% better" figure** for question-at-the-end. The docs scope that to 20k+ token multi-document inputs; an unscoped percentage on a board all staff watch would read as a claim about everyday asks.
- **Reverse prompting / prompt repair** - that is docx Module 10, and beats 4 and 7 stop short of it deliberately.

## Refresh triggers

- **Beat 15 dates fastest.** Re-check the per-model prompting pages before any re-record; the beat says so on the board.
- **Beat 11's plan caveat** changes if Anthropic changes the Team/Enterprise memory default, or if Phlo's plan changes.
- **Beat 12's rule** changes if the default-excluded sensitive-topic list changes.
- Tool-specific boards refresh every 90 days per the production notes.
