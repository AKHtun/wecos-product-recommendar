# Source SOP Reference

This file preserves the original SOP content extracted from
`Technical_Product Recommendation Process.xlsx`. The SKILL.md operationalizes
these flows; refer back here if you need the canonical wording.

## T-SOP-0003 — Product Recommendation Request Process (DSR side)

1. DSR raises product recommendation request.
2. DSR provides basic information for product recommendation:
   - a. 3rd party product name
   - b. Application
   - c. Equipment OEM / Model
   - d. Operating temperature
   - e. RPM, shaft diameter, bearing dimension (for grease)
3. Check whether information is enough for product recommendation.
   - 3.A. Request necessary information from DSR.
   - 3.B. Follow T-SOP-0002.
4. Register the recommendation in Recommendation Record file and obtain a Recommendation Record ID.
5. Recommend suitable product(s) with the Recommendation Record ID.
6. DSR receives the recommendation; process ends.

## T-SOP-0002 — Equivalent / Alternative Product Selection Process (DLE side)

1. DLE receives the product recommendation request.
2. DLE checks whether the information is enough to proceed.
3. If enough → step 4. If not → 3.A.
   - 3.A. Request the missing information from DSR. Must be resolved before T-SOP-0002 starts.
4. Choose sub-procedure based on product line:
   - 4.A. Lubricant → T-SOP-002-1
   - 4.B. Coolant → T-SOP-002-2
   - 4.C. Fuel → T-SOP-002-3
5. Recommend product per sub-procedure → step 6 if product(s) exist, step 7 if none.
6. Recommend the product(s).
7. Inform DSR no product can be recommended.
8. Process end.

## T-SOP-002-1 — Lubricant sub-procedure

1. Receive request and information for lubricant.
2. Read 3rd-party product data sheet and capture:
   - 2.1 Usage / application — CVL/Automotive/Locomotive, IL, Diesel engine, Automotive gearbox, Gearbox, Hydraulic, Grease, Compressor, Refrigeration compressor, Gas engine, Turbine, Heat-transfer system.
   - 2.2 Base oil source — Mineral, Synthetic, Environmentally Friendly.
   - 2.3 Viscosity / VI / NLGI — SAE, ISO VG, VI; NLGI for grease.
   - 2.4 Industry standards — API, ACEA, DIN, ISO, AGMA, JASO.
   - 2.5 Operating temperature — Max, Min, Flash Point, Pour Point.
   - 2.6 OEM requirements — MAN, Volvo, MB, Cummins, etc.
3. Compare against VE distribution catalog data sheets; filter sequentially:
   - 3.1 Filter by 2.1 finding.
   - 3.2 Filter by 2.2 finding.
   - 3.3 Filter by 2.3 finding.
   - 3.4 Filter by 2.4 finding.
   - 3.5 Filter by 2.5 finding.
   - 3.6 Filter by 2.6 finding.
4. Decision — equivalent / alternative can be selected based on 3rd-party product?
   - Yes → step 9.
   - No → step 5.
5. Consult OEM manual based on OEM / Maker / Model.
6. Does the OEM manual recommend any VE product?
   - Yes → step 7.
   - No → step 10.
7. Open the OEM-recommended product data sheets and re-run steps 2 and 3.
8. Can an alternative be selected based on OEM-recommended products?
   - Yes → step 9.
   - No → step 10.
9. Recommend the product as equivalent / alternative.
10. Inform DSR no product can be recommended.
11. Process end.

### Special-case notes (from the flow)

- **PAG oils** — Not compatible with other oils or with PAGs of different formulation. May require flushing. Provide PAG flushing procedure.
- **Greases** — Always verify grease thickener compatibility. If incompatible, purge old grease and replace with the recommended grease.
- **Refrigeration compressor** — Additional inputs required: OEM, equipment model, application, refrigerant, evaporation temperature.

> The original Excel file referenced "VE" as the distribution catalog. This
> skill replaces that single source with a user-selectable supplier scope
> (ExxonMobil, Shell, Chevron/Caltex, Castrol, TotalEnergies, plus any
> supplier the DSR names).
