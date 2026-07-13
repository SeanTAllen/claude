---
name: reap-memories
description: Review the memory inbox — the plain fallback captures written to ~/.claude/memory-inbox during sessions — and decide with Sean which few are worth promoting into a CLAUDE.md or a skill and which to discard, opening a PR per promotion. Load when Sean runs /reap-memories.
disable-model-invocation: true
---

# Reap Memories

The memory inbox holds captures the agent wrote during sessions — plain, worth-remembering facts, written the way the built-in auto-memory would but to a directory nothing loads. Capture is deliberately permissive, so most of what's here is noise: drifted, trivial, one-off, or already said somewhere. Reaping is where the filtering happens. You read the inbox with Sean, keep the few captures worth having, decide where each belongs, and promote it there by PR. Then you clean the inbox out.

Most captures get discarded. That is the expected outcome, not a failure.

This skill has external side effects — it opens PRs — so it is human-initiated only (`disable-model-invocation: true`). Sean runs it; the model does not trigger it on its own.

## What the inbox is

- **Location**: `~/.claude/memory-inbox/<repo>/<file>.md` — one file per captured memory. Each file's parent directory is the repository the capture came from, so that origin never needs to be written inside the file; it's how you route the candidate.
- **Format**: each file is one memory — one or two plain lines, a fact stated so it stands on its own. No evidence, no session narration.
- **Inert**: nothing loads or reads this directory during normal work. A capture has no effect on any session until it is reaped here.

## The reap

1. **Understand the inbox** before you start: the points above. Most memories will be discarded.
2. **Gather.** Read every `~/.claude/memory-inbox/*/*.md`. If the inbox is missing or empty, there is nothing to reap — say so and stop. Present the memories to Sean grouped by origin repository.
3. **Triage.** For each memory, decide keep-or-discard. Discard the drifted, the wrong, the trivial, the one-off, and the session-specific. Keep only what is durable, general, and worth knowing at the start of a future session.
4. **Propose a home** for each survivor — see "Where a survivor goes" below.
5. **Check it isn't already said.** Read the current content of the proposed target (the relevant CLAUDE.md or skill). If the fact is already there, discard it — or, if the survivor sharpens what's there, fold it into the existing rule rather than adding a near-duplicate. Minting a second rule that says almost the same thing is the drift problem in a new form; this step is most of the work.
6. **Decide each survivor with Sean, one at a time.** Present the fact, its origin, and the proposed home. This is you and Sean deciding together — not an ensemble review. Each survivor ends as **promote** or **discard**; there is no holding one for later.
7. **Promote by PR.** For each accepted promotion, make the change in the target repo on a branch (never main), following that repo's conventions — including its changelog if it has one (ponylang/llm-skills does and needs `/pony-release-notes`; seantallen/claude does not). Write the PR in Sean's voice (`/seans-voice`, `/review-for-seans-voice`). One PR per promotion, or one per target repo — Sean chooses per run.
8. **Clean out.** Once a promotion's content is safe in a PR branch (git preserves it — don't wait for merge), delete its inbox file. Delete the files of discarded memories too. When every memory is promoted or discarded, the reap is done.

## Where a survivor goes

Route by what the fact is about, and lean on the existing routing conventions rather than reinventing them:

- **A general working habit, preference, or correction of Sean's** → his global CLAUDE.md, or a new/existing personal skill → **seantallen/claude**.
- **A Pony language, stdlib, or tooling fact, or a Pony workflow rule** → the right pony skill → **ponylang/llm-skills**. Use the `pony-skills` routing index to pick the skill.
- **A fact specific to one project** → that project's `CLAUDE.md` or `AGENTS.md`. Use `pony-agents-md` for what belongs there versus what doesn't.
- **Something substantial and standalone** → a new skill in whichever repo owns it.

`pony-agents-md` is language-agnostic and governs the CLAUDE.md/AGENTS.md decision for any project. `pony-skills` is Pony-specific and only matters for Pony-destined promotions. Both are installed in `~/.claude/skills`, so they load in any session; this skill assumes they're present. If the pony index is ever absent, the global-versus-project routing above still works through the language-agnostic `pony-agents-md`.

## What reaping does not do

Promotions do not go through the pre-PR review ensemble. Deciding a promotion is you and Sean looking at one candidate and agreeing where it goes — that decision is the review, right-sized. But a promotion is still a real change to a repo, so it rides that repo's normal mechanics: a branch, a PR, its conventions, its changelog. The review is collapsed into the decision; nothing else is skipped.
