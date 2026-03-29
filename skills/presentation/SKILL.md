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
Simple box-and-arrow diagrams. Not complex architecture diagrams. Used to
illustrate a concept visually, often with progressive reveal (arrows
appearing, elements highlighting).

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
