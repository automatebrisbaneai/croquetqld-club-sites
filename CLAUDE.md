# Club Websites - Build System

This folder contains the club website builder for `websites.croquetwade.com`. Each example is a different design of the same club data, built from a style reference submitted by a committee member.

---

## How It Works

1. Someone fills out the form on `websites.croquetwade.com`
2. They provide: their name, email, and a link to a website design they like
3. Claude builds a club website styled like their reference, using the source data
4. Deploy it, email them the link, iterate on feedback

---

## Checking for Submissions

Submissions come via n8n webhook. Check for new ones:

```
mcp__n8n-mcp__n8n_executions action=list, workflowId=NiIGx5b4NC3rP5G5, limit=5
```

Get submission data: `action=get, id=<ID>, includeData=true` - the form data is in `body.name`, `body.email`, `body.design_url`, `body.description`.

---

## Building a New Example

### Step 1: Create the folder

```
apps/club-sites/example[N]/
```

### Step 2: Site teardown

Pull the reference site apart. Don't just look at it, read its source.

- Fetch the HTML source: `mcp__searxng__web_url_read` with the reference URL
- Extract: colour values, font families, CSS animations/transitions, layout techniques (grid/flex/etc), spacing patterns, hover effects, scroll behaviours
- Note specific techniques worth replicating (parallax, reveal animations, gradient overlays, etc.)
- This is what stops you building a vague impression. You get the actual recipe.

### Step 3: Generate DESIGN.md

Combine the teardown findings into a structured design brief:

- Save to `apps/club-sites/example[N]/DESIGN.md`
- Include: palette (exact hex values), typography (Google Fonts pairing), layout approach, specific CSS effects to replicate, mood/concept in one sentence
- Optionally use Stitch (labs.google/stitch) + `enhance-prompt` skill for richer output
- Procedure: `system/memory/procedure_stitch.md`

### Step 4: Create assets

Generate custom images and visual elements BEFORE building. This is what gives a site life instead of feeling flat.

- Use `apps/generate-image.py` (6 styles: ink, watercolour, vintage, neon, pattern, poster)
- Transform club photos from `example1/images/` to match the design concept
- If the reference uses hero illustrations, textures, SVG patterns, gradient overlays, create equivalents
- Save to `apps/club-sites/example[N]/images/`

### Step 5: Read the source data

Source data: `apps/club-sites/data/headland-buderim.md`

The source data determines what content goes on the site. The data drives the sections - if the club has venue hire info, build a venue hire section. If they don't list fees, skip it. Don't force a fixed structure.

For now all examples use Headland-Buderim. When real clubs submit, their source data replaces this file.

### Step 6: Build the HTML

- Use the `/frontend-design` skill
- Read DESIGN.md + source data + created assets together
- The reference site is a style idea, not a structural template
- Build a single self-contained HTML file with inline CSS
- No frameworks. Mobile-first. Semantic HTML.
- All image paths must be relative (`images/filename.jpg`), never `file:///`
- No em dashes in any visible text (use commas, periods, colons instead)

### Step 7: Quality check

The current example1 scored 6/10. We need 8-9/10. Before deploying, check:

1. Does it capture the style/feel of the reference site?
2. Does it feel like a real place, not a template?
3. Would a committee member be proud to show this to their club?
4. Does the club data read naturally in this layout?
5. Mobile responsive?
6. No broken paths, all images relative?
7. No em dashes in visible text?

What makes a site feel professional:
- A concept that drives every decision (one sentence, specific to the style)
- Real photography of real people
- Restraint - fewer effects, each one purposeful
- Generous whitespace (100px+ section gaps)
- Confident typography (big headlines, generous line-height)
- One well-executed scroll effect > ten competing gimmicks

What kills quality ("ugly glam"):
- Gradient text, marquee tickers, cursor spotlights, parallax fade
- Effects that don't serve the concept
- Generic stock-photo feel
- Cramped spacing

### Step 8: Deploy

```bash
bash apps/deploy-club-sites.sh
```

Site goes live at `websites.croquetwade.com/example[N]/`

Deploy script: copies files to `.deploy/` repo, commits, pushes to GitHub `main` branch, triggers Coolify redeploy.

- GitHub repo: `automatebrisbaneai/croquetqld-club-sites`
- Coolify app UUID: `j4gc4g0c8ookw40k4ksgokos`
- Coolify FQDN: `https://websites.croquetwade.com`

### Step 9: Email the submitter

Reply to their email address with:
- Link to their site
- Ask what they think, what they'd change
- Use LobsterMail (`hello@croquetclaude.com`)

---

## File Structure

```
apps/club-sites/
  index.html              <- Landing page (websites.croquetwade.com)
  images/                 <- Landing page images
  data/
    headland-buderim.md   <- Source data (constant for now)
  example1/               <- First demo (Claude's own style choice)
    index.html
    DESIGN.md
    images/
  example2/               <- Next submission...
    index.html
    DESIGN.md
    images/
  .deploy/                <- Git repo for deployment (gitignored)
```

---

## Key Rules

- Each site must look different. No two examples should share a palette or feel.
- The reference site is a style idea. The source data determines content.
- No em dashes on any public-facing text.
- All image paths relative. Never `file:///`.
- Single HTML file, inline CSS, no frameworks.
- Quality bar is 8-9/10, not "good enough."

---

## Infrastructure

- **Landing page:** `websites.croquetwade.com` (this folder's `index.html`)
- **Form webhook:** `https://n8n.croquetwade.com/webhook/club-design-submission` (n8n workflow ID: NiIGx5b4NC3rP5G5)
- **Deploy:** `bash apps/deploy-club-sites.sh`
- **Coolify:** UUID `j4gc4g0c8ookw40k4ksgokos`, pulls from GitHub `main` branch
- **Local PocketBase:** `localhost:8090`, collection `submissions` (superuser: `claude@croquetclaude.com`)
- **Stitch procedure:** `system/memory/procedure_stitch.md`
- **Design feedback:** `~/.claude/projects/C--croquet-os/memory/feedback_design_serves_concept.md`
- **Identity feedback:** `~/.claude/projects/C--croquet-os/memory/feedback_club_sites_unique_identity.md`
