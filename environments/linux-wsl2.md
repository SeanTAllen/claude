## GitHub Workflow

**Use `gh` CLI for GitHub operations**: `gh` is installed and authenticated. Prefer it over WebFetch/WebSearch for reading PRs, issues, discussions, and for creating discussions or other GitHub API operations.

**GitHub issues have types and labels**: GitHub issues have both a **type** (bug, feature, task) and **labels**. These are separate concepts. Every issue should have a type set. The `gh` CLI does not yet support setting issue types — after creating an issue, note that the type needs to be set and let Sean handle it via the GitHub website. Don't create labels for bug/feature/task — use the built-in type system instead.

**Research documents go in GitHub Discussions**: Post research, planning, or analysis documents as Discussions under the "Research" category — not as repo files. Use `gh api graphql` to create them. Title from the `#` heading; body is everything after. Content must be environment-agnostic (no local paths, build flags, etc.).

**Use Discussions as living design documents**: For design work, use a Discussion as the anchor and add comments iteratively as decisions are made. Body is the overview; comments are the decision trail. Related discussions can reference each other.

**GraphQL via Bash**: Load `/graphql-bash` when using `gh api graphql`.

## Git

**Always work on a branch**: Create a feature branch for all changes unless explicitly told to work on main. Never commit directly to main.

**GPG signing is on by default**: Always use `--no-gpg-sign` when making git commits on this machine. This also applies to rebases (`git pull --rebase --no-gpg-sign`, `git rebase --no-gpg-sign`) since rebases create new commits that trigger signing. This flag only exists on commit-creating commands (commit, rebase, merge, cherry-pick) — do not use it with `git push`.

**Squash before PR**: Squash all branch commits into one before opening a PR (use `git reset --soft`, then `--force-with-lease`). **After a PR is open**, push additional changes as separate commits — don't squash unless asked.

**Squash merge is the only merge strategy**: Repos under the `ponylang` and `seantallen-org` GitHub organizations only allow squash merges. After a PR is merged, use `git branch -D` (not `-d`) to delete local branches, since git won't recognize squash-merged branches as "fully merged".

**Update project CLAUDE.md in the PR**: When changes affect anything documented in the project's CLAUDE.md (conventions, build steps, dependencies, architecture, API patterns, etc.), include the CLAUDE.md updates in the same PR. Stale instructions are worse than no instructions — they actively mislead.

**Commit messages are for "why", not "what"**: The diff shows what changed — the message should explain *why*. A subject line alone is sufficient for small changes. If a body is warranted, add context or rationale not obvious from the code.

**Link issues in commit messages**: Include `Closes #N` when a PR addresses an Issue. For work originating from a Discussion, use `Design: #N` instead (no auto-close). Place control lines at the end of the commit body.

**PR descriptions are just a summary**: Don't include a "Test plan" section in PR descriptions unless asked. Keep it to a summary of what changed and why. Don't add section headers like "## Summary" — the content is obviously a summary from its position, so the header adds nothing.

## Docker

**Never touch Docker credential state**: Don't run `docker login` or `docker logout` — Docker credentials are user-managed. If a push fails with a permissions error, report it and let Sean handle authentication. Running `docker logout` to "fix" a bad login destroys existing working credentials.

## WSL2 Temp Files

**Use `~/tmp` instead of `/tmp`**: Store temporary files in `~/tmp`, not `/tmp`. Create the directory if it doesn't exist. WSL doesn't automatically clean `/tmp` on reboot the way a native Linux install does, and `~/tmp` keeps temp files in the user's space where they're easier to find and manage. Still clean up after yourself — delete temp files when you're done.

## WSL2 Mirrored Networking

**Localhost connection hang on unoccupied ports**: WSL2 mirrored networking has a Hyper-V bug (WSL #10855) where connecting to `127.0.0.1` on an unoccupied port hangs ~130s instead of getting connection refused. Workaround in Pony: `ifdef linux then "127.0.0.2" else "localhost" end`. `127.0.0.2` stays within the Linux kernel, bypassing the bug. Doesn't work on macOS, hence the platform conditional.

## Pony Build Environment

**SSL version**: This machine has OpenSSL 3.x. If a project's Makefile has an `ssl` option, use `ssl=3.0.x` (e.g., `make ssl=3.0.x`). Most Pony projects don't have this option.

**PonyCheck source**: `/home/sean/code/ponylang/ponyc/packages/pony_check/`

**Documentation locations**:
- Tutorial: `/home/sean/code/ponylang/pony-tutorial/docs/` (subdirs: `reference-capabilities/`, `c-ffi/`, `generics/`, `gotchas/`)
- Patterns: `/home/sean/code/ponylang/pony-patterns/docs/`
- Website: `/home/sean/code/ponylang/ponylang-website/docs/`
- Style guide: `/home/sean/code/ponylang/ponyc/STYLE_GUIDE.md`
- Stdlib source: `/home/sean/code/ponylang/ponyc/packages/`
- Compiler source: `/home/sean/code/ponylang/ponyc/src/`
- Examples: `/home/sean/code/ponylang/ponyc/examples/`

## Zulip

Use `/zulip` when Sean shares a Zulip link.
