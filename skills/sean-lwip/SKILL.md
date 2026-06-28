---
name: sean-lwip
description: Sean's entry point for writing a Last Week in Pony post. Seeds voice and process before any drafting, then runs the public /lwip for the form. Load this when Sean writes an LWIP, not the bare /lwip.
disable-model-invocation: false
---

# Sean's Last Week in Pony

This is how Sean writes a Last Week in Pony post. Run it when Sean asks for an
LWIP, instead of jumping straight into the public `/lwip`.

It adds no rules of its own. Every rule it leans on already lives in the skills
below. Its only job is to load them, in order, and seed the right context before
a word gets drafted. That seeding is the part that gets skipped, and skipping it
is how an LWIP comes out sounding like someone gussied up Sean's words.

## The order

1. **Load `/how-to-write` and follow it.** Plain first. Write the true thing with
   no decoration, then add flourish only on top, and cover-test every bit of it:
   cover the flourish, and if the plain fact isn't still there underneath, cut
   it. This is the step that gets skipped. Do not skip it.

2. **Load `/seans-voice`** for the sound.

3. **Calibrate on the real source.** Read 2-3 recent posts from
   `~/code/seantallen/seantallen.com/content/posts/`. Those are the voice
   reference. The Last Week in Pony posts already in the ponylang-website repo
   are for format and structure only, never voice. They carry earlier dress-up,
   and calibrating on them reproduces it.

4. **Run `/lwip`** for the form and the week's mechanics: rotating the issue, the
   structure, the releases list, the footer, the domain notes. `/lwip` owns the
   form. This skill does not repeat it.

5. **Review.** `/review-for-seans-voice` is the authority on voice. It calibrates
   on Sean's posts, not the repo. Let `/lwip`'s own review (`ponylang-prose-review`)
   cover the rest: format, accuracy, link sanity, the mechanical pre-check.

## Why this exists

Nothing was missing the last time it went wrong. `/how-to-write` already had
plain-first and the cover-test. `/lwip` already said to read Sean's personal
posts for voice. The post still came out dressed up, because those steps were
skipped and then the review ran against the same dressed-up examples. This skill
removes the chance to skip. Load it, and the right context is in place before
the first sentence.
