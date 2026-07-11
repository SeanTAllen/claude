#!/usr/bin/env python3
"""Context-injection hooks for Claude Code.

SessionStart:
  environment   - Platform-specific environment configuration (all events)
  claude-md     - Global CLAUDE.md re-injection (after compaction)

UserPromptSubmit:
  pre-send      - Names the checks to run against a draft reply, read from
                  CLAUDE.md so the hook cannot name a check that isn't there
"""

import json
import platform
import re
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


CHECKS_BLOCK = re.compile(
    r"<!-- pre-send-checks -->(.*?)<!-- /pre-send-checks -->", re.DOTALL
)
CHECK_HEADING = re.compile(r"^\*\*(.+?)\*\*:", re.MULTILINE)


def pre_send_context():
    """Name the checks to run against a draft reply.

    The names are read from the pre-send-checks block in CLAUDE.md rather than
    kept here, so renaming a check cannot leave this hook pointing at one that
    no longer exists. A missing block is reported instead of passing silently:
    a hook that quietly stops naming the checks looks exactly like a hook that
    is working.
    """
    claude_md = claude_home() / "CLAUDE.md"
    if not claude_md.is_file():
        return f"WARNING: pre-send checks unavailable, no {claude_md}."

    block = CHECKS_BLOCK.search(claude_md.read_text())
    if block is None:
        return (
            "WARNING: pre-send checks unavailable. CLAUDE.md has no "
            "<!-- pre-send-checks --> block. Tell Sean; do not work around it."
        )

    names = CHECK_HEADING.findall(block.group(1))
    if not names:
        return (
            "WARNING: the <!-- pre-send-checks --> block in CLAUDE.md holds no "
            "checks. Tell Sean; do not work around it."
        )

    return "Before you send, run these checks from CLAUDE.md against your draft. " + " ".join(
        f"{name}." for name in names
    )


def print_pre_send():
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": pre_send_context(),
                }
            }
        ),
        end="",
    )


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else "environment"
    if command == "environment":
        print_environment()
    elif command == "claude-md":
        print_claude_md()
    elif command == "pre-send":
        print_pre_send()


if __name__ == "__main__":
    main()
