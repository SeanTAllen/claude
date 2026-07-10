---
name: vet-suspected-issues
description: How to handle a problem you spot while working on something else — decide whether it means the work at hand is scoped too small, and if it doesn't, capture it as a suspected issue instead of filing on the spot or chasing it, then after the main work's PR is open, vet each one (verify, scope, review) and file a correct issue or discard it. Load when you find an incidental problem mid-task, or when the main PR is open and you have suspected issues to work through.
disable-model-invocation: false
---

# Vet Suspected Issues

When you spot a problem while working on something else, you first decide whether it means the work at hand is scoped too small — the capture test below. If it does not, you do not file an issue on the spot and you do not chase it. You write it down as a suspected issue and keep going. After the main work's PR is open, you vet each one — verify it, scope it, review it — and only then file an issue, or discard it with a reason.

The reason for the deferral: issues filed on the spot are often wrong or incomplete. You file them from a sideways glance while loaded on the main task, off a single observation, without verifying the claim, searching for related cases, or reviewing the issue itself. Moving the work to a phase with full attention and real verification is what makes the issue correct.

## Three lists, kept distinct

- **Suspected issues** — this skill. Problems you noticed mid-work that the capture test places outside your change, held back for vetting before any issue is filed.
- **Parked items** — decisions awaiting Sean's input on the current change.
- **Decision log** — autonomous mode only; decisions you made and acted on, recorded for later review (see `/autonomous-mode`).

A suspected issue is none of the other two. It is not a parked decision and it is not a logged one — it is a problem to look into later.

## Capture (while working)

When you notice a problem, one question decides what happens to it — the capture test. **Does it mean the change you are making is scoped too small?**

Not whether it sits nearby. Not whether the ticket mentioned it. Whether the work you are doing should have covered it.

When you are fixing a bug, the question takes a sharp form: could one cause produce both this and the bug you were sent to fix? If it could, your fix is scoped to a symptom.

When you are adding a feature or reshaping code, the same question takes another form: would leaving this alone leave the thing you are building wrong or half-done? Not merely leave value on the table somewhere else — wrong, here, for what you set out to do. If so, your change is scoped to one instance of an idea that has several.

- **You cannot yet say what your own change is responsible for** → you cannot answer this about anything, so settle that first. Whatever the work is, you cannot say what belongs in it until you can say what it is for. When the work is a bug, that means you have not found the cause; go find it (`/pony-debug`). When it is a feature, its shape hasn't settled; go settle it (`/pony-software-design`). Write down what you found while you go, so it doesn't get lost. The uncertainty is never about the thing you found.
- **You cannot state any way it belongs** → suspected issue. Write it down and keep moving. Most of the time you cannot even begin the sentence — a stale comment three files away has nothing to do with what you are building, and seeing that costs nothing.
- **You can state a way it belongs** → look. If it does belong, it is part of the current work, not a suspected issue — handle it as a plan step (see "Research findings belong in the plan" in CLAUDE.md). If it turns out not to, it goes on the list like anything else.

Set the bar low. A wrong "this might belong" costs you a look. A wrong "this doesn't belong" costs you a change scoped to whatever somebody happened to notice, and nothing will tell you it happened. Nobody wrongly dismisses the stale comment. The wrong dismissals happen where a connection is plausible and passing on it is convenient.

**Looking is not expanding.** Following the hunch commits you to nothing but finding out. If it does turn out to belong, it goes in the change. What stays a separate decision is anything *further* the looking turned up — the cleanup next door, the refactor you can now see. Keep the two apart: if looking meant committing to all of that, you would stop looking.

Each entry on the list records enough to vet it later without rediscovering it:

- What you saw, and where (`file:line`).
- What you were doing when you noticed it.
- Your initial hypothesis — **marked as a hypothesis, not a conclusion.**
- Why you think it is separate from the work at hand — one sentence.

That last line is cheap to write now and hard to reconstruct later. It is also the sentence that reads as plainly wrong once a shared cause turns up, which is what it is for.

Capture bar: a concrete problem you can point at in code. A vague "this could be nicer" does not go on the list.

Keep the list in the conversation, the way the decision log lives there. When the main PR opens, surface the open suspected issues so the vetting phase works from them and a long session doesn't lose them.

## Re-read the list once your change comes into focus

The moment you can say what your change is responsible for — for a bug, when you know why it happens; for a feature, when its shape settles — and before you write any code, read the suspected-issue list once and ask which entries it now covers.

This catches what capture cannot. Two symptoms of one cause often look nothing alike. A crash on an empty config file and a logger that misbehaves at startup share no description, so nothing at capture time connects them. Once you are holding the initialization-order bug, both are obvious. A feature does the same thing: the shape you settle on turns out to cover something you had already written off.

It costs one pass over a list you already wrote, at the one moment when the answer is free. Anything your change now covers stops being a suspected issue and becomes part of the work.

## Vet (after the main PR is open)

Run this after the main work's PR is open, as its own closing phase — not while the main work is in flight. The whole point is that it is not a side quest. (If a suspected issue turns out to be specifically about the work at hand, it stops being one and folds into that work instead — though normally you caught that when you found the cause.)

Lock down each suspected issue. Default to the lightweight path; escalate when one is bigger than it looked.

1. **Establish that it is real.** Spawn a fresh-context subagent. Give it the suspected issue — the observation, the location, your hypothesis — and have it read the actual code and judge from evidence, not argument ("How do you know that you know that?"). For a behavioral bug that means reproducing it: load `/pony-debug` and work the protocol until the failure happens in front of you. Outcomes:
   - **Confirmed** — it is real. Continue.
   - **Not a problem** — discard it and record why. This is a real outcome, not a failure. It is the wrong issue caught before it ships.
   - **Needs more information** — dig until you can confirm or discard.
2. **Debug it.** Carry on through `/pony-debug`, as far as the fix, without writing one. That gives you the cause and every place it reaches. A premature issue describes one symptom; this is what finds the whole shape, and it is what stops issues from missing points.
3. **Check for duplicates.** Search the existing issues so you do not file one that is already there.
4. **Draft the issue** under the existing conventions — "An issue body is the issue, nothing else" and "GitHub issues have types and labels" in CLAUDE.md. Load `/how-to-write` for the writing.
5. **Review the draft on two axes.**
   - **Correctness and completeness** — a fresh-context reviewer checks that the claim holds, the scope is right, and nothing is missing. This is the direct fix for issues that miss points.
   - **Voice and craft** — run `/review-for-seans-voice` over it; it scales to size (cheap on a short issue, an ensemble on a long one).
6. **File it.** Set the type (`/graphql-bash` has the recipe; personal-account repos have none — skip it).

**Escalate** from the lightweight path to a heavier ensemble review when a suspected issue turns out to be a pattern across the codebase or a design problem rather than a single bug — `/pony-code-review` for code, `/pony-software-design` for a design problem.

If vetting a suspected issue surfaces a question that is Sean's to decide — a design call, an ambiguous tradeoff — it stops being a suspected issue and becomes a parked item (a decision-log entry in autonomous mode), rather than being forced into an issue.

**Fast path:** a problem with nothing behavioral behind it — a typo, a stale comment — skips steps 1 and 2. Check that first: a comment recording a gap in behavior is a bug with a docstring on it, and takes the full path. When there is genuinely nothing behavioral, there is no failure to reproduce and no cause to find. Give it a light check and file. Anything that claims a bug or a behavior takes the full path. "It's obviously fine to skip" is exactly the judgment that has been going wrong.

## In autonomous mode

The vetting is part of reaching the goal, so it runs to completion — including filing the issues. Filing them is an authorized outward action for this phase, the same way opening the PR is the authorized outward action for the main work (see `/autonomous-mode`). Surface the results in the end-of-run report alongside the decision log: which suspected issues became filed issues, with their numbers, and which you discarded and why.
