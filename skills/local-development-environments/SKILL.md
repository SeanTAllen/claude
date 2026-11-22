---
name: local-development-environments
description: Load when choosing or connecting to one of Sean's development machines for platform-specific builds, tests, or performance testing.
---

# Local development environments

| SSH alias | Environment |
| --- | --- |
| `pony-macos-air` | macOS on Apple silicon |
| `perf-tester` | Ubuntu Linux with glibc, used primarily for performance testing |
| `pony-windows` | Windows 11 on x86 |
| `pony-rpi4-64` | 64-bit ARM Raspberry Pi running Debian Linux |
| `pony-rpi4-32` | 32-bit ARM Raspberry Pi running Debian Linux |

From most machines, you can connect over SSH using a key. Use the alias configured on the machine you're connecting from, for example `ssh pony-macos-air`.
