---
name: pr-overview
description: Generate a navigable HTML overview of a PR — structured sections with progressive disclosure, file map, API surface, architecture diagrams, and release notes.
disable-model-invocation: false
---

Generate a self-contained HTML document that presents a PR's changes in a
structured, navigable format. The overview is for Sean — it replaces reading
raw diffs with a curated walkthrough of what changed, how the public API
looks now, and what the release notes say.

## When to use

When Sean asks for a PR overview, or when generating one as part of opening
a PR. Not every PR needs one — use it for changes substantial enough that
the diff alone doesn't convey the shape of the change.

## Data gathering

Before writing any HTML, read the PR and collect:

1. **PR metadata**: title, number, org/repo, head SHA, branch name, file
   count, total additions/deletions.
2. **PR description**: the motivation and context the author wrote.
3. **Changed files**: every file path with its additions/deletions. Group
   them by role (new code, modified code, deleted code, tests, examples,
   build/CI, docs, release notes). Use your judgment on grouping — the
   categories should reflect the PR's structure, not a fixed template.
4. **Public API**: for every public type that was added or changed, read
   the source file and extract the full public API surface. "Public" means
   no underscore prefix in the language's convention (e.g., in Pony,
   methods starting with `_` are private).
5. **Release notes**: read `.release-notes/` files and `CHANGELOG.md` (or
   equivalent) from the branch. These are included verbatim.
6. **Architecture**: understand the structural change well enough to
   describe it and, if applicable, diagram it.

## Section order

Every overview uses this section order. Omit a section if the PR has no
content for it — don't include empty sections.

1. **Summary** — one-sentence description in a highlighted box, plus stats
   (files changed, additions, deletions).
2. **Motivation** — why this change exists. Drawn from the PR description.
   This is a justification, not a behavioral description.
3. **File Map** — all changed files grouped by role, in expandable panels.
   Each file links to the full file on the branch (not the diff).
4. **Behavioral Changes** — what's different from the user's perspective.
   Only observable behavior goes here, not justifications or internal
   restructuring.
5. **API Changes** — specific changes with before/after code blocks.
6. **Public API Surface** — the full public API of added or changed types.
7. **Architecture** — diagrams and structural explanation.
8. **Release Notes** — verbatim from the release notes files in the PR.
9. **CHANGELOG** — verbatim from the changelog file in the PR.

## Content rules

### Don't synthesize what doesn't exist

The overview presents what's in the PR, organized for readability. It does
not editorialize.

- Don't write migration guides unless the release notes contain one.
- Don't invent behavioral changes — describe only what the code does.
- Don't paraphrase release notes or changelog entries. Include them
  verbatim.
- Don't add sections the PR has no content for.

### Public API Surface

Show the complete public API of every type that was added or meaningfully
changed.

- **Only public methods.** No underscore-prefixed (private) methods.
- **Every method on its own line** with its full signature. Never
  abbreviate with `(...)` or group methods on one line like
  `assert_true / assert_false / assert_error`. The point of this
  section is to see the full API at a glance — abbreviation defeats
  the purpose.
- **Full type parameters and constraints.** Show `[A: Equatable[A] val]`,
  not just `[A]`.
- Use the `type-block` component for each type (see CSS framework).

### Release notes and CHANGELOG

Read the actual files from the branch and include their content verbatim.
Common locations:

- `.release-notes/` directory (individual note files)
- `CHANGELOG.md` or `CHANGES.md`
- `release-notes/next-release.md`

If the PR doesn't touch release notes or changelog files, omit those
sections entirely. Don't generate release notes from the diff.

### File map

- Group files by role. Name the groups after what the files do in this PR,
  not generic categories.
- Each file links to the full file on the branch:
  `https://github.com/{org}/{repo}/blob/{head_sha}/{path}`
- Deleted files don't get links — show them in muted text.
- Show per-file additions/deletions as `+N` / `-N` stats.
- Wrap each group in an expandable panel.

### Before/after code blocks

When showing API changes, use side-by-side before/after blocks with the
`before-after` grid component. Show full code in both columns — no
abbreviation, no `...` placeholders. Both sides should be complete enough
that a reader sees the full change without referring to the diff.

## SVG diagram guidance

Architecture diagrams use inline SVG. Key rules:

- **Stack vertically when a diagram has more than one section** (e.g.,
  before/after, phase comparisons). Use a horizontal dashed divider
  between sections. Horizontal space is constrained; vertical is
  unlimited.
- **Minimum sizing**: nodes at least 140px wide and 44px tall. At least
  36px vertical gap between rows of nodes. Font size 12px minimum for
  node labels, 14px for section headings.
- **No overlapping elements.** Check that node rectangles don't share
  x-ranges unless they're on different rows. When placing three nodes
  in a row, space them with at least 10px gap between rectangles.
- Use `width="100%"` with a `viewBox` and `style="max-width:700px"` so
  the diagram scales responsively.
- Use CSS custom properties for colors: `var(--diagram-node)` for fills,
  `var(--diagram-edge)` for strokes, `var(--diagram-highlight)` for
  emphasis.
- Define arrowhead markers in a `<defs>` block.

## HTML framework

The output is a complete, self-contained HTML document — `<!DOCTYPE html>`
through `</html>`, ready to serve as a static page.

### Fonts

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@400;500;600;700&display=swap">
```

- `Inter` for body text.
- `IBM Plex Mono` for code, signatures, file paths, badges, and the nav
  label.

### Color tokens

Define all colors as CSS custom properties on `:root`, with dark-mode
overrides under `@media (prefers-color-scheme: dark)` guarded by
`:root:not([data-theme="light"])` and again under
`:root[data-theme="dark"]`. Give `body` an explicit `background:
var(--bg)`.

Required tokens:

```
--bg, --fg, --muted, --accent, --accent-soft, --border, --code-bg,
--added-bg, --added-fg, --removed-bg, --removed-fg, --card-bg,
--nav-bg, --nav-fg, --nav-active,
--diagram-node, --diagram-edge, --diagram-highlight
```

### Layout

- Fixed left nav rail (220px wide) with section links, PR label, and
  keyboard shortcut hints.
- Main content area (`margin-left: 220px`, `max-width: 860px`).
- Mobile: nav goes static, main gets full width.

### Components

- **`.panel`** — expandable card with `.panel-header` (click toggles
  `.open`) and `.panel-body`. Arrow rotates on open.
- **`.badge`** — inline label. Variants: `.badge-added` (green),
  `.badge-removed` (red), `.badge-changed` (blue).
- **`.before-after`** — two-column grid for before/after code. Each side
  has a colored label and a `<pre>` block. Stacks to one column on mobile.
- **`.type-block`** — API surface card with `.type-block-header` (kind
  badge + type name) and `.type-body` (doc string + `.method-list`).
- **`.summary-box`** — highlighted box with left accent border.
- **`.file-list`** — monospace list of file paths with stats.
- **`.diagram-container`** — card wrapper for SVG diagrams.
- **`.release-notes-content`** — card wrapper for release note text.
- **`.type-link`** — inline link to a type definition within the report.

### Type navigation

Every `.type-block` gets an `id` of the form `type-TypeName` where
`TypeName` is the bare type name (no type parameters, no `is` clause,
no package prefix). After the page loads, a script builds an index of
these anchors and walks the document's text nodes, wrapping each mention
of a defined type name in an `<a class="type-link" href="#type-Name">`
link. A type name inside its own `.type-block` is not linkified. Links
inside `<pre>`, `<code>`, `<a>`, and `<svg>` elements are skipped.

The clickability signals "this type is defined in this report" — types
not in the report stay plain text.

**Future direction**: a full symbol index that also linkifies type names
in method signatures and field types. Not implemented yet — the
straightforward type-to-type linking is the starting point.

### JavaScript

- **Scroll spy**: `IntersectionObserver` highlights the active nav link
  as the user scrolls.
- **Keyboard navigation**: `j`/`k` move between sections, `Enter`
  expands all panels in the current section, `Esc` collapses all panels.
- **Nav click handling**: smooth scroll to target section.
- **Type linkification**: builds a type index from `.type-block[id]`
  elements and wraps matching text nodes as anchor links.

## Hosting

Reports are published to the `ponylang/reports` GitHub Pages site. Follow
the instructions in that repo's `AGENTS.md` for the full process. The
short version:

1. Use the checkout at `~/code/ponylang/reports` (pull latest first). If
   it's not on `main` or doesn't exist, clone from GitHub into `~/tmp`.
2. Pick a slug for the report. For PR overviews, include the repo name
   and enough context to be meaningful on its own — e.g.
   `stallion-chunked-transfer-encoding`, not `pr-42`.
3. Write the report to `r/<slug>/index.html`.
4. Update `r/index.html` to add the report under the appropriate
   category.
5. Squash into a single commit and push to main.
6. The report will be live at
   `https://ponylang.github.io/reports/r/<slug>/`.

## Reference

Read `skills/pr-overview/template.html` for the complete CSS framework,
JS, and structural example before writing an overview. Use its styles and
component patterns — don't reinvent them.
