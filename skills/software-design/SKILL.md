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

## The disciplines

These aren't a checklist you run top-to-bottom. They're lenses you apply as you
explore. Sometimes one sends you back to revisit another. The design process is
an OODA loop — observe the problem, orient around what the consumer needs,
decide on the smallest next piece, act by sketching it, then loop.

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
