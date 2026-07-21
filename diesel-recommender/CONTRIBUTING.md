WEcoS Product Recommendar
Copyright © 2026 Aung Khaing Htun, CLS. All rights reserved.
Licensed under PolyForm Noncommercial License 1.0.0.

# Contributing to diesel-recommender

This skill recommends equivalent or alternative diesel fuels (ULSD / EN 590, off-road / mining / construction diesel, additized premium diesel, marine distillate fuels) for an incumbent third-party product.

## Before you start

- [ ] Read the parent repo's [CONTRIBUTING.md](../CONTRIBUTING.md) (5 min)
- [ ] Read this skill's [SKILL.md](./SKILL.md) §0 (hard rules) and §2 (fuel categories) (10 min)

## Quick onboarding

### What should I edit?

| If you want to… | Edit this file | Why |
|---|---|---|
| Add a new regional ULSD variant (e.g., Singapore NEA ULSD ≤ 10 ppm S) | `references/supplier_catalogs.md` | Keeps product database separate |
| Add a premium diesel additive package (e.g., Caltex Techron) | `references/supplier_catalogs.md` | Additive products are reference data |
| Fix a stale diesel specification PDS URL | `SKILL.md` (the line with the old URL) | Minimal change; no test needed |
| Change fuel category filter (e.g., add biodiesel branch) | `SKILL.md` §3–§4 + `CONTRIBUTORS.md` | Methodology change |
| Change report format for diesel recommendations | `templates/report_template.md` | Template separate from logic |
| Fix PDF/Excel rendering bugs | `scripts/render_pdf.py` or `scripts/append_record.py` | Test before PR |

**Decision tree:** Not sure? Start with `references/supplier_catalogs.md`.

---

## Common contribution scenarios

### Scenario A: Add a new regional ULSD specification

**Example:** "Malaysia has introduced a new ULSD standard (≤5 ppm S, effective 2026); I want to add this."

**Steps:**

1. **Fetch the specification:**
   - Source: Malaysian Standards (MS) or PETRONAS standards
   - EN 590 equivalent (most ASEAN countries adopt EN 590 with regional tweaks)

2. **Add to `references/supplier_catalogs.md` under Regional ULSD:**
   ```markdown
   #### ULSD — Southeast Asia
   
   - **Malaysia ULSD 2026 (≤5 ppm S)**
     - Specification: MS 1449:2023 / EN 590 equivalent
     - Sulphur content: ≤5 ppm (ultra-low, Euro 5/6 diesel compatible)
     - Cetane number: ≥51
     - Density: 820–860 kg/m³
     - Flash point: >55 °C
     - Suppliers: PETRONAS (Petronas Diesel Euro 5M)
     - Approved for: Euro 5, Euro 6, SCR-equipped vehicles
     - Effective date: January 1, 2026
     - Standards ref: MS 1449:2023, EN 590:2009+A1:2017
   ```

3. **Smoke test:**
   ```bash
   python scripts/render_pdf.py \
     --incumbent="Shell Diesel Ultra" \
     --application="diesel" \
     --region="Malaysia" \
     --oem="MAN TGX" \
     --output=/tmp/test-malaysia-ulsd.pdf
   
   # Verify: New Malaysia ULSD recommendation appears
   ```

4. **Open a PR:**
   ```
   Title: [diesel-recommender] add Malaysia ULSD 2026 (≤5 ppm S)
   
   Body:
   ## What does this PR change?
   Adds Malaysia ULSD 2026 regional specification (≤5 ppm S, MS 1449:2023).
   
   ## Why?
   New regional standard effective Jan 2026; affects Euro 5/6 fleet recommendations in Malaysia.
   
   ## Standards ref
   - MS 1449:2023 (Malaysian Standards)
   - EN 590:2009+A1:2017 (European equivalent)
   ```

---

### Scenario B: Fix a stale fuel specification URL

**Example:** "EN 590 standard link is broken (2009 revision outdated; 2009+A1:2017 revision exists)."

**Steps:**

1. **Update SKILL.md:**
   ```markdown
   # Before:
   EN 590:2009 — standard.iso.org/.../en-590-2009
   
   # After:
   EN 590:2009+A1:2017 — standard.iso.org/.../en-590-2009-a1-2017
   ```

2. **No test needed.** Verify HTTP 200.

3. **Open a PR.**

---

### Scenario C: Add a biodiesel (FAME) or synthetic diesel (XTL) branch

**Example:** "I want to add biodiesel (FAME 10 / B10) as an alternative fuel category."

**Steps:**

1. **Read §3 (Fuel Categories) in SKILL.md.**
   - Understand the current categories (ULSD, off-road diesel, marine distillate)
   - Biodiesel (FAME) is a separate category with different compatibility rules

2. **Edit SKILL.md §3:**
   ```markdown
   # Add new fuel type:
   - ULSD (Diesel 1)
   - Off-road diesel (marked red)
   - Marine distillate (ISO 8217 DMA / DMZ / DMB)
   - **Biodiesel / FAME (Fatty Acid Methyl Ester)**
   ```

3. **Edit SKILL.md §4 (Filter logic for FAME):**
   - Cetane number: ≥48 (lower than ULSD)
   - Compatibility check: Rubber seals, fuel injector deposits, winter gelling
   - OEM approval: Many truck OEMs restrict to FAME 10 (10% bio, 90% mineral)

4. **Update CONTRIBUTORS.md:**
   ```markdown
   - **2026-07-21 — biodiesel (FAME) filter:** Added FAME 10 branch with compatibility warnings.
     Note: Many OEMs restrict to ≤10% FAME. Check PDS for compatibility.
     Author: [Your Name]
   ```

5. **Smoke test:**
   ```bash
   # Test existing ULSD still works
   python scripts/render_pdf.py \
     --incumbent="Shell Diesel Ultra" \
     --application="diesel" \
     --oem="MAN" \
     --output=/tmp/test-ulsd.pdf
   
   # Test new FAME filter
   python scripts/render_pdf.py \
     --incumbent="CALTEX StarDiesel Pro B10" \
     --application="diesel" \
     --fuel-type="biodiesel" \
     --oem="Volvo FH" \
     --output=/tmp/test-fame.pdf
   ```

6. **Open a PR with methodology change label.**

---

## Test flow

### Test 1: PDF render

```bash
cd diesel-recommender

python scripts/render_pdf.py \
  --incumbent="Shell Diesel Ultra" \
  --application="diesel" \
  --region="Singapore" \
  --oem="MAN D0826" \
  --target-suppliers="Shell,Caltex,ExxonMobil" \
  --output=/tmp/test-diesel.pdf

# Expected:
# - PDF renders (valid)
# - Standard + Upgraded recommendations shown
# - All PDS citations are URLs
# - Regional specification called out (NEA ULSD ≤ 10 ppm S, etc.)
```

### Test 2: Excel append

```bash
python scripts/append_record.py \
  --record=templates/recommendation_record.xlsx \
  --incumbent="Shell Diesel Ultra" \
  --standard-pick="Caltex Techron Diesel" \
  --upgraded-pick="ExxonMobil Diesel Efficient" \
  --rationale="ULSD ≤10ppm S; Techron additive package; cost-neutral" \
  --dle-notes="Singapore fleet, MAN D0826 diesel"

# Expected: Row appended, no corruption
```

### Test 3: Verify no hard-rule violations

- [ ] Did I cite a fuel specification (PDS) for every claim? (hard rule #1)
- [ ] Did I recommend without fetching the standard? (hard rule #2)
- [ ] Did I flag compatibility warnings (biodiesel, additives)? (hard rule #3)
- [ ] Did I ask for OEM/region and application? (hard rule #4)
- [ ] Did I produce all three deliverables? (hard rule #5)
- [ ] Did I append the standard disclaimer? (hard rule #6)

---

## File reference guide

| File | Purpose | Edit if… |
|---|---|---|
| `SKILL.md` | Methodology + fuel categories | Changing category filter, fuel type classification |
| `references/supplier_catalogs.md` | Regional ULSD specs + additive products | Adding regional specs or premium diesel variants |
| `references/sop-flow.md` | SOP diagrams (fuel category decision tree) | Updating flowcharts for new categories (biodiesel, etc.) |
| `templates/report_template.md` | Chat report format | Changing output structure |
| `scripts/render_pdf.py` | PDF rendering | Fixing rendering bugs |
| `CONTRIBUTORS.md` | Authorship lineage | Methodology change |

---

## Questions?

### Diesel-specific questions
- **What's the difference between ULSD, off-road diesel, and marine distillate?**
  - **ULSD (Ultra-Low Sulphur Diesel):** ≤10 ppm S, for on-road vehicles; EN 590 standard
  - **Off-road diesel:** Higher sulphur (≤500 ppm), colored red (marked), for construction/mining equipment
  - **Marine distillate:** ISO 8217 standard (DMA/DMZ/DMB), specialized for marine engines, different viscosity range
  - See SKILL.md §2 for details.

- **Why does sulphur content matter?**
  - Low sulphur protects SCR (Selective Catalytic Reduction) systems and fuel injectors. High sulphur can poison SCR catalysts and damage engine components. OEM approval depends on sulphur level.

- **Can I use off-road diesel in a Euro 5 truck?**
  - **No.** Off-road diesel has higher sulphur (damages SCR); plus it's marked red (legal issue in many regions). SKILL.md hard rule #3 (compatibility warnings) applies.

### PDS & standards questions
- **Where do I find fuel specifications?**
  - EN 590 (Europe): standard.iso.org
  - ISO 8217 (Marine): standard.iso.org
  - Regional: PETRONAS (Malaysia), JBPA (Japan), etc.

- **Stale fuel specification URL?**
  - Open an Issue with `[stale-pds]` + old standard + new revision.

---

## Thank you

Every new regional spec, every additive package reference, every fuel compatibility fix makes the suite more accurate for fleet operators worldwide.

— Aung Khaing Htun, CLS, Licensor
