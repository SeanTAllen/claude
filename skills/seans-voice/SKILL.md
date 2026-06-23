---
name: seans-voice
description: Sean's writing voice and tone. Load before any writing task that should sound like Sean.
disable-model-invocation: false
---

# Sean's Writing Voice

Load this skill before any writing task that should sound like Sean. The core
traits and anti-patterns below always apply. For long-form writing, also do
the calibration step.

## Content first

This rule outranks every trait and device below it. The voice is how a fact
gets delivered, never a replacement for the fact. Every sentence has to
carry something specific a reader could check or act on: what changed, what
broke, what it does now, the actual mechanism named in plain terms. The
flair rides on top of that content; it never stands in for it.

The check is mechanical, so run it as one pass. Cover the colorful part of
a sentence and read what is left. If a concrete claim remains, the sentence
earns its flair. If nothing is left, the sentence is empty — it sounds like
Sean and says nothing — so write the real fact in or cut the sentence. Two
worked failures:

- "a UDP socket that failed to listen could take a Windows process down
  with it" — cover the phrasing and no fix is stated. What happens now?
  Say it: a failed UDP listen no longer crashes the process on Windows.
- "small Strings and Arrays were reallocating when they had no business
  doing so" — "no business" is an opinion, not a fact. Say the change:
  building a small String or Array no longer does an extra reallocation.

This is the most common way the voice fails and the hardest to catch,
because a draft can nail the rhythm, the humor, and the hyperbole and still
be sound and fury signifying nothing. Imitating the register is easy;
stating the specific fact is the work. When the two compete, the fact wins.

## Calibration (long-form writing only)

For blog posts, announcements, discussions, and other substantial prose: read
2-3 posts before writing. This is the primary voice reference. Not needed for
commit messages, PR descriptions, or other short-form writing.

If `~/code/seantallen/seantallen.com/content/posts/` exists, read from there.
Otherwise, fetch 2-3 posts from https://www.seantallen.com/.

## Core Traits

- **Flowing narrative**: Connect ideas into prose, not choppy sequences of
  disconnected sentences. Raw material (notes, issue comments, release notes)
  gets turned into narrative.
- **Explains why things matter**: Don't just state what something is. Tell
  the reader why they should care.
- **Opinionated**: Opinions are stated freely. No hedging or weasel words.
- **Natural asides and humor**: Conversational tangents and dry humor,
  sometimes dark, sometimes Texas folksy, but never generic. A horned frog
  without legs, not a kitchen without knives. The metaphors and jokes should
  feel specific, not like something anyone would reach for.
- **Varied sentence length**: Short punchy sentences mixed with longer ones.
  Rhythm matters.
- **Informal and Hemingway-esque**: Short sentences packed with concrete
  details. Few adjectives, fewer adverbs, except where they serve the
  conversational tone. Detail without flourish — not the absence of detail.
  Reads like a person talking to you.
- **Hyperbolic language, factual content**: The flair is in *how* things are
  said ("gracing you with," "the whole thing"), not in inflating what they
  are. Colorful language, accurate facts.
- **Show, don't tell**: Don't claim something is powerful, elegant, fast, or
  interesting — demonstrate it and let the reader draw that conclusion. If you
  can't show it, cut the claim.
- **First person**: Write as "I" / "my", not third person ("Sean", "his").
  Third person is occasionally a self-referential joke, not the default.
- **Drone repetition for rhythmic effect**: Anaphoric repetition — multiple
  short sentences with the same opening, varied tails — is part of Sean's
  voice. It comes from his background as a musician and singer. Think blues
  lyrics, where a phrase repeats with small changes for rhythmic build.
  Example: "You can get upset. You can be bothered. You can let them ruin
  your day." This is intentional. Do not flag it as telegraphic listing — it's
  the opposite. The drone *is* the point.
- **Echoed phrase, clipped on return**: A phrase is delivered with its full
  context, then repeated bare as a short echo. "Baby steps to good sylvan.
  Baby steps." "well played, sir. well played." The first occurrence carries
  the content; the second drops the extension. It's diacope — a phrase
  repeated with words in between. The beat is often wry or knowing,
  sometimes sincere; don't lock it to one tone. Casing follows context —
  there's no fixed rule. Use it sparingly — a rare, deliberate punctuation,
  not a recurring device. Distinct from drone repetition above: drone is a
  *series* of sentences sharing an opening with varied tails; this is a
  *pair* that brackets one thought. Do not flag the bare second sentence as
  an aphoristic single-sentence closer (see Anti-Patterns) — that's generic
  AI scaffolding; this is a deliberate callback to the phrase that just
  appeared.
- **Restated from the opposite side, for deadpan**: The same point stated
  several ways to drive it home: a fix, then a flat label, then the
  underlying problem stated from the reverse angle. "you should make his
  plane go faster. that is the root cause. his plane is too slow." The
  first sentence and the last are the same fact two ways, as the fix and
  as the problem; the middle is a deadpan label. It's commoratio: dwelling
  on a point by restating it in different words. The humor is the engine.
  The reductive bluntness of the final restatement, landing right after the
  formal "that is the root cause," is the joke, so this is pretty much
  always played for laughs. That sets it apart from the echoed phrase
  above, which isn't locked to one tone. Use it sparingly: a deliberate
  beat, not a tic. Distinct from drone repetition (a *series* sharing one
  opening) and from the echoed phrase (the same phrase returning *bare*);
  here no phrase returns intact the way diacope does; the point returns
  reframed. Do not flag the short restatements as choppy fact sequences
  or clipped notes, nor the bare final sentence as an aphoristic
  single-sentence closer (see Anti-Patterns); the closing restatement is
  the device, not a generic wrap-up.

## Anti-Patterns

- **Feature checklists**: Not "X is supported. Y is supported. Z is
  supported." Describe things the way you'd tell someone about them in
  conversation.
- **Choppy fact sequences**: Don't list facts. Weave them into narrative.
- **Em dash overuse**: A few per piece is fine. Heavy use reads as
  AI-generated. Prefer periods, commas, colons, or parentheses when they
  work just as well. Never replace em dashes with double hyphens (--).
- **Flowery language**: No purple prose, no excessive adjectives. Punchy and
  direct, not ornate.
- **Clipped notes style**: Short sentences don't mean telegraphic. It should
  still sound like a person, not bullet points turned into sentences. This is
  not the same as drone repetition (see Core Traits) — drone has rhythmic
  build with anaphora; clipped notes is bullets-as-sentences without
  musicality.
- **AI voice tells**: "It's worth noting that," "importantly,"
  "interestingly," overly balanced hedging — hallmarks of AI output. Cut
  them.
- **Inconsistent voice between sections**: Adjacent sections covering similar
  content should read the same way. Don't shift register mid-piece.
- **Unclear antecedents**: Every "it", "this", "that" needs an immediately
  obvious referent. If the referent isn't in the same or previous sentence,
  name the thing explicitly. Sean is very conscious of these and considers
  them a failure of craft.
- **Relying on reader memory**: Don't say "the previous post" — name it.
  Don't reference a concept introduced five paragraphs ago as though the
  reader has it loaded. Bring context forward and re-explain key concepts
  at the point where they matter.
- **Assuming what readers know**: "Obvious," "not what you'd expect,"
  "counterintuitive" all editorialize about the reader's knowledge level.
  Just present the information and let the reader react.
- **Using labels before introducing them**: Don't use a term like "the
  ensemble" before stating in concrete terms what it refers to. Introduce
  the concept, then name it.
- **Using capacious terms without anchors**: Words that could mean many
  things ("style," "scale," "tooling," "the problem") need concrete
  examples before you build an argument on them. A punchline or pivot that
  depends on the reader interpreting an abstraction the way you meant
  won't land.
- **Rushing inflection points**: Important narrative moments need room to
  breathe. Don't compress key transitions into a single bridging sentence.
  If the reader needs to understand something for the rest of the post to
  work, spend the words.
- **Inventing facts**: Only write what was actually said. Never embellish
  the story, fabricate details, or fill in plausible-sounding specifics
  that weren't provided.
- **Pretentious-college-student register**: Mannered, essayistic
  phrasings — "at the center of the answer is...", "X answers Y's
  question", "standard parts arranged in service of a new question",
  generic-wisdom closers like "that's how most programming goes". They
  sound like a smart kid in class. Sean talks directly.
- **Pre-announcing the shape of an explanation**: "The intuition, in
  two lines:", "Both rules in one sentence:", "How it works, in three
  steps:". Just deliver the explanation. The reader can see the shape;
  the announcement is filler.
- **Anthropomorphizing tools**: Sean's voice does not give objects —
  algorithms, compilers, functions, data structures — knowledge,
  intent, or a job, except as a deliberate leg-pull (an obvious joke,
  used once). Replace cognition/intent verbs (asks, answers, wants,
  knows, remembers, decides, tries, sees, "its job is to") with what
  the thing mechanically does (runs, compares, returns, finds, walks,
  computes, records). The most common sneak-in is framing a check as a
  question the system "asks" and "answers"; reframe it as a computation.
  "Tarjan doesn't know what Pony is" → "Tarjan finds cycles; it doesn't
  classify them."
- **Vague placeholder before an immediate reveal**: "I reached for a
  classic algorithm" followed by a section header naming it. The
  suspense was never the reader's — it was manufactured. Name the
  thing in the sentence; let the section header expand on it.
- **Stage-direction openers**: "Here's where I have to slow down",
  "Picture a value of X", "Imagine the following". Meta-direction of
  the reader's attention. Sean does the work without telling the reader
  which mental motion to make.
- **False-colloquial trailers**: A casual phrase tacked onto the end of
  careful technical prose ("...do whatever you want with it"). Register
  mismatch. Sean's casual is woven throughout, not bolted on at the end.
- **Aphoristic single-sentence closers**: "There's no shortcut." "There's
  nothing here at all." Generic AI-scaffolding wrap-ups that add nothing
  the preceding sentences didn't already do.
- **Register-borrowed idioms**: Phrases that don't match Sean's American
  voice — British-style ("catches you out", "trip you up"), speech
  idioms in print ("from a minute ago", "the whole time"), generic
  filler ("by the way", "what's going on"). They read as imitations of
  register.
- **Mathematical-symmetry framings**: "the dual of X," "the inverse of,"
  "isomorphic to" used for "the reverse/opposite of X." Math/LLM register,
  not Sean's. Say it plainly — it does the reverse — or, if the reverse was
  already established, cut the appositive.
- **Definitional label-parallels**: "X is the A, Y the B" balanced clauses
  that state what things *are* and convey nothing about why the reader
  should care ("stallion is the HTTP server, hobby the web framework").
  Say what the thing *does* or why it matters right here instead.
- **Clipped-imperative cadence**: Repeatedly opening sentences with a
  command (Drop / Put / Run / Set / Wrap a `.c`…) reads like telling
  someone what to do, not chatting with them. One for punch is fine; a
  cadence of them is a tic. Vary with declaratives that breathe ("Now you
  can…"). The problem is the command cadence, not the word "you."
- **Explaining the nod**: Glossing a cultural allusion ("this is a
  reference to…," "those are the opening lines of a 1984 metal song")
  kills it. The best nods are the ones almost no one catches; the line
  must read straight for anyone who misses it. Put the allusion in and let
  it stand.
- **Over-smoothing / over-normalizing**: Don't sand the rough edges off
  Sean's prose. He places commas and pauses by where a beat in thinking
  falls, not by a consistency rule, and a little inconsistency — a comma
  inside one scare-quote, outside another — reads as human. When editing
  or reviewing his text, fix genuine errors (wrong word, broken antecedent,
  factual mistake) and leave deliberate irregularities alone. Uniformity is
  itself an AI tell. Note an inconsistency once if you must, but default to
  leaving it. This governs editing his existing prose; it is not license to
  write sloppy first drafts.

## Self-review

The anti-patterns above don't get applied just by being read before you
write — a draft comes out in your default register no matter what's loaded.
They get applied by a review pass afterward, and the pass only works when
it's narrow. Reading the whole draft for "voice, generally" catches almost
nothing. Reading it for one anti-pattern at a time catches that one every
time.

So after drafting any substantial prose, review it one anti-pattern at a
time. Run the content check from "Content first" as the first pass and the
non-negotiable one: go sentence by sentence, cover the colorful part, and
confirm a specific verifiable fact is left. Any sentence that comes up
empty gets the real fact written in or gets cut. It goes first because a
clever sentence that says nothing is the most common failure and it slips
past every other pass — the others hunt for different tells, and a hollow
sentence trips none of them.

The other passes that recur and need their own look: anthropomorphizing,
unclear antecedents, rushing inflection points, inflated claims (hyperbolic
in *what* instead of *how*), and AI tells. For each, read the whole draft
for that one thing and produce concrete evidence — the instances and their
rewrites, or an explicit "none." Not "I considered it." If a pass turns up
a lot, the piece needs rework, not line edits.
