## Git

**GPG signing is on by default**: Always use `--no-gpg-sign` when making git commits on this machine. This also applies to rebases (`git pull --rebase --no-gpg-sign`, `git rebase --no-gpg-sign`) since rebases create new commits that trigger signing. This flag only exists on commit-creating commands (commit, rebase, merge, cherry-pick) — do not use it with `git push`.

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
