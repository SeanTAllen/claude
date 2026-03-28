---
name: test-design
description: Disciplines for writing meaningful tests. Load when writing tests for new features or reviewing test quality. Counters the tendency to write tests that exercise the stdlib instead of your code.
disable-model-invocation: false
---

# Test Design Disciplines

## 1. Test the Code You Wrote

Before writing a test, ask: "Does this exercise code I wrote, or code the stdlib already tests?" If your feature is a thin wrapper around a stdlib function, testing the wrapper in isolation tests the stdlib. Test through the integration boundary instead — the path where your code parses input, makes decisions, calls the stdlib function, and produces output.

**Bad**: Your feature calls `sort(array)` internally. Your test creates an array, calls `sort` directly, and asserts it's sorted. That tests the sort function, not your feature.

**Good**: Your feature parses a CLI flag, collects items, sorts them, and prints the result. Your test creates the system with controlled CLI args and a captured output stream, then verifies the printed output is sorted. This exercises your argument parsing, collection logic, and output formatting — the code you actually wrote.

## 2. Test at Integration Boundaries

Find the narrowest boundary that still exercises your actual code paths. For an actor, this means creating it with controlled inputs and observing its outputs — not testing extracted helper functions in isolation.

Before concluding something is untestable, check what's actually available: public constructors, injectable dependencies, interface types you can implement. The answer is often "constructable with controlled inputs" rather than "impossible to test."

## 3. Each Test Owns Its Inputs

Shared test fixtures create hidden coupling. Changing the fixture breaks every test that uses it, even if those tests don't care about the change.

Each test should define its own inputs inline. This makes tests independent — you can change one test's inputs without touching the others. The slight repetition is worth the decoupling.

## 4. Properties and Edge Cases

Favor property-based tests over example-based unit tests. An example-based test says "this specific input produces this exact output." A property test says "across many inputs, this invariant holds." Examples test one point; properties test the rule. When a PBT framework isn't available, write the property loop manually — iterate over inputs, collect results, assert the invariant. Load `/pbt-patterns` for generator triads, compositional hierarchies, and coverage strategies when writing PBT.

Use example-based tests for edge cases and boundary conditions. Edges are where bugs live: zero, empty, one element, maximum value, off-by-one at a threshold, the exact boundary between valid and invalid. These deserve explicit tests with known inputs and exact expected outputs because you're testing a specific decision point, not general behavior. Properties and edge-case examples complement each other — properties cover the space, examples nail the borders.

## 5. Magic Values Are Unverified Assumptions

If a test uses a specific input and assumes it triggers a particular behavior (e.g., "this value is large enough to overflow," "this string contains invalid characters"), that's an unverified assumption. Either:
- Compute the expected output empirically and assert exactly (makes the assumption explicit and verifiable)
- Test the property across multiple inputs so no single value matters

Never rely on "this input probably triggers the behavior" — verify it or test the property.

## 6. Counterfactual Testing

After writing new tests, temporarily break each assertion to confirm it fires. A counterfactual that passes (assertion doesn't fire) means the assertion is weak — treat this as a bug found, not just a confidence check. Always assert on the *specific dimension* being tested, not the whole output. For property tests, also verify the generator covers the relevant range before concluding the assertion is weak.

**Workflow**: After a new test passes, do NOT report success yet — do counterfactual checks first. Run only the specific test during iterations, not the full suite. Full suite once at the end.

## 7. Consistent Rigor Across Variants

When code implements the same pattern across multiple variants (type families, format handlers, similar APIs), test quality tends to taper — the first variant gets careful attention, later ones get less. If the first variant has boundary tests at every transition point, every other variant should too. When reviewing, compare thoroughness across variants; inconsistency is a smell.

## 8. Tests Are Part of Done

Test coverage gaps for new code are not follow-up work. Tests for code introduced in the current change are part of "done" — don't defer them. Only tests for pre-existing untested code belong in follow-up issues. Plans for test work must include the specific command(s) to build and run the tests.
