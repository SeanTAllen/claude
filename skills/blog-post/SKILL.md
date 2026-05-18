---
name: blog-post
description: Draft a blog post on Sean's behalf. Covers announcement posts, feature posts, architecture walkthroughs, and essays. Not for Last Week in Pony — use /lwip for those.
disable-model-invocation: false
---

Draft a blog post on Sean's behalf. Use this for library release
announcements, feature posts, architecture walkthroughs, and essays.
For Last Week in Pony posts, use `/lwip` instead.

## Voice foundation

Load `/seans-voice` before writing. It has the core voice principles:
first person, flowing narrative, hyperbolic in *how* things are said and
factual in *what*, no AI tells, em dash frugality, varied sentence
length. Everything below adds to those rules for blog-post-specific
concerns.

## The core principle

**Sell what the software has, not what work went into it.**

A post about software is about what it currently does and why those
things matter for real applications. Not a changelog. Not a bug-fix
tour. Not "here's what changed since the last release."

Consequences:

- No dedicated "bugs we fixed" or "what's new" sections. Release notes
  enumerate fixes; the post doesn't repeat them.
- No "we used to lack X, now we have X" framing in section openers.
  Lead with what the software does in the present.
- No bug stories as section openers. Open with the working feature, not
  the bug that was fixed.
- No version-anchored body prose ("0.3.0 supports SSL"). Once the
  section header names the topic, the body talks about what the
  software does in present tense.

Historical contrast is allowed when it earns its place. A "dormant for
two years, then a leap" arc is honest framing that sets up stakes
without enumerating absences. A list of absences that the post then
fills in section by section is saying the same thing twice.

## Sweep for ghosts after cutting prior-version framing

When you cut "we used to lack X" content, the surrounding prose often
has linguistic markers that depended on the removed context. After the
cut they're hanging in space. Sean calls these *ghosts*. Common ones:

- *still* ("Strings still work" — still vs. what?)
- *new* ("a new callback" — new vs. what?)
- *now* ("now takes an optional X" — now vs. when?)
- *also new*, *is new too*
- *no longer*
- *instead of* ("arrives typed instead of as text")
- "Existing code is unaffected" (only meaningful to a reader with
  existing code)

After writing, grep the post for these explicitly and rewrite. Leave
them only when they refer to the current post's own structure, not to a
prior version of the software.

## Reach for accurate, not punchy

The tightest failure mode when writing in Sean's voice: inflating a
fact to land a "cool" line. The voice rule is hyperbolic in *how*
things are said, not in *what*. The flair is in phrasing, not in
exaggerating the facts.

Watch for:

- Claiming something was unusable when it was usable but limited
- Labeling prior versions as "proof-of-concept" when they were real
  but small
- Imperative closers ("Go do X") that weren't earned by the narrative
- Generic tech-criticism tropes as metaphors ("it's a press release")

The test: can you defend the straight version of the claim? If the
straight version is softer than what you wrote, you inflated.

## Don't extend good metaphors

When a metaphor lands, leave it alone. Extending it to make another
point usually kills what made the original work. Use once, land,
move on.

## Section structure

**Grouping by concept, not proximity.** Features that happen to be
near each other in the code or API aren't necessarily in the same
section. If you can't name the shared concept of a section in one
phrase, the grouping is wrong.

**Narrative within a section.** Each feature should land because it
answers a problem the reader is about to hit, not because it's next on
a list. The shape is: problem the reader hits → solution → next
problem → next solution. If every paragraph can be rewritten as "also,
here's feature N," the section is enumeration, not narrative.

**Openers lead with the subject, not background.** If the paragraph
is supposed to be about what the software does, make the software the
subject. Don't open with trivia about the domain the software operates
in.

**Section transitions.** Don't jump from a high-level contextual
section (history, broader ecosystem story) straight into low-level
technical detail with no bridge. End the contextual section with a
handoff; start the technical section with something that lands the
topic before diving into specifics.

**Headers name the subject, not the position.** "After Tarjan",
"Meet X", "What I built" telegraph where you are in the post without
describing what the section is about. A header should answer "what
is this section about?", not "where am I in the post?".

**Don't leave a single H3 in a section.** A solitary subheading reads
as a structural mistake. Either promote it to its peer level or fold
the content into the parent section's flow.

## Pair concept with its implementation

When a post has rules + their algorithmic checks (or properties + their
verification, or invariants + the code that enforces them), deliver each
rule with its check inline rather than putting all the rules upfront and
the checks much later. Otherwise the reader has to carry the rules
across many sections before seeing them applied.

The pattern that's wrong: state every rule, then walk through every
example, then introduce the algorithm. The pattern that works: rule
one, its check, its failure examples; then rule two, its check, its
failure examples.

This applies anywhere a post states a property at one abstraction and
shows how to verify it at another. Deliver them together.

## Teaching technical material

**Pair contrast in pedagogical diagrams.** A single legal-case diagram
just shows "here's a graph with some labels." The teaching happens in
the comparison. When introducing a rule, show both a legal example and
an illegal one. Same diagram type, different verdict. Reader sees the
rule in action.

**Make state snapshots visually distinct in algorithm traces.** When
walking through an algorithm, the snapshots of state (a stack, a heap,
a set of variables) are the things the reader needs to track between
steps. Inline backticks in prose are skimmable. Code blocks make state
changes scannable and visually anchor each step.

## Temporal honesty for in-flight work

When writing about work that isn't yet finished — a PR in review, a
library not released, a deployment pending — be honest about state.
Don't write past tense as if it's done.

Honesty alone reads as hedge ("This isn't merged yet"). Pair it with
a confidence statement about what does hold:

> Details may shift before it does, but everything in this post is
> foundational. It should all hold.

The reader gets both the truth about state and a sense of what's
load-bearing.

## Writing about gaps

A "what's missing" or "limitations" section is honest and welcome.
The tone should not be dismissive.

Avoid:

- "You'll have to write it" (dismissive)
- "Use X instead" as a workaround suggestion (dismissive)
- "Not supported and may never be" (editorial finality)
- Gates on contribution ("the constraint is X and Y")

Prefer neutral statements of what's not there and close with an
invitation. The door is open.

## First person when you're the maintainer

When Sean is the maintainer of the software being written about, the
post should own the decisions. "I didn't touch it for a couple years"
beats "it didn't receive updates." Passive voice hides the agent; Sean
is not hiding, so the post shouldn't either.

## Don't offload context

If something matters to the post, the post says what matters. "Go read
the other post for context" tells the reader you're not giving them
what they need here. Bring the relevant context forward and explain it
inline.

## Compressed recaps of prior posts can strip framing

When the post references an earlier piece, the natural one-sentence
recap is the place where careful framing gets dropped. The original
may have been explicit that an analogy is a metaphor, drawn a
distinction, or stepped around a trap with surrounding context. The
shorthand collapses all of that into a verb phrase.

Example: a post that says "I treated Claude like a junior developer
with no memory" frames the analogy as a deliberate metaphor. The
shorthand "mentor it like a junior developer" presents the same
analogy as a literal claim and reintroduces the trap the original
sidestepped.

Before writing a recap, identify what the original was *careful
about* — the qualifications it made, the traps it stepped around,
the distinctions it drew. The recap has to preserve those, even when
compressing. If you can't preserve them in one sentence, use two.

For series posts, the same principle applies in reverse: a one-line
teaser of what the prior post covered is enough. Don't open the
current post with a verbose recap. The current post is doing its own
work; the prior post's content doesn't need to be repeated.

## Grammar: intros and lists

When an intro sentence ends with a colon and sets up a list, the
bullets must grammatically complete the intro. Read the intro + each
bullet out loud.

Broken: an intro that promises status statements followed by noun
fragments that describe topics but don't state a status.

Fixed: an intro that promises noun phrases ("what you won't find")
followed by noun phrases that complete the sentence.

## Review passes

Beyond the standard `principle-review` and `docs-review` pipeline,
blog posts benefit from two additional passes before opening the PR:

1. **Voice review.** A fresh-context reviewer reads the draft against
   Sean's actual writing — his personal blog at
   `~/code/seantallen/seantallen.com/content/posts/` and recent posts
   on whatever blog the post targets. The question is whether the
   draft sounds like Sean talking or like a careful imitation. The
   reviewer looks for sentence rhythm, repeated tics, generic
   metaphors where Sean would use a specific image, forced
   colloquialisms, openers and closers that don't land like his, and
   anything that sets off a "this sounds AI" alarm.

2. **Narrative review.** A fresh-context reviewer walks each section
   and asks: "Is this telling a story or enumerating features?" An
   enumeration feels mechanical even when each sentence is fine on its
   own. A story has problem hooks tying features together.

## Workflow steps

1. **Calibrate on voice.** Read 2-3 recent posts on the target blog
   and 2-3 posts from Sean's personal blog at
   `~/code/seantallen/seantallen.com/content/posts/`. Load
   `/seans-voice`.

2. **Research the topic.** For a release announcement: read the
   release notes in full (`gh release view`), the README, and the
   release history. Understand what "new" actually means against the
   project's timeline.

3. **Draft an outline.** Name each section and identify the narrative
   arc within it. If you can't articulate the arc in a sentence, the
   section will end up as enumeration. Run `principle-review` on the
   outline before writing prose.

4. **Present the outline to Sean and wait for approval.** Don't write
   prose until Sean has seen and approved the outline. Surface parked
   items (title options, scope questions, tone decisions) for his
   input.

5. **Write the draft.** Apply the principles above as you write.
   Don't inflate. Don't extend metaphors. Watch for ghosts. Keep
   sections narrative, not enumerative.

6. **Self-review loop.** Lightweight single-agent `principle-review`.
   Iterate until clean.

7. **Docs review (lightweight mode).** Accuracy, completeness, and
   principles personas. Apply findings.

8. **Re-evaluate the outline.** After review passes, assess whether
   findings indicate a problem with the outline or approach, not
   just the prose. If the outline's structure is wrong, go back to
   step 4 rather than patching forward.

9. **Voice review and narrative review.** The two extra passes
   described above.

10. **Build verification.** Run whatever the project requires to
    verify the post renders (project CLAUDE.md has the specifics).
    Re-read the rendered output — issues visible in rendered form
    (broken layout, missing images, formatting that doesn't land)
    aren't always visible in source.

11. **Open the PR.** Feature branch, squashed commit, `Closes #N`
    in the body if there's an associated issue.
