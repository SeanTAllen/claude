---
name: export-config
description: Export general-purpose Claude Code configuration (CLAUDE.md and skills) as a bundle for use in another environment. Filters out environment-specific and open-source-only content.
disable-model-invocation: false
---

# Export Config Bundle

Sean maintains Claude Code configuration across multiple WSL environments. This skill produces an export bundle — a directory of files that a Claude in another environment can use to merge into that environment's configuration.

## Process

1. **Ask for the output directory** — prompt Sean for where to write the bundle.
2. **Classify content** — review the current ~/.claude/CLAUDE.md and ~/.claude/skills/ to classify each section and skill as general (transfers) or environment/project-specific (stays). Discuss the classification with Sean before proceeding.
3. **Write the bundle**:
   - README.md — describes what the bundle contains and instructs the receiving Claude to merge the contents into ~/.claude/, preserving existing config and raising conflicts.
   - CLAUDE.md — the general-purpose portions only. Include the "Environment-Specific" section with items that apply across environments (same paths, same tools), but keep the "do not export" header so the receiving environment knows to add its own specifics.
   - skills/<name>/SKILL.md — each general-purpose skill, copied as-is.

## Classification Guidelines

**General** (transfers): working style preferences, code design principles, code change discipline, testing philosophy, debugging discipline, Pony language knowledge (pony-ref skill, build conventions, package docstring guidance), git workflow (branching, squash-before-PR, commit message style, GPG signing), gh CLI preference, graphql-bash skill.

**Open source only** (stays): release note workflows, pony-release-notes skill, "classify changes by type early" (tied to release notes), squash-merge-only strategy (ponylang/seantallen-org orgs), research docs in GitHub Discussions.

**Environment-specific** (stays, but verify): SSL version, documentation paths, PonyCheck source paths. These may or may not match across environments — ask Sean.

## Bundle Format

```
<output-dir>/
  README.md          # What this is, instructions for receiving Claude
  CLAUDE.md          # General config to merge into ~/.claude/CLAUDE.md
  skills/
    <skill>/
      SKILL.md       # Each transferable skill
```
