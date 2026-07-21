WEcoS Product Recommendar
Copyright © 2026 Aung Khaing Htun, CLS. All rights reserved.
Licensed under PolyForm Noncommercial License 1.0.0.

# Contributing to adblue-def-recommender

This skill recommends equivalent or alternative AdBlue / DEF (Diesel Exhaust Fluid) products — ISO 22241 AUS 32 urea solution for SCR-equipped diesel vehicles.

## Before you start

- [ ] Read the parent repo's [CONTRIBUTING.md](../CONTRIBUTING.md) (5 min)
- [ ] Read this skill's [SKILL.md](./SKILL.md) §0 (hard rules) and §2 (intake fields) (10 min)

## Quick onboarding

### What should I edit?

| If you want to… | Edit this file | Why |
|---|---|---|
| Add a new AdBlue/DEF supplier or regional variant | `references/supplier_catalogs.md` | Keeps product database separate |
| Fix a stale AdBlue/DEF PDS URL | `SKILL.md` (the line with the old URL) | Minimal change; no test needed |
| Change storage/compatibility warnings (temperature, container) | `SKILL.md` §6 (warnings) + `CONTRIBUTORS.md` | Methodology change |
| Change report format for DEF recommendations | `templates/report_template.md` | Template separate from logic |
| Fix PDF/Excel rendering bugs | `scripts/render_pdf.py` or `scripts/append_record.py` | Test before PR |
| Add a new DEF regional certification (e.g., Chinese GB 29914) | `references/sop-flow.md` + `SKILL.md` §3 | Major change; needs review |

**Decision tree:** Not sure? Start with `references/supplier_catalogs.md`.

---

## Common contribution scenarios

### Scenario A: Add a new regional AdBlue/DEF supplier

**Example:** "I found a VDA-certified AdBlue supplier in Malaysia; want to add it."

**Steps:**

1. **Verify VDA certification:**
   - VDA (Verband der Automobilindustrie) certification is mandatory for all AdBlue/DEF products
   - Check: Is the supplier listed on the VDA register? (https://www.vda.de)

2. **Fetch the product PDS:**
   - Source: Supplier's technical data sheet
   - Must show: ISO 22241 AUS 32 compliance, VDA cert, storage temperature range

3. **Add to `references/supplier_catalogs.md` under Regional AdBlue:**
   ```markdown
   #### AdBlue / DEF — Southeast Asia
   
   - **WSOIL AdBlue (Malaysia)**
     - Chemistry: 32.5% urea solution (ISO 22241 AUS 32)
     - Certification: VDA (Verband der Automobilindustrie)
     - Package sizes: 10 L, 200 L, 1000 L
     - Storage temp: -11 °C to +30 °C (sealed container)
     - Compatibility: All ISO 22241 AUS 32-compliant SCR systems (Euro 4+)
     - Availability: Malaysia, Singapore, Thailand
     - Supplier cert: VDA register entry #2024-05-001
     - PDS: https://www.wsoil.com/.../wsoil-adblue-malaysia (dated 2024-06-20)
   ```

4. **Smoke test:**
   ```bash
   python scripts/render_pdf.py \
     --incumbent="ARLA 32" \
     --application="adblue" \
     --region="Malaysia" \
     --oem="MAN TGX" \
     --output=/tmp/test-wsoil-adblue.pdf
   
   # Verify: New WSOIL recommendation appears
   ```

5. **Open a PR:**
   ```
   Title: [adblue-def-recommender] add WSOIL AdBlue (VDA-certified, Malaysia)
   
   Body:
   ## What does this PR change?
   Adds WSOIL AdBlue to regional supplier catalog (Malaysia availability).
   
   ## Why?
   Regional supplier expansion; WSOIL is only VDA-certified manufacturer in Malaysia (per ISO 22241).
   
   ## VDA certification
   - Certification: VDA register #2024-05-001
   - Compliance: ISO 22241 AUS 32
   
   ## PDS citations
   - https://www.wsoil.com/.../wsoil-adblue-malaysia (PDS 2024-06-20)
   ```

---

### Scenario B: Fix a stale AdBlue PDS URL or storage warning

**Example:** "AdBlue storage temperature range in SKILL.md is outdated; PDS now specifies 0–+30 °C (not -11 to +30 °C)."

**Steps:**

1. **Fetch the latest PDS and verify storage temp range.**

2. **Edit SKILL.md §6 (Storage & Warnings):**
   ```markdown
   # Before:
   Storage temp: -11 °C to +30 °C (sealed)
   
   # After:
   Storage temp: 0 °C to +30 °C (sealed) — freezing below 0 °C can crystallize urea
   ```

3. **Update PDS citation with new URL + date.**

4. **No test needed for storage-only changes.**

5. **Open a PR.**

---

### Scenario C: Add a new DEF regional certification standard

**Example:** "China adopted GB 29914 (Chinese DEF standard); I want to add this."

**Steps:**

1. **Research the standard:**
   - GB 29914 (China DEF equivalent)
   - ISO 22241 (international standard)
   - Both define 32.5% urea solution, but with regional testing protocols

2. **Edit SKILL.md §3 (Intake) — add certification awareness:**
   ```markdown
   ### 3b. Certification standards (new field, best-effort)
   - ISO 22241 (international; most common)
   - GB 29914 (China)
   - National variants exist; ask customer if known
   ```

3. **Edit SKILL.md §2 (Product Categories) — add reference:**
   ```markdown
   All AdBlue/DEF products in this skill comply with:
   - ISO 22241 AUS 32 (primary, international)
   - GB 29914 (China equivalent)
   - Regional certifications (VDA, ACEA)
   ```

4. **Update CONTRIBUTORS.md:**
   ```markdown
   - **2026-07-21 — GB 29914 (China) DEF standard:** Added certification awareness for Chinese market.
     Note: Chinese-market DEF products often dual-certified (ISO 22241 + GB 29914).
     Author: [Your Name]
   ```

5. **Smoke test:**
   ```bash
   # Test existing (ISO 22241) recommendations still work
   python scripts/render_pdf.py \
     --incumbent="ARLA 32" \
     --application="adblue" \
     --region="Europe" \
     --oem="Volvo FH" \
     --output=/tmp/test-iso22241.pdf
   
   # Test Chinese DEF (if suppliers available)
   python scripts/render_pdf.py \
     --incumbent="Sinopec DEF" \
     --application="adblue" \
     --region="China" \
     --oem="Sinotruk" \
     --output=/tmp/test-gb29914.pdf
   ```

6. **Open a PR with methodology change label.**

---

## Test flow

### Test 1: PDF render

```bash
cd adblue-def-recommender

python scripts/render_pdf.py \
  --incumbent="ARLA 32" \
  --application="adblue" \
  --region="Europe" \
  --oem="MAN TGX" \
  --target-suppliers="ARLA,Cummins,Shell" \
  --output=/tmp/test-def.pdf

# Expected:
# - PDF renders (valid)
# - Standard + Upgraded recommendations
# - All PDS citations are URLs
# - Storage warnings highlighted (temp range, sealed container)
# - VDA certification called out
```

### Test 2: Excel append

```bash
python scripts/append_record.py \
  --record=templates/recommendation_record.xlsx \
  --incumbent="ARLA 32" \
  --standard-pick="ARLA 32 (standard)" \
  --upgraded-pick="Cummins DEF Blue Diesel Exhaust Fluid" \
  --rationale="ISO 22241 AUS 32 compliant; VDA certified" \
  --dle-notes="Euro 5 MAN TGX, European fleet"

# Expected: Row appended, no corruption
```

### Test 3: Verify no hard-rule violations

- [ ] Did I cite VDA certification for every AdBlue product? (hard rule #1)
- [ ] Did I recommend a non-VDA product? (hard rule #2, violation — must use only VDA-certified)
- [ ] Did I flag storage warnings (temperature, sealed container)? (hard rule #3)
- [ ] Did I ask for OEM/model and SCR system type? (hard rule #4)
- [ ] Did I produce all three deliverables? (hard rule #5)
- [ ] Did I append the standard disclaimer? (hard rule #6)

---

## File reference guide

| File | Purpose | Edit if… |
|---|---|---|
| `SKILL.md` | Methodology + hard rules | Changing certification rules, storage warnings, regional standards |
| `references/supplier_catalogs.md` | AdBlue/DEF suppliers by region + certification | Adding new regional suppliers or VDA-certified products |
| `references/sop-flow.md` | SOP diagrams (certification check, storage flow) | Updating flowcharts for new certifications (GB 29914, etc.) |
| `templates/report_template.md` | Chat report format | Changing output structure or warning format |
| `scripts/render_pdf.py` | PDF rendering | Fixing rendering bugs |
| `CONTRIBUTORS.md` | Authorship lineage | Methodology change |

---

## Questions?

### AdBlue/DEF-specific questions
- **What's the difference between AdBlue and DEF?**
  - **AdBlue:** Trademark (mostly Europe)
  - **DEF (Diesel Exhaust Fluid):** Generic term (mostly North America, Australia)
  - Both are ISO 22241 AUS 32 (32.5% urea solution); functionally identical
  - See SKILL.md §0 for details.

- **Why is VDA certification mandatory?**
  - Urea concentration, water quality, and contaminants must be within ISO 22241 specs. Incorrect urea concentration can damage SCR catalysts (very expensive). VDA certification ensures compliance. Hard rule #2: Never recommend non-VDA product.

- **Can I use expired AdBlue?**
  - **No.** Storage at wrong temperature (outside 0 to +30 °C) can crystallize urea. Degraded product damages SCR systems. SKILL.md §6 (storage warnings) applies unconditionally.

- **What's an SCR system?**
  - **SCR (Selective Catalytic Reduction):** Emission control system. AdBlue is injected into exhaust stream where it reacts with NOx pollutants. Requires ISO 22241 AUS 32 (32.5% urea). Wrong product = system failure.

### PDS & certification questions
- **How do I verify VDA certification?**
  - Check: https://www.vda.de (Verband der Automobilindustrie register)
  - All legitimate AdBlue/DEF suppliers are listed with cert date + serial

- **Stale PDS or storage warning?**
  - Open an Issue with `[stale-pds]` + product name + old/new spec.

---

## Critical: ISO 22241 AUS 32 Only

This skill recommends **only ISO 22241 AUS 32 compliant, VDA-certified products.** Non-compliant or counterfeit AdBlue/DEF damages SCR systems and voids warranties. Every recommendation must cite VDA certification.

---

## Thank you

Every new regional supplier, every storage warning clarification, every certification update makes the suite more reliable for SCR fleet operators worldwide.

— Aung Khaing Htun, CLS, Licensor
