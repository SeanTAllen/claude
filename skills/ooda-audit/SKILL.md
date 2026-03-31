---
name: ooda-audit
description: Audit skills and CLAUDE.md for instructions that discourage continuous observation, orientation, and re-evaluation. Run manually to find OODA violations.
disable-model-invocation: false
---

# OODA Audit

Audit `~/.claude/CLAUDE.md`, project CLAUDE.md files, and all skills for
instructions that work against continuous observe-orient-decide-act cycles.

Run this manually when you suspect instructions have drifted or after a session
where pipeline thinking caused problems.

## Scope — read this first

This audit has one job: find instructions that discourage continuous
observe-orient-decide-act cycles. That's it.

Do NOT flag:
- Instructions that seem heavy, verbose, or overkill for small tasks
- Process choices you'd do differently (ensemble vs solo, review loops, etc.)
- Style, wording, or organizational issues
- Missing instructions (things that should exist but don't)
- General "this could be better" feedback

The test for every finding: **does this instruction cause someone to skip
observation, orientation, or re-evaluation that they should be doing?** If you
can't point to a specific moment where the instruction causes blindness, it's
not a finding. Drop it.

## What is an OODA violation?

Good instructions build in feedback loops. They encourage observing the current
state, orienting against what you know, deciding based on evidence, acting, and
then observing again. Bad instructions create pipelines — sequences of steps
that execute without re-evaluation, or workflows that treat phases as one-way
gates.

An OODA violation is any instruction that:

1. **Encourages blind execution** — "do X then Y then Z" with no moment to
   check whether Y still makes sense after doing X. The presence of sequential
   steps isn't the problem; the absence of re-evaluation between them is.

2. **Treats phases as one-way gates** — implies that once you're past design
   and into planning, or past planning and into implementation, you don't look
   back. Design, planning, and implementation are concurrent activities. New
   information at any phase should trigger re-evaluation of prior phases.

3. **Conflates observation with action** — "when you see X, do Y" without
   space to orient. Seeing X might mean different things in different contexts.
   The instruction should leave room to ask "why am I seeing X?" before
   prescribing the response.

4. **Suppresses re-evaluation** — any language that discourages revisiting
   decisions, questioning the plan, or raising concerns during execution.
   "Don't stop" and "keep moving" are red flags unless they're specifically
   about not seeking approval (which is different from not re-evaluating).

5. **Missing observe points** — a workflow description where multiple
   significant actions happen with no point where you stop and check whether
   the results match expectations. If a workflow has steps that produce
   observable output but no instruction to look at that output before
   proceeding, that's a gap.

6. **Prescribes action without orientation** — "always do X when Y happens"
   without considering that Y might have different causes or contexts. Good
   instructions say "when you see Y, consider A and B, then decide." Bad
   instructions skip the consider step.

## How to run the audit

1. Read `~/.claude/CLAUDE.md` in full.
2. Read the project CLAUDE.md (if in a project directory).
3. Read every skill file in `~/.claude/skills/*/SKILL.md`.
4. For each file, evaluate every instruction against the violation categories
   above.
5. Report findings grouped by file, with:
   - The specific text that violates
   - Which violation category it falls under
   - A concrete scenario where the violation would cause a problem
   - A suggested revision (or "delete" if the instruction is pure noise)

## Severity levels

**High** — The instruction actively causes pipeline behavior. It will
predictably lead to missed re-evaluation in common workflows. Example: "execute
all steps to completion" without any re-evaluation language.

**Medium** — The instruction has a gap where an observe-orient moment should
exist but doesn't. It won't always cause problems, but in complex work it
creates a blind spot. Example: a multi-step workflow with no checkpoints.

**Low** — The instruction is slightly pipeline-flavored but unlikely to cause
harm in practice. Example: language that implies sequential phases but doesn't
explicitly discourage re-evaluation.

## After the audit

Present findings to Sean. Don't make changes — the audit identifies issues, the
human decides what to do about them. Some findings might be intentional
trade-offs (e.g., "don't stop for approval at each step" is intentionally
suppressing one kind of pause to avoid a different problem). Those trade-offs
should be discussed, not unilaterally resolved.
