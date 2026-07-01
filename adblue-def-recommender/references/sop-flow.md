# T-SOP-002-4 — Equivalent / Alternative AdBlue / DEF Selection (DLE side)

Source: derived from the same `Technical_Product Recommendation Process.xlsx` workbook that produced T-SOP-002-1 (lubricant), T-SOP-002-2 (coolant), T-SOP-002-3 (diesel). The AdBlue / DEF sub-procedure is added as T-SOP-002-4 to cover the SCR-aftertreatment consumable that nearly every Euro VI / EPA 2010+ HD truck, every Stage V off-road SCR machine, and every IMO Tier III marine engine now requires.

This file preserves the SOP text and the ISO 22241 / API / VDA decoder. The SKILL.md operationalises the flow; refer back here for canonical wording.

## Flow

1. Receive product recommendation request and information for AdBlue / DEF.
2. Check 3rd-party AdBlue / DEF product data sheet / SDS / Certificate of Analysis and capture:
   - **2.1 Application / OEM-emission-tier** — On-road HD truck (Euro VI / EPA 2010+ SCR), Off-road / mining / construction SCR (Stage V / EPA Tier 4 Final), Marine SCR (IMO Tier III ECA), Stationary gen-set SCR, Passenger-car SCR (BlueHDi / BlueTec / TDI / AdBlue), or Bulk depot / resale.
   - **2.2 Certification scope + OEM approval coverage** — ISO 22241 part 1 / 2 / 3 / 4 conformance; API Diesel Exhaust Fluid Certification mark (North America); VDA AdBlue trademark licence (EMEA / Asia-Pacific); OEM-specific approval lists (MB 325.x, VW TL 774, Cummins CES, Detroit Diesel Power Cool, MAN, Scania, Iveco, DAF, Volvo, FPT, etc.).
3. Compare with the supplier product data sheets:
   - 3.1 Filter by 2.1 finding (application / OEM emission tier).
   - 3.2 Filter by 2.2 finding (certification scope + OEM approvals).
4. Equivalent / alternative product can be selected based on 3rd-party product?
   - Yes → step 9.
   - No → step 5.
5. Consult OEM Manual based on OEM / Maker / Model **and** consult the regulator-published certified-producer list (VDA-approved list for AdBlue in EMEA; API certified-producers list at api.org/DEF for North America).
6. Does the OEM Manual / regulator list allow any supplier-catalog product?
   - Yes → step 7.
   - No → step 10.
7. Open the OEM-recommended / regulator-listed product data sheets and re-run steps 2 and 3.
8. Can an alternative be selected based on OEM-recommended / regulator-listed products?
   - Yes → step 9.
   - No → step 10.
9. Recommend the product as equivalent or alternative.
10. Inform DSR no product can be recommended.
11. Process end.

## Special-case rules (T-SOP-002-4 notes)

- **ISO 22241 conformance is non-negotiable.** A product that is not certified to ISO 22241 part 1 (quality), part 2 (test methods), part 3 (handling, transportation, and storage), and part 4 (refilling interface) MUST NOT be recommended regardless of price. Out-of-spec DEF crystallises in the SCR catalyst and causes irreversible damage.
- **API mark vs AdBlue trademark.** For North American sales, the API Diesel Exhaust Fluid Certification mark is the regulator-blessed marker; for EMEA / APAC sales the VDA AdBlue trademark licence is the equivalent. Both imply ISO 22241 conformance but the certification chain differs — do not assume one implies the other.
- **OEM approval list must be explicit.** A candidate PDS that says "suitable for SCR systems" or "compatible with all major OEMs" without naming the OEM is **not** an OEM approval. Reject it.
- **Dilution & top-up.** DEF is dosed by the SCR module at a ratio calibrated to ISO 22241 chemistry (typically 3 – 5 % of fuel consumption). Diluting with water, mixing with off-spec urea solutions, or topping up with windshield washer fluid destroys the SCR catalyst within hours. Always issue the "do not dilute" warning.
- **Storage & shelf-life.** Shelf life is typically 12 – 36 months depending on storage temperature; storage above 30 °C accelerates hydrolysis (urea → ammonia + CO₂). Bulk tanks must be HDPE or stainless steel with sealed venting; carbon steel tanks and copper / brass fittings contaminate the fluid. Always issue the storage & shelf-life warning.
- **Cold climate.** DEF freezes at –11 °C; the vehicle / equipment SCR system is designed to thaw and re-use the fluid. Do **not** add anti-freeze or kerosene.
- **Marine SCR.** IMO MARPOL Annex VI Tier III NOx compliance requires ECA-grade fuel **plus** a certified SCR system. The AdBlue / DEF chemistry itself is ISO 22241, but the candidate must additionally hold the relevant class-society approval (DNV, Lloyd's Register, ABS, BV) and the SCR-OEM explicit approval (Hug Engineering, Yara Marine Technologies, Wärtsilä PureNOx, etc.).
- **Hot-start DEF / iDEF** (freeze point depressed to ≈ –20 °C or below) is **out of scope** for this skill — it is outside ISO 22241 and must be escalated.

## ISO 22241 decoder

| Part | Title | What it covers |
|---|---|---|
| **ISO 22241-1** | Quality requirements | Urea concentration (31.8 – 33.2 % w/w), alkalinity as NH3 (≤ 0.2 %), biuret (≤ 0.3 %), aldehydes (≤ 5 mg/kg), phosphate (≤ 0.5 mg/kg), individual metals (Ca, Fe, Na, K, Cu, Zn, Cr, Ni, Al, Mg each ≤ 0.5 mg/kg; total ≤ 1.0 mg/kg), insolubles (≤ 20 mg/kg), density @ 20 °C (1.087 – 1.093 g/cm³), refractive index @ 20 °C (1.381 – 1.384). |
| **ISO 22241-2** | Test methods | Reference analytical methods for every quality parameter in part 1 (refractometry for concentration, ICP-OES for metals, ion chromatography for anions, etc.). |
| **ISO 22241-3** | Handling, transportation, and storage | Tank material requirements (HDPE / stainless), temperature limits (–5 °C to +30 °C storage; –11 °C freezing point), contamination prevention, shelf-life expectations (12 – 36 months depending on temperature). |
| **ISO 22241-4** | Refilling interface | Nozzle / coupling geometry for service-station and IBC filling — keeps non-DEF fluids from being pumped into the DEF tank by mistake. |

## Regional certification marker decoder

| Region | Regulator-blessed mark | What it confirms |
|---|---|---|
| EMEA / APAC (AdBlue name) | **VDA AdBlue trademark licence** + ISO 22241 certificate number | Producer is licensed by the German VDA to make / market the product under the AdBlue name; ISO 22241 conformance is audited annually. |
| North America (DEF name) | **API Diesel Exhaust Fluid Certification mark** + ISO 22241 certificate | Producer is on the API certified-producers list (api.org/DEF); ISO 22241 conformance is audited by API. |
| Brazil (ARLA 32) | ANP / Inmetro certification (separate) | Same chemistry (AUS 32), separate regulator chain; covered by the same flow once the DSR names a Brazilian producer. |
| Japan | JIS K 2247 (urea AUS 32 grade) + ISO 22241 | Domestic Japanese-spec equivalent; most Japanese producers also carry ISO 22241 for export. |
| China | GB 29518-2013 (urea AUS 32) + ISO 22241 | National standard; covers domestic SCR truck market. |

## OEM-approval landscape (where the customer equipment is the binding constraint)

| OEM family | Approval route | Where to verify |
|---|---|---|
| Mercedes-Benz trucks (Actros, Antos, Arocs) | MB-Approval 325.5 / .6 (AdBlue) list | Mercedes-Benz Special Equipment / BeVo portal; AdBlue producer must hold current MB 325 approval. |
| VW Group commercial (MAN, Scania) | VW TL 774 / MAN 328 / Scania approval lists | OEM service portal; cross-listed with VDA-approved AdBlue producers. |
| Volvo / Renault Trucks | Volvo STD 417-0001 / Renault approval | Volvo IMPACT portal; most VDA-licensed producers qualify by default. |
| Iveco / FPT | Iveco approval list (linked to VDA AdBlue list) | Iveco service portal. |
| DAF / PACCAR | DAF approval (linked to VDA AdBlue list) | DAF service portal. |
| Cummins (ISB, ISX, X12, X15, L9) | Cummins CES 14603 / SB-3-A005 (AdBlue spec) | cummins.com → Fluids & Lubricants. |
| Detroit Diesel (DD13, DD15, DD16) | Detroit Diesel Power Cool / 93K217 specification list | Detroit Diesel service portal. |
| Caterpillar (C13, C15, C18 ACERT marine / gen-set) | Caterpillar SCR-fluids list | cat.com → Fluids Reference (SEBU6250 series). |
| Marine SCR (Hug, Yara Marine Technologies, Wärtsilä PureNOx) | Class-society certified + SCR-OEM explicit | DNV / Lloyd's Register / ABS / BV → type approval database. |
| Passenger-car SCR (VW BlueMotion, MB BlueTec, PSA BlueHDi, FCA Blue&Me, Hyundai-Kia, Honda, GM Duramax) | OEM AdBlue supplier lists | OEM service portal; most VDA-licensed producers qualify. |

## Density / refractive-index quality grid (use to spot-check any candidate)

| Property | Min | Max | What it tells you |
|---|---|---|---|
| Urea concentration (% w/w) | 31.8 | 33.2 | Below 31.8 → NOx breakthrough; above 33.2 → ammonia slip. |
| Density @ 20 °C (g/cm³) | 1.087 | 1.093 | Correlates directly with urea concentration. |
| Refractive index @ 20 °C | 1.381 | 1.384 | Field-screening tool (refractometer). |
| Alkalinity as NH3 (%) | — | 0.2 | High alkalinity → biuret / ammonia breakdown. |
| Biuret (%) | — | 0.3 | High biuret → polymerisation / deposits on catalyst. |
| Insolubles (mg/kg) | — | 20 | High insolubles → tank / filter blockage. |
| Sum of metals (mg/kg) | — | 1.0 | Any single metal over 0.5 mg/kg is a red flag — poisons the catalyst. |

## Out of scope for this SOP

- **Hot-start DEF / iDEF** (aqueous urea with reduced freeze point, e.g., –20 °C).
- **DEF used in stationary power-generation SCR with ammonia slip injection** (chemistry differs from AUS 32).
- **Concentrated urea solutions** (e.g., 40 % w/w urea) — these are NOT AdBlue / DEF and must not be sold or recommended as such.
- **Non-urea SCR reductants** (e.g., ammonia, hydrocarbon SCR) — entirely different chemistry.
- Anything where the customer has not provided a verifiable incumbent product spec / lot number.

> The original Excel workbook referenced "VE" as the distribution catalog. This skill replaces that single source with a user-selectable supplier scope (Yara / Air1, BASF, CF Industries, Mitsui, Borealis, SK Chemicals, plus any blender / OEM-branded product the DSR names).