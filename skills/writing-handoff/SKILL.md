---
name: writing-handoff
description: "The process for producing any writing on Sean's behalf: the agent holding the context designs the piece with Sean, a fresh agent writes the words, and the context-holding agent checks the result for fidelity. Load before writing anything for Sean — comments, commit messages, issues, discussions, blog posts, LWIP, all of it."
disable-model-invocation: false
---

# Writing handoff

Writing for Sean fails in a specific way. The agent that did the thinking writes
the prose, and it can't tell that its own prose is unclear. It has the whole
backstory loaded, so a compressed, idiom-laden sentence reads as plain to it,
because it fills in the missing meaning from memory. A reader without that memory
gets nothing. This is the curse of knowledge, and it is why the agent that holds
the context should not be the agent that writes the words.

This skill splits the work across two agents. The context-holding agent gets the
shape and the facts right; a fresh agent turns them into words; the context-holding
agent then checks that the words still say what the facts say. Each agent works the
half its context is good for, and neither does the half its context is bad for.

The same context that makes an agent correct makes it a poor plain writer. The
same freshness that makes an agent a good plain writer makes it unable to judge
whether the content is right. So the division is not a workaround; it is the point.

## The three steps

1. **Design the piece with Sean — the context-holding agent.** The audience, the
   narrative, and what goes in and stays out are design choices, so this step is a
   conversation and not a deliverable. Produce the audience, the narrative, and the
   facts, show them to Sean before any prose exists, and expect to revise.
   Iterating here is the process working. It is cheap, and everything downstream is
   built on it.

   **The artifact carries facts with their sources, not sentences for the reader.**
   Quote each fact from wherever it came from, or mark it as something Sean said.
   Write a sentence meant to appear in the piece and you are the author again: the
   writer adopts it whole, because a locked draft is exactly what it must not
   change. Your paraphrase then ships looking as sourced as everything around it.

   Gaps are still fatal, because a fresh writer fills a gap by guessing and guessing
   is inventing, so get every fact, every caveat, and the load-bearing structure
   down. **This is where content correctness is checked** — by whatever review the
   work warrants (a technical review, a principle review, running the thing). Do not
   hand off until the content is right, because the check in step 3 does not catch
   content errors (see Guardrails).

   The design iterates with Sean; the handoff does not. Once he agrees on the
   direction and the content is right, it is locked for the writer — no fact
   changes from there. The lock is on the writer, not on the design itself: if a
   later step shows the design was wrong, the context-holding agent reopens step
   1 with Sean rather than patching it downstream (see Guardrails).

2. **Write it — a fresh agent.** Spawn a fresh-context sub-agent. Give it the
   locked draft, the rulebook for the form (below), and, for voice forms, two or
   three of Sean's real posts for calibration. It has no accumulated context, so it
   has to make the words carry the meaning; it can't lean on a backstory it doesn't
   have. Let it reshape for plainness and flow — that latitude is what produces a
   clear draft — but bind it hard: change no fact, drop no caveat, invent nothing.
   It returns the rewritten draft to the orchestrator; it takes no external action.

3. **Check the result — the context-holding agent.** For a **voice form**, run
   `/review-for-seans-voice` on the fresh draft. It is the full voice-and-craft
   ensemble, and it does two jobs at once: its content-honesty and accuracy lenses
   are the fidelity check (did the draft keep every fact and caveat, and invent
   nothing), and its other lenses — voice, agency, narrative, orientation,
   tightness — catch the register drift and anthropomorphizing a fresh writer can
   introduce. For a **plain form** taken through the full handoff, run a lighter
   fidelity check by hand: did the draft keep the fact and describe the code
   correctly. Either way, the context-holding agent is the right judge of fidelity —
   it knows the ground truth — and the wrong judge of whether the prose reads
   plainly, for the same reason it couldn't write plainly. So when the check finds a
   dropped or distorted fact, hand the fix back to the writer to re-phrase; do not
   rewrite the wording yourself, or you compress the plainness right back out. If a
   fix introduces a new problem, that is another short round: writer, then check
   again.

## Which rulebook the fresh writer uses

The form decides how the writer writes. Hand it the matching rulebook:

- **Voice forms** — blog posts, LWIP, discussions, issues, PR descriptions, commit
  messages, announcements: `how-to-write` for the process, `seans-voice` for the
  sound, and the form skill where there is one (`/blog-post`, `/sean-lwip`). These
  read like Sean.
- **Plain forms** — comments, docstrings, release notes, READMEs: `pony-prose`, plus
  `pony-comments` for comments and docstrings. These only have to be plain; there is
  no voice and no narrative.

## Scale it

The full handoff — a fresh sub-agent plus a step-3 review — earns its keep on
substantial prose: a blog post, an LWIP entry, a discussion, a long issue, a PR
description. On a one-line commit subject, a short PR comment, or a docstring, it is
pure overhead, and slow.

So above a couple of paragraphs, run the full handoff. Below it, the context-holding
agent writes the draft, then does a **fresh-reader pass on its own draft**: read it
as if you have only the words, not the backstory, and rewrite anything that is clear
only because you know what it means. For a short voice form, `/review-for-seans-voice`
still runs, but on its own cheap inline path rather than the full ensemble. Same
principle throughout — fresh eyes beat the curse of knowledge — at a cost that fits
the size, which is how `/review-for-seans-voice` already scales (full ensemble over
two paragraphs, cheap inline pass under).

## Guardrails

- **The fidelity check catches only what the writer changed.** A wrong fact that was
  already in the locked draft passes through it unchanged — the writer renders it
  plainly, the check confirms it matches, and now it is plausible and wrong. Content
  correctness is a separate, earlier gate (step 1), not something step 3 catches.
- **The context-holding agent must not rewrite the wording in step 3.** Its context
  is why it writes badly; using it to "fix" the fresh draft's wording undoes the
  handoff.
- **The writer changes no fact, drops no caveat, invents nothing.** Reshaping for
  plainness is allowed and wanted; changing meaning is not. The step-3 check enforces
  this.
- **Your prose in the artifact becomes the piece's defects.** A fact with a citation
  is checkable, and the writer renders it in its own words. A sentence you drafted is
  unverified, and the writer adopts it whole. Decisions still have to be recorded, or
  they get lost on any restart — but record them as constraints the writer applies
  ("treat these two absences as one", "no cognition verbs on that function"), never
  as sentences it can lift.
- **Reviews test the implementation; they cannot validate the design.** A clean
  step-3 review means the prose matches the facts and follows the rules. It says
  nothing about whether the audience, the narrative, or the selection were right.
  Those get settled in step 1, with Sean, or not at all. Running more review passes
  on a piece whose design is wrong produces clean reports and a piece he rejects on
  sight.
- **A design problem sends it back, not around.** A design error usually surfaces
  in the writing or the check — the arc doesn't carry once it's drafted, the payoff
  doesn't land. When it does, stop and reopen step 1 with Sean. Don't hand it to the
  writer to patch, and don't run it around the review loop again — that only
  produces the clean report on a rejected piece from the bullet above. Going back to
  the design is the process working, not a break from it, the same move
  `how-to-write` names.
- **Adherence is the weak point.** Nothing forces the handoff — it runs because the
  agent follows this process. On any writing task for Sean, run it; do not let the
  context-holding agent talk itself into writing the final words directly, which is
  the exact failure this skill exists to prevent.
