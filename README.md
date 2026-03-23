# Claude Code Configuration

My global CLAUDE.md, skills, and environment-specific settings for Claude Code.

## Installation

Clone the repo, then run the install script:

```
python install.py
```

This creates symlinks from `~/.claude/` into the repo:

- `~/.claude/CLAUDE.md` → repo's `CLAUDE.md`
- `~/.claude/environments/` → repo's `environments/`
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

Environment-specific configuration lives in `environments/`. The dispatch table at the bottom of `CLAUDE.md` tells Claude which environment file to load based on platform info it sees at startup.

To add a new environment, create a file in `environments/` and add a matching rule to the dispatch table in `CLAUDE.md`.
