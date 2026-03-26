# Design System: Headland-Buderim Croquet Club (Example 2)

**Reference:** https://www.royalhotel.com.au/ (Royal Hotel Paddington)
**Submitted by:** Margaret Chen, Treasurer
**Concept in one sentence:** A gracious, heritage-feel croquet club website that borrows the Royal Hotel's confident typography and generous photography layout, but swaps pub warmth for lawn-and-linen elegance.

## 1. Visual Theme & Atmosphere

Classic Australian venue website. Heritage without being stuffy. The Royal Hotel uses bold uppercase headlines, large candid photography, and plenty of breathing room. For the croquet club, that translates to: big photos of the lawns and players, confident type, warm but refined palette. It should feel like walking through the clubhouse gate on a Saturday morning.

## 2. Colour Palette & Roles

- **Lawn Green** (#2D5A27) -- Primary accent, nav highlights, CTA buttons
- **Deep Green** (#1B3B19) -- Header/footer backgrounds, strong text
- **Cream** (#FAF6F0) -- Page background, content panels
- **Warm Gold** (#C5A55A) -- Secondary accent, borders, decorative details, hover states
- **Soft White** (#FFFFFF) -- Cards, alternating sections
- **Charcoal** (#2C2C2C) -- Body text
- **Light Sage** (#E8EFE6) -- Subtle section backgrounds, alternating panels

## 3. Typography

- **Headlines:** Playfair Display, 700 weight, uppercase with generous letter-spacing (0.08em). Large sizes (clamp 2rem to 3.5rem). Reference: Royal Hotel uses bold uppercase serif for impact.
- **Body:** Lato, 400 weight, 1.7 line-height, 17px base. Clean and readable.
- **Labels/Nav:** Lato, 600 weight, uppercase, 0.12em letter-spacing, 14px. Small and precise.
- **Accent text:** Playfair Display italic for pull quotes and schedule headers.

## 4. Geometry & Shape

- Border radius: minimal (2-4px on cards, 0 on buttons for a sharp, classic feel)
- Borders: thin gold accent borders (1px) for section dividers; 3px solid green on CTA buttons
- Generous section padding: 100px+ vertical gaps between major sections (following Royal Hotel's breathing room)

## 5. Depth & Elevation

- Minimal shadows. One subtle box-shadow on cards: `0 2px 20px rgba(0,0,0,0.06)`
- No parallax or scroll-jacking
- Depth from photography contrast against cream backgrounds, not from CSS effects
- Hover: gentle lift on cards (translateY -2px), gold border glow on CTAs

## 6. Component Patterns

- **Hero:** Full-width photo with dark overlay, centred white text, single CTA button. Like the Royal's "YOUR LOCAL IN THE HEART OF PADDO" hero.
- **Navigation:** Horizontal, centred club name as logo, clean links. Sticky on scroll. Deep green background, cream text.
- **Section blocks:** Alternating cream/white backgrounds. Photo left + text right, then swap. Like the Royal's about/dining sections.
- **Photo gallery:** 3-column grid with subtle hover zoom (scale 1.03). Inspired by the Royal's Instagram/photo grid.
- **Schedule table:** Clean table with gold header row, alternating light sage rows. Playfair italic for game-type headers.
- **CTA buttons:** Solid green background, cream text, sharp corners, 3px border. Hover: gold background swap.
- **Footer:** Deep green background, cream text, simple columns (contact, schedule, links).

## 7. Layout Principles

- Max content width: 1200px, centred
- Mobile-first: single column below 768px, two-column layouts above
- Hero: full viewport width, 70vh height
- Section gaps: 100px (desktop), 60px (mobile)
- Image aspect ratios: 16:9 for hero/features, 1:1 for gallery grid
- Nav collapses to simple stacked links on mobile (not hamburger -- only 5 nav items)
