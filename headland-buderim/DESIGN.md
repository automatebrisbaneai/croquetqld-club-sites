# DESIGN.md — Headland Buderim Croquet Club

## Concept

**"Buderim's Eternal Afternoon."**

The feeling of a long, unhurried afternoon on the ridge — subtropical light filtering through the canopy, the quiet clack of mallet on ball, ginger-scented warmth. Not a corporate site. Not a template. A living postcard from a garden village 100 metres above the coast.

Every design decision answers: "Does this feel like a slow afternoon in Buderim?"

---

## Palette

Derived from Buderim's landscape — the ginger heritage, subtropical canopy, ridge earth, and soft hinterland light. No standard croquet colours. No maroon.

| Token | Hex | Role | Derived from |
|-------|-----|------|-------------|
| `--ginger` | `#E57325` | Primary accent — CTAs, highlights, warmth | Buderim Ginger Factory, heritage spice |
| `--canopy` | `#4E6D50` | Primary surface — headers, nav, depth | Subtropical rainforest remnants |
| `--canopy-deep` | `#2C3E2F` | Dark surface — footer, overlays, text on light | Deep shade under the trees |
| `--ridge` | `#B08968` | Warm neutral — cards, borders, secondary elements | Red-earth ridge soil |
| `--haze` | `#D4E2D4` | Light background — sections, whitespace | Diffused afternoon light |
| `--afternoon` | `#F5F0E8` | Lightest surface — page background, clean space | Warm cream of fading daylight |
| `--text` | `#1C2A1E` | Body text — dark forest-tinged black | Shadow on the lawn |
| `--text-muted` | `#6B7D6E` | Secondary text — captions, labels | Muted eucalyptus |

### CSS Custom Properties
```css
:root {
  --ginger: #E57325;
  --ginger-light: #F0A06A;
  --ginger-glow: rgba(229, 115, 37, 0.12);
  --canopy: #4E6D50;
  --canopy-deep: #2C3E2F;
  --canopy-light: #7A9B7C;
  --ridge: #B08968;
  --ridge-light: #D4C4B0;
  --ridge-subtle: rgba(176, 137, 104, 0.1);
  --haze: #D4E2D4;
  --afternoon: #F5F0E8;
  --text: #1C2A1E;
  --text-muted: #6B7D6E;
}
```

---

## Typography

**Display:** Playfair Display (Google Fonts) — high-contrast serif with heritage elegance. The curl of ginger vines.
**Body:** Work Sans (Google Fonts) — clean, open, effortlessly readable. The quiet clarity of a garden village.

### Scale (dramatic, not timid)
```
H1: clamp(3rem, 8vw, 5rem)      — 48-80px, the ridge headline
H2: clamp(2rem, 5vw, 3rem)      — 32-48px, section anchors
H3: clamp(1.25rem, 2.5vw, 1.5rem) — 20-24px, card titles
Body: clamp(1rem, 1.5vw, 1.125rem) — 16-18px
Small: 0.85rem                    — labels, captions
```

### Rules
- Letter-spacing on H1: +0.03em (premium feel)
- Line-height body: 1.75 (generous, unhurried reading)
- Line-height headlines: 1.1 (tight, dramatic)
- Max line length: 65ch (comfortable reading)
- `text-wrap: balance` on headlines

---

## Layout

- **Full-width sections** with contained content (max-width: 1100px)
- **Section gaps:** 100-140px (generous, breathing)
- **Hero:** 95vh minimum, centred, commanding
- **Asymmetric layouts** where content allows — not everything centred
- **CSS Grid** with named areas for semantic placement
- **No hard edges** between sections — use gradient fades, curves, or organic transitions

---

## Components

### Buttons
- Gradient background (ginger → ginger-light)
- Subtle inner shadow for depth
- 3D press effect: lift on hover (translateY -4px + shadow expansion), press on click (translateY +1px)
- Border-radius: 8px
- Generous padding: 14px 32px
- Text: Work Sans 700, uppercase, small letter-spacing

### Cards
- Background: var(--afternoon) with subtle ridge-subtle border
- Soft glow shadow: `0 8px 32px rgba(44, 62, 47, 0.08)`
- On hover: shadow deepens, slight lift
- Optional: faint ginger-leaf SVG watermark at corner (3% opacity)

### Navigation
- Fixed, glassmorphic: `backdrop-filter: blur(12px)` over canopy-deep at 85% opacity
- Links in --afternoon colour, ginger underline on hover
- Thin bottom border in ginger at 30% opacity
- Scroll progress bar in ginger

### Schedule Table
- Alternating row tints (afternoon / haze)
- Row hover: warm ginger-glow background
- Active day highlighted
- Season toggle: smooth crossfade, not abrupt show/hide

### Scrollbar
- Custom styled: track in haze, thumb in canopy with ridge border
- Thumb hover: canopy-light

---

## Micro-Details (Target: 12+)

1. **Button lift** — translateY(-4px) + shadow expansion on hover, press on click
2. **Scroll progress bar** — thin ginger line growing across top of nav
3. **Section reveals** — staggered fade-up with IntersectionObserver (children animate 100ms apart)
4. **Link underline grow** — ginger underline expands from left on hover
5. **Schedule row highlight** — warm ginger-glow on hover
6. **Season toggle crossfade** — smooth opacity transition, not display:none toggle
7. **Contact cards** — subtle tilt on hover (perspective + rotateY 2deg)
8. **Custom scrollbar** — canopy thumb, haze track
9. **Glassmorphic nav** — blur + transparency, gets more opaque on scroll
10. **Ginger flower SVG** — subtle decorative motifs in section dividers (5% opacity)
11. **Focus rings** — ginger-coloured, 3px offset, matches the palette
12. **Footer depth** — gradient from canopy-deep to canopy, rich with links and detail
13. **Easter egg** — hero has a faint ginger root SVG that glows slightly warmer on hover (Buderim's signature)

---

## Mood Keywords

**Unhurried. Leafy. Golden. Grounded. Alive.**

---

## Section Transitions

NOT flat horizontal lines. Use:
- Curved clip-paths (`clip-path: ellipse()`)
- Gradient fades between section background colours
- Subtle SVG ginger-leaf dividers at 5% opacity
- Alternating background tones (afternoon → haze → afternoon)

---

## Imagery Direction

Use `apps/generate-image.py` with `--style watercolour` or `--style vintage`:
- Hero: watercolour-style subtropical garden with croquet lawns
- Section dividers: ginger leaf patterns
- Not ink drawings — this isn't CAQ Classic. It's Buderim's own visual language.

---

## What This Site Is NOT

- Not a government information page
- Not a CAQ-branded template
- Not maroon and cream
- Not a grid of boxes with data in them
- Not timid typography
- Not flat shadows
- Not generic

This site is a **place** — Buderim, on a long afternoon, with the sound of mallets and the smell of ginger.
