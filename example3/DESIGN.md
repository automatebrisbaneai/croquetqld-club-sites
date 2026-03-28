# DESIGN.md — example3 (Headland-Buderim, ref: tenbinlabs.xyz)

## Submission Brief

- **Name:** Jan Whitfield (Secretary) [GENERATED]
- **Email:** jan.whitfield@pretendmail.com [GENERATED]
- **Reference URL:** https://tenbinlabs.xyz
- **Description:** "We'd love something sophisticated and modern. Tenbinlabs has that dark, clean feel that seems premium and serious. Our club has been around a long time and we're proud of our competitive players. We want something that feels like we mean business, but still welcoming."

---

## Visual Concept

**"The ridge at nightfall."** Four lawns under a darkening sky, quiet and deliberate. The Sunshine Coast doesn't need to shout. This site is for a club that knows its craft.

Tenbin's institutional minimalism transplanted to a croquet ridge: deep black, white type, lavender accents that appear only when you lean in.

---

## Colour Palette (extracted from tenbinlabs.xyz)

| Token | Hex | Use |
|-------|-----|-----|
| `--bg` | `#000000` | Page background |
| `--text-primary` | `#ffffff` | Headlines, nav |
| `--text-secondary` | `#f0f3f3` | Body, descriptions |
| `--accent` | `#cecafb` | Hover states, highlights, accent labels |
| `--glass` | `rgba(0,0,0,0.4)` | Frosted glass buttons |
| `--glass-light` | `rgba(255,255,255,0.05)` | Subtle card fills |
| `--divider` | `rgba(255,255,255,0.3)` | Dashed dividers |
| `--glow` | `rgba(204,186,228,0.5)` | Button hover glow shadow |

---

## Typography

**Headlines (PP Telegraf equivalent):** `Syne` from Google Fonts — geometric, tight, weight 400
- Letter-spacing: -0.03em
- Large: 6vw desktop, 10vw mobile

**Body / Labels / Stats / Buttons:** `Space Mono` from Google Fonts — monospace, weight 400
- Letter-spacing: 0.02-0.04em
- Body: 16-18px, line-height 1.5

---

## Layout

- Fixed nav: logo left, phone/CTA right. Padding 32px. Transparent.
- Hero: full viewport height, centered, large headline. Stats row below.
- Sections: `min-height: 100vh` padding. Generous whitespace: 120px section gaps.
- Schedule: monospace table, dashed dividers, no heavy borders.
- Photos: dark overlay (`brightness(0.35) contrast(1.1)`) — photos work as texture, not illustration.
- Footer: two-column, left club info, right contact.

---

## Effects to Replicate (extracted)

- **Noise texture:** CSS grain via SVG filter or `background-image` on `::before` pseudo-element
- **Frosted glass buttons:** `background: rgba(0,0,0,0.4); backdrop-filter: blur(5px); border-radius: 8px`
- **Hover glow:** `box-shadow: 0px 4px 40px rgba(204,186,228,0.5)`
- **Dashed dividers:** `border-top: 0.5px dashed rgba(255,255,255,0.3)`
- **Transitions:** `all 300ms ease-in-out`
- **Outline button:** `border: 1px solid #f0f3f3; background: rgba(0,0,0,0.05)`

---

## What NOT to Do

- No gradient text
- No marquee/ticker effects
- No cursor spotlight
- No WebGL or canvas effects
- No parallax
- No counters or animated numbers
- Effects must serve the concept, not decorate it

---

## Images

Reusing club photos with dark CSS treatment:
- `images/players-golden-hour.jpg` — hero background at brightness(0.35)
- `images/clubhouse-mural.jpg` — mid-section feature
- `images/family-playing.jpg` — come and try section

No new image generation needed: the dark overlay treatment makes these work in the black aesthetic.
