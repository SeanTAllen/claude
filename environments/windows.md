## Windows Build Environment

**CMake is on PATH**: ponyc's Windows build calls `cmake` directly (see BUILD.md), so it has to be on your PATH — and it is, in any new shell. Visual Studio bundles it at `C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin`; that's the directory to re-add if it ever falls off PATH.

**Python command is `python`, not `python3`**: On Windows, use `python` instead of `python3`.

## Running Tests

**WSL holds the ports lori tests need**: Don't run lori's test binaries on this machine without checking with Sean first. When WSL is running it holds the TCP ports lori's tests bind to, and they fail with "Unable to open listener." Confirm WSL is shut down before running them — don't assume it is.
