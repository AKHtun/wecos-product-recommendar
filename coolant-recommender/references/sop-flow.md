# T-SOP-002-2 — Equivalent / Alternative Coolant Selection (DLE side)

Source: Technical_Product Recommendation Process.xlsx, sheet T-SOP-002-2, drawing4.

## Flow

1. Receive product recommendation request and information for coolant.
2. Check 3rd-party coolant product data sheet and capture:
   - **2.1 Usage / application** — Engine (light-duty automotive, heavy-duty diesel, off-highway, marine, gen-set) or Other (industrial heat-transfer).
   - **2.2 Coolant technology** — OAT (G30 / G40 / G48), Si-OAT (G64), HOAT (HOAT with nitrite, borates, silicates = G05), PSI-OAT, IAT (less common).
3. Compare with the supplier product data sheets:
   - 3.1 Filter by 2.1 finding (application).
   - 3.2 Filter by 2.2 finding (technology).
4. Equivalent / alternative product can be selected based on 3rd-party product?
   - Yes → step 9.
   - No → step 5.
5. Consult OEM Manual based on OEM / Maker / Model.
6. Does OEM Manual recommend any supplier-catalog product?
   - Yes → step 7.
   - No → step 10.
7. Open the OEM-recommended product data sheets and re-run steps 2 and 3.
8. Can an alternative be selected based on OEM-recommended products?
   - Yes → step 9.
   - No → step 10.
9. Recommend the product as equivalent or alternative.
10. Inform DSR no product can be recommended.
11. Process end.

## Special-case rules (drawing4)

- "Always remind DSR to drain the previous coolant and not to mix with incumbent coolant." This is mandatory on EVERY recommendation, not conditional. The drain/no-mix language is reproduced in §6 of SKILL.md.
- HOAT with nitrite, borates, and silicates is the G05 family.
- "Not common products" tag applies to IAT today — flag it if encountered.
