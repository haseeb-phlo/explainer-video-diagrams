What is AI and how does it work? 

 

Voiceover script: "What an LLM actually is" 

  

  Total runtime: ~7:30. Pace target: ~150 words/min. British English. Technical terms are introduced in plain language first, then named, so techy viewers get the 

  proper vocabulary and everyone else doesn't get tripped up. 

  

  --- 

  Scene 1 — What's an LLM? (0:00–0:35) 

   

  On screen: "LLM" draws in big → expands to "Large Language Model" → seven brand cards (Claude, ChatGPT, Gemini, Llama, Mistral, DeepSeek, Grok) fade in one by 

  one → tagline. 

  

  ▎ Let's unpack the term "LLM". It stands for Large Language Model. And that's almost the whole story - it's software that learned patterns from an enormous  

  ▎ amount of text. Books. Websites. Code. Forums. Papers. All of it.  

  ▎ 

  ▎ The names you've heard - Claude, ChatGPT, Gemini, Llama, Mistral, DeepSeek, Grok - those are brands. Different companies. Different training. Different  

  ▎ personalities. But the underlying machinery is essentially the same. 

  ▎ 

  ▎ Different brand, same engine. So everything we cover next applies to all of them. 

  

  --- 

  Scene 2 — Under the hood: a neural network (0:35–1:35) 

  

  On screen: Layered nodes appear column by column, faint connection lines, the "billions of dials" side note → training loop (show → predict → nudge) → arrow 

  loops back → caption. 

  

  ▎ Inside every LLM is a "neural network" - a stack of layered math, loosely inspired by brain cells. 

  ▎ 

  ▎ Picture a wall of dials. The biggest models have hundreds of billions of them. 

  ▎ 

  ▎ Here's how it learned to be useful. We showed it a chunk of text, asked it to predict the next word, checked whether it got it right, and nudged the dials a  

  ▎ tiny bit toward "better". Then we did it again. And again. Trillions of times. 

  ▎ 

  ▎ That's it. That's the whole training process. No rules programmed in. Just prediction, error, tiny nudge, repeat. At enormous scale, those tiny nudges add up  

  ▎ to something that can write code, summarise a clinical note, or hold a conversation. 

  ▎ 

  ▎ The specific architecture has a name - "transformer" - and there's also a follow-on step where humans rate its outputs to make it more helpful. But the  

  ▎ dial-tuning metaphor is the right one to hold in your head. 

  

  --- 

  Scene 3 — Tokens become coordinates (1:35–2:50) 

  

  On screen: LEFT — "paracetamol" → arrow down → three purple token boxes [para][ceta][mol]. RIGHT — 2D plot with delivered/shipped/sent/mailed clustered green, 

  cat/dog/fish clustered pink → "close = similar meaning" / "far = different meaning" → banner. 

  

  ▎ Now the part that actually makes this work. If you remember one thing about how LLMs operate, make it this. 

  ▎ 

  ▎ Step one. The model doesn't see words the way you do. It chops text into chunks called "tokens". "Paracetamol" becomes "para", "ceta", "mol". Common words  

  ▎ might be a single token. Rare ones get split. Models think in tokens - and that's why everyone talks about them, because that's also how you're billed. 

  ▎ 

  ▎ Step two - and this is the actual trick. Every token gets converted into a point in space. Imagine a giant invisible graph. Every word in the language has  

  ▎ coordinates on it. 

  ▎ 

  ▎ The magic: tokens with similar meanings end up close together. "Delivered", "shipped", "sent", "mailed" - all clustered in one neighbourhood. "Cat", "dog",  

  ▎ "fish" - somewhere completely different. 

  ▎ 

  ▎ This is how the model "understands" meaning. Not by reading a dictionary. By geometry. Things that mean similar things are physically close in this space.  

  ▎ Things that don't, are far apart. 

  ▎ 

  ▎ The technical term for these coordinates is "embeddings". They're the foundation of everything an LLM does. 

  ▎ 

  ▎ Geometry, not magic. 

  

  --- 

  Scene 4 — How it actually answers (2:50–4:10) 

  

  On screen: Prompt appears → "next token?" box → three candidate bars with probabilities → winner pulses orange → sentence grows → second cycle → final sentence → 

   caption. 

  

  ▎ Combine those two ingredients - the dial-tuned network, and tokens-as-coordinates - and here's what actually happens when you ask it something. 

  ▎ 

  ▎ It's autocomplete. Sophisticated autocomplete, but autocomplete. 

  ▎ 

  ▎ Watch. The prompt: "The patient needs their prescription..." 

  ▎ 

  ▎ The model looks at every possible next token and scores each one. "Delivered" - 62%. "Refilled" - 28%. "Cat" - basically zero. It picks "delivered". 

  ▎ 

  ▎ Now the sentence reads "The patient needs their prescription delivered..." - and it does it all over again. "Today" wins at 55%. "Urgently" second. "By" third. 

  ▎ 

  ▎ It keeps going. One token at a time. Each one sampled from a probability distribution. Until it produces: "The patient needs their prescription delivered today 

  ▎  to their door."  

  ▎ 

  ▎ That's the whole trick. Token by token. The technical name is "next-token sampling", and there's a setting called "temperature" that controls how random the  

  ▎ picks are - lower means it almost always picks the top option, higher means it'll occasionally roll the dice for variety. 

  ▎ 

  ▎ Just at vast scale. Across a vocabulary of around a hundred thousand tokens. With billions of dials informing each probability. 

  

  --- 

  Scene 5 — Fluent does not mean true (4:10–5:00) 

  

  On screen: Two thought bubbles side by side - LEFT green halo with paracetamol facts + ✓; RIGHT pink halo with invented Phlo numbers + "Confidently invented" → 

  arrow up → banner. 

  

  ▎ Here's why all this matters for trust. 

  ▎ 

  ▎ The exact mechanism that makes it write fluent prose about paracetamol - generating plausible next tokens - is the same mechanism that lets it write fluent  

  ▎ prose about anything.  

  ▎ 

  ▎ Including things that aren't true. 

  ▎ 

  ▎ Watch. On the left, it confidently explains what paracetamol is. Correct. On the right, it confidently quotes Phlo's Q3 dispensing volume - down to the exact  

  ▎ number, with a year-on-year growth figure. That number is completely made up. It sounds real because it pattern-matches what real numbers look like. 

  ▎ 

  ▎ Same mechanism. Same confidence. Wildly different reliability. 

  ▎ 

  ▎ This is what people mean by "hallucination". The model isn't lying. It's doing exactly what it always does - producing plausible next tokens - on a topic where 

  ▎  the training data didn't have the actual answer. 

  

  --- 

  Scene 6 — Memory is a layer, not the model (5:00–5:45) 

   

  On screen: Three conversation cards (blue / pink / green) → door icon between 1 and 2 → "I don't know" shakes → blue Projects callout slides in → green 

  conversation 3 with "Hi Sam". 

  

  ▎ A practical quirk: the model itself has no memory across conversations. Claude does remember you now - memory is on by 

  ▎ default on Pro and Max - but that is a feature layered on top, and it works exactly the way we are about to see. 

  ▎ 

  ▎ Each chat is a fresh start. Watch. 

  ▎ 

  ▎ Conversation one. You tell it your name is Sam. It says "Got it, Sam". Great. You close the tab. 

  ▎ 

  ▎ Conversation two, the next morning, with memory off. You ask, "What's my name?" It has no idea. As far as it's concerned, you've never met. 

  ▎ 

  ▎ The fix is context. Features like Projects, "Instructions for Claude", and memory all do the same thing - they re-feed your background into every new conversation, 

  ▎  so the model "remembers" what you've told it. 

  ▎ 

  ▎ So conversation three, with a Project attached: "Hi Sam, ready to continue?" Same model. Same lack of real memory. Just more context fed in upfront. 

  

  --- 

  Scene 7 — Tools and recency (5:45–6:35) 

  

  On screen: "the model" box with "training cutoff" badge → question → pink-halo "can't see live data" reply → three tool cards plug in (web search orange, file 

  upload teal, connectors purple) → reply morphs to blue with the right answer → caption. 

  

  ▎ Another quirk: by default, an LLM has no idea what's happening in the world right now. 

  ▎ 

  ▎ It has a "training cutoff" - a date past which it just doesn't know anything. Ask it for the NHS Drug Tariff price of paracetamol this month, and it'll  

  ▎ correctly tell you it can't see live data.  

  ▎ 

  ▎ The fix is tools. You plug capabilities into the model. Web search, so it can look things up. File upload, so it can read documents you share. Connectors, so  

  ▎ it can talk to Slack, Jira, your databases - whatever you wire up. 

  ▎ 

  ▎ Now the same question gets answered with the actual current price. 

  ▎ 

  ▎ Same model. Different toolbox. 

  ▎ 

  ▎ The technical names are "tool use" or "function calling", and a closely related technique called RAG - retrieval-augmented generation. They're where most of  

  ▎ the practical value of LLMs at work shows up. 

  

  --- 

  Scene 8 — Pattern, not knowledge (6:35–7:15) 

  

  On screen: Purple training-data cloud with content icons → arrow down → "the LLM" → three zones light up in turn (green strong, yellow shaky, pink unreliable) → 

  sticky note on pink zone. 

  

  ▎ Step back, and the whole picture clicks. 

  ▎ 

  ▎ An LLM doesn't "know" things. It pattern-matches against the data it saw during training. 

  ▎ 

  ▎ That data was vast - books, news, forums, papers, code. So general knowledge? Strong. It's seen the same idea explained ten thousand ways. 

  ▎ 

  ▎ Niche or specialist topics? Shakier. Less training data on each one. More room to hallucinate. 

  ▎ 

  ▎ Recent stuff, or anything proprietary - like Phlo's internal data? Unreliable. Until you give it tools. 

  ▎ 

  ▎ This last zone - your zone, your data - is where prompting, context, and tool choice actually matter. It's the difference between a clever toy and something  

  ▎ genuinely useful at work. 

  

  --- 

  Scene 9 — Closing (7:15–7:30) 

  

  On screen: Large hand-drawn sentence "Brilliant pattern-matching. Not knowledge." → orange underline draws → subtitle "Next: Prompting fundamentals". 

  

  ▎ If you remember one thing from this video, remember this. 

  ▎ 

  ▎ Brilliant pattern-matching. Not knowledge. 

  ▎ 

  ▎ Treat it that way - and everything else, prompting, hallucinations, tool use, context, all of it - starts making obvious sense. 

  ▎ 

  ▎ Next: how to actually prompt these things well. 

  

  --- 

  Total: ~1,150 words / 7:30 at conversational pace. 

   

  Technical terms surfaced (for the techy folks in the audience): neural network, transformer, training, tokens, embeddings, next-token sampling, temperature, 

  hallucination, context window, tool use / function calling, RAG, training cutoff. Each is paired with a plain-English explanation so nobody needs to look them up 

   to follow along. 