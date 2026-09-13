# LLM Agent Configuration

My global instructions, settings, skills, hooks, and environment-specific configuration for Claude Code and Codex CLI.

## Layout

```
AGENTS.md              Global instruction file (installed as CLAUDE.md / AGENTS.md per harness)
skills/                Shared skills (installed to all harnesses)
environments/          Platform-specific environment config
claude/
  settings.json        Claude Code settings
  hooks/               Claude Code context-injection hooks
codex/                 Codex CLI-specific config (placeholder)
install.py             Symlink installer for all harnesses
```

## Installation

Clone the repo, then run the install script:

```
python install.py
```

With no flags, the script auto-detects which harnesses are installed (`~/.claude` for Claude Code, `~/.codex` or `~/.agents` for Codex) and installs for all of them. Use `--claude` and/or `--codex` to target specific harnesses.

**Shared** (always installed):

- `~/.agents/AGENTS.md` → repo's `AGENTS.md` (canonical path for skills to read regardless of harness)

**Claude Code:**

- `~/.claude/CLAUDE.md` → repo's `AGENTS.md`
- `~/.claude/settings.json` → repo's `claude/settings.json`
- `~/.claude/environments/` → repo's `environments/`
- `~/.claude/hooks/` → repo's `claude/hooks/`
- Each skill directory in `skills/` → `~/.claude/skills/<name>/`

**Codex CLI:**

- `~/.codex/AGENTS.md` → repo's `AGENTS.md`
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

## Migrating from the old layout

If you have an existing install from before the restructure (when the repo had `CLAUDE.md`, `settings.json`, and `hooks/` at the top level):

1. `git pull` to get the new structure.
2. `python install.py --uninstall` to remove old symlinks.
3. `python install.py` to create new ones.
4. If you have an existing memory inbox, move it: `mv ~/.claude/memory-inbox ~/.agents/memory-inbox`

If you renamed or moved the local directory (e.g. to match a repo rename), update your clone path first, then run the install script — symlinks point to the local filesystem path, not the GitHub URL.

## Editing

Since everything is symlinked, edits to the installed files are edits in the repo. Just commit and push.

## Environments

Environment-specific configuration lives in `environments/`. A Claude Code `SessionStart` hook in `claude/settings.json` runs `claude/hooks/session-init.py` to detect the platform and inject the right environment file automatically.

To add a new environment, create a file in `environments/` and add a detection rule to `claude/hooks/session-init.py`.

## Hooks

Claude Code context-injection hooks live in `claude/hooks/`. Currently:

- `session-init.py` — Injects platform-specific environment config on all session starts, and re-injects the global instruction file after context compaction. It also runs on every prompt to name the checks to run against a draft reply, reading their names from the `pre-send-checks` block in the instruction file so it can never name a check that isn't there.
