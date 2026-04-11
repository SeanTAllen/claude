---
name: upgrade-llvm
description: Load when upgrading the vendored LLVM submodule in ponyc. Covers the per-version commit strategy, submodule mechanics, patch hash computation, and common API migration patterns.
disable-model-invocation: false
---

# Upgrading the Vendored LLVM in ponyc

## Strategy

Upgrade one major version at a time. Each version gets its own commit. This isolates which LLVM version introduced each breaking change and makes bisection straightforward if something breaks later.

## Per-Version Steps

### 1. Update the submodule

```bash
# Reset any applied patches first
git -C lib/llvm/src checkout -- .
# Fetch and checkout the new tag
git -C lib/llvm/src fetch origin tag llvmorg-XX.Y.Z
git -C lib/llvm/src checkout llvmorg-XX.Y.Z
```

### 2. Update `lib/CMakeLists.txt`

Get the new commit hash:
```bash
git -C lib/llvm/src rev-parse HEAD
```
Set `LLVM_DESIRED_HASH` to this value.

### 3. Handle patches

Check if patches in `lib/llvm/patches/` still apply:
```bash
git -C lib/llvm/src apply --check -p 1 ../patches/PATCH_NAME.diff
```

If a patch has been upstreamed (apply fails because the changes are already present), delete the patch file.

### 4. Update `PATCHES_DESIRED_HASH`

The CMake patch hash computation (lines ~93-100 of `lib/CMakeLists.txt`):
- Initializes with seed string `"needed_if_no_patches"`
- Iterates over patch files, computing SHA256 of each and concatenating
- Takes final SHA256 of the concatenated result

If no patches remain, compute: `SHA256("needed_if_no_patches")` = `3e16c097794cb669a8f6a0bd7600b440205ac5c29a6135750c2e83263eb16a95`

To compute this value:
```bash
echo -n "needed_if_no_patches" | sha256sum
```

### 5. Make source changes

Fix compilation errors from removed/deprecated LLVM APIs. See "Common Migration Patterns" below.

### 6. Commit submodule + source changes together

The submodule pointer must be committed before building because CMake runs `git submodule update --init` which would revert an uncommitted pointer change.

```bash
git add lib/llvm/src lib/CMakeLists.txt src/libponyc/codegen/...
git commit -m "Upgrade LLVM XX.Y.Z → XX.Y.Z"
```

### 7. Build and test

```bash
make cleanlibs && make libs build_flags="-j12"   # Build LLVM (~30-60 min)
make                                              # Build ponyc
make test-full-programs-release                   # Run full-program tests
```

If the build finds additional errors, assess whether they're the same
class of API change already handled (fix and amend) or indicate a
different migration pattern is needed (revisit step 5).

## Common Migration Patterns

### `LLVMConst*` → `LLVMBuild*` (constant expression removal)

LLVM progressively removed constant expression functions. The `LLVMBuild*` equivalents auto-constant-fold when given constant operands, so they're drop-in replacements:

```c
// Before:
return LLVMConstShl(l_value, r_value);
// After:
return LLVMBuildShl(c->builder, l_value, r_value, "");
```

Removal timeline (approximate):
- **LLVM 19**: `LLVMConstICmp`, `LLVMConstFCmp`, `LLVMConstShl`
- **LLVM 20**: `LLVMConstAdd`, `LLVMConstSub`
- **LLVM 21**: `LLVMConstMul`

### `make_binop` NULL fallthrough

In ponyc's `genoperator.c`, `make_binop` takes a `const_i` function pointer. Passing `NULL` causes the null guard (line ~68) to fall through to the builder path, which constant-folds automatically:

```c
// Before:
make_binop(c, left, right, NULL, LLVMConstAdd, LLVMBuildFAdd, LLVMBuildAdd);
// After:
make_binop(c, left, right, NULL, NULL, LLVMBuildFAdd, LLVMBuildAdd);
```

### Deprecated → newer API variants (LLVM 22+)

```c
LLVMArrayType(elemTy, count)          → LLVMArrayType2(elemTy, count)        // uint64_t
LLVMConstArray(elemTy, vals, count)   → LLVMConstArray2(elemTy, vals, count)  // uint64_t
LLVMConstStringInContext(ctx, s, len) → LLVMConstStringInContext2(ctx, s, len) // size_t
LLVMGetMDKindID(name, len)           → LLVMGetMDKindIDInContext(ctx, name, len)
```

### C++ API changes

- **LLVM 19**: `DIBuilder::insertDeclare` returns `DbgInstPtr` (PointerUnion) instead of `Instruction*`. If callers don't use the return value, change wrapper return type to `void`.
- **LLVM 19**: `LLVMBuildNSWNeg`/`LLVMBuildNUWNeg` deprecated → use `LLVMBuildNeg` + `LLVMSetNoSignedWrap`/`LLVMSetNoUnsignedWrap`.
- **LLVM 20**: `Intrinsic::getDeclaration` → `Intrinsic::getOrInsertDeclaration`.
- **LLVM 20**: Optimizer extension point callbacks (`registerOptimizerEarlyEPCallback`, `registerOptimizerLastEPCallback`) add `ThinOrFullLTOPhase` parameter to the lambda.
- **LLVM 21**: `Attribute::NoCapture` → `Attribute::getWithCaptureInfo(ctx, CaptureInfo::none())`.
- **LLVM 21**: `LintPass()` constructor requires `bool AbortOnError` parameter → `LintPass(false)`.
- **LLVM 22**: `createTargetMachine` takes `const Triple&` instead of `StringRef` → wrap with `Triple(opt->triple)`.

## Watch Table

APIs used in ponyc that may break in future LLVM versions. Check during each upgrade:

| API | Location | Likely replacement |
|-----|----------|-------------------|
| `LLVMConstNeg` | genoperator.c | `LLVMBuildNeg` |
| `LLVMConstNot` | genoperator.c | `LLVMBuildNot` |
| `LLVMConstXor` | genoperator.c | `LLVMBuildXor` |
| `LLVMConstTrunc` | genreference.c | `LLVMBuildTrunc` |

## Files Typically Modified

- `lib/CMakeLists.txt` — `LLVM_DESIRED_HASH`, `PATCHES_DESIRED_HASH`
- `lib/llvm/patches/` — patch files (may be added/removed)
- `src/libponyc/codegen/genoperator.c` — constant expression replacements
- `src/libponyc/codegen/genreference.c` — constant expression replacements
- `src/libponyc/codegen/gendebug.cc` / `gendebug.h` — debug info API changes
- `src/libponyc/codegen/host.cc` — target machine, intrinsics
- `src/libponyc/codegen/genopt.cc` — optimizer pass pipeline
- `src/libponyc/codegen/gendesc.c` — array/descriptor construction
- `src/libponyc/codegen/codegen.c` — core codegen types and helpers
- `src/libponyc/codegen/gencontrol.c` — metadata APIs
