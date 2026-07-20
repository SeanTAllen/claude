---
name: how-to-write
description: "A process for how to go about writing anything: know who you are writing for, outline the narrative, write it plain, fix the structure, give the important parts weight, then add flourish last, on top of the plain. Form-agnostic; the core under blog-post, lwip, commit messages, and the rest. Load before any writing task."
disable-model-invocation: false
---

# How to Write

Writing fails the same way every time: it comes out fluent and hollow. The
sentences sound right, the rhythm is there, and nothing underneath is true,
structured, or worth the reader's time. The cure is not a longer list of things
to check. It is a process — an order of operations that forces the real content
and the structure first and treats flourish as the last, optional move.

This is that process. It is the same for prose that carries a narrative: a blog
post, a Last Week in Pony entry, a discussion, an issue, a commit message. Each
form has its own shape. How you go about writing is one thing.

It does not run for prose that only has to be plain — a comment, a docstring, a
release note, a README. There is no narrative to outline and no flourish to add;
plain is the whole job, and it is the finished state, not a step on the way to
one. Those forms have their own rulebook, and CLAUDE.md says which.

## The process

1. **Know who you are writing for.** Write down the answers to two questions
   before you draft. What do they know? That sets the level you write at, what
   you have to explain, and what you can assume. Why are they reading? That sets
   what belongs in the piece and what doesn't. Answering once is not enough.
   Writing shows you where the answers were too loose, and any later step can
   send you back to sharpen them.

2. **Outline the narrative.** Decide the story before you write a sentence of
   it. What question does the piece open, and what is the payoff that answers it?
   For an argument: what is the claim, and what carries it? You are not writing
   yet. You are deciding the shape.

3. **Write it simply and plainly.** Get the true thing down with no decoration.
   Short, direct sentences. State each fact as plainly as you can. No flourish
   yet. You have not earned it, and reaching for it here is how plain never
   happens.

4. **Examine the narrative structure.** A real draft exists now, so read it for
   structure, not words. Does the question stay open and pull the reader
   through? Does the payoff land where it should? Is anything given away too
   early, or buried too late? If the structure is wrong, fix the structure
   before you touch a sentence.

5. **Identify the important parts.** Find the few places that carry the piece:
   the hook that sets up the payoff, the payoff itself, the turn, the reveal.
   Most of a piece is connective tissue. A few parts are load-bearing.

6. **Put more weight there. Let it breathe.** Spend words at the load-bearing
   parts. Add concrete detail and color — real specifics, not filler. Slow down.
   The tools are concrete detail, short flat lines used as pauses, and slow
   builds to the reveal. A good piece takes its time where it matters and moves
   quickly where it doesn't. The unit is a paragraph, not a sentence: state the
   fact, show what it means, let it land. Spacing facts further apart is not
   breathing — one fact per paragraph is a list with the bullets taken out.

7. **Add flourish, only on top of the plain.** Now you may add rhetorical
   flourish. It sits alongside the plain fact, never in place of it. It
   augments. It never replaces. Cover the flourish and the plain fact has to
   still be there underneath. If covering it leaves nothing, the flourish is
   doing the work the fact should do. Cut it, or write the fact in.

## The order is the discipline

The steps are not interchangeable. The order is what does the work.

- **Plain before flourish.** You write the true thing plainly first, so you
  cannot skip plain and go straight to sounding good. Sounding good with no
  plain fact underneath is the single most common failure, and the hardest to
  catch after the fact, because it reads well.
- **Audience before shape.** The question a piece opens is the reader's question.
  You cannot know it until you know whose it is, so step 1 comes before step 2.
  Go looking for the question in your material instead and you will find a thread
  that isn't the reader's, and build the piece on it.
- **Structure on a real draft, not an outline.** You examine structure in step 4,
  after a plain draft exists, so you are looking at the real thing instead of an
  idea of it.
- **Weight on purpose.** You add weight in step 6, deliberately, at the parts you
  identified. Not evenly, and not everywhere. Even weight is no weight.

Do it out of order and you get the thing this process exists to prevent: fluent
prose with no spine.

Going back is not going out of order. The order is the first pass. A later step
often shows an earlier one was wrong — you weight the load-bearing parts and see
that the structure you settled in step 4 no longer holds, or you reach for
flourish and find the plain fact under it was never there. When that happens, go
back to the earlier step and redo it from what you now know. Out of order means
reaching forward for a step you have not earned — flourish before plain. Looping
back to a step you already did, because the draft taught you something, is the
process working, not a break from it. The `/blog-post` form names this loop as a
step; the same move applies to every form.

## The same process, any form

This is form-agnostic across the narrative forms. A blog post, a Last Week in
Pony entry, a GitHub discussion, an issue, a PR description, a commit message —
each one runs this same process. What changes is the form laid on top:

- the form's structure (a commit message's subject and body is not a blog post's
  arc),
- what counts as "important," and how much room it gets (a commit message
  breathes in a sentence; a blog post breathes in a section),
- the form's own conventions.

Load the skill for the form you are writing (`/blog-post`, `/lwip`, and so on)
for the form. This skill is the process underneath all of them.

## What to check at each step

The steps tell you what to do. These are what to check while you do it. Most of
them live in `/seans-voice` (the full rulebook) and `/review-for-seans-voice`
(the after-the-fact review). Here is which check belongs to which step.

- **Know the audience (1):** Would this reader recognize what you wrote from
  their own experience, or does it need them to know what you know? A fact that
  only lands for someone who read what you read buries the piece, however true
  and however well sourced. Run this against every step after, not just this one.
- **Outline / examine structure (2, 4):** Is it an actual narrative — a question
  that stays open and a payoff that answers it — or a set of explanations in the
  order things happened? Don't give the answer away in the title or the opening.
  The hook sells why the reader should care; it is not for explaining mechanics
  or admiring itself. Don't reach for section headers a short piece doesn't need;
  a short narrative flows.
- **Write it plain (3):** State the plain fact; never dress it up (`/seans-voice`
  "Content first"). No anthropomorphizing, and not just of tools — of any noun: a
  bug, the data, a test, the layout, an order, the runtime, the seed. Don't
  inflate "non-obvious" into "impossible." Don't assert a cause you can't
  support. Don't invent specifics; if you don't know one, state the idea and flag
  it.
- **Let it breathe (6):** Concrete detail, not filler. The setup has to set up
  the payoff — what you plant early pays off at the end.
- **Flourish (7):** Augment, never replace. This is the content-first rule,
  applied as the last move.

Honesty runs across all of it: no overreach, no invented facts, and don't claim
a draft was reviewed when it wasn't.

## Where this sits

- `/seans-voice` is what the writing should sound like.
- `/review-for-seans-voice` checks a finished draft against that.
- This skill is how you produce the draft in the first place.

Load order: this skill first, then the form skill for the form, then
`/seans-voice` for the sound from step 3 onward, and `/review-for-seans-voice` at
the end, before it ships.
