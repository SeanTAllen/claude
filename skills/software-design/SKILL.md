---
name: software-design
description: Disciplines for software design work. Load when designing APIs, type systems, features, or system boundaries. Counters the tendency to retrieve familiar patterns instead of discovering what the problem actually needs.
disable-model-invocation: false
---

# Software Design

Load this skill when doing design work — APIs, type systems, features, system
boundaries. The core problem it addresses: LLMs default to *retrieving*
familiar patterns from training data rather than *discovering* what a specific
problem needs. The result is designs that look right (they have the right nouns)
but weren't derived from the problem.

Design is the act of discovering what is needed. It's about finding surprising
affordances and avoiding candy-machine interfaces riddled with footguns.

Design is not a phase. It's a continuous loop: observe what you have, orient
against what you know, decide, act, then observe again. Every decision you make
reveals new information. That information might confirm prior decisions or
invalidate them. Either way, you have to look. "I already decided that" is never
a reason to skip re-evaluation — it was decided with less information than you
have now.

## Process: design uses ensemble

Design work is where pattern-matching failures are most costly and hardest to
self-detect. A single agent applying design disciplines will still
pattern-match — the disciplines become post-hoc rationalizations for a
retrieved design rather than actual constraints on the exploration.

Use the ensemble workflow with three design-specific personas. Load `/ensemble`
for the mechanical process; the personas below replace the generic attention
focuses.

### Design personas

Each persona applies all the disciplines below but enters the problem from a
different direction. The decorrelation comes from where they start, not what
they know.

**Consumer-first designer.** Starts by writing the code that *uses* the API —
every call site, every configuration point, every error path. Derives the types
and interfaces from what makes that code clean. When the design claims two APIs
are "the same," writes both side by side and verifies they literally use the
same names and signatures. The consumer sketch is not an illustration of the
design — it IS the design.

**Skeptic.** For every type, trait, or abstraction — proposed *and existing* —
asks: what if we didn't have this? Is this still the right structure for what
we're building on top of it? A prior decision that was correct in its original
context may be wrong for the new feature. The skeptic doesn't just question new
abstractions; it questions whether the existing foundation is still sound given
what's being added. Tries to subtract from the design rather than add. Proposes
the smallest possible design that solves the problem. When existing code already
handles part of the need, starts from that rather than inventing a parallel
structure.

**Principle checker.** Runs each design principle from this skill and from
CLAUDE.md as a hard verification gate — not "consider whether this applies" but
"does this hold? show evidence." Writes down the answer for each principle.
Specifically checks: is every outcome explicit? Can the user forget a step? Can
something compile but silently do the wrong thing? Are there two representations
for the same concept?

### Synthesis focus

The synthesizer should pay special attention to:
- Where the consumer-first designer's sketches conflict with the skeptic's
  subtractions — the tension usually reveals the right boundary
- Where the principle checker found a violation that the other two missed —
  this is the highest-value finding
- Whether all three converged on the same abstraction — convergence from
  different starting points is strong signal

## The disciplines

These are the foundation each persona builds on. Every agent applies all of
them.

### Start from the problem, not the solution

State what problem the user has before proposing any types, traits, or APIs.
"The user needs X" comes before "here's a `SessionStore` trait." If you can't
articulate the problem without referencing your solution, you don't understand
the problem yet.

### Sketch consumer code first

Before designing any API, write the code that *uses* it. The handler, the
call site, the configuration — the actual application code a user would write.
Not as an afterthought example, but as the first artifact. The consumer sketch
is the specification. It reveals:

- What the API actually needs to provide (and what it doesn't)
- Where type safety breaks down (runtime casts, stringly-typed maps)
- Whether the abstraction can actually serve its purpose (can middleware do
  async work? can the handler access typed data?)
- What the error paths look like from the consumer's perspective

If the consumer code is awkward, the API is wrong. Fix the API, not the
consumer code.

**When claiming consistency between two APIs** (e.g., "guards use the same API
as handlers"), write both consumer sketches side by side. If the method names,
signatures, or interaction patterns differ, the claim is false — address the
discrepancy before proceeding.

### Inventory before inventing

Before proposing a new type, trait, or abstraction, write down what already
exists that addresses the same need: in the codebase, in the language's stdlib,
in the ecosystem. If nothing exists, say so explicitly. If something exists,
start from it — extend, adapt, or compose it rather than building a parallel
structure.

On a greenfield project, "what already exists" means the language's built-in
types, stdlib, and idioms. A new type that duplicates what the language provides
is a smell.

This is not "reuse for reuse's sake." It's a forcing function against the
pattern-matching tendency to invent new abstractions when the problem doesn't
require them.

### Build up incrementally

Don't design the whole thing at once. Start with the smallest coherent piece.
Validate it with a consumer sketch. Then add the next piece and see if it fits.

At each step, ask:
- Does the new piece fit naturally with what's already there?
- Or is it fighting the existing design?
- If it's fighting, is the problem upstream? Would a different foundation make
  this piece fit naturally?

This is how you discover the shape of the problem. A big-bang design papers
over these tensions. Incremental exploration surfaces them while they're cheap
to fix.

### Every step changes what you can see

Every design decision is made with incomplete information. As you explore
further, the territory expands. At step B you could see one option and picked
it. At step D you can see two options that weren't visible from B. Step C might
provide evidence that the option you didn't pick is actually better. None of
this means B was wrong at the time — it means the landscape changed and you need
to look again.

The way you discover this is by constantly pushing on the design: "what if we
did it this other way?" "Does this conform to our principles?" "This doesn't
feel right — why?" These aren't idle questions. They're how you explore more of
the map. Each question might reveal new options, new evidence, or new
connections between decisions you thought were independent.

When the landscape changes, trace back through prior decisions. Not to check
whether they were "disproved" — that's too binary. Check whether the option
space has expanded. Maybe at step B you picked X because it was the only option
you could see. Now at step D you can see X and Y. Which is better given
everything you've learned? Maybe X is still right. Maybe Y is clearly better.
Maybe you need to explore further to tell. All three of those outcomes require
you to actually go back and look rather than assuming B is settled.

This is the core of the design loop. Skipping it is how you end up with designs
that look coherent on the surface but have quiet contradictions baked in — an
app-level-only registration model sitting next to a radix tree that already
knows the route hierarchy, because nobody went back to check whether "app-level
only" still made sense after discovering what the tree could do.

The cost of revisiting decisions is real but bounded. The cost of building on a
decision that should have been revisited compounds with every step forward.

### Question every abstraction

For each type, trait, or interface in your design, ask: is this here because the
problem requires it, or because other systems have it? "Sessions usually have a
SessionStore" is not a reason. "The framework needs to persist session data" is
a reason — but only if the framework actually needs to own that responsibility.

The strongest signal that you're importing rather than discovering: your design
has the same nouns as Rails/Phoenix/Express/Django and you're working in a
language with fundamentally different idioms.

### Reason about ownership boundaries

For every capability in the design, ask: does the framework/library own this, or
does the user own this? The answer should come from analysis of the consumer
sketch, not from "frameworks usually own this."

The test: if you removed this from the framework and the user did it themselves,
would anything break? Would anything get worse? If the user can do it better
(more type-safe, more flexible, more natural in the language), the framework
shouldn't own it.

### Look for footguns

After sketching a design, look for ways a user could do something that *looks*
correct but fails silently or in non-obvious ways:

- Can the user set up a configuration that appears valid but doesn't work?
- Can the user call methods in an order that compiles but produces wrong results?
- Are there boolean flag combinations that represent illegal states?
- Does the API make it easy to forget a step?
- Can the user confuse two values that have different semantics but the same type?
- Is any outcome implicit (success by silence, failure by absence)?

A candy-machine interface is one where the user can put the money in the slot
and push the button and get something other than what they expected. Good design
makes the right thing easy and the wrong thing impossible (or at least loud).

### When in doubt, ask

Design is full of decision points where two reasonable paths diverge. When you
hit one — when a design choice could go either way and you don't have a clear
reason to prefer one — stop and ask. Present the tradeoff, say what you're
uncertain about, and get input before committing to a direction.

The instinct to keep moving and produce a complete design is the enemy here.
An unasked question that leads to a wrong turn costs more than the pause. The
whole point of collaboration is that the human has context and judgment that
the model doesn't. Use it.

This applies especially to:
- Ownership boundaries (should the framework own this or the user?)
- Abstraction level (is this too much? too little?)
- When the consumer sketch reveals a tension and you're not sure which side to
  resolve it on
- When you're about to add something because other systems have it but you're
  not sure this system needs it

### Design is the map, the plan is one path

Design explores the territory — the full space of what could exist, how pieces
relate, where the constraints are. A plan picks one path through explored
territory to implement within a specific scope. The map doesn't stop being
useful once you pick a path. Keep mapping while you walk, because what you learn
during implementation changes your understanding of the territory.

Design insights that go beyond the current plan's scope are still valuable. They
inform constraints on what you build now (don't build something incompatible
with where you're headed) and get recorded (discussions, issues, plan notes) so
future work can use them. "This is the right design" and "we implement all of it
now" are separate decisions.

The disciplines in this skill — consumer sketches, abstraction questioning,
footgun scanning — are not a checklist you run once during a "design phase."
They're lenses you keep applying. Every time the design changes, run them again
on the changed parts and on the parts that depend on what changed. A discipline
that only runs once is a ritual, not a practice.

## Anti-patterns

These are the specific failure modes this skill exists to prevent. If you catch
yourself doing any of these, stop and reorient.

**Designing the complete system at once.** If your first artifact is a full
design document with all types, all interactions, all edge cases — you skipped
the discovery process. Back up. What's the smallest piece?

**Starting from solution shape instead of problem statement.** If your design
document opens with type definitions rather than "the user needs to..." — you're
retrieving, not designing.

**Importing patterns without questioning fit.** String-keyed maps, middleware
chains, context objects, store traits — these exist in many frameworks. Their
presence elsewhere is not evidence that your system needs them. Evaluate each
one against the actual consumer code.

**Consumer code as an afterthought.** If the example usage appears at the end of
the design document (or not at all), the API was designed without its primary
constraint. Move the consumer code to the beginning.

**Giving the framework too much responsibility.** When in doubt, the user owns
it. The framework can always take on more responsibility later; taking it back
is a breaking change.

**Claiming consistency without verifying it.** "This uses the same API as X"
is a testable claim. Write both usages side by side. If they don't match, the
design has a problem — either make them actually match or drop the claim and
design each on its own merits.

**Inventing when extending would suffice.** Proposing a new type when the
codebase, language, or stdlib already has something that serves the same
purpose. The new type may feel cleaner in isolation but adds a concept the user
must learn and the codebase must maintain.

## Pony-specific design guidance

When designing Pony APIs, libraries, or framework features:

- **Leverage the type system.** Union types for state instead of boolean flags.
  Distinct types for distinct semantics. `Any val` is almost always a sign that
  the design is avoiding a harder type-safety question — answer that question
  instead.
- **Make illegal states unrepresentable.** Pony's type system is strong enough
  to encode most constraints. If a combination of values is illegal, the types
  should prevent it from existing.
- **Be skeptical of patterns from dynamic-language frameworks.** Middleware
  chains, string-keyed context maps, convention-over-configuration — these
  patterns compensate for weak type systems. Pony has a strong type system. Use
  it. The idiomatic solution in Pony often looks nothing like the idiomatic
  solution in Ruby or Python.
- **Think about capabilities.** Who can read this? Who can write it? Who can
  send it across actor boundaries? If the design requires `val` but the consumer
  naturally produces `ref`, there's a friction point worth examining.
- **Understand what composition looks like in the specific context.** Don't
  assume a single composition pattern. In a web framework with actor-per-request,
  the handler actor might be the composition unit. In a parsing library, it
  might be function composition. In a template engine, it might be class
  hierarchies. Let the problem dictate the composition model.
