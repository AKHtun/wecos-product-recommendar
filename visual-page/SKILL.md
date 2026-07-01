---
name: visual-page
description: >-
  Create a visual HTML page when plain text cannot effectively convey the information.
  Use this skill when: the content involves diagrams (flowcharts, architecture, sequence diagrams),
  data comparisons (tables, charts), timelines, interactive demos, visual layouts, or any scenario
  where a simple webpage would communicate more clearly than markdown text.
  Also use when the user explicitly asks for a visual page, a webpage, or says "show me" / "draw a diagram" / "make a page" / "visualize".
  This skill should be used proactively by the model — do not wait for the user to ask.
---

# Visual Page Skill

## Workflow

Create a self-contained local HTML webpage and deliver it to the user.

1. Choose an output path:
   - If the user specified an output path, use it.
   - If the user provided an input file or directory and no output path, save the HTML next to the input when appropriate.
   - Otherwise, create a descriptive `.html` file in a temp or workspace directory (e.g. `/tmp/visual-page/<descriptive-name>/index.html`). The descriptive name (e.g. `agent-arch-overview`, `mr-1234-changes`) lives in the **directory name**; the file inside is always `index.html`. Each page gets its own directory — **never overwrite another page's directory**.
2. Write one complete HTML document with all CSS and JavaScript inlined unless an external CDN library is genuinely useful (Tailwind, Chart.js, Mermaid, D3).
3. Verify the page is valid enough to open directly in a browser: no missing local assets, no broken relative references, responsive layout.
4. Send the file to the user with a `<media />` tag:
   ```
   <media type="file" src="/absolute/path/to/index.html" caption="Visual page" />
   ```

When the user asks to revise, update, or tweak a page, edit the existing HTML file so previously shared paths remain valid. If the previous file is unavailable, create a new one and mention it is a refreshed copy.

### Multi-page sites

When building multiple linked pages (e.g. a main report + detail pages):

1. Create **sibling directories**:
   ```
   /tmp/visual-page/my-report/index.html        <- main page
   /tmp/visual-page/my-report-detail/index.html  <- detail page
   ```
2. Cross-link with **relative paths**: `<a href="../my-report-detail/index.html">Detail</a>`
3. Send the main entry point via `<media />`.

---

## Design Philosophy

**Aesthetics is the goal, not decoration.** A page that "works" but looks cheap is a failure. The reader's eyes judge in 2 seconds before reading a single word. Treat beauty as a non-negotiable requirement equal to data correctness.

**Charts and diagrams first, text assists.** Visuals are the PRIMARY communication tool — they let readers grasp the point in seconds. Text exists to annotate details that visuals can't convey alone. When building a page, start from "what chart/diagram tells this story?" not "what paragraphs explain this?" If a section has 3+ paragraphs without a visual, find the chart, flow, or illustration that replaces most of that text.

**Design for the reader.** You are guiding a human eye, not displaying your work. One H1, one core conclusion, F-pattern scanning. Empty space is a feature. Charts and inline SVG beat dense paragraphs for any structured comparison or hierarchy.

**Less is more.** Every element earns its place. No filler sections, no data slop (pointless stats/badges). When unsure between "add another card" or "let it breathe" — let it breathe.

---

## Rules

### 1. Pick the page mode FIRST

| Mode | When | Background | Font |
|---|---|---|---|
| **Data UI** | Dashboards, charts, tables | `#fafafa` / white | Sans (Outfit) |
| **Long-read / Report** | Research, design docs, architecture pages | Warm cream `#f7f5f0` | Sans body + **serif headlines** (DM Serif Display) |
| **Terminal** | Code demos, log viewers | `#1a1a2e` (NEVER `#000`) | Mono-prominent |

Wrong-mode = ugly page. Research report on dark slate -> dashboard look. Dashboard with serif -> poster look.

### 2. Color

**BANNED:** pure `#000`, purple/blue AI gradients, neon glows, oversaturated accents.

**Accent — pick ONE per page:**
- Data UI: `#10b981` / `#3b82f6` / `#f59e0b` / `#f43f5e` / `#6366f1`
- Report: `#2f6f5e` / `#c97b3f` / `#b06367`

Use at 5-10% opacity for backgrounds, 100% for headers/icons only.

**Report palette:** cream `#f7f5f0`, cards white + border `#e9e3d6`, text `#14171e` / `#3a4256` / `#7c7a72`. Optional: two corner radial gradients at 5% opacity.

### 3. Typography

**BANNED fonts:** Inter, Roboto, Arial, Fraunces, system defaults.

**Use:** `Outfit` (sans), `JetBrains Mono` (mono), `DM Serif Display` (Report headlines only).

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Outfit:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

Report headlines: `font-serif text-3xl font-normal tracking-[-0.005em]`. Body always sans. Serif forbidden on Data UI.

### 4. Layout

**BANNED:** 3 equal cards in a row, centered-everything heroes, `border-l-4` accent cards, `h-screen`.

**Use:** `max-w-5xl mx-auto px-6 md:px-8`, `space-y-16`, CSS Grid 12-column, `min-h-[100dvh]`. Mobile: single-column below 768px, no horizontal scroll.

### 4.5 Density — CJK pages need tighter spacing

Most CSS frameworks assume Latin typography. CJK characters are square blocks with built-in visual mass — copying Latin defaults (`line-height: 1.7+`, body `16-17px`, section gap `80px+`, card padding `28-32px`) makes Chinese pages feel sparse, with the first screen showing only a hero and one card.

Calibrate: **does the first screen communicate the core idea, or is it just hero + breathing room?**

Working ranges for CJK-heavy text (adjust by content, not hard rules):
- Body: 14-15px, line-height 1.5-1.65
- Headlines: H1 28-34px, H2 22-26px
- Section gaps: 40-56px
- Paragraph margin-bottom: 8-12px
- Card padding: 16-22px

Latin-only pages can be more generous. Mixed CJK + Latin follows the CJK side.

### 5. Surfaces

`rounded-2xl`, `border border-zinc-200/50`. Diffusion shadows only: `shadow-[0_2px_8px_rgba(0,0,0,0.04)]` / `shadow-[0_4px_16px_-2px_rgba(0,0,0,0.06)]`. Hover: `hover:-translate-y-0.5 hover:shadow-md transition-all duration-200`.

### 6. Icons & diagrams — inline SVG only

**No emoji as icons, no ASCII art for diagrams.** Use inline SVG from [lucide.dev](https://lucide.dev) with `currentColor`, `stroke-width="2"`, `viewBox="0 0 24 24"`. One icon per section header max.

For diagrams: use Pattern Library components (arch-row, flow-node) or Mermaid for 4+ nodes. Never box-drawing characters.

### 7. Visualization — chart-first, pick the right tool

**Default mindset:** every key point deserves a visual. Ask "what chart explains this?" before writing paragraphs. Text annotates what the visual can't show alone.

| Data shape | Tool |
|---|---|
| 2-8 comparisons | CSS bench bars or `<table>` |
| Time-series / >8 points | Chart.js |
| Hierarchy / modules | Arch-row pattern or inline SVG |
| Process flow >= 4 nodes | Mermaid |
| Process flow 2-3 nodes | Flow-node pattern |
| Key-value <= 6 rows | KV-card pattern |
| Roadmap / phases | Step-timeline pattern |

**Rule:** don't import Chart.js/Mermaid for <5 data points or <4 nodes — hand-roll CSS/SVG.

Chart.js defaults: `font.family = "'Outfit'"`, `color = '#71717a'`, `borderColor = 'rgba(0,0,0,0.04)'`, `borderRadius: 6`.

### 8. Pattern Library

Copy-paste components. CSS vars assume Report palette.

**Bench bar:**
```html
<div class="bench-row">
  <span class="label">Name</span>
  <div class="bar-bg"><div class="bar-fill" style="width:42.5%"></div></div>
  <span class="val">42.5%</span>
</div>
```
```css
.bench-row { display: grid; grid-template-columns: 140px 1fr 60px; gap: 14px; align-items: center; padding: 7px 0; }
.bar-bg { height: 18px; background: var(--line-soft); border-radius: 6px; overflow: hidden; }
.bar-fill { height: 100%; background: linear-gradient(90deg, var(--primary), #4a8e7c); border-radius: 6px; }
```

**Step timeline:**
```css
.timeline { position: relative; }
.timeline::before { content: ""; position: absolute; left: 22px; top: 6px; bottom: 6px;
  width: 2px; background: linear-gradient(180deg, var(--primary), var(--accent)); }
.step { position: relative; padding-left: 60px; margin-bottom: 32px; }
.step-icon { position: absolute; left: 6px; top: 0; width: 36px; height: 36px;
  border-radius: 50%; background: white; border: 2px solid var(--primary);
  display: inline-flex; align-items: center; justify-content: center; }
```

**Arch row** (replaces ASCII trees): two-column grid `130px 1fr`, tier label left, blocks flow right.
```html
<div class="arch-row">
  <span class="arch-tier">Layer</span>
  <div class="arch-blocks">
    <span class="arch-block">Module <span class="desc-mini">description</span></span>
  </div>
</div>
```

**Flow node + arrow** (replaces ASCII boxes): two cards stacked, arrow row in middle with SVG arrowheads + protocol label.

**KV card:** two-column grid `110px 1fr`, dashed borders between rows. Better than tables for <= 6 rows.

---

## Anti-Slop Checklist

- [ ] 2-second test — first impression crafted, not generic?
- [ ] Reader gets core conclusion within one screen
- [ ] **Every key point has a visual** — no section with 3+ paragraphs and zero charts/diagrams
- [ ] Enough whitespace — if "full", remove a section
- [ ] Page mode picked correctly (not dark dashboard for a report)
- [ ] No `#000`, no AI gradients, no neon, no Inter/Roboto/Arial
- [ ] No emoji icons — inline SVG with `currentColor`
- [ ] No ASCII art diagrams — using CSS/SVG patterns
- [ ] No 3-equal-cards, no `border-l-4` accent cards
- [ ] Didn't import Chart.js/Mermaid for <5 data points
- [ ] No filler, no round-number stats, no banned copy ("Elevate", "Seamless")
- [ ] Mobile responsive, every interactive element has hover state
- [ ] Delivered the `.html` file via `<media />`

---


## Example Output

> Here's a visual page — much clearer than text:
>
> `<media type="file" src="/tmp/visual-page/agent-arch-overview/index.html" caption="Architecture overview" />`
