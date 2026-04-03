# Claude Code Configuration

My global CLAUDE.md, settings, skills, hooks, and environment-specific configuration for Claude Code.

## Installation

Clone the repo, then run the install script:

```
python install.py
```

This creates symlinks from `~/.claude/` into the repo:

- `~/.claude/CLAUDE.md` → repo's `CLAUDE.md`
- `~/.claude/settings.json` → repo's `settings.json`
- `~/.claude/environments/` → repo's `environments/`
- `~/.claude/hooks/` → repo's `hooks/`
- Each skill directory in `skills/` → `~/.claude/skills/<name>/`

Skills are symlinked individually so that skills from other repos can coexist in `~/.claude/skills/`.

Use `--dry-run` to preview what would be done without making changes.

### Prerequisites

- Python 3
- On Windows, symlinks require Developer Mode enabled or running as administrator

### Existing files

The script never overwrites files that aren't symlinks. If you have existing files in `~/.claude/` that conflict, remove them first, then re-run.

## Editing

Since everything is symlinked, edits in `~/.claude/` are edits in the repo. Just commit and push.

## Environments

Environment-specific configuration lives in `environments/`. A `SessionStart` hook in `settings.json` runs `hooks/session-init.py` to detect the platform and inject the right environment file into the conversation automatically.

To add a new environment, create a file in `environments/` and add a detection rule to `hooks/session-init.py`.

## Hooks

Session hooks live in `hooks/`. Currently:

- `session-init.py` — Injects platform-specific environment config on all session starts, and re-injects CLAUDE.md after context compaction.
