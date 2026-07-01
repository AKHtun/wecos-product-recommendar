# T-SOP-002-3 — Equivalent / Alternative Diesel Fuel Selection (DLE side)

Source: Technical_Product Recommendation Process.xlsx, sheet T-SOP-002-3.

## Flow

1. Receive product recommendation request and information for diesel fuel.
2. Check 3rd-party diesel product data sheet / refinery COA and capture:
   - **2.1 Usage / application** — Inland (on-road automotive, off-road / mining / construction, rail, stationary gen-set) or Marine (vessel category, ECA / non-ECA route).
   - **2.2 Sulfur content + additive technology** — Sulfur tier (ULSD ≤ 10 ppm / 50 ppm / LSD 500 ppm / Marine 0.1 % ECA / Marine 0.5 % VLSFO) AND whether the fuel is Normal Diesel (ADO) or Additized Premium Diesel (e.g., SFSD, EDE, Techron D, V-Power, Excellium, Dynamic Diesel).
3. Compare with the supplier product data sheets:
   - 3.1 Filter by 2.1 finding (application).
   - 3.2 Filter by 2.2 finding (sulfur tier + additive technology).
4. Equivalent / alternative product can be selected based on 3rd-party product?
   - Yes → step 9.
   - No → step 5.
5. Consult OEM Manual based on OEM / Maker / Model and local regulator fuel spec.
6. Does OEM Manual / regulator allow any supplier-catalog product?
   - Yes → step 7.
   - No → step 10.
7. Open the OEM-recommended product data sheets and re-run steps 2 and 3.
8. Can an alternative be selected based on OEM-recommended products?
   - Yes → step 9.
   - No → step 10.
9. Recommend the product as equivalent or alternative.
10. Inform DSR no product can be recommended.
11. Process end.

## Special-case rules (T-SOP-002-3 notes)

- **Tank changeover** is always reminded — detergent-additized premium can
  dislodge tank-bottom deposits and overload the fuel filter on first fill.
- **DPF / SCR equipped** engines require ULSD ≤ 10 ppm — higher sulfur poisons
  the catalyst.
- **Cold-flow climate** — verify CFPP / cloud point against the customer's
  coldest expected ambient; recommend winter-grade or kerosene blend if needed.
- **FAME (bio) ceiling** — engine OEMs publish maximum B-grade (B0 / B5 / B7
  / B10 / B20); exceeding voids warranty.
- **Marine ECA** — IMO 2020 cap is 0.5 % m/m global, 0.1 % m/m inside ECA
  (North America, US Caribbean, North Sea, Baltic Sea, Mediterranean from
  2025); scrubber-equipped vessels can use higher-sulfur fuel.

## Grade decoder

| Tag | Full name | Sulfur | Typical use |
|---|---|---|---|
| **ULSD** | Ultra-Low Sulfur Diesel | ≤ 10 ppm | EU EN 590, US ASTM D975 S15, JIS K 2204 #2, SS EN 590 |
| **LSD** | Low Sulfur Diesel | 50–500 ppm | Legacy markets only |
| **HSD** | High Sulfur Diesel | > 500 ppm | Off-grid mining only; not permitted in most regulated markets |
| **B7** | Up to 7 % FAME | as host | EN 590 default mandate in EU |
| **B20** | Up to 20 % FAME | as host | US fleets, some Asian markets |
| **DMA / DMZ** | Marine distillate ISO 8217 | ≤ 0.1 % (ECA) / ≤ 0.5 % | Marine MGO |
| **DMB** | Marine distillate (slightly heavier) | ≤ 0.5 % | Marine MDO |
| **VLSFO** | Very-Low Sulfur Fuel Oil | ≤ 0.5 % | IMO 2020 compliant residual blend |
| **ULSFO** | Ultra-Low Sulfur Fuel Oil | ≤ 0.1 % | ECA-compliant residual blend |
| **Additized Premium** | ULSD + detergent/cetane/lubricity package | matches host | Shell V-Power, BP Ultimate, Total Excellium, Caltex Techron D, Petronas Dynamic Diesel, Mobil Diesel Efficient |
