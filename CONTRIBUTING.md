# Contributing to WEcoS Product Recommendar

First off — thank you for considering a contribution. Whether it's a
typo fix, a methodology improvement, a new PDS reference, or a new
product-line branch in `grease-recommender`, every contribution makes
the suite more accurate for the next DSR or end customer who uses it.

This document covers:

1. [Code of conduct](#code-of-conduct)
2. [What we'd love contributions on](#what-wed-love-contributions-on)
3. [Pull request process](#pull-request-process)
4. [Contribution-license agreement](#contribution-license-agreement)
5. [Style guide](#style-guide)
6. [Testing](#testing)
7. [Communication](#communication)

---

## Code of conduct

This project follows a simple, lightweight code of conduct:

- **Be specific and grounded.** Cite the PDS / TDS / SDS for every spec
  you assert. The methodology relies on producer data, not background
  knowledge.
- **Be willing to update your recommendation.** If a reviewer finds a
  newer PDS or an OEM rep note that supersedes your citation, accept
  the correction and update your contribution.
- **No vendor-hardcoding without a flag.** Recommendations that lock
  to a single brand without a "verified against alternative suppliers"
  note will be declined.

That's it. We don't need a 30-page CoC for this scope.

---

## What we'd love contributions on

### High-value

| Area | Why |
|---|---|
| **New producer PDS / SDS verified references** | Every spec cited in any `SKILL.md` ultimately traces back to a producer document. Adding a new verified PDS reference strengthens the methodology. |
| **Currency-check findings** | If you find a producer has consolidated, renamed, or replaced a SKU, add the legacy → current mapping to the relevant skill's `references/` file. |
| **Customer-corrected methodology** | If a customer pushes back on a recommendation and the methodology needs to absorb the correction (the same loop that produced this Jul 2026 version), document it. |
| **Grease product-line diagrams** | The `grease-recommender` skill has 10 product-line Mermaid diagrams at `/workspace/output/visual-page/grease-skill-pipeline/`. New branches welcome. |
| **Regional supplier verification** | Singapore / SEA / APAC / EU / US regional availability is currently lighter than I'd like. Adding local distributor / refiner data strengthens the customer-facing tiered recommendations. |

### Welcome but lower priority

- Typo fixes, broken-link patches
- Reference-document cleanup (move PDFs into per-skill `verified-pds/` folders)
- Cross-reference tables between brands (e.g., Mobil vs Shell equivalents)

### Out of scope

- Re-licensing under any other license (MIT / Apache / proprietary) —
  the PolyForm Noncommercial 1.0.0 license is locked.
- Vendor-specific preference / bias without a technical rationale —
  the methodology is vendor-neutral by design.

---

## Pull request process

### 1. Fork and branch

```bash
# One-time
gh repo fork AKHtun/wecos-product-recommendar --clone --remote
cd wecos-product-recommendar

# Per change
git checkout -b fix/<short-slug>
# or
git checkout -b feature/<short-slug>
# or
git checkout -b docs/<short-slug>
```

### 2. Make the change

- Edit the relevant `SKILL.md`, `references/*.md`, or scripts.
- If you cite a PDS / TDS / SDS, include the URL and the PDS publication
  date inline.
- If you change methodology, update `CONTRIBUTORS.md` with a new entry
  under the affected skill.
- If you add a new file, give it the same License & Copyright footer
  block (or run the patch script in `scripts/` if available).

### 3. Sign your commit (DCO)

We use the **Developer Certificate of Origin (DCO)** for contribution
tracking. Sign off your commits with `-s`:

```bash
git commit -s -m "Add Singapore SPC regional availability to coolant tier table"
```

The `-s` flag adds a `Signed-off-by: Your Name <your@email>` line,
certifying that you wrote the contribution or have the right to submit
it under the project's license.

### 4. Push and open the PR

```bash
git push origin fix/<short-slug>
gh pr create --title "..." --body "..."
```

**PR title format:** `[skill-name] short description`
Examples:
- `[grease-recommender] add SKF LGEP 2 to standard tier for electric-motor bearings`
- `[lubricant-recommender] fix Volvo VDS-5 out-of-scope clarification`
- `[docs] update README with new contributor onboarding flow`

### 5. PR body template

```markdown
## What does this PR change?

<one-paragraph description>

## Why?

<what gap does this close? what PDS / rep note / customer correction drove this?>

## PDS / SDS citations (if any)

- <URL 1>
- <URL 2>

## Checklist

- [ ] Skill-name(s) updated (or N/A)
- [ ] Per-skill `CONTRIBUTORS.md` lineage updated (or N/A)
- [ ] License & Copyright footer present on new files
- [ ] No hardcoded PDS that wasn't fetched this session
- [ ] No fabricated specs
```

### 6. Review

The Licensor (Aung Khaing Htun, CLS) reviews within ~5 business days.
Trivial changes may be merged same-day. Larger methodology changes may
go through 1-2 review rounds.

---

## Contribution-license agreement

By submitting a pull request to this repository, you affirm that:

1. The contribution is your own original work, **or** you have sufficient
   rights to submit it under this project's license.
2. You agree to license your contribution under the **PolyForm
   Noncommercial License 1.0.0** — the same license as the rest of the
   suite.
3. You understand that the Licensor may re-license the combined work
   in the future under compatible terms (e.g., to a different
   non-commercial open-source license), and you grant the Licensor
   permission to do so for the combined suite.
4. Your contribution does not infringe any third-party copyright,
   patent, trademark, or trade secret.

This is the standard DCO + CLA flow adapted for a PolyForm Noncommercial
license. There is no separate paper CLA — the DCO sign-off on your commit
is sufficient.

---

## Style guide

### YAML frontmatter on `SKILL.md` files

```yaml
---
name: <skill-name>
description: <one-line summary for skill catalog>
allowed-tools: <comma-separated list>
license: PolyForm-Noncommercial-1.0.0
copyright: "(c) 2026 Aung Khaing Htun, CLS. All rights reserved."
author: Aung Khaing Htun, CLS
project: WEcoS Product Recommendar
contributors:
  - human: Aung Khaing Htun, CLS (sole author, methodology and validation)
  - ai-assistance: WEcoS Agents, MuleRun Agent, Mavis by MiniMax
  - session: "#414668884336737 (Jul 2026)"
---
```

### License & Copyright footer

Every `SKILL.md` ends with the License & Copyright footer block. The
template is maintained at the bottom of each `SKILL.md`. If you're adding
a new `SKILL.md`, copy the footer block from any existing skill — do not
paraphrase or compress.

### Tables

Use narrow tables (≤ 5 columns) so they fit on a 1024px-wide GitHub
rendering. Wide attribute tables should be broken into per-axis rows.

### PDS citations

Inline URL + PDS publication date, e.g.:

> `mobil.com/en-au/.../sp-xx-mobil-delvac-modern-15w-40-full-protection` (PDS 12.08.2024)

### Disambiguation

If your change introduces ambiguity between two products, name them in
full on first mention (e.g., "Mobil Delvac Modern 15W-40 Full Protection",
not "Mobil 15W-40 Full Protection").

---

## Testing

Each skill ships with `scripts/render_pdf.py` and `scripts/append_record.py`.
Before opening a PR:

1. **Smoke test** the methodology on the test incumbent named in the
   skill's `output/` folder (if present). If your change breaks the
   test incumbent → the methodology regression is yours to fix.
2. **Render PDF** for the test record and visually verify the rendering.
3. **Append to Excel log** to confirm the record template still produces
   a valid row.

If you're adding a new product line (e.g., a new grease branch), add
a smoke-test incumbent and expected-match in the `references/` folder
for the next contributor to verify against.

---

## Communication

For questions, methodology debates, or to flag a methodology regression
without opening a PR:

- **GitHub Issue** — preferred for any persistent record
- **PR comment** — for changes already in flight
- **Discussion** (if enabled) — for open-ended methodology debate

We don't have a Discord / Slack channel for this project. The issue
tracker is the canonical record of methodology changes.

---

## Recognition

Every accepted PR gets a credit line in the affected skill's
`CONTRIBUTORS.md`. Major contributions (sustained over multiple PRs) get
listed in the master `CONTRIBUTORS.md` suite-level authorship section.

---

**Once more, thank you.** The methodology only stays accurate because
people like you take the time to push corrections back upstream.

— Aung Khaing Htun, CLS, Licensor