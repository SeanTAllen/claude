---
name: seans-voice
description: Sean's writing voice and tone. Load before any writing task that should sound like Sean.
disable-model-invocation: false
---

# Sean's Writing Voice

Load this skill before any writing task that should sound like Sean. The core
traits and anti-patterns below always apply. For long-form writing, also do
the calibration step.

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
- **Informal and Hemingway-esque**: Short sentences. Minimal adjectives and
  adverbs except where they serve the conversational tone. Reads like a
  person talking to you.
- **Hyperbolic language, factual content**: The flair is in *how* things are
  said ("gracing you with," "the whole thing"), not in inflating what they
  are. Colorful language, accurate facts.
- **Show, don't tell**: Don't claim something is powerful, elegant, fast, or
  interesting — demonstrate it and let the reader draw that conclusion. If you
  can't show it, cut the claim.
- **First person**: Write as "I" / "my", not third person ("Sean", "his").
  Third person is occasionally a self-referential joke, not the default.

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
  still sound like a person, not bullet points turned into sentences.
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
- **Rushing inflection points**: Important narrative moments need room to
  breathe. Don't compress key transitions into a single bridging sentence.
  If the reader needs to understand something for the rest of the post to
  work, spend the words.
- **Inventing facts**: Only write what was actually said. Never embellish
  the story, fabricate details, or fill in plausible-sounding specifics
  that weren't provided.
