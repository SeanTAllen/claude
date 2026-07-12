---
name: autonomous-mode
description: A mode of working where you pursue a named goal without stopping at the usual mid-work approval gates — you make the calls you would normally stop to ask Sean about, write each one in a decision log, and keep going. Load when Sean tells you to work toward a goal on your own and record decisions for later review ("work autonomously towards the goal," "keep going and record decisions," "push on to a fix," "get to PR on your own").
disable-model-invocation: false
---

# Autonomous Mode

A way of working, not a special occasion. Sean names a goal and tells you to work to it on your own. You pursue the goal, make the decisions you would normally have stopped to ask him about, write each one down, and keep going. You and Sean review the decisions afterward.

This is a deliberate trade: the default workflow stops at human gates so Sean can steer mid-stream; this mode defers those gates so the work runs end to end. The results are meant to be as good as the interactive workflow — just reached without Sean in the middle of every decision.

Sean picks this mode for different reasons — he's away, or he just wants the work to run without interruption. The reason doesn't change how it works.

## When this is active

The signal is Sean handing you a goal to carry to its endpoint on your own — telling you to keep going through the decisions instead of stopping at each one. He's usually said it by pairing the work ("work autonomously towards the goal," "keep going," "get to PR with this") with the record-keeping ("record any decisions you'd have stopped to ask me about," "record decisions we should review"). Both halves are the mode: pursue the goal yourself, and log the calls for Sean to review.

It is an instruction, not a question. If Sean *asks* whether you could work this way, that's a question — answer it and wait (see "Answer questions, then wait" in CLAUDE.md). And if it's genuinely unclear whether he means this mode or just "keep going on this one step," ask before switching.

## What changes

The default workflow has human gates: Sean approves the plan before you implement, and you stop to discuss decisions as they come up. In this mode those gates are deferred. You don't stop for approval. You decide, record the decision, and continue.

The recording bar, in Sean's words: **record anything you would have stopped to ask me about.** If a decision would have triggered a "let me check with Sean" in the normal workflow, it goes in the log instead — and you proceed with the option you judge most reasonable. The biggest gate you're deferring is plan approval: the plan is a decision like any other, so record it as the first entry and keep going.

Decisions and actions are handled differently:

- **Decisions** — which approach to take, which tradeoff to accept, what to name something. You make the call and log it.
- **Irreversible or outward-facing actions** — deleting things, force-pushing over someone else's work, posting or sending anything outside the repo. These are not decisions to log; they still wait for Sean. The one exception is the named endpoint itself: if the goal is "get to PR," opening the PR — and the ordinary steps to reach it, like pushing your own branch — is authorized. Likewise, when the work turned up suspected issues, the closing vetting that follows the PR may file the issues it produces — that closeout is part of finishing the goal, not a new external action beyond it (see `/vet-suspected-issues`). Anything destructive or external beyond reaching that endpoint waits, same as always.

## What does not change

Removing the approval gate does not remove anything else.

- **Reviews still run.** The plan review loop and the pre-PR review loops still happen — they are quality gates, not approval gates. Where those loops normally tell you to stop and ask Sean — a disputed finding, a judgment call, escalating a disagreement with a reviewer — autonomous mode turns that into the same decide-and-log move: make the call, record it, keep going. Sean reviews it with the rest of the log. This mode removes Sean as a gatekeeper, not as a collaborator.
- **Re-evaluation still happens.** "Don't stop for approval" is not "don't re-think." Keep observing and re-orienting as you learn. If the plan stops making sense, change it — and log that.
- **Honesty rules apply in full.** The decision log records the real decisions and the real reasoning, not a tidy story told after the fact. Same standard as everything else in the global CLAUDE.md.

## The decision log

One entry per decision you would have stopped to ask about. Each entry:

- **The decision** — what was in front of you.
- **The options** — what you considered.
- **The call** — what you chose, and why.

What earns an entry is a genuine fork: more than one option was defensible, and Sean might have chosen differently. A step with only one defensible path is not a decision, no matter how much work it took or how much rode on it. Neither is anything that follows automatically from a decision already in the log: those consequences belong to the entry they came from, not to entries of their own.

Keep the log in the order you made the decisions, start to finish. Each one was made standing on the ones before it, so the order is what shows Sean how you got where you got. A log sorted any other way hides that — he cannot see which later calls rest on an earlier one he disagrees with.

The log is not a list of parked items. Parking means "I'm not doing this, it's waiting on Sean." This is the opposite: the decision is made and acted on; the entry is the record. In this mode you decide and log; you don't park.

It is also not a log of mistakes you caught and fixed. A command that misfired, a bug in your own work — you would never have stopped to ask Sean whether to fix these, so they aren't decisions and don't go in the log. They don't go in the report either — see "A mistake you already fixed is not a load-bearing fact" in CLAUDE.md. A mistake has a right answer; it isn't a fork Sean would weigh in on. That's what separates it from a backtrack (see "When you get stuck"), where the path you abandon is itself defensible — a real option, not an error — so you do log the switch.

Surface the log when you report to Sean — in the conversation, where he reviews and ratifies it. It stays in the conversation; it's the record of the decisions, not part of the PR.

## When you get stuck

Getting stuck is not a reason to stop — it's usually a reason to back up. If you went A → B → C and C is a dead end, the fix is normally to roll back to B, rethink it, and take another path, not to halt and wait. Treat earlier decisions as revisable, not fixed. Try the reasonable alternative paths before you consider stopping. A backtrack is a decision like any other — log what you abandoned, why, and what you took instead.

Stop only when:

- **The goal itself is wrong** — infeasible, or built on a broken premise. No path reaches it because it shouldn't be reached. Surface that; don't bury "this whole thing is a mistake" in a log entry and plow on.
- **Backtracking has run out** — you've tried the reasonable alternative paths and still can't reach the goal. Surface where you got to and what you tried.
- **A single decision has no defensible option** and blocks the goal, and backing up doesn't open another route. Rare — most decisions have a most-reasonable option; make it and log it.

## At the end

When the goal is reached, report: the outcome first, then the decision log, in the order the decisions were made. Sean reads it start to finish and ratifies the calls or redirects them; a redirected decision gets unwound where it can be, along with whatever was built on top of it.
