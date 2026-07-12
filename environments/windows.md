## Windows Build Environment

**CMake must be on PATH**: ponyc's Windows build calls `cmake` directly (see BUILD.md), so CMake has to be on your PATH. Visual Studio bundles it at `C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin` — add that directory to PATH before running the BUILD.md commands.

**Python command is `python`, not `python3`**: On Windows, use `python` instead of `python3`.
