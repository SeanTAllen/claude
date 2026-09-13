#!/usr/bin/env python3
"""Install configuration by symlinking repo files into your AI harness.

Usage:
    python install.py              Install for all detected harnesses
    python install.py --claude     Install for Claude Code
    python install.py --codex      Install for Codex
    python install.py --claude --codex   Install for both
    python install.py --uninstall  Remove all symlinks pointing into this repo
    python install.py --dry-run    Show what would be done without doing it

What it does:
- Shared: symlinks AGENTS.md into ~/.agents/AGENTS.md (canonical path
  for skills to read regardless of harness).
- Claude Code: symlinks AGENTS.md as CLAUDE.md, claude/settings.json,
  claude/hooks/, environments/, and each skill directory into ~/.claude/.
- Codex: symlinks AGENTS.md into ~/.codex/AGENTS.md and each skill
  directory into ~/.agents/skills/.

Harness selection:
- With no --claude/--codex flag, installs for every harness detected on this
  machine: Claude Code if ~/.claude exists; Codex if ~/.codex or ~/.agents
  exists. Pass --claude and/or --codex to force specific targets regardless of
  what is detected (the target directories are created as needed).

Existing symlinks pointing into this repo are updated silently.
Existing files/directories that are NOT symlinks are never overwritten —
the script reports them and skips. Remove them manually first if you want
the symlink to take over.

On Windows, symlinks require either Developer Mode enabled or running as
administrator.
"""

import sys
from pathlib import Path

HARNESSES = {
    "claude": {
        "label": "Claude Code",
        "markers": (".claude",),
        "skills": (".claude", "skills"),
    },
    "codex": {
        "label": "Codex",
        "markers": (".codex", ".agents"),
        "skills": (".agents", "skills"),
    },
}


def repo_dir():
    return Path(__file__).resolve().parent


def skills_dir(home, name):
    return home.joinpath(*HARNESSES[name]["skills"])


def detected(home, name):
    return any((home / marker).is_dir() for marker in HARNESSES[name]["markers"])


def selected_harnesses(args, home):
    forced = [name for name in HARNESSES if f"--{name}" in args]
    if forced:
        return forced
    return [name for name in HARNESSES if detected(home, name)]


def blocking_ancestor(path):
    """Return the nearest existing ancestor of path that is not a directory."""
    for candidate in (path, *path.parents):
        if candidate.is_symlink() and not candidate.exists():
            return candidate
        if candidate.exists():
            return None if candidate.is_dir() else candidate
    return None


def symlink(src, dst, dry_run):
    """Create a symlink from dst -> src. Returns a status message."""
    if dst.is_symlink():
        current_target = dst.resolve()
        if current_target == src.resolve():
            return f"  skip (already linked): {dst}"
        if not dry_run:
            dst.unlink()
            dst.symlink_to(src, target_is_directory=src.is_dir())
        return f"  update link: {dst} -> {src}"

    if dst.exists():
        return f"  SKIP (exists, not a symlink): {dst}"

    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.symlink_to(src, target_is_directory=src.is_dir())
    return f"  link: {dst} -> {src}"


def install_skills(repo, dst, dry_run, indent=""):
    """Symlink each skill directory from repo's skills/ into dst."""
    skills_src = repo / "skills"
    blocker = blocking_ancestor(dst)
    if blocker is not None:
        print(f"{indent}  SKIP (not a directory): {blocker}")
        return
    if not skills_src.exists():
        print(f"{indent}  (no skills/ directory in repo)")
        return
    found_any = False
    for skill_dir in sorted(skills_src.iterdir()):
        if not skill_dir.is_dir():
            continue
        found_any = True
        msg = symlink(skill_dir, dst / skill_dir.name, dry_run)
        print(f"{indent}{msg}")
    if not found_any:
        print(f"{indent}  (no skill directories found)")
    remove_stale_symlinks(skills_src, dst, dry_run, indent)


def install_shared(repo, home, dry_run):
    """Install harness-neutral config: canonical AGENTS.md."""
    agents_home = home / ".agents"
    print("  AGENTS.md (canonical):")
    print("  " + symlink(repo / "AGENTS.md", agents_home / "AGENTS.md", dry_run))


def install_claude(repo, home, dry_run):
    """Install Claude Code config: AGENTS.md as CLAUDE.md, settings, environments, hooks, skills."""
    claude_home = home / ".claude"

    print("  CLAUDE.md:")
    print("  " + symlink(repo / "AGENTS.md", claude_home / "CLAUDE.md", dry_run))

    print("  settings.json:")
    print("  " + symlink(repo / "claude" / "settings.json",
                         claude_home / "settings.json", dry_run))

    envs_src = repo / "environments"
    if envs_src.exists():
        print("  environments/:")
        print("  " + symlink(envs_src, claude_home / "environments", dry_run))

    hooks_src = repo / "claude" / "hooks"
    if hooks_src.exists():
        print("  hooks/:")
        print("  " + symlink(hooks_src, claude_home / "hooks", dry_run))

    print("  skills:")
    install_skills(repo, skills_dir(home, "claude"), dry_run, indent="  ")


def install_codex(repo, home, dry_run):
    """Install Codex config: AGENTS.md and skills."""
    codex_home = home / ".codex"

    print("  AGENTS.md:")
    print("  " + symlink(repo / "AGENTS.md", codex_home / "AGENTS.md", dry_run))

    print("  skills:")
    install_skills(repo, skills_dir(home, "codex"), dry_run, indent="  ")


def remove_stale_symlinks(source_root, dst, dry_run, indent=""):
    """Remove symlinks in dst that point into source_root but whose targets are gone."""
    if not dst.is_dir():
        return
    stale = []
    for entry in sorted(dst.iterdir()):
        if not entry.is_symlink():
            continue
        target = entry.resolve()
        try:
            target.relative_to(source_root.resolve())
        except ValueError:
            continue
        if not target.exists():
            stale.append(entry)
    if stale:
        print(f"{indent}  Stale symlinks:")
        for entry in stale:
            if not dry_run:
                entry.unlink()
            print(f"{indent}    remove: {entry}")


def find_skill_symlinks(repo, dst):
    """Find symlinks in dst that point into repo's skills/."""
    skills_src = repo / "skills"
    if not dst.is_dir():
        return []
    found = []
    for entry in sorted(dst.iterdir()):
        if not entry.is_symlink():
            continue
        target = entry.resolve()
        try:
            target.relative_to(skills_src.resolve())
        except ValueError:
            continue
        found.append(entry)
    return found


def find_repo_symlink(repo, path):
    """Return path if it is a symlink pointing into repo, else None."""
    if not path.is_symlink():
        return None
    target = path.resolve()
    try:
        target.relative_to(repo.resolve())
    except ValueError:
        return None
    return path


def remove_symlinks(entries, dry_run, indent="  "):
    for entry in entries:
        if not dry_run:
            entry.unlink()
        print(f"{indent}  {entry}")


def uninstall_shared(repo, home, dry_run):
    """Remove the canonical ~/.agents/AGENTS.md if it points into this repo."""
    agents_md = home / ".agents" / "AGENTS.md"
    found = find_repo_symlink(repo, agents_md)
    if found:
        print("  AGENTS.md (canonical):")
        remove_symlinks([found], dry_run)
    else:
        print("  No canonical AGENTS.md symlink found.")


def uninstall_claude(repo, home, dry_run):
    """Remove all symlinks in ~/.claude/ that point into this repo."""
    claude_home = home / ".claude"
    if not claude_home.is_dir():
        print("  Nothing to uninstall (~/.claude does not exist).")
        return

    config_items = [
        claude_home / "CLAUDE.md",
        claude_home / "settings.json",
        claude_home / "environments",
        claude_home / "hooks",
    ]
    removed_config = []
    for item in config_items:
        found = find_repo_symlink(repo, item)
        if found:
            removed_config.append(found)

    removed_skills = find_skill_symlinks(repo, skills_dir(home, "claude"))

    if not removed_config and not removed_skills:
        print("  No symlinks pointing into this repo found.")
        return

    if removed_config:
        print("  config:")
        remove_symlinks(removed_config, dry_run)
    if removed_skills:
        print("  skills:")
        remove_symlinks(removed_skills, dry_run)


def uninstall_codex(repo, home, dry_run):
    """Remove all symlinks in ~/.codex/ and ~/.agents/skills/ that point into this repo."""
    codex_home = home / ".codex"
    removed_config = []

    agents_md = codex_home / "AGENTS.md"
    if codex_home.is_dir():
        found = find_repo_symlink(repo, agents_md)
        if found:
            removed_config.append(found)

    dst = skills_dir(home, "codex")
    removed_skills = find_skill_symlinks(repo, dst) if dst.is_dir() else []

    if not removed_config and not removed_skills:
        print("  No symlinks pointing into this repo found.")
        return

    if removed_config:
        print("  config:")
        remove_symlinks(removed_config, dry_run)
    if removed_skills:
        print("  skills:")
        remove_symlinks(removed_skills, dry_run)


INSTALLERS = {"claude": install_claude, "codex": install_codex}
UNINSTALLERS = {"claude": uninstall_claude, "codex": uninstall_codex}


def main():
    args = sys.argv[1:]
    if "-h" in args or "--help" in args:
        print(__doc__.strip())
        sys.exit(0)

    known = {"--dry-run", "--uninstall", "--claude", "--codex"}
    unknown = [arg for arg in args if arg not in known]
    if unknown:
        print(f"Unknown option(s): {' '.join(unknown)}")
        print("Run with --help for usage.")
        sys.exit(2)

    dry_run = "--dry-run" in args
    do_uninstall = "--uninstall" in args

    if dry_run:
        print("=== DRY RUN (no changes will be made) ===\n")

    repo = repo_dir()
    home = Path.home()
    targets = selected_harnesses(args, home)

    if not targets:
        print("No supported harness detected (looked for ~/.claude, ~/.codex, "
              "~/.agents).")
        if do_uninstall:
            print("Pass --claude and/or --codex to uninstall from a specific "
                  "harness.")
        else:
            print("Pass --claude and/or --codex to install anyway.")
        return

    print("Shared:")
    if do_uninstall:
        uninstall_shared(repo, home, dry_run)
    else:
        install_shared(repo, home, dry_run)
    print()

    for name in targets:
        print(f"{HARNESSES[name]['label']}:")
        if do_uninstall:
            UNINSTALLERS[name](repo, home, dry_run)
        else:
            INSTALLERS[name](repo, home, dry_run)
        print()

    if dry_run:
        print("=== DRY RUN complete (no changes were made) ===")
    else:
        print("Done.")


if __name__ == "__main__":
    main()
