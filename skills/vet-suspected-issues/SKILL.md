---
name: vet-suspected-issues
description: How to handle a problem you spot while working on something else — capture it as a suspected issue instead of filing on the spot or chasing it, then after the main work's PR is open, vet each one (verify, scope, review) and file a correct issue or discard it. Load when you find an incidental, out-of-scope problem mid-task, or when the main PR is open and you have suspected issues to work through.
disable-model-invocation: false
---

# Vet Suspected Issues

When you spot a problem while working on something else, you do not file an issue on the spot and you do not chase it. You write it down as a suspected issue and keep going. After the main work's PR is open, you vet each one — verify it, scope it, review it — and only then file an issue, or discard it with a reason.

The reason for the deferral: issues filed on the spot are often wrong or incomplete. You file them from a sideways glance while loaded on the main task, off a single observation, without verifying the claim, searching for related cases, or reviewing the issue itself. Moving the work to a phase with full attention and real verification is what makes the issue correct.

## Three lists, kept distinct

- **Suspected issues** — this skill. Incidental, out-of-scope problems you noticed mid-work, held back for vetting before any issue is filed.
- **Parked items** — decisions awaiting Sean's input on the current change.
- **Decision log** — autonomous mode only; decisions you made and acted on, recorded for later review (see `/autonomous-mode`).

A suspected issue is none of the other two. It is not a parked decision and it is not a logged one — it is a problem to look into later.

## Capture (while working)

When you notice something incidental, do not investigate it and do not file it. Triage:

- **Related to the work at hand** → it is part of the current work. Handle it as a plan step (see "Research findings belong in the plan" in CLAUDE.md). It does not go on this list.
- **Out of scope** → add it to the suspected-issue list and keep moving.

Each entry records enough to vet it later without rediscovering it:

- What you saw, and where (`file:line`).
- What you were doing when you noticed it.
- Your initial hypothesis — **marked as a hypothesis, not a conclusion.**

Capture bar: a concrete problem you can point at in code. A vague "this could be nicer" does not go on the list.

Keep the list in the conversation, the way the decision log lives there. When the main PR opens, surface the open suspected issues so the vetting phase works from them and a long session doesn't lose them.

## Vet (after the main PR is open)

Run this after the main work's PR is open, as its own closing phase — not while the main work is in flight. The whole point is that it is not a side quest. (If a suspected issue turns out to be specifically about the work at hand, it stops being one and folds into that work instead.)

Lock down each suspected issue. Default to the lightweight path; escalate when one is bigger than it looked.

1. **Verify it's real.** Spawn a fresh-context subagent. Give it the suspected issue — the observation, the location, your hypothesis — and have it read the actual code and judge whether the problem is real, empirically, not by argument ("How do you know that you know that?"). For a behavioral bug, verifying means reproducing it (load `/pony-debug` in a Pony project). Outcomes:
   - **Confirmed** — continue.
   - **Not a problem** — discard it and record why. This is a real outcome, not a failure. It is the wrong issue caught before it ships.
   - **Needs more information** — dig until you can confirm or discard.
2. **Find the true scope and root cause.** One instance or a pattern? What is the actual extent? A premature issue describes one symptom; vetting finds the whole shape. This is what stops issues from missing points.
3. **Check for duplicates.** Search the existing issues so you do not file one that is already there.
4. **Draft the issue** under the existing conventions — "An issue body is the issue, nothing else" and "GitHub issues have types and labels" in CLAUDE.md. Load `/how-to-write` for the writing.
5. **Review the draft on two axes.**
   - **Correctness and completeness** — a fresh-context reviewer checks that the claim holds, the scope is right, and nothing is missing. This is the direct fix for issues that miss points.
   - **Voice and craft** — run `/review-for-seans-voice` over it; it scales to size (cheap on a short issue, an ensemble on a long one).
6. **File it.** Set the type (`/graphql-bash` has the recipe; personal-account repos have none — skip it).

**Escalate** from the lightweight path to a heavier ensemble review when a suspected issue turns out to be a pattern across the codebase or a design problem rather than a single bug — `/pony-code-review` for code, `/pony-software-design` for a design problem.

If vetting a suspected issue surfaces a question that is Sean's to decide — a design call, an ambiguous tradeoff — it stops being a suspected issue and becomes a parked item (a decision-log entry in autonomous mode), rather than being forced into an issue.

**Fast path:** a problem with nothing behavioral to verify — a typo, a stale comment — skips the reproduction in step 1. Give it a light check and file. Anything that claims a bug or a behavior takes the full path. "It's obviously fine to skip" is exactly the judgment that has been going wrong.

## In autonomous mode

The vetting is part of reaching the goal, so it runs to completion — including filing the issues. Filing them is an authorized outward action for this phase, the same way opening the PR is the authorized outward action for the main work (see `/autonomous-mode`). Surface the results in the end-of-run report alongside the decision log: which suspected issues became filed issues, with their numbers, and which you discarded and why.
