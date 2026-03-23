---
name: ensemble
description: Ensemble workflow for producing higher-confidence outputs through decorrelated reasoning paths. Load when Sean explicitly requests the ensemble approach.
disable-model-invocation: false
---

# Ensemble Workflow

Produce higher-confidence outputs through decorrelated reasoning paths. Multiple agents work the same problem with slightly different attention focuses, then a synthesizer integrates their reviewed outputs. Small differences in focus cascade through the reasoning chain, producing meaningfully different outputs that cover more of the solution space than any single attempt.

## Process

1. Spawn one agent per attention focus in parallel, each as a Task with subagent_type="general-purpose" and model="opus". Each agent's prompt must include:
   - Instructions to read ~/.claude/CLAUDE.md (and project CLAUDE.md if applicable) and follow those principles, including loading any skills they reference
   - The task description
   - An attention focus — a short directive that shifts where the agent goes deeper (e.g., "pay particular attention to security implications"). This is a spotlight, not blinders — the agent still covers everything
   - The agent output format (below)
   - Instructions to run a reviewer loop per CLAUDE.md before returning
   - Instructions that this is an ensemble agent — return output and any local file paths to the orchestrator. Do not take external actions (publishing to GitHub Discussions, creating PRs, pushing branches, etc.)
2. Pass all reviewed agent outputs to a synthesis agent loaded with `/synthesize`
3. Reviewer loop on the synthesis
4. Present to Sean

## Attention Focuses

Specified per invocation — Sean provides them, or the orchestrator selects contextually appropriate ones. They should be small perturbations, not fundamentally different approaches. The diversity comes from how small differences cascade through the reasoning chain.

## Agent Output Format

Every agent produces:
- **Approach**: The actual output (research findings, plan, or code)
- **Key decisions**: For each significant choice — what was decided, alternatives considered, confidence level, and reasoning
- **Uncertainties**: Things the agent wasn't sure about, flagged explicitly
- **Assumptions**: Things taken as given that could be wrong
