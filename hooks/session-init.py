#!/usr/bin/env python3
"""SessionStart hook for Claude Code.

Injects context at session boundaries:
  environment  - Platform-specific environment configuration (all events)
  claude-md    - Global CLAUDE.md re-injection (after compaction)
"""

import platform
import sys
from pathlib import Path


def claude_home():
    return Path.home() / ".claude"


def print_environment():
    """Print platform-specific environment configuration."""
    home = claude_home()
    if platform.system() == "Windows":
        env_file = home / "environments" / "windows.md"
    else:
        env_file = home / "environments" / "linux.md"
        try:
            if "microsoft" in Path("/proc/version").read_text().lower():
                env_file = home / "environments" / "linux-wsl2.md"
        except FileNotFoundError:
            pass
    if env_file.is_file():
        print(env_file.read_text(), end="")


def print_claude_md():
    """Print global CLAUDE.md for re-injection after compaction."""
    claude_md = claude_home() / "CLAUDE.md"
    if claude_md.is_file():
        print(claude_md.read_text(), end="")


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else "environment"
    if command == "environment":
        print_environment()
    elif command == "claude-md":
        print_claude_md()


if __name__ == "__main__":
    main()
