---
name: principle-review
description: Load at mandatory review checkpoints (after planning, before opening a PR). Covers both manual and automated principle review protocols.
disable-model-invocation: false
---

# Principle Review Protocol

A structured code review that combines general correctness checking with systematic evaluation against the principles in ~/.claude/CLAUDE.md and the project CLAUDE.md.

## Manual Mode

Sean says "conduct a principle review" to a Claude with repo access:
1. Ask Sean for the sources to review (PR URL, discussion link, local branch changes, etc.).
2. Read the source material (design doc, spec, issue), read the code, build and run tests.
3. **Preamble**: List the principles identified as relevant to this review. Ask Sean if any are missing or if there are clarifying questions before proceeding. Go slow to go fast.
4. Deliver the review in two parts: (a) general correctness findings — bugs, logic errors, spec compliance, and (b) principle-by-principle evaluation — each relevant principle listed with pass/fail and supporting evidence. Show both passes and failures; passes prove coverage, failures are actionable.
5. After delivering the review to the screen, prompt Sean for a file path to write it to so he can share it with the code's author.

## Automated Mode

The writer session spawns a reviewer Task subagent:
1. Use Task with subagent_type="general-purpose" and model="opus". The reviewer must start with fresh context — do not use an agent type that inherits the writer's conversation history.
2. The prompt must include:
   - Instructions to read ~/.claude/CLAUDE.md and the project CLAUDE.md for principles and project context.
   - The sources to review (branch name, base branch, design doc location — discussion URL or issue URL).
   - Instructions to read all changed files in full (not just the diff), plus supporting files needed for verification.
   - Instructions to build and run tests.
   - Skip the preamble step (no interactive approval inside a subagent).
   - Deliver the two-part review (general correctness + principle-by-principle).
   - **Context from prior reviews**, if any: settled decisions ("Sean ruled X is acceptable"), opened issues ("issue #N tracks Y — don't re-flag"), or fixes already in progress.
3. **Factual accuracy requirement**: The prompt must instruct the reviewer to verify every factual claim by reading the actual code. Do not summarize from memory or inference. If stating a count (e.g., "5 property tests"), verify by reading the test list.
4. **Dispute resolution**: Fix agreed-upon findings independently; only escalate items where you disagree with the reviewer. Present the dispute to Sean. Sean rules. Pass the ruling to the next reviewer as prior-review context in the prompt. Rulings are transient — they belong in the prompt, not in CLAUDE.md, because they're specific to the current review cycle.

## Both Modes

Assume counterfactual testing has already been performed — do not flag it as missing.

## Behavioral Guidance During Review Loops

At any point during the review loop — when fixing findings, when unsure about a reviewer's suggestion, when making tradeoff decisions — stop and ask Sean. The automated review removes Sean as a gatekeeper, not as a collaborator. After a clean review at the pre-PR checkpoint, go straight to opening the PR — don't stop to report "ready for PR" and wait for permission. Open the PR, then report completion with the PR URL.
