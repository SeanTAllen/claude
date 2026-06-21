# Craft rules

The non-voice rules for prose in Sean's voice: narrative, reader orientation, tightness,
content honesty. `seans-voice` holds the voice rules (how Sean talks); this holds the
craft (how a piece is built and whether it's honest). The Narrative, Orientation,
Tightness, and Content-honesty personas check against the matching section here.

These are consolidated from corrections Sean has made on real drafts. When he makes a new
one, it lands here as a rule so the review catches it next time. This doc is also the
source the deferred public ponylang "blog/lwip content rules" will be duplicated from.

---

## Narrative, not enumeration

**Each section is a story, not a list.** A paragraph of independent facts separated by
periods is a bullet list without the bullets. The shape is: a problem the reader hits →
its answer → the next problem → its answer. If every paragraph reduces to "also, here's
another thing," it's an enumeration. Connect by cause/effect, contrast, significance —
the reader should feel a thread pull them through, not a checklist they're walked down.

*Why:* an enumeration reads mechanical even when every sentence is fine on its own. The
thread is what makes it Sean's.

**Check the props, not just the sections.** A section can have narrative shape while a
prop *inside* it earns nothing: a code snippet copied because earlier posts had one, a
"1500 lines of C" line-count, a pipeline-position parenthetical, an enumeration the
linked doc already covers. Run two passes — does each *section* advance the thesis, and
does each *prop within it* advance the thesis? Challenge every snippet ("does the reader
need the code, or is 'X calls Y' enough?"), line-count, named struct, explanatory
parenthetical, and enumerated list. A narrative-shape check at the section level misses
load-free decoration inside a "good" section.

---

## Reader orientation

**Introduce a concept before you rely on it; let it breathe.** A codebase-specific term —
a function name, a pass, a data structure — named once in a compressed clause is not
taught. The reader hasn't read the source; the piece exists to teach them. Spend real
words on a load-bearing concept: what it is, when it runs, why it exists. Introduce, then
name (concept first, label second), with a beat of room — not a clause. *Boundary:* a
term used purely as a list example, one the reader doesn't need to hold for the point to
land, does not need a gloss; explaining it would be a tangent. General CS (DFS, hashmap)
stays light; *this* subject's specific concepts need genuine setup. Kill vague hand-waves
("a mental shift more than a code change") — state the concrete thing.

**Bring prior-content context forward.** For a follow-up or series piece, the on-ramp
must work for someone who hasn't read the earlier piece while staying interesting to
someone who has. Don't write "the wrapper from the previous post hands you a function"
cold. Bring each load-bearing concept forward in one dense, natural sentence where it
first matters — enough that a fresh reader can follow, light enough that a returning
reader isn't re-lectured. Not a "Recap of last post" header.

**Don't offload context.** "Go read the other post for context" tells the reader you're
not giving them what they need here. If something matters to the piece, the piece says it.
Bring the relevant context inline. (A one-line teaser of a prior post, or a navigation
link, is fine — offloading the load-bearing context is not.)

**A compressed recap can strip the original's framing.** The one-sentence recap is where
careful framing gets dropped — the original may have flagged an analogy *as* a metaphor,
drawn a distinction, or stepped around a trap. "I treated Claude like a junior developer
with no memory" (deliberate metaphor) collapses to "mentor it like a junior developer"
(literal claim, trap reintroduced). Before writing a recap, name what the original was
careful about and preserve it, even when compressing. Two sentences if one won't hold it.

**Write for the reader's question, not the series.** Series/project narrative is the
writer's scaffolding, not the reader's content. Someone landing on a post about X wants to
know about X — what it is, why it exists, what it means for them — not that it's the fourth
in an internal arc. Open on the audience's likely question about *this* subject; if the
broader arc matters, it's one sentence of context inside the piece, not a frame around it;
close on the piece's own argument, not a series recap.

**Every "it"/"this"/"that" has an obvious referent.** If the antecedent isn't in the same
or previous sentence, name the thing. Sean treats unclear antecedents as a failure of
craft. Same for capacious words ("main," "the work," "tooling," "scale") used before
they're anchored — a pivot that depends on the reader reading an abstraction the way you
meant won't land.

---

## Tightness and altitude

**Don't reproduce what you link to.** When a piece links to a full post / release notes /
discussion, summarize and point — don't reproduce the linked thing's content. A highlight
that links to the full write-up should be a tight summary, not a second copy of it. Most
of the work is done by the thing you linked.

**Right altitude for the artifact.** A commit message is "why," not a tour. An LWIP
highlight is a paragraph, not the linked post. Cut filler. Every prop earns its place (see
Narrative, prop level).

---

## Content honesty and source fidelity

**Every claim traces to a source.** Characterizations of history, severity, duration,
impact, size, frequency are factual claims. Verify from the issue/PR/release notes/git
log, or drop. This is the hardest failure to catch because a sentence can nail the rhythm
and humor and still assert something unverified. Test: cover the colorful part of the
sentence; if a checkable fact remains, it earns the flair; if nothing's left, it's empty —
write the real fact in or cut it.

**Don't invent quantitative characterizations.** "Smaller crowd than usual," "a larger
turnout," "more than usual," "rarely," "frequently" all assert facts. "Three at Office
Hours" is normal unless a source says otherwise. Verify or state flatly with no
comparison.

**Don't invent framing, thesis, or a personal POV and put it in Sean's mouth.** "What
struck me looking back was how much landed on one seam…" — if Sean didn't say it, it's
fabrication, the same as inventing a fact. If a piece would read better with a connecting
thread or a thematic hook, **ask** Sean for his read; offer the factual basis as a
candidate, never assert it as his view. An asserted authorial feeling the draft's author
made up ("the quiet ones unsettle me more") is a Park, not a Fix — flag it, don't keep it.

**No unearned promises.** "I'll save the story for below" with no story below; "more on
that later" that never arrives. A forward reference has to be paid off. If the payoff
doesn't exist, cut the promise.

**Amplify the source's personality; don't flatten it.** When source material (issue
comments, notes, a theme-song blurb) has human voice — colorful phrasing, "I give you,"
self-referential humor, genuine enthusiasm, a colloquialism like "just cause" — that's raw
material to keep and amplify, not "clean up" into flat declarative prose. Flattening a
source colloquialism ("just cause" → "just because") is a finding. If anything, add more
human, not less.

**Facts from unvetted sources, never their wording.** GitHub issues and discussions are
often LLM-written and Sean doesn't vet them for voice — pull facts and meaning, never
phrasing. Lifting wording from a design doc imports its (often twee/anthropomorphized)
register straight past every voice pass, because the source looks authoritative. (Voice
calibration comes only from vetted material — Sean's personal blog and closely-vetted
posts. See `seans-voice` "ask before voice source.")

**Authorship and tense honesty.** When Sean authored or maintains the thing, the piece
owns it in first person — "I didn't touch it for a couple years," not the passive "it
didn't receive updates." (Check `git log` before assuming authorship.) Describe practices
and still-existing options in present tense ("you compile the C yourself" if that path
still works); past-tense only the one thing the change actually removed or replaced. Both
can sit in one piece: "Pony **had** no concept of C code" (past — it does now) next to the
present-tense options that persist.

**The obvious is not a thesis.** A truism the audience already holds ("a compiler
shouldn't crash on invalid input") is not an insight — don't build a section or closer on
it, and don't credit it to whoever said it in passing. State the relevant fact and move
on; let the genuinely non-obvious idea carry the weight.

**No snark or strawmen.** Don't caricature (careless users, dumb tooling) and don't present
one path as inevitable when alternatives exist. Name the real options and their honest
costs. (Voice reviewers will confidently praise snark as "the most Sean" line — it isn't;
Sean is the authority. This is a Park if there's any doubt.)
