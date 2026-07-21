WEcoS Product Recommendar
Copyright © 2026 Aung Khaing Htun, CLS. All rights reserved.
Licensed under PolyForm Noncommercial License 1.0.0.

# Contributing to coolant-recommender

This skill recommends equivalent or alternative engine coolants and antifreeze (light-duty, heavy-duty diesel, off-highway, marine, stationary gen-set, OEM concentrates) for an incumbent third-party product.

## Before you start

- [ ] Read the parent repo's [CONTRIBUTING.md](../CONTRIBUTING.md) (5 min) — covers DCO sign-off, PR process, license agreement
- [ ] Read this skill's [SKILL.md](./SKILL.md) §0 (hard rules) and §3 (intake fields for coolants) (10 min)

## Quick onboarding

### What should I edit?

| If you want to… | Edit this file | Why |
|---|---|---|
| Add a new coolant OEM concentrate or regional variant | `references/supplier_catalogs.md` | Keeps product database separate from methodology |
| Fix a stale coolant PDS URL (HTTP 404/410) | `SKILL.md` (the line with the old URL) | Minimal change; no test needed |
| Change coolant classification logic (e.g., add IAT vs OAT filter) | `SKILL.md` §3–§4 + `CONTRIBUTORS.md` | Methodology is in SKILL.md |
| Change report format for coolant recommendations | `templates/report_template.md` | Templates are separate from logic |
| Fix PDF/Excel rendering bugs | `scripts/render_pdf.py` or `scripts/append_record.py` | Scripts are utilities; test before PR |
| Add OEM approval mapping (e.g., new Volvo VCS variant) | `references/sop-flow.md` + `SKILL.md` | Major change; needs review + documentation |

**Decision tree:** Not sure? Start with `references/supplier_catalogs.md` (safest; lowest test burden).

---

## Common contribution scenarios

### Scenario A: Add a new coolant concentrate variant

**Example:** "I found Shell Duratherm EC concentrate (not pre-mixed) with updated Volvo VCS approval."

**Steps:**

1. **Fetch the PDS from Shell's official site:**
   ```
   https://www.shell.com/en-au/.../shell-duratherm-ec-concentrate
   ```

2. **Extract the four key attributes for coolants:**
   - Product type (concentrate, ready-mixed, hybrid)
   - Color & chemistry (IAT / HOAT / OAT — critical for mixing compatibility)
   - Freeze/boil protection (typically -35 to +110 °C)
   - OEM approvals (Volvo VCS, MB 325.0, Cummins, John Deere, etc.)

3. **Add to `references/supplier_catalogs.md` under the Shell section:**
   ```markdown
   #### Duratherm Concentrate Series (OAT)
   
   - **Shell Duratherm EC Concentrate**
     - Type: Concentrate (mix 1:1 with distilled water)
     - Chemistry: OAT (Organic Acid Technology)
     - Color: Yellow
     - Freeze protection: -35 °C (when mixed 1:1)
     - OEM approvals: Volvo VCS, MB 325.0, DAF
     - Service life: 5 years / 250,000 km
     - Mixing caveat: Never mix with IAT or HOAT coolants (incompatible inhibitor packages)
     - PDS: https://www.shell.com/.../shell-duratherm-ec-concentrate (dated 2024-07-15)
   ```

4. **Test the reference (smoke test):**
   ```bash
   python scripts/render_pdf.py \
     --incumbent="Shell Duratherm FC" \
     --application="coolant" \
     --oem="Volvo D9" \
     --target-supplier="Shell" \
     --output=/tmp/test-duratherm-concentrate.pdf
   
   # Manually verify: Does your new concentrate appear in recommendations?
   # Does the mixing caveat appear in the output?
   ```

5. **Open a PR:**
   ```
   Title: [coolant-recommender] add Shell Duratherm EC concentrate (OAT, Volvo VCS)
   
   Body:
   ## What does this PR change?
   Adds Shell Duratherm EC concentrate to the coolant product database.
   
   ## Why?
   Customer request; OAT concentrate variant with Volvo VCS approval for tropical regions.
   
   ## PDS citations
   - https://www.shell.com/.../shell-duratherm-ec-concentrate (PDS 2024-07-15)
   
   ## Checklist
   - [x] Skill name(s) updated (coolant-recommender)
   - [x] CONTRIBUTORS.md updated (no methodology change)
   - [x] Mixing caveat documented (OAT + never mix with IAT/HOAT)
   - [x] No hardcoded PDS (fetched this session)
   ```

---

### Scenario B: Fix a stale coolant approval PDS URL

**Example:** "Volvo VCS approval PDS link is outdated (2020 revision; 2025 revision exists)."

**Steps:**

1. **Find the new PDS on Volvo's site:**
   - Old: `https://volvo.com/.../vcs-2020` (outdated)
   - New: `https://volvo.com/.../vcs-2025` (current)

2. **Edit SKILL.md:**
   ```markdown
   # Before:
   Volvo VCS (2020) — volvo.com/.../vcs-2020
   
   # After:
   Volvo VCS (2025) — volvo.com/.../vcs-2025
   ```

3. **No test needed.** Just verify HTTP 200 in browser.

4. **Open a PR:**
   ```
   Title: [coolant-recommender] update Volvo VCS approval link (2020→2025)
   
   Body:
   ## What does this PR change?
   Updates stale Volvo VCS PDS to 2025 revision.
   
   ## PDS citations
   - https://volvo.com/.../vcs-2025 (PDS 2025-01-10, new)
   ```

---

### Scenario C: Add a new OAT vs HOAT filter branch

**Example:** "Customers are asking for HOAT (Hybrid OAT) coolants; I want to add this chemistry type to the filter."

**Steps:**

1. **Read §3–§4 (Intake & Filter) in SKILL.md carefully.**
   - Understand the chemistry classification (IAT, HOAT, OAT)
   - HOAT is a subtype of OAT, so you'll need to modify the filter logic

2. **Edit SKILL.md §3 (Intake) — add new field:**
   ```markdown
   ### 3c. Coolant chemistry preference (new)
   - If customer has strong chemistry preference (IAT, HOAT, OAT), ask in intake
   - Affects filter §4.2 (base chemistry type)
   ```

3. **Edit SKILL.md §4 (Filter) — axis 4.2:**
   ```markdown
   # Before (axis 4.2 — base chemistry):
   - IAT (Inorganic Acid Technology), OAT (Organic Acid Technology)
   
   # After (axis 4.2 — base chemistry):
   - IAT (Inorganic Acid Technology), HOAT (Hybrid OAT), OAT (Organic Acid Technology)
   ```

4. **Update CONTRIBUTORS.md:**
   ```markdown
   - **2026-07-21 — HOAT (Hybrid OAT) chemistry filter:** Added axis 4.2 branch for HOAT coolants.
     Rationale: HOAT provides OAT protection with faster cooling than pure OAT; popular in EU/UK markets.
     Author: [Your Name] (contribution accepted via PR #XYZ)
   ```

5. **Smoke test:**
   ```bash
   # Test existing IAT/OAT incumbents still work
   python scripts/render_pdf.py \
     --incumbent="Shell Duratherm FC" \
     --application="coolant" \
     --oem="Volvo D9" \
     --output=/tmp/test-oat-existing.pdf
   
   # Test new HOAT filter works
   python scripts/render_pdf.py \
     --incumbent="Zerex G-05" \
     --application="coolant" \
     --oem="VW/Audi" \
     --output=/tmp/test-hoat-new.pdf
   ```

6. **Open a PR with methodology change label.**

---

## Test flow

**Before opening any PR, run these three tests:**

### Test 1: PDF render (smoke test)

```bash
cd coolant-recommender

python scripts/render_pdf.py \
  --incumbent="Shell Duratherm FC" \
  --application="coolant" \
  --oem="Volvo D9" \
  --target-suppliers="Shell,Mobil" \
  --output=/tmp/test-coolant.pdf

# Expected:
# - PDF renders (valid, not corrupted)
# - Chat report shows Standard + Upgraded recommendations
# - All PDS citations are URLs (no "N/A")
# - Mixing caveats displayed (if OAT + HOAT or IAT + OAT mixes flagged)
```

### Test 2: Excel append

```bash
python scripts/append_record.py \
  --record=templates/recommendation_record.xlsx \
  --incumbent="Shell Duratherm FC" \
  --standard-pick="Shell Duratherm EC" \
  --upgraded-pick="Mobil Coolant Concentrate ES" \
  --rationale="OAT chemistry; marine-grade inhibitor for salt-spray environment" \
  --dle-notes="Auxiliary engine cooling, tropical region, seawater exposure"

# Expected: New row appended; no corruption
```

### Test 3: Verify no hard-rule violations

- [ ] Did I cite a PDS for every coolant spec? (hard rule #1)
- [ ] Did I recommend without fetching the PDS? (hard rule #2)
- [ ] Did I flag mixing warnings (IAT/OAT/HOAT incompatibility)? (hard rule #3, critical for coolants)
- [ ] Did I ask for OEM/Model and operating conditions? (hard rule #4)
- [ ] Did I produce all three deliverables? (hard rule #5)
- [ ] Did I append the standard disclaimer? (hard rule #6)

---

## File reference guide

| File | Purpose | Edit if… |
|---|---|---|
| `SKILL.md` | Methodology + hard rules (§0–§13) | Adding/changing chemistry filter, OEM approval logic |
| `references/supplier_catalogs.md` | Product database (by supplier + type) | Adding new coolant concentrates or variants |
| `references/sop-flow.md` | SOP diagrams (OAT vs IAT vs HOAT decision tree) | Updating flowcharts for new chemistry branches |
| `templates/report_template.md` | Chat report format | Changing output structure or warning format |
| `scripts/render_pdf.py` | PDF rendering | Fixing rendering bugs or new PDF sections |
| `CONTRIBUTORS.md` | Authorship lineage | Methodology change or major correction |

---

## Questions?

### Coolant-specific questions
- **What's the difference between IAT, HOAT, and OAT?**
  - **IAT:** Inorganic Acid Technology (older, silicate-based, ~2 year life)
  - **HOAT:** Hybrid OAT (organic acids + silicates, ~5 year life, faster cooling than OAT)
  - **OAT:** Organic Acid Technology (modern, ~5 year life, slower cooling but extended protection)
  - Read SKILL.md §3 for compatibility rules.

- **Can I mix IAT and OAT coolants?**
  - **No.** Different inhibitor packages; mixing causes corrosion and silicate precipitation. SKILL.md hard rule #3 (compatibility warnings) applies unconditionally.

- **Why does the shell/OEM approval matter?**
  - Different engines have different coolant requirements (Volvo VCS, MB 325.0, etc.). Mixing the wrong coolant voids warranty and can cause overheating. SKILL.md §5 (OEM cross-check) explains.

### Script & PDS questions
- **Rendering fails; what do I check?**
  - Is the PDF file locked? Is the incumbent PDS malformed? Open an Issue with `[coolant-recommender-script-bug]`.

- **I found a 404 PDS link.**
  - Open an Issue with `[stale-pds]` + old URL + new URL (if you found one).

---

## Thank you

Every new coolant concentrate, every stale-link fix, every chemistry filter improvement makes the suite more accurate. Your contribution matters.

— Aung Khaing Htun, CLS, Licensor
