# LLM Agent Configuration

My global CLAUDE.md, settings, skills, hooks, and environment-specific configuration for Claude Code and Codex.

## Installation

Clone the repo, then run the install script:

```
python install.py
```

With no flags, the script auto-detects which harnesses are installed (`~/.claude` for Claude Code, `~/.codex` or `~/.agents` for Codex) and installs for all of them. Use `--claude` and/or `--codex` to target specific harnesses.

**Claude Code** gets the full configuration:

- `~/.claude/CLAUDE.md` → repo's `CLAUDE.md`
- `~/.claude/settings.json` → repo's `settings.json`
- `~/.claude/environments/` → repo's `environments/`
- `~/.claude/hooks/` → repo's `hooks/`
- Each skill directory in `skills/` → `~/.claude/skills/<name>/`

**Codex** gets skills only:

- Each skill directory in `skills/` → `~/.agents/skills/<name>/`

Skills are symlinked individually so that skills from other repos can coexist.

Other options:

- `--dry-run` — preview what would be done without making changes
- `--uninstall` — remove all symlinks pointing into this repo

### Prerequisites

- Python 3
- On Windows, symlinks require Developer Mode enabled or running as administrator

### Existing files

The script never overwrites files that aren't symlinks. If you have existing files that conflict, remove them first, then re-run.

## Editing

Since everything is symlinked, edits in `~/.claude/` are edits in the repo. Just commit and push.

## Environments

Environment-specific configuration lives in `environments/`. A `SessionStart` hook in `settings.json` runs `hooks/session-init.py` to detect the platform and inject the right environment file into the conversation automatically.

To add a new environment, create a file in `environments/` and add a detection rule to `hooks/session-init.py`.

## Hooks

Context-injection hooks live in `hooks/`. Currently:

- `session-init.py` — Injects platform-specific environment config on all session starts, and re-injects CLAUDE.md after context compaction. It also runs on every prompt to name the checks to run against a draft reply, reading their names from the `pre-send-checks` block in CLAUDE.md so it can never name a check that isn't there.
