WEcoS Product Recommendar
Copyright © 2026 Aung Khaing Htun, CLS. All rights reserved.
Licensed under PolyForm Noncommercial License 1.0.0.

# Contributing to grease-recommender

This skill recommends equivalent or alternative greases (industrial, automotive, food-grade NSF H1, marine, mining / heavy-load, electric-motor, refrigeration-compressor, central-lube, railway axlebox, high-temperature) for an incumbent third-party product.

**Note:** This is the most complex skill. Grease recommendations require chemistry-grounded logic: thickener type, base oil, NLGI grade, and OEM approval all interact. Read §0–§13 carefully before contributing.

## Before you start

- [ ] Read the parent repo's [CONTRIBUTING.md](../CONTRIBUTING.md) (5 min)
- [ ] Read this skill's [SKILL.md](./SKILL.md) §0–§2 (hard rules + intake fields) (15 min)
- [ ] Skim the DIN 51502 / ISO 6743-9 designation decoder in §3 (5 min)
- [ ] Read the ExxonMobil 7×7 thickener compatibility matrix in §4 (understand C/M/I columns)

## Quick onboarding

### What should I edit?

| If you want to… | Edit this file | Why |
|---|---|---|
| Add a new grease product (thickener + base oil combination) | `references/supplier_catalogs.md` | Keeps product database separate |
| Fix a stale grease PDS URL | `SKILL.md` (the line with the old URL) | Minimal change; no test needed |
| Add a new grease application (e.g., wind-turbine bearings) | `SKILL.md` §2–§4 + `references/` | Requires filter logic update + test incumbent |
| Add a new thickener compatibility rule (e.g., polyurea + lithium mix warning) | `SKILL.md` §6 + `CONTRIBUTORS.md` | Methodology change; high priority |
| Change NLGI preference logic (e.g., when to recommend NLGI 3 vs 2) | `SKILL.md` §5–§6 + `CONTRIBUTORS.md` | Methodology change |
| Fix PDF/Excel rendering bugs | `scripts/render_pdf.py` or `scripts/append_record.py` | Test before PR |

**Decision tree:** Not sure? Start with `references/supplier_catalogs.md`.

---

## Common contribution scenarios

### Scenario A: Add a new grease product to the database

**Example:** "I found SKF LGEP 2 (lithium complex, mineral, NLGI 2) with new NSF H1 approval."

**Steps:**

1. **Fetch the product PDS:**
   - Source: SKF's official site
   - Extract: thickener type, base oil, NLGI, DIN code, OEM approvals, NSF cert

2. **Add to `references/supplier_catalogs.md` under SKF section:**
   ```markdown
   #### SKF General Purpose (Lithium Complex)
   
   - **SKF LGEP 2**
     - Thickener: Lithium complex
     - Base oil: Mineral ISO VG 100
     - NLGI: 2
     - DIN code: KP 2 K -20
     - Drop point: 180 °C
     - Approvals: NSF H1 (food-grade), ISO 12922
     - Compatibility (ExxonMobil 7×7 matrix): C row (lithium complex)
     - Applications: General-purpose, industrial, automotive
     - Shelf life: 3 years (store in cool, dry place)
     - PDS: https://www.skf.com/.../lgep-2 (dated 2024-08-10)
   ```

3. **Smoke test (critical for grease):**
   ```bash
   python scripts/render_pdf.py \
     --incumbent="Shell Gadus S3 V60D2 2" \
     --application="grease" \
     --oem="rolling-bearing" \
     --target-supplier="SKF" \
     --output=/tmp/test-skf-lgep2.pdf
   
   # Manually verify:
   # - DIN code correct? (KP vs K vs K2 — matters for compatibility)
   # - Thickener compatibility checked? (does matrix show no conflicts?)
   # - Recommendations grounded in PDS specs (drop point, NLGI, approval)?
   ```

4. **Open a PR:**
   ```
   Title: [grease-recommender] add SKF LGEP 2 (Li complex, NSF H1, NLGI 2)
   
   Body:
   ## What does this PR change?
   Adds SKF LGEP 2 to general-purpose grease catalog (food-grade NSF H1 approved).
   
   ## Why?
   Customer request; NSF H1 certification expands food-processing equipment recommendations.
   
   ## Chemistry
   - Thickener: Lithium complex (ExxonMobil matrix: C row)
   - Base oil: Mineral ISO VG 100
   - NLGI: 2
   - DIN code: KP 2 K -20
   
   ## PDS citations
   - https://www.skf.com/.../lgep-2 (PDS 2024-08-10)
   
   ## Checklist
   - [x] DIN code verified (matches ExxonMobil matrix row)
   - [x] Thickener compatibility checked (no conflicts in 7×7 matrix)
   - [x] Drop point & NLGI extracted from official PDS
   - [x] Smoke test passed (recommendations grounded in specs)
   ```

---

### Scenario B: Fix a stale grease PDS URL

**Example:** "Shell Gadus PDS link is 404; new revision exists."

**Steps:**

1. **Find the new PDS.**
2. **Edit SKILL.md with new URL + date.**
3. **No test needed.**
4. **Open a PR.**

---

### Scenario C: Add a new grease application (e.g., wind-turbine bearings)

**Example:** "I want to add wind-turbine main-bearing greases (large, slow-rotating, high-load)."

**Steps:**

1. **Read §2 (Application Categories) in SKILL.md carefully.**
   - Current: industrial, automotive, NSF H1, marine, mining/heavy-load, electric-motor, refrigeration-compressor, central-lube, railway axlebox, high-temperature
   - Wind-turbine falls into "heavy-load, high-temperature"; existing category might suffice

2. **If truly new, create a test incumbent:**
   - Create `references/test-incumbent-wind-turbine.md`:
   ```markdown
   # Test incumbent: Mobil Grease XMP 320 (wind turbine)
   
   ## Input
   - Incumbent: Mobil Grease XMP 320
   - Application: Wind-turbine main bearing (large, slow, high-load)
   - OEM: Vestas V164
   - Operating conditions: -20 to +60 °C, RPM 5–15, load extreme
   
   ## Expected standard recommendation
   - Mobil Grease XMP 320 (incumbent, high-quality polyurea)
   
   ## Expected upgraded recommendation
   - Kluber Barrierta L 55 (polyurea, synthetic base oil, extended repack interval)
   
   ## Key decision rationale
   - Polyurea thickener: high-speed instability not an issue (slow RPM); excellent mechanical stability under high load
   - Synthetic base oil: temperature range, oxidation stability in service
   - Repack interval: XMP 320 ~2 years; Barrierta L 55 ~3 years (OEM-dependent)
   ```

3. **Edit SKILL.md §2 (add if truly new category):**
   ```markdown
   - **Wind-turbine main bearing** (polyurea preferred; high-load, slow-rotating, extended repack)
   ```

4. **Edit SKILL.md §4 (filter logic) for wind-turbine branch:**
   ```markdown
   ### 4.8 Wind-turbine main bearing filter
   - Application: Slow-rotating (RPM 5–15), large bearing, high constant load
   - Thickener: Polyurea preferred (mechanical strength, temperature range)
   - NLGI: 0 or 1 (soft for easy repacking in large bearings)
   - Base oil: Synthetic (ISO VG 220–320)
   - OEM approvals: Vestas, GE, Siemens-Gamesa, Enercon
   ```

5. **Update CONTRIBUTORS.md:**
   ```markdown
   - **2026-07-21 — wind-turbine main-bearing filter:** Added application category + filter branch (§4.8).
     Note: Polyurea dominant; repack intervals 2-3 years depending on load monitoring.
     Author: [Your Name]
   ```

6. **Smoke test (critical):**
   ```bash
   # Test existing applications unaffected
   python scripts/render_pdf.py \
     --incumbent="Shell Gadus S3 V60D2 2" \
     --application="grease" \
     --subtype="industrial" \
     --oem="SKF" \
     --output=/tmp/test-industrial.pdf
   
   # Test new wind-turbine filter
   python scripts/render_pdf.py \
     --incumbent="Mobil Grease XMP 320" \
     --application="grease" \
     --subtype="wind-turbine" \
     --oem="Vestas" \
     --output=/tmp/test-vestas.pdf
   
   # Manually verify: Recommendations make sense for slow-rotating, high-load profile?
   ```

7. **Open a PR with methodology change label.**

---

### Scenario D: Add a thickener incompatibility warning

**Example:** "Customers sometimes mix lithium and polyurea greases (dangerous). I want to add an explicit warning."

**Steps:**

1. **Read §6 (Warning Matrix) in SKILL.md.**
   - Current warnings: over-greasing, purge-out-old-grease, base-oil vs NLGI confusion, vertical-mount NLGI 3, water exposure, shelf-life
   - Thickener compatibility is implicit in ExxonMobil 7×7 matrix but not explicit warning

2. **Add to SKILL.md §6 (new warning order):**
   ```markdown
   ### 6.0 Warning matrix (in priority order)
   1. Over-greasing (bearing seizure risk)
   2. Purge-out-old-grease (thickener mismatch risk)
   3. **Thickener incompatibility** (NEW: never mix Li + Polyurea without purging)
   4. Base-oil vs NLGI confusion
   5. Vertical-mount NLGI 3 (gravity slumping)
   6. Water exposure (corrosion)
   7. Shelf-life advisory
   ```

3. **Add specific warning text:**
   ```markdown
   ### 6.3 Thickener incompatibility (never mix without purging)
   
   Some thickener types are **NOT compatible** when mixed in-service:
   - Lithium (Li) + Polyurea = Incompatible (can form gels, clog grease paths)
   - Lithium complex (Li-complex) + Clay = Incompatible
   - Recommended action: If switching thickener type, **purge bearing completely** (grease till new type exits drain plug) before adding new product
   
   See ExxonMobil 7×7 compatibility matrix (§4) for full thickener pair compatibility.
   ```

4. **Update CONTRIBUTORS.md:**
   ```markdown
   - **2026-07-21 — thickener incompatibility warning:** Added priority warning (§6.3) for incompatible thickener pairs (Li + Polyurea, etc.).
     Ref: ExxonMobil 7×7 matrix + field experience.
     Author: [Your Name]
   ```

5. **No test needed for warning-only changes (non-methodology).**

6. **Open a PR.**

---

## Test flow (Critical for Grease)

Grease is the highest-friction recommendation category. Every test is **mandatory**.

### Test 1: PDF render (smoke test)

```bash
cd grease-recommender

python scripts/render_pdf.py \
  --incumbent="Shell Gadus S3 V60D2 2" \
  --application="grease" \
  --subtype="industrial-bearing" \
  --oem="SKF" \
  --rpm="500" \
  --shaft-diameter="50mm" \
  --bearing-type="deep-groove-ball" \
  --target-suppliers="Shell,Mobil,Kluber" \
  --output=/tmp/test-grease.pdf

# Expected:
# - PDF renders (valid)
# - Standard + Upgraded recommendations
# - DIN codes displayed (KP 2 K -20 vs K 2 P -20 X) ← CRITICAL
# - Thickener compatibility checked (no mixing warnings for same pair)
# - NLGI preference explained (why 2 vs 3, if applicable)
# - Over-greasing warning highlighted
# - Purge-procedure standard phrase included
# - Drop point & shelf-life cited from PDS
```

### Test 2: Excel append

```bash
python scripts/append_record.py \
  --record=templates/recommendation_record.xlsx \
  --incumbent="Shell Gadus S3 V60D2 2" \
  --standard-pick="Mobil Polyrex EM" \
  --upgraded-pick="Kluber Temprogid" \
  --rationale="Polyurea thickener, drop point 260→270 °C, salt-air resistant" \
  --dle-notes="Maritime bearing, vertical-mount (NLGI 3 preferred)"

# Expected: Row appended, columns populated, no corruption
```

### Test 3: Hard-rule verification (manual)

- [ ] Did I cite every grease spec from a PDS? (hard rule #1)
- [ ] Did I recommend without fetching the PDS? (hard rule #2)
- [ ] Did I flag thickener compatibility warnings (Li + Polyurea, etc.)? (hard rule #3, critical for grease)
- [ ] Did I ask for application, OEM, RPM, bearing type? (hard rule #4)
- [ ] Did I produce all three deliverables? (hard rule #5)
- [ ] Did I append the standard disclaimer? (hard rule #6)
- [ ] Did I include DIN 51502 code (e.g., KP 2 K -20)? (grease-specific §3)
- [ ] Did I consult ExxonMobil 7×7 matrix for compatibility? (grease-specific §4)
- [ ] Did I include purge procedure standard phrase? (grease-specific §6)

---

## File reference guide

| File | Purpose | Edit if… |
|---|---|---|
| `SKILL.md` | Methodology + 13 hard rules + thickener matrix | Changing application filter, thickener compatibility, warning priority |
| `references/supplier_catalogs.md` | Grease products by supplier + thickener type | Adding new greases (product name, thickener, NLGI, DIN code) |
| `references/sop-flow.md` | SOP diagrams (DIN decoder, thickener decision tree) | Updating flowcharts or adding new application branch |
| `templates/report_template.md` | Chat report format (standard + upgraded + warnings) | Changing output structure |
| `scripts/render_pdf.py` | PDF rendering (includes DIN code decoder output) | Fixing rendering bugs |
| `CONTRIBUTORS.md` | Authorship lineage | Methodology change or major thickener compatibility update |

---

## Questions?

### Grease-specific (critical) questions
- **What's the difference between Li, Li-complex, and polyurea?**
  - **Li (Lithium):** Simple lithium soap; ~2 year shelf-life; low cost; 180 °C drop point
  - **Li-complex:** Lithium + complexing agent; better mechanical stability; ~5 year life; 200–220 °C drop point
  - **Polyurea:** Synthetic thickener; temperature-stable (-30 to +270 °C); salt-water resistant; ~5 year life; premium cost
  - See SKILL.md §3 (DIN decoder) + ExxonMobil 7×7 matrix (§4) for full details.

- **Why does DIN code matter?**
  - DIN 51502 / ISO 6743-9 designation (e.g., KP 2 K -20) encodes thickener type, NLGI, base oil, and approvals. "KP 2 K" = Lithium complex, NLGI 2. "K 3 P" = Polyurea, NLGI 3. Misreading the code = wrong thickener selection.

- **Can I mix two greases?**
  - **Only if compatible thickeners.** Check ExxonMobil 7×7 matrix (§4):
    - Polyurea + Polyurea = ✅ OK
    - Li + Li-complex = ⚠️ Caution (purge recommended)
    - Li + Polyurea = ❌ Never (incompatible; gels form)
  - When in doubt, purge completely before adding new grease.

- **What's "over-greasing"?**
  - Applying too much grease → bearing overheats, seals fail, contaminant ingress. Standard purge procedure: "till new grease exits drain plug" (not "add amount X").

- **NLGI 3 vertical-mount preference — why?**
  - Vertical bearings have gravity slumping (grease slides down). NLGI 3 (stiffer) prevents slumping, maintains bearing film longer. NLGI 2 acceptable but higher repack frequency. Hard rule #12.

### Chemistry & compatibility questions
- **Polyurea vs synthetic base oil — are they the same?**
  - **No.** Polyurea is the thickener type. Synthetic base oil (PAO, ester, etc.) is separate. A polyurea grease can have mineral or synthetic base oil. Polyurea thickener + synthetic base oil = premium grade.

- **Shelf-life varies — why?**
  - Depends on thickener chemistry, base oil antioxidant, storage temp/humidity, container seal, and additive package. Never hardcode "3 years" — always cite PDS shelf-life (hard rule #9).

### PDS & testing questions
- **Stale grease PDS URL?**
  - Open an Issue with `[stale-pds]` + product + old/new URL.

- **My smoke test failed (PDF rendering or recommendation mismatch).**
  - Open an Issue with `[grease-recommender-script-bug]` + test incumbent + error message.

---

## Critical: Thickener Compatibility

Grease is the highest-friction recommendation category. Thickener compatibility errors directly damage equipment (bearing seizure, seal failure). Before every PR:

1. **Verify DIN codes match ExxonMobil 7×7 matrix.** 
2. **Check compatibility pairs.** (Polyurea + Lithium = ❌ Never)
3. **Include purge procedure.** (Till new grease exits drain plug)
4. **Cite PDS drop point, shelf-life, OEM approval.**

---

## Thank you

Every new grease product, every thickener compatibility clarification, every warning improvement makes the suite more reliable for fleet maintenance teams worldwide.

— Aung Khaing Htun, CLS, Licensor
