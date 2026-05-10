---
name: presentation
description: Build reveal.js presentations in Sean's style. Load when creating or working on slide decks.
disable-model-invocation: false
---

# Presentation Skill

Load this skill when building reveal.js presentations for Sean. Read 2-3 of
the reference PDFs in `references/` before starting to absorb the visual
style and pacing.

## Calibration

Before building a presentation, read 2-3 PDFs from the `references/`
directory alongside this skill. These are exports of prior presentations.
Focus on:

- Slide density (how much text per slide)
- Pacing and progressive disclosure
- How section transitions work
- The relationship between slide content and what a speaker would say

The PDFs are the primary style reference. The guidelines below are distilled
from them but the PDFs are the ground truth.

### Reference presentations

| File | Talk | Style notes |
|------|------|-------------|
| `deny-caps.pdf` | On Deny Capabilities for Safe, Fast Actors | Clean white background, rose/pink accent stripe, very sparse, progressive bullet reveal |
| `data-corrupting-wide.pdf` | Data Corrupting Architectures We Know and Love | Dark charcoal, NYC photography, blue headings, orange accents, speech-bubble callout boxes |
| `pony.pdf` | Pony: How I learned to stop worrying... | Orange/red with textured paper, slab serif, chalkboard-style content slides, street art imagery |
| `pat-helland-and-me.pdf` | Pat Helland and Me | Dark theme, street art, blue headings, progressive reveal with animation |
| `adventues_in_cgo_performance_version_3.pdf` | Adventures in CGo Performance | Neutral beige textured background, street art imagery, clean sans-serif |

## Slide Design Principles

**One idea per slide.** Often one sentence, one phrase, or one word. The
speaker carries the talk, not the slides. If a slide works without a speaker,
it probably has too much on it.

**Progressive disclosure.** Bullet points revealed one at a time using
reveal.js fragments. Never dump a full list on the audience. Let each point
land before showing the next.

**Bold, punchy statements.** Short declarative sentences. Key words bolded
for emphasis. No hedging, no filler.

**Let silence do work.** A slide with a single word ("Safe", "Pain",
"Results") creates a pause. The audience reads it instantly and waits for
the speaker. These section-divider slides are powerful pacing tools.

## Slide Types

These are the recurring patterns across Sean's presentations. Not every talk
uses all of them.

### Title slide
Talk name and subtitle. Sets the visual tone for the entire deck.

### About me slide
Name, current roles/affiliations, social handles, and one fun personal
detail ("Chicharrones Lover", "Lover of Artisanal Street Art"). Usually
includes a photo — either a portrait or thematic image.

### Section divider
Single word or short phrase, large, centered. Used to introduce a new
section or create a dramatic pause. Examples: "Safe", "Pain", "Actor model",
"GENERALIZATIONS AHEAD", "SOME JUSTIFICATION AHEAD".

### Content slide
Heading plus short bullet list. Often two-column layout with text on the
left and an image on the right. Bullets appear progressively via fragments.
Keep to 3-5 bullets maximum.

### Quote slide
An attributed quote on a distinctive colored background. The quote is the
entire slide. Used to bring in an external voice or anchor a key idea.

### Big statement slide
Large bold text filling most of the slide. A provocative or surprising
claim. These are the memorable takeaways. Examples: "OUR SIMPLE WEB APP IS
A DISTRIBUTED SYSTEM", "DISTRIBUTED SYSTEMS AREN'T HARD. THEY'RE EASY*.
CONCURRENCY IS THE HARD PART."

### Diagram slide
Simple shape-and-arrow diagrams used to make a concept visible. Not
architecture diagrams. The shapes carry meaning and the colors carry
meaning — the slide should be readable as a picture before it's read as
labels. See **Diagrams** below for the full vocabulary, tool guidance,
and the rules for progressive reveal.

## Visual Identity

**Each talk gets its own distinct visual identity.** Never reuse a previous
talk's palette or theme. The goal is visual pop and distinctiveness.

### Style vocabulary

Street art and urban photography is a recurring motif in Sean's past
presentations, but it's not the only option. The visual identity should be
bold, expressive, and have energy. Some approaches:

| Style | Description |
|-------|-------------|
| Street art / urban photography | NYC bridges, graffiti walls, murals. Sean's most-used style historically. |
| Clean cartoon | Whimsical cartoon style with bold outlines and warm colors |
| Street graffiti illustration | Cartoony graffiti with bold spray-paint outlines, vivid colors, dripping paint accents |
| Retro comic book | Halftone dots, bold primary colors, thick ink outlines, dramatic poses |
| Pop art | Flat vibrant colors, thick black outlines, Ben-Day dots, Lichtenstein-inspired |
| Gorillaz | Gritty urban cartoon, heavy ink, street culture aesthetic, moody lighting |
| Invader Zim | Angular, dark but colorful, sharp geometric shapes, neon accents on dark backgrounds |
| Chanoir street mural | Bold Latin American street art, saturated candy colors, mischievous cartoon characters, packed composition |
| Peter Bagge's Hate | Underground comics, exaggerated anatomy, angular distorted perspectives, grungy ink |

These styles can inform both imagery and the overall deck theme (color
palette, typography feel, background textures).

### Color and typography

- **Dark themes** work well for bold, dramatic talks (dark charcoal
  background with bright accent colors)
- **Light themes** work well for technical or academic talks (white or
  light gray with a single strong accent color)
- **Textured backgrounds** (paper, chalkboard) add warmth and visual
  interest
- **Pick 2-3 colors** and use them consistently: one for headings, one
  for accents/emphasis, one for the background
- **Typography should match the energy**: condensed all-caps bold for
  punchy talks, slab serif for serious/technical, clean sans-serif for
  modern/minimal

### Layout constants

- **16:9 widescreen** — always
- **Two-column layouts**: text left, image right for content slides
- **Generous whitespace** — sparse slides need room to breathe
- **Center important text** on section dividers and big statement slides

## Diagrams

Diagrams in Sean's decks are a deliberate visual language, not decoration.
A good diagram lets the audience see the idea before they read any labels.
The shape, the layout, the color — those carry the meaning. Labels confirm
what the picture already said.

### Two visual modes

Most diagrams in Sean's talks fall into one of two modes. Identify which
mode you're in before you start drawing.

- **Spatial.** Shows *where things are* and *what is connected to what*.
  Entities are circles or rectangles in space, arrows show messages or
  flow, dashed borders mark system boundaries. Used when the audience
  needs to understand topology — who talks to whom, what owns what,
  where a request crosses a boundary. Pat Helland's Alice/Bob diagrams
  and the BoC actor-station diagrams are spatial. (See
  `pat-helland-and-me.pdf` for the canonical example.)

- **Temporal.** Shows *when things happen* and *what value is in play
  at each step*. Operations are color-coded rows (or columns) read in
  order; alternating background shading separates steps; a highlighted
  row calls out the moment that matters. Used when the audience needs
  to follow a sequence and see how state changes over time. The
  `data-corrupting-wide.pdf` deck is the canonical reference.

Don't mix the two modes on a single slide. If you need both, make two
slides and let the speaker bridge them.

### Shape vocabulary

A shape should mean the same thing every time it appears within a talk.
The vocabulary below is a default starting point — adopt or replace it
talk-by-talk, but commit to one set of meanings before drawing any
diagram and apply it everywhere in the deck.

| Shape | Default meaning |
|-------|-----------------|
| Circle | An entity, actor, or active participant — something that *does* things |
| Rectangle | Data, state, a table, or a passive resource — something that *is acted on* |
| Arrow | A message, call, or flow of information |
| Dashed/thin border | A system boundary (the edge of the world being drawn) |
| Colored overlay | A spotlight or highlight applied on top of an existing diagram during a progressive reveal |

Shape semantics must be consistent **within a context** (a single talk,
or at least a single section). They can differ **across contexts** —
another talk may use rectangles for actors and circles for data — but
the shift has to be signaled clearly to the audience when it happens.

### Color semantics

- **One color per entity, used everywhere that entity appears.** If
  Users are terracotta on slide 4, they're terracotta on every slide
  they show up on. The audience learns the color and stops re-reading
  labels.
- **Pull entity colors from the deck's palette**, not from outside it.
  Diagrams should look like they belong to the deck.
- **Reserve a highlight color** (often a saturated yellow or rust) for
  progressive-reveal spotlights. It should not be one of the entity
  colors — it has to read as "look here now."
- **Role-based coloring** (e.g., green=input, blue=state, orange=output)
  works when the diagram is about data flow rather than identity. Pick
  identity-coloring or role-coloring per diagram and stick with it; don't
  mix.

### Tool selection

Default to **HTML/CSS in the deck's palette**. Hand-rolled `<div>`s with
the talk's color variables produce diagrams that look like they belong
to the deck, render crisply at any zoom, and animate cleanly with reveal.js
fragments. This is the right default for almost every diagram slide.

Avoid **Mermaid** for visually-committed decks. Mermaid is good for
README architecture diagrams. It is not good for slides where the
diagram is the focal point — its layouts are rigid, its styling fights
the deck palette, and it can't match the visual weight a slide demands.
A Mermaid diagram on a Sean slide will look like it was pasted in from
somewhere else. Use it only for genuinely throwaway sketches.

Avoid **DALL-E (or other image generation)** for diagrams. Image
generators produce inconsistent text, drift on shape proportions, and
can't be edited without re-rolling. Use them for hero/illustration
images, not for diagrams that need to be precise.

If a diagram is genuinely too complex for HTML/CSS, that is a signal the
diagram is too complex for a slide — break it into a progressive reveal
across multiple slides before reaching for a heavier tool.

### Progressive reveal

Diagrams should build, not appear all at once. The pattern:

1. Show the base diagram (the stable structure that won't change).
2. Add layers using reveal.js fragments — a new arrow, a new entity, a
   spotlight overlay on an existing piece.
3. Change the slide subtitle as each layer appears so the audience knows
   what they're looking at now versus what they were looking at a beat
   ago.

The base diagram stays put across the reveal. Don't redraw the world on
each fragment — the audience loses the through-line. If the picture
genuinely needs to change shape, that's a new slide.

### Diagram slide checklist

Before shipping a diagram slide, confirm:

- [ ] The picture reads as the right idea **before** any label is read.
- [ ] Every shape's meaning matches the talk's vocabulary.
- [ ] Every entity is in its assigned color.
- [ ] The diagram uses the deck's color palette (no external defaults).
- [ ] The diagram is HTML/CSS unless there's a deliberate reason
      otherwise.
- [ ] Anything new vs. the previous slide is reachable via a fragment
      reveal, not a redraw.
- [ ] The same diagram doesn't try to be both spatial and temporal.

## reveal.js Implementation

### Fragments for progressive disclosure

```html
<section>
  <h2>Actor model basics</h2>
  <ul>
    <li class="fragment">Actors communicate via messaging</li>
    <li class="fragment">Actors process messages</li>
    <li class="fragment">Actors "protect resources"</li>
  </ul>
</section>
```

### Section divider slide

```html
<section>
  <h1>Safe</h1>
</section>
```

### Big statement slide

```html
<section>
  <h2 style="font-size: 2.5em; font-weight: bold;">
    OUR SIMPLE WEB APP IS<br>
    A DISTRIBUTED SYSTEM
  </h2>
</section>
```

### Two-column content slide

```html
<section>
  <h2>Today's topics include...</h2>
  <div style="display: flex; gap: 2em;">
    <div style="flex: 1;">
      <ul>
        <li class="fragment">Data corruption</li>
        <li class="fragment">Concurrency</li>
        <li class="fragment">Data races</li>
      </ul>
    </div>
    <div style="flex: 1;">
      <img src="images/photo.jpg" alt="description">
    </div>
  </div>
</section>
```

### Quote slide

```html
<section data-background-color="#4a9a8a">
  <blockquote style="font-size: 1.5em;">
    "A programming language is just another tool. It's not about syntax.
    It's not about expressiveness. It's about managing hard problems."
  </blockquote>
  <p><strong>—Sylvan Clebsch</strong></p>
</section>
```

### Project structure

```
talk-name/
├── index.html
├── css/
│   └── custom.css      # Talk-specific theme overrides
├── images/
│   └── ...             # Photos, diagrams
└── lib/
    └── reveal.js/      # Or use CDN
```

## Anti-Patterns

- **Walls of text** — if it takes more than a glance to read, there's too
  much
- **Too many bullets at once** — always use fragments for progressive
  reveal
- **Generic stock photography** — use images with personality and energy
- **Reusing another talk's color palette** — each talk is its own thing
- **Slides that work without a speaker** — these are presentation aids,
  not documents
- **Clip art or corporate graphics** — the visual identity should feel
  personal, not institutional
- **Centered bullet lists** — left-align body text; only center headings
  and section dividers
- **Gratuitous animation** — fragments for progressive disclosure are
  good; flying/spinning/bouncing transitions are not
- **Mermaid (or other generic diagram tools) for focal diagrams** —
  rigid layouts and palettes that fight the deck. Use HTML/CSS in the
  deck's color variables instead
- **DALL-E for diagrams** — inconsistent text, drifting proportions,
  and uneditable. Hero images yes; diagrams no
- **Inconsistent shape or color meaning across slides** — once a
  circle means "actor" or terracotta means "Users," it has to mean
  that everywhere in the deck. Audiences learn the vocabulary; don't
  break it
- **Mixing spatial and temporal modes on one diagram** — pick one. If
  both views matter, they're two slides
