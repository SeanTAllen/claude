---
name: review-for-seans-voice
description: Ensemble review of prose written in Sean's voice — blog posts, LWIP, GitHub discussions and issues, commit messages, PR comments and descriptions. Runs lens personas in parallel, checks the draft against seans-voice and the craft rules, and returns Fix/Park findings. Load after a draft exists, before it ships.
disable-model-invocation: false
---

# Review for Sean's Voice

The review that applies `seans-voice` to a draft. It does not replace `seans-voice`
— it reads it. `seans-voice` is the rulebook (what the voice is); this skill is the
machine that checks a draft against the rulebook and the craft rules with fresh,
decorrelated eyes.

A skill's own built-in review is the **floor**. For any prose in Sean's voice, this
runs **on top** of whatever review the drafting skill specifies.

This skill has **no dependency on any ponylang/pony skill** — Sean writes personal
prose that must load only Sean-world skills. All the ensemble mechanics it needs are
inlined below; nothing is loaded from `pony-ensemble` / `pony-synthesize`.

## When to run

After a draft of prose in Sean's voice exists, before it ships. Artifacts:

- Blog posts — personal (seantallen.com) and LWIP / ponylang.
- GitHub discussions and issues written in Sean's voice.
- Commit messages.
- PR comments and PR descriptions.

Not for: release notes / CHANGELOG entries, READMEs, or other templated/structured
docs — those have their own skills and aren't voice prose.

## Two rulebooks this skill reads

- **`seans-voice`** — the voice rulebook. The Voice persona reads it in full.
- **`references/craft-rules.md`** (alongside this skill) — the non-voice craft rules
  (narrative, reader-orientation, tightness, content-honesty/source-fidelity). The
  other four personas read the relevant sections.

## Mode selection by size

Count the draft's **prose paragraphs**: blank-line-separated blocks of running prose.
Do not count fenced code blocks, YAML/metadata, headings, or list items. A commit
message's subject line and a trailer block (`Closes #N`) are not prose paragraphs.

```
PARAGRAPH_THRESHOLD = 2
```

- **> 2 prose paragraphs → full review.** The five-lens ensemble below — six when the
  draft has code or technical claims, where the conditional Accuracy lens joins.
- **≤ 2 prose paragraphs → cheap inline pass.** No subagents. The orchestrator reads
  the draft once against `seans-voice` and the content-honesty section of
  `craft-rules.md`, plus the mechanical pre-check, and returns Fix/Park findings
  directly. This is the path for most commit messages and short PR comments.

`PARAGRAPH_THRESHOLD` is one line on purpose — move it (or switch a specific run to
full) when the size heuristic misjudges an artifact. A manual **lightweight** ensemble
(Voice + Narrative + Content-honesty only) is also available as an override when a
mid-size artifact wants more than the inline pass but not the full ensemble
(Content-honesty still needs its source bundle).

## Source bundle

The content-honesty persona can only catch invented claims and flattened source voice if
it has the source, and the tightness persona can only catch reproduced-source the same
way. Assemble it per artifact and hand it to **both** of those personas (the voice,
narrative, and orientation personas work from the draft and their rulebook):

| Artifact | Source bundle |
|---|---|
| LWIP | the rotated issue + all its comments; linked prior LWIP/blog posts; release notes (`gh release view`) |
| personal / feature blog post | linked posts; release notes / `gh release view`; the originating discussion or issue |
| GitHub discussion / issue | the related issues/PRs and any doc it responds to |
| commit message | the diff (`git show` / `git diff`) |
| PR comment / PR description | the diff + the thread or review it answers |

Unvetted sources (GitHub issues, discussions) are LLM-written and are **not** voice
references — pull facts and meaning from them, never their wording. (See
`seans-voice` "ask before voice source.")

## Mechanical pre-check (scripted, not an agent)

Run before spawning personas; feed results to synthesis. What applies depends on the
artifact:

- **Everywhere:** em-dash count (flag heavy use), and link-target sanity (does each
  link's text match what it points at?).
- **Website-repo prose only** (post lives in a repo with a cspell config and a buildable
  site): cspell over the file, and the project build (e.g. `mkdocs build --strict`).
- **Commit messages / PR text / GitHub issues & discussions:** em-dash + link sanity
  only; no cspell/build.

## Full process

1. **Identify the artifact and assemble the source bundle** (tables above).
2. **Run the mechanical pre-check.** Capture results.
3. **Make an evidence dir:** `~/tmp/voice-review-<timestamp>/`. Each persona writes its
   detailed evidence to a file there; pass the path in the prompt.
4. **Spawn the lens personas in parallel**, each a fresh-context subagent on your most
   capable model. Five always run: Voice, Narrative, Orientation, Tightness,
   Content-honesty. A sixth, **Accuracy**, joins **only when the draft has code or makes
   technical/behavioral claims about a system** (a feature post, an architecture
   walkthrough); skip it for an essay or opinion piece with nothing to verify. Each prompt
   includes:
   - The persona document, read from `personas/<lens>.md`.
   - Its rulebook slice: the **Voice** persona gets the full `seans-voice` content; the
     Narrative, Orientation, Tightness, and Content-honesty personas get the relevant
     sections of `references/craft-rules.md`. The **Accuracy** persona reads the actual
     source instead — it checks against ground truth, not a rulebook.
   - The draft in full.
   - For the **Voice** persona: 2–3 of Sean's real posts from
     `~/code/seantallen/seantallen.com/content/posts/` for calibration (read them and
     include, or point the persona to read them).
   - For the **Content-honesty** and **Tightness** personas: the full source bundle.
   - For the **Accuracy** persona: the source the draft describes — the repo/files behind a
     code example, the release notes / API for a feature claim, the version it targets.
   - The shared persona output format (below).
   - "You are an ensemble agent — return findings to the orchestrator, take no external
     actions, edit nothing."
5. **Triage persona outputs** — confirm each addressed the actual draft and stayed on its
   lens. Drop nothing silently.
6. **Synthesize** (inlined below — no external synthesizer skill).
7. **Triage into Fix / Park** and act (below).

## Shared persona output format

Include in every persona prompt. Each persona produces two artifacts.

**Evidence file** (written to the provided path): every finding with the exact quoted
text from the draft, what's wrong, the rule it violates, and the concrete rewrite.

**Summary** (returned to the orchestrator):

- **Findings**, ordered by severity (Blocking > Should-fix > Minor). Each:
  - **Quote**: the exact span from the draft.
  - **Lens**: this persona.
  - **Problem**: what's wrong (concise — full reasoning is in the evidence file).
  - **Fix or Park**: the persona's call — is the right change obvious (Fix), or does it
    need Sean (Park)? With the suggested rewrite (Fix) or the question (Park).
- **Passes**: key things checked that read true. Brief — builds confidence.
- **Uncertainties**: anything the persona couldn't judge without Sean or more source.

## Synthesis (inlined)

The synthesizer is a fresh-context agent (or the orchestrator) given all persona
summaries and the mechanical-check results, with these instructions:

**Job:** integrate the persona findings into one deduplicated list. You are not
averaging opinions — you are assembling the strongest, non-redundant set of findings.

**Focus:**
- **Don't drop anything.** Every persona finding appears in the output or is explicitly
  merged into another. A review that surfaces a real problem and then loses it has
  wasted the discovery.
- **Cross-persona corroboration is high-confidence.** When two personas flag the same
  span from different angles (e.g. Voice flags a flattened colloquialism as register,
  Content-honesty flags it as source-fidelity), merge them into one finding marked
  high-confidence — never let each assume the other owns it and drop both.
- **Clusters signal structure.** Several small findings in one section often mean the
  section's shape is wrong (an enumeration, a reproduced source, a missing on-ramp).
  Call out the structural problem, not just the symptoms.
- **Severity stands.** If one persona says Blocking with evidence and another didn't
  mention it, it's Blocking. Don't soften by consensus.

## Fix / Park triage

Categorize every finding. Nothing is silently dropped.

- **Fix** — the right change is obvious from the finding itself: a misspelling, an
  unclear antecedent, a term used before it's introduced, an enumeration to reweave,
  prose reproduced from the linked source, a flattened source colloquialism, an em-dash
  glut. Apply these directly.
- **Park** — needs Sean: is this POV actually yours? is this the right register? keep
  this metaphor or cut it? your colloquialism or mine? a thesis/framing the draft
  asserts that no source supports. **Never ship a parked call as final** — that's the
  exact failure this skill exists to prevent (an invented POV shipped as Sean's). Batch
  parked items and present them as questions.

When run inside a drafting skill's pipeline: apply the Fix items, list the Park items for
Sean (in the PR description / the conversation), and proceed. When run standalone: return
both lists.

## Output format

```
## Voice review — <artifact>  (<full | inline pass>, N findings)

### Applied (Fix)
- <quote> → <change>  [lens]
...

### Parked for you (Park)
- <quote> — <the question>  [lens]
...

### Mechanical
- cspell: <clean | issues>   build: <pass | fail>   em-dashes: <count>   links: <ok | …>

### Passes
- <brief confidence notes>
```

## The lenses

| Persona | Catches |
|---|---|
| `voice.md` | register/voice: anthropomorphizing, AI tells, math-symmetry framings, definitional label-parallels, clipped-imperative cadence, glossed allusions, flattened colloquialisms, em-dash overuse, clipped-notes. Reads `seans-voice`. |
| `narrative.md` | enumeration vs story, at section **and** prop level (a snippet/line-count/parenthetical can be dead cargo inside a good section). |
| `orientation.md` | concept-before-use, unclear antecedents, missing on-ramps, offloaded context, compressed recaps that strip framing, series-framing over the reader's question. |
| `tightness.md` | reproduced linked source, props that don't earn their place, filler, wrong altitude for the artifact. **Gets the source bundle.** |
| `content-honesty.md` | unsourced claims, invented framing/POV/thesis, invented quantitative characterizations, unearned promises, flattened source personality, lifted wording from unvetted sources, authorship/tense honesty. **Gets the source bundle.** |
| `accuracy.md` | **conditional** — runs only when the draft has code or technical/behavioral claims. Verifies code examples, API signatures, behavior claims, version claims against the actual source (ground truth, not the source bundle). |
