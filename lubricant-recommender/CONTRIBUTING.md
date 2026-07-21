WEcoS Product Recommendar
Copyright © 2026 Aung Khaing Htun, CLS. All rights reserved.
Licensed under PolyForm Noncommercial License 1.0.0.

# Contributing to lubricant-recommender

This skill recommends equivalent or alternative lubricants (engine oils, gear oils, hydraulic oils, compressor oils, turbine oils, refrigeration-compressor oils, PAG fluids, and heat-transfer fluids) for an incumbent third-party product.

## Before you start

- [ ] Read the parent repo's [CONTRIBUTING.md](../CONTRIBUTING.md) (5 min) — covers DCO sign-off, PR process, license agreement
- [ ] Read this skill's [SKILL.md](./SKILL.md) §0 (hard rules) and §4 (filter logic) (10 min) — you'll need these when reviewing test outcomes

## Quick onboarding

### What should I edit?

| If you want to… | Edit this file | Why |
|---|---|---|
| Add a new PDS/SDS reference for a product | `references/supplier_catalogs.md` | Keeps product database separate from methodology |
| Fix a stale or 404 PDS URL | `SKILL.md` (the line with the old URL) | Minimal change; no test needed |
| Change filter logic (e.g., add biodegradable-oil branch) | `SKILL.md` §4 + `CONTRIBUTORS.md` | Methodology is in SKILL.md; authorship in CONTRIBUTORS.md |
| Change report format or templates | `templates/report_template.md` or `templates/recommendation_record.xlsx` | Templates are separate from logic |
| Fix a PDF/Excel rendering bug | `scripts/render_pdf.py` or `scripts/append_record.py` | Scripts are utilities; test them before PR |
| Update methodology (e.g., new hard rule) | `SKILL.md` §0–§13 + `CONTRIBUTORS.md` + `../docs/releases/` | Major change; needs review + documentation |

**Decision tree:** Not sure? Start with `references/supplier_catalogs.md` (safest; lowest test burden).

---

## Common contribution scenarios

### Scenario A: Add a new PDS / SDS verified reference

**Example:** "I found the latest Mobil Delvac Modern 15W-40 Full Protection PDS."

**Steps:**

1. **Fetch the PDS from the manufacturer's official site:**
   ```
   https://www.mobil.com/en-au/.../technical-data-sheet-mobil-delvac-modern-15w-40-full-protection
   ```

2. **Extract the six attributes:**
   - Application (engine oil, SAE 15W-40)
   - Base oil (synthetic PAO)
   - Viscosity (SAE 15W-40, VI ~140)
   - Industry standards (API CK-4, ACEA E9, JASO DH-2)
   - Operating temp (flash 230 °C, pour -27 °C)
   - OEM approvals (Volvo VDS-4, MB 226.14, Cummins CES 20.081)

3. **Add to `references/supplier_catalogs.md` under the ExxonMobil section:**
   ```markdown
   #### Delvac Modern Series (Synthetic PAO)
   
   - **Mobil Delvac Modern 15W-40 Full Protection**
     - Viscosity: SAE 15W-40 (VI ~140)
     - Base oil: Synthetic PAO
     - Industry standards: API CK-4, ACEA E9, JASO DH-2
     - OEM approvals: Volvo VDS-4, MB 226.14, Cummins CES 20.081
     - Drain interval: 60,000 km (OEM standard, synthetic advantage)
     - PDS: https://www.mobil.com/.../mobil-delvac-modern-15w-40-full-protection (dated 2024-08-15)
   ```

4. **Test the reference (smoke test):**
   ```bash
   python scripts/render_pdf.py \
     --incumbent="Shell Rimula R5 E 10W-40" \
     --application="engine" \
     --oem="MAN D0834" \
     --target-supplier="ExxonMobil" \
     --output=/tmp/test-mobil.pdf
   
   # Manually verify: Does your new Mobil product appear in the recommended set?
   # If yes, ✅ pass. If no, check if it matches the incumbent specs (viscosity, OEM approval, etc.)
   ```

5. **Open a PR:**
   ```
   Title: [lubricant-recommender] add Mobil Delvac Modern 15W-40 Full Protection to engine-oil tier
   
   Body:
   ## What does this PR change?
   Adds Mobil Delvac Modern 15W-40 Full Protection to the engine-oil product database.
   
   ## Why?
   Customer request (Issue #123); latest PDS shows Cummins CES 20.081 approval (not in old PDS).
   
   ## PDS citations
   - https://www.mobil.com/.../mobil-delvac-modern-15w-40-full-protection (PDS 2024-08-15)
   
   ## Checklist
   - [x] Skill name(s) updated (lubricant-recommender)
   - [x] CONTRIBUTORS.md updated (no methodology change)
   - [x] License & Copyright footer present (N/A, edited references file only)
   - [x] No hardcoded PDS (fetched this session)
   - [x] No fabricated specs (all from official PDS)
   ```

---

### Scenario B: Fix a stale or 404 PDS URL

**Example:** "The Shell Rimula R6 M PDS link in SKILL.md is returning HTTP 404."

**Steps:**

1. **Find the new PDS on Shell's site:**
   - Old link: `https://www.shell.com/en-au/.../shell-rimula-r6-m` (404)
   - New link: `https://www.shell.com/en-au/business-customers/motorsport/shell-rimula/shell-rimula-r6-m` (200 OK)

2. **Edit SKILL.md:**
   ```markdown
   # Before:
   shell.com/en-au/.../shell-rimula-r6-m (PDS 2022-05-10)
   
   # After:
   shell.com/en-au/business-customers/motorsport/shell-rimula/shell-rimula-r6-m (PDS 2024-06-15)
   ```

3. **No test needed.** Just verify the URL works in your browser (HTTP 200).

4. **Open a PR:**
   ```
   Title: [lubricant-recommender] fix Shell Rimula R6 M PDS URL (stale)
   
   Body:
   ## What does this PR change?
   Updates stale Shell Rimula R6 M PDS link (HTTP 404 → 200).
   
   ## PDS citations
   - https://www.shell.com/.../shell-rimula-r6-m (PDS 2024-06-15, new)
   
   ## Checklist
   - [x] No hardcoded PDS
   - [x] No methodology change
   ```

---

### Scenario C: Add a new product-line filter branch

**Example:** "I want to add a biodegradable engine oil filter to §4."

**Steps:**

1. **Read §4 (Sequential Filter) in SKILL.md carefully.**
   - Understand the six-axis filter (application → base oil → viscosity → standards → temp → OEM)
   - Biodegradable oils are a base-oil type (axis 2.2), so you'll modify the filter there

2. **Edit SKILL.md §4:**
   ```markdown
   # Before (axis 2.2 — base oil):
   - Mineral, semi-synthetic, fully synthetic (PAO / ester), PAG
   
   # After (axis 2.2 — base oil):
   - Mineral, semi-synthetic, fully synthetic (PAO / ester), PAG, biodegradable (HETG / ester / plant-based)
   ```

3. **Update CONTRIBUTORS.md:**
   Add a new entry under "lubricant-recommender" with your name, date, and the change:
   ```markdown
   - **2026-07-21 — biodegradable engine oil filter:** Added axis 2.2 branch for HETG (polyol ester) biodegradable oils. Aligns with EU Ecolabel and ISO 12922 HETG category.
     Author: [Your Name] (contribution accepted via PR #XYZ)
   ```

4. **Add a test incumbent:**
   Create `references/test-incumbent-biodegradable.md`:
   ```markdown
   # Test incumbent: Mobil EAL 224H (biodegradable ester)
   
   ## Input
   - Incumbent: Mobil EAL 224H
   - Application: Hydraulic oil (ISO VG 46)
   - OEM: Volvo loader (L60H)
   - Operating conditions: 40–60 °C, outdoor (rain exposure)
   
   ## Expected standard recommendation
   - Mobil EAL 224H (incumbent, matches all axes)
   
   ## Expected upgraded recommendation
   - Kluber Isoflex TOPAS NB 52 (higher biodegradability, Ecolabel-certified)
   ```

5. **Smoke test:**
   ```bash
   cd lubricant-recommender
   
   # Test the new filter doesn't break existing incumbents
   python scripts/render_pdf.py \
     --incumbent="Shell Rimula R5 E 10W-40" \
     --application="engine" \
     --oem="MAN" \
     --output=/tmp/test-existing.pdf
   
   # Test the new biodegradable filter works
   python scripts/render_pdf.py \
     --incumbent="Mobil EAL 224H" \
     --application="hydraulic" \
     --oem="Volvo L60H" \
     --output=/tmp/test-biodegradable.pdf
   
   # Manually verify both PDFs render correctly and recommendations are sensible
   ```

6. **Open a PR:**
   ```
   Title: [lubricant-recommender] add biodegradable (HETG) engine oil filter
   
   Body:
   ## What does this PR change?
   Extends §4 filter to include biodegradable ester-based oils (ISO 12922 HETG category).
   
   ## Why?
   Growing customer demand for Ecolabel-certified / EU-compliant hydraulic oils.
   
   ## Changes
   - SKILL.md §4, axis 2.2: added biodegradable base-oil type
   - CONTRIBUTORS.md: added lineage entry
   - references/test-incumbent-biodegradable.md: added test case
   
   ## Test outcome
   ✅ Existing incumbents (Shell Rimula, Mobil Delvac) produce same recommendations as before
   ✅ New biodegradable incumbent (Mobil EAL 224H) correctly filtered
   
   ## Checklist
   - [x] SKILL.md updated (methodology)
   - [x] CONTRIBUTORS.md updated (lineage)
   - [x] Test incumbent added (for next contributor to verify)
   - [x] No hardcoded PDS
   ```

---

## Test flow

**Before opening any PR, run these three tests:**

### Test 1: PDF render (smoke test methodology)

```bash
cd lubricant-recommender

python scripts/render_pdf.py \
  --incumbent="Shell Rimula R5 E 10W-40" \
  --application="engine" \
  --oem="MAN D0834" \
  --target-suppliers="ExxonMobil,Shell,Caltex" \
  --output=/tmp/test-render.pdf

# Expected output:
# - PDF file created (valid, not corrupted)
# - Chat report section shows Standard + Upgraded recommendations
# - All PDS citations are URLs (no "N/A")
# - No hard-rule violations (e.g., every spec cites a source URL)
```

### Test 2: Excel append (verify template structure)

```bash
python scripts/append_record.py \
  --record=templates/recommendation_record.xlsx \
  --incumbent="Shell Rimula R5 E 10W-40" \
  --standard-pick="Mobil Delvac Modern 15W-40" \
  --upgraded-pick="Mobil Delvac Modern 15W-40 Full Protection" \
  --rationale="Volvo VDS-4 mandatory; Cummins CES 20.081 upgrade extends drain interval" \
  --dle-notes="Customer fleet: Singapore B9TL buses"

# Expected output:
# - New row appended to Excel
# - All columns populated (no blanks)
# - Excel file still opens in LibreOffice / Excel (not corrupted)
```

### Test 3: Verify no hard-rule violations

**Manual checklist:**

- [ ] Did I cite a PDS / TDS / SDS for every spec I added? (hard rule #1)
- [ ] Did I recommend a product without fetching its PDS? (hard rule #2, violation = must fix)
- [ ] Did I apply compatibility warnings (if PAG, grease, or refrigeration compressor oil)? (hard rule #3)
- [ ] Did I ask for OEM / Model and operating conditions before recommending? (hard rule #4)
- [ ] Did I produce all three deliverables (chat, PDF, Excel)? (hard rule #5)
- [ ] Did I append the standard disclaimer verbatim? (hard rule #6)

---

## File reference guide

| File | Purpose | Edit if… | Don't edit if… |
|---|---|---|---|
| `SKILL.md` | Methodology + hard rules (§0–§13) | Adding/changing filter logic, hard rules, methodology | Just adding a product reference (use `references/`) |
| `references/supplier_catalogs.md` | Product database (organized by supplier + category) | Adding new products / updating PDS links for existing products | Changing methodology logic or hard rules |
| `references/sop-flow.md` | SOP diagrams / visual methodology | Updating flowcharts or decision trees | If no SOP changed |
| `templates/report_template.md` | Chat report format (what DSR sees) | Changing report structure or output format | Adding a new product (use `references/`) |
| `templates/recommendation_record.xlsx` | Excel row structure | Changing column names / adding fields | If columns stay the same (just append rows via script) |
| `scripts/render_pdf.py` | PDF rendering logic | Fixing rendering bugs or adding new sections to PDF | If rendering works fine |
| `scripts/append_record.py` | Excel append logic | Fixing append bugs or new Excel columns | If appending works |
| `CONTRIBUTORS.md` | Authorship lineage | You made a methodology change or major correction | You just added a product (no CLA update needed) |
| `LICENSE` | Pointer to parent LICENSE | Never (copy only) | Always (read-only pointer) |

---

## Questions?

### Methodology questions
- **How do I know if a filter applies?** Read SKILL.md §4 (Sequential Filter). It walks through each axis step-by-step.
- **What counts as an OEM approval?** See SKILL.md §3 (attribute 2.6) and §5 (OEM cross-check).
- **Can I skip any hard rules?** No. Hard rules §0–§6 are non-negotiable. If you think one should change, open a GitHub Issue with the label `[methodology-question]`.

### Script bugs
- **`render_pdf.py` crashes.** Open an Issue with `[lubricant-recommender-script-bug]` + error message + the incumbent product name.
- **Excel row doesn't append.** Check the Excel file isn't locked (close it in Excel / Calc first). If still broken, open an Issue.

### PDS currency
- **I found a 404 link.** Open an Issue with `[stale-pds]` + the old URL + a link to the new one (if you found it).
- **The PDS is outdated.** If > 2 years old and a newer revision exists, open an Issue with `[stale-pds]` + skill name + product.

### General questions
- **I don't know where to start.** Begin with Scenario A (add a PDS reference to `supplier_catalogs.md`). Lowest barrier; builds confidence.
- **This guide doesn't cover my case.** Open an Issue with `[contribution-guidance]` + describe your scenario.

---

## One more thing

**Thank you for considering a contribution.** Every new PDS reference, every stale-URL fix, every filter improvement makes the suite more accurate for the next DSR or end customer. Your work matters.

— Aung Khaing Htun, CLS, Licensor
