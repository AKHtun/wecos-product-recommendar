# T-SOP-002-5 — Equivalent / Alternative Grease Selection (DLE side)

Source: derived from `Technical_Product Recommendation Process.xlsx` (T-SOP-0003, T-SOP-0002, T-SOP-002-1) and the supplemental grease training material (PPTX slides 1–42) plus the ExxonMobil *Grease Compatibility — To Be or Not To Be!* technical paper and the *Grease Static Oil Bleed* technical topic. The grease sub-procedure is added as **T-SOP-002-5** to cover the thickener / base-oil / consistency / performance axes that the lubricant SOP already singles out as special-case (T-SOP-002-1 drawing3 explicitly lists "Grease" as one of the 12 application categories and "NLGI Grade for grease" as one of the 2.3 sub-axes).

This file preserves the SOP text, the **ExxonMobil Generic Compatibility Chart** (C/M/I matrix for 7 thickener families), the **DIN 51502 → ISO 6743-9 decoder**, the **speed factor (DN / NDm)** formula, and the key ASTM references. The SKILL.md operationalises the flow; refer back here for canonical wording.

## Flow

1. Receive product recommendation request and information for grease.
2. Check 3rd-party grease product data sheet / SDS and capture:
   - **2.1 Usage / application** — rolling-element bearing (deep-groove ball / cylindrical roller / spherical / tapered / needle), plain bearing / bushing, gear (open / enclosed / worm), spline / coupling, chassis / UJ / CV joint / wheel bearing / kingpin, brake caliper pin, electric-motor bearing, kiln car / oven conveyor, steel-mill roll-neck, mining crusher / shovel pinion, wire-rope / dragline, marine deck equipment, refrigeration compressor bearing, central lubrication system, food-processing line (NSF H1), railway axlebox / wheel-flange.
   - **2.2 Base oil source** — mineral (Group I / II / III) / PAO / ester (natural or synthetic) / PAG / PFPE / silicone / vegetable / bio.
   - **2.3 Base oil viscosity** — ISO VG of the base oil trapped inside the thickener. Typical range 32 – 460. **Do not confuse with NLGI consistency.**
   - **2.4 NLGI consistency grade** — 000 / 00 / 0 / 1 / 2 / 3 / 4 / 5 / 6 (most common is 2). Measured as worked penetration after 60 strokes per ASTM D217.
   - **2.5 Thickener type** — lithium / lithium 12-hydroxy / lithium complex / calcium / calcium complex (anhydrous) / calcium sulfonate / aluminium complex / polyurea (shear stable) / bentone (clay) / silica / PTFE / sodium / barium.
   - **2.6 Performance envelope** — dropping point (ASTM D566 / D2265), worked penetration 60 strokes (ASTM D217), oil separation / bleed (ASTM D1742), water washout (ASTM D1264), water spray-off (ASTM D4049), EP four-ball weld point (ASTM D2596), wear scar (ASTM D2266), copper-strip corrosion (ASTM D4048), oxidation stability (ASTM D942), NSF H1 registration, OEM approval list.
   - **2.7 *(fallback)*** — **DIN 51502 designation** code (e.g., `KP 2 N -30`) and its **ISO 6743-9** equivalent (e.g., `L-XBCHA 2`).
3. Compare against supplier product data sheets; filter sequentially:
   - 3.1 Filter by 2.1 finding (application).
   - 3.2 Filter by 2.2 finding (base oil source).
   - 3.3 Filter by 2.3 finding (base oil viscosity).
   - 3.4 Filter by 2.4 finding (NLGI consistency).
   - 3.5 Filter by 2.5 finding (thickener type) — cross-check against the Generic Compatibility Chart below when thickener family changes.
   - 3.6 Filter by 2.6 finding (performance envelope + OEM approvals).
4. Equivalent / alternative product can be selected based on 3rd-party product?
   - Yes → step 9.
   - No → step 5.
5. Apply the **DIN 51502 / ISO 6743-9 fallback** (attribute 2.7): search the selected supplier catalogs for products whose designation code matches the incumbent's. This widens the candidate pool to "functionally-equivalent for the application family" instead of exact-attribute match.
6. Does the OEM manual / OEM grease-approval chart recommend any supplier-catalog product?
   - Yes → step 7.
   - No → step 10.
7. Open the OEM-recommended product data sheets and re-run steps 2 and 3.
8. Can an alternative be selected based on OEM-recommended products?
   - Yes → step 9.
   - No → step 10.
9. Recommend the product as equivalent or alternative. Render the **purge-out-old-grease** warning (§6 of SKILL.md) on every recommendation.
10. Inform DSR no product can be recommended.
11. Process end.

## Special-case rules (T-SOP-002-5 notes)

- **Purge out old grease — ALWAYS.** ASTM D6185 confirms that the Generic Compatibility Chart measures only structural stability of the thickener matrix; it does NOT predict additive chemistry, seal compatibility, copper / yellow-metal corrosion, wear under load, or long-term effects. **In practice, always purge.**
- **Base-oil viscosity ≠ NLGI consistency.** Base-oil ISO VG is the property that lubricates; NLGI consistency is how stiff the finished grease is. They are independent. The most common grease-selection mistake is to substitute one for the other.
- **Speed factor DN / NDm.** For rolling-element bearings: DN = rpm × bearing bore (mm); NDm = rpm × pitch diameter (mm). Use this to size base-oil viscosity (lower for higher DN).
- **DIN 51502 is the historical European designation; ISO 6743-9 superseded it in 2003.** Both codes are still printed on packaging. The agent must be able to read either, and convert between them.
- **NSF H1 is mandatory for incidental food contact.** No NSF number on the PDS = not H1. Check the registration is current.
- **Open-gear / wire-rope greases** are usually not NLGI-rated in the normal sense — they are often "semi-fluid" or "adhesive" greases with tackifiers. Treat them as a separate sub-flow if the supplier catalog distinguishes them.
- **High-temperature greases** (> 150 °C continuous service): synthetic base oil + high-dropping-point thickener.
- **Refrigeration compressor greases** must be refrigerant-compatible (NH3, CO2, HFC, HFO). Cross-check with the compressor OEM.

## ExxonMobil Generic Compatibility Chart (Table 1)

Source: *Mobil Industrial Lubricants — Grease Compatibility — To Be or Not To Be!* (ExxonMobil, 2009; ASTM D6185 protocol).

| | Aluminum Complex | Calcium Complex | Calcium Sulfonate | Lithium 12-Hydroxy | Lithium Complex | Polyurea (shear stable) | Clay |
|---|---|---|---|---|---|---|---|
| **Aluminum Complex** | C | I | M | I | I | M | I |
| **Calcium Complex** | I | C | M | I | M | C | I |
| **Calcium Sulfonate** | M | M | C | M | C | I | I |
| **Lithium 12-Hydroxy** | I | I | M | C | C | M | I |
| **Lithium Complex** | I | M | C | C | C | M | I |
| **Polyurea (shear stable)** | M | C | I | M | M | C | M |
| **Clay** | I | I | I | I | I | M | C |

Legend: **C** = Compatible (low risk of structural instability within a short timeframe), **M** = Moderately Compatible (change beyond repeatability of the least-performing grease but within test reproducibility), **I** = Incompatible (significant hardening / softening / oil separation likely after a short time in application).

> ⚠ **This matrix addresses structural stability only.** It does NOT address additive-related incompatibilities, seal compatibility, yellow-metal corrosion, or long-term performance. **Always purge out the old grease** regardless of chart rating (ExxonMobil's own paper recommends this — and SKF, FAG, Timken, NSK publish the same guidance).

## DIN 51502 → ISO 6743-9 decoder

### DIN 51502 code (historical European designation)

Format: **`<lubricant type> <consistency> <performance class> <temp range>`**

Example: **KP 2 N -30** → K = grease (Schmierfett), P = plain bearings + rolling-element bearings (Lager), 2 = NLGI 2, N = normal operating temperature (–30 to +120 °C), –30 = lower temperature limit (°C).

#### Position 1 — Lubricant type
| Code | Meaning |
|---|---|
| **K** | Lubricating grease (Schmierfett) |
| (no prefix) | Older DIN code variant |
| **OG** | Open gear grease (off-road) |
| **G** | Gear oil / box grease |
| **M** | Pastes (assembly / anti-seize) |

#### Position 2 — Application family
| Code | Meaning |
|---|---|
| (none) | General |
| **P** | Plain bearings + rolling-element bearings (Lager) |
| **F** | Rolling-element bearings only (Wälzlager) |
| **G** | Enclosed gears (Getriebe) |
| **OG** | Open gears |
| **R** | Threaded spindles / guides |

#### Position 3 — NLGI consistency
| Code | NLGI grade |
|---|---|
| 000 | 000 |
| 00 | 00 |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |

#### Position 4 — Performance class (additive load)
| Code | Meaning |
|---|---|
| (none) | No EP / AW additives |
| **K** | Corrosion + aging protection only (no EP) |
| **P** | Corrosion protection + EP (older code) |
| **N** | Normal operating temperature range (–30 to +120 °C mineral) |
| **M** | Water resistance (Marine / wet) |
| **L** | Low temperature |
| **H** | High temperature (> 150 °C) |
| **F** | Solid lubricant additives (PTFE, MoS2, graphite) — for EP / boundary |
| **E** | EP additives for high load |
| **W** | Wide temperature range |
| **S** | Special additive package |

#### Position 5 — Lower temperature limit
Always preceded by a minus sign, in °C. Example: `-30` = –30 °C lower limit.

### ISO 6743-9 code (current ISO standard, 2003)

ISO 6743-9 superseded DIN 51502 in 2003. The code format is `L-XBCHA 2` style:

Format: **`L-X<application><temp><water><load><NLGI>`**

Example: **L-XBCHA 2** → L = lubricant, X = grease, B = plain + rolling bearings, C = low temperature (–30 °C), H = high temperature (≤ 120 °C), A = water-stable, 2 = NLGI 2.

#### Decoder summary
| Code | Position | Meaning |
|---|---|---|
| **L** | 1 | Lubricant (ISO 6743 family) |
| **X** | 2 | X = lubricating grease (Y = pastes, Z = open-gear compounds) |
| **B** | 3 | Application: A = total-loss lubrication; B = plain + rolling bearings; C = enclosed gears; D = open gears (compound); E = threaded spindles; F = chassis (older code); G = wire-rope; H = chains |
| **C** | 4 | Lower temperature limit: A = 0 °C, B = –10 °C, C = –20 °C, D = –30 °C, E = –40 °C, F = –50 °C |
| **H** | 5 | Upper temperature limit: A = 60 °C, B = 90 °C, C = 120 °C, D = 140 °C, E = 160 °C, F = 180 °C, G = 200 °C, H = 220 °C, I = 240 °C, J = 260 °C, K = 280 °C, L = 300 °C |
| **A** | 6 | Water resistance: A = non-water-resistant, B = water-resistant, C = water-stable, D = very water-stable |
| **2** | 7 | NLGI grade (000 – 6) |

#### Conversion table (common DIN 51502 → ISO 6743-9)
| DIN 51502 | ISO 6743-9 | Typical use |
|---|---|---|
| KP 2 N -30 | L-XBCHA 2 | Multipurpose industrial bearing grease |
| KP 2 K -30 | L-XBCHA 2 | Same as above (K = corrosion/aging additives, no EP) |
| KP 2 P -30 | L-XBCHA 2 | Older EP code |
| KP 2 M -30 | L-XBCHA 2 | Water-resistant bearing grease |
| KP 2 H -30 | L-XBDHB 2 | High-temperature industrial bearing grease |
| KPG 2 N -30 | L-XCCIB 2 | Gear grease (enclosed) |
| KPF 2 K -20 | L-XBCIB 2 | Rolling bearing, low-temperature, EP |
| K 2 K -30 | L-XABHB 2 | Chassis grease (older DIN code) |

> When a candidate PDS publishes only one of the two codes, the agent can convert using this table to widen the search.

## Speed factor (DN / NDm)

For rolling-element bearings, the speed factor determines the required base-oil viscosity. Higher speed factor → lower base-oil viscosity required (less churning heat, better channeling).

```
DN    = N (rpm) × Db (bearing bore, mm)
NDm   = N (rpm) × Dm (pitch diameter, mm)
        where Dm = (Db + De) / 2  and  De = outside diameter
```

### Viscosity selection by DN (typical mineral oil guide)
| DN range | Recommended ISO VG of base oil | Notes |
|---|---|---|
| < 50 000 | 460 – 680 | Very slow speed, heavy load |
| 50 000 – 100 000 | 220 – 460 | Slow / moderate |
| 100 000 – 300 000 | 100 – 220 | Moderate |
| 300 000 – 500 000 | 46 – 100 | Moderate / high |
| 500 000 – 1 000 000 | 32 – 68 | High speed (spindle bearings) |
| > 1 000 000 | 22 – 46 | Very high speed (machine-tool spindles, turbo machinery) |

> Adjust ±1 ISO VG if all other axes (NLGI, thickener, performance envelope) match.

## ASTM standards quick reference

| Standard | Title | What it tells you |
|---|---|---|
| **ASTM D217** | Cone penetration of lubricating grease | Worked penetration 60 strokes → NLGI grade |
| **ASTM D566** | Dropping point of lubricating grease (older method) | Upper temperature limit of the thickener matrix |
| **ASTM D2265** | Dropping point of lubricating grease (modern method, higher range) | Same as D566, wider range |
| **ASTM D1742** | Oil separation from lubricating grease (static, cone screen) | Storage bleed — small amount is normal |
| **ASTM D1264** | Water washout characteristics of lubricating grease | Wet-environment resistance |
| **ASTM D4049** | Water spray-off resistance of lubricating grease | Spray vs standing water |
| **ASTM D2596** | Measurement of extreme-pressure properties of lubricating grease (four-ball method) | Weld point (kg) — load-carrying capacity |
| **ASTM D2266** | Wear preventive characteristics of lubricating grease (four-ball method) | Wear scar diameter (mm) |
| **ASTM D4048** | Detection of copper corrosion from lubricating grease | Yellow-metal compatibility |
| **ASTM D942** | Oxidation stability of lubricating grease (pressure vessel) | High-temp oxidation life (hours to pressure drop) |
| **ASTM D4175** | Standard terminology relating to petroleum, petroleum products, and lubricants | Defines "lubricating grease" |
| **ASTM D6185** | Standard practice for evaluating compatibility of binary mixtures of lubricating greases | The compatibility testing protocol |
| **ASTM D4950** | Classification and specification of automotive service greases | GC-LB (chassis / wheel bearing) classification |

## NLGI consistency quick reference

| NLGI grade | Worked penetration (mm/10, 60 strokes) | Appearance | Typical use |
|---|---|---|---|
| **000** | 445 – 475 | Semi-fluid | Centralised lube, gearboxes |
| **00** | 400 – 430 | Semi-fluid | Centralised lube |
| **0** | 355 – 385 | Very soft | Centralised lube, gearboxes |
| **1** | 310 – 340 | Soft | High-speed bearings, gearboxes |
| **2** | 265 – 295 | Standard | Most common — general bearing grease |
| **3** | 220 – 250 | Stiff | Heavy-load, low-speed bearings |
| **4** | 175 – 205 | Very stiff | Sealed-for-life bearings, water pumps |
| **5** | 130 – 160 | Hard | Slow-speed, sealed bearings |
| **6** | 85 – 115 | Block grease | Slow, heavily loaded, grease blocks |

## Thickener family cheat sheet

| Family | Typical dropping point | Water resistance | Cost | Common use |
|---|---|---|---|---|
| **Lithium 12-hydroxy** | 180 – 200 °C | Good | Low | Multipurpose (most common worldwide) |
| **Lithium complex** | 250 – 280 °C | Good | Low–Mid | EP multipurpose, high-temp |
| **Calcium (anhydrous)** | 90 – 110 °C | Excellent | Low | Wet environment, low-temp |
| **Calcium complex (anhydrous)** | 150 – 180 °C | Excellent | Low–Mid | Wet, low-to-moderate temp |
| **Calcium sulfonate** | 280 – 300 °C | Excellent | Mid | Heavy-load, wet, high-temp |
| **Aluminium complex** | 230 – 260 °C | Excellent | Mid | High-temp, water-resistant, food-grade variants |
| **Polyurea (shear-stable)** | 240 – 280 °C | Good | Mid–High | Electric-motor bearings, sealed-for-life |
| **Bentone (clay)** | No true drop point (stable to ~200 °C) | Good | Mid | High-temp, non-melt |
| **Silica (fumed)** | No true drop point | Good | Mid–High | High-temp, specialty |
| **PTFE** | Very high | Excellent | Very High | Chemical / oxygen service, low-outgassing |
| **Sodium** | 150 – 180 °C | Poor (emulsifies) | Low | Legacy, rarely used today |

## OEM grease approval families (where to look)

| OEM family | Where to look | What to check |
|---|---|---|
| SKF | SKF bearing greases (LGEP, LGMT, LGEP 2, LGHP 2) | SKF → "Bearing grease selection" tool |
| Schaeffler / FAG / INA | Schaeffler → medias greases | Schaeffler approval chart |
| NSK | NSK → "NSK Grease Catalogue" | NSK approval list |
| NTN-SNR | NTN-SNR → "Grease selection" | NTN approval list |
| Timken | Timken → grease approval | Timken approval list |
| Mercedes-Benz | bevo.mercedes-benz.com → operating fluids sheet | MB 331 (chassis), MB 332 (wheel bearing) |
| MAN | MAN → lubricant approval list | MAN 284 Li-H, Li-K, Li-Ca |
| Volvo | Volvo Trucks service portal | Volvo 97720 / 97721 |
| Scania | Scania service portal | Scania grease approvals |
| Caterpillar | cat.com → SEBU6250 fluids reference | Cat multipurpose EP grease |
| Komatsu | Komatsu service portal | Komatsu grease approvals |
| Hitachi / Kobelco / JCB | OEM service portals | EP multipurpose greases |
| Deutsche Bahn (DB) | DB → operating regulation | Railway axlebox grease approvals |
| AAR (American Association of Railroads) | AAR M-942 | Railway grease specs |
| NSF | NSF International White Book | H1 / H2 / 3H / HT1 registrations |
| InS / H1 (UK) | InS services | H1 registrations |

## Out of scope for this SOP

- **Liquid lubricants / oils** — use `lubricant-recommender`.
- **Engine coolants** — use `coolant-recommender`.
- **Diesel and marine fuels** — use `diesel-recommender`.
- **AdBlue / DEF** — use `adblue-def-recommender`.
- **Direct food-contact greases** (not just NSF H1 incidental contact) — escalate.
- **Biodegradable / environmental greases** (EU Ecolabel, USDA BioPreferred, VGP-compliant) — include in scope but require explicit environmental spec capture.
- **Conductive / anti-static greases** for electrical connectors — escalate.
- **Aviation greases** (MIL-PRF-23827, MIL-G-21164, DMS 2019, BMS 3-3, etc.) — escalate.
- **Solid lubricants / dry-film coatings** (MoS2, graphite, PTFE coatings) — different product category.

> The original Excel workbook referenced "VE" as the distribution catalog. This skill replaces that single source with a user-selectable supplier scope (ExxonMobil, Shell, Chevron/Caltex, Castrol/BP, TotalEnergies, Fuchs, Klüber, SKF/LG, plus any regional blender the DSR names).