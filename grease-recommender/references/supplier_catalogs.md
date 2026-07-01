# Grease Supplier Catalog Reference

The DLE agent must let the DSR choose which supplier catalogs to search. The
list below is a *starting* set, not a hardcoded scope — accept any regional
blender or specialty supplier the DSR names and apply the same PDS / SDS
workflow.

Always prefer the manufacturer's own domain. Reject blogs, distributor
rebrands, and resellers as primary sources.

## Tier-1 majors

| Supplier | Primary domain(s) | Core grease brands | Notes |
|---|---|---|---|
| ExxonMobil | mobil.com, exxonmobil.com | Mobilgrease (MM, BRB, 28, 33, 532, Polyrex, Centaur, FM, Food Grease) | World's largest grease blender. Specialty lines for aviation, food, mining, electric motor. |
| Shell | shell.com | Shell Gadus (S2, S3, S4, S5, S7 series — V100, V150, V220, V460, V550, S5 T100, S5 V100) | Gadus S5 / S7 are premium synthetic. V100 / V150 are mainstream mineral. |
| Chevron / Caltex | chevronlubricants.com, caltex.com | Chevron Ultra-Duty Grease, Texaco Starplex, Caltex Multifak | Ultra-Duty EP, Starplex polyurea for long-life. |
| Castrol / BP | castrol.com, bp.com | Castrol Spheerol (LMM, EPL, SX, L 2), BP Energrease | Long history; Spheerol series is the workhorse. |
| TotalEnergies | totalenergies.com | Total Multis (Complex, EP, MS), Total Ceran (HT, HV, XM, GEP, AD), TotalCopal | Ceran = high-temp / water-resistant. Copal = open-gear. |
| Fuchs | fuchs.com | Fuchs Renolit, Fuchs Ecogrease, Stabylan | Specialises in EP and food-grade. |
| Klüber | klueber.com | Klüberplex, Klüberlub, Klüberbio, Klübersynth, Hotemp, Barrierta | Premium specialty; strong in food, pharma, high-temp. |
| SKF | skf.com | SKF LGEP 2, LGEP 3, LGMT 2/3, LGHP 2, LGWA 2, LGGB 2, LGLT 2, LGWM 2/3, LMCV 2 | Bearing-OEM brand. Use SKF's bearing-grease selection tool. |
| Schaeffler / FAG / INA | schaeffler.com | Arcanol | Bearing-OEM brand; tied to Schaeffler approval list. |
| NSK | nsk.com | NSK grease series | Bearing-OEM brand. |
| NTN-SNR | ntn-snr.com | NTN-SNR LUB | Bearing-OEM brand. |
| Timken | timken.com | Timken food-safe grease | Bearing-OEM brand. |

## Tier-2 / regional (accept on request)

| Supplier | Primary domain | Notes |
|---|---|---|
| PetroChina (Kunlun) | kunlun-lub.com | Chinese market; growing international. |
| Sinopec Lubricant | lubricant.sinopec.com | Chinese market. |
| CNPC | cnpc.com.cn | Chinese market. |
| Petronas Lubricants | pli-petronas.com | Malaysia / APAC. |
| Idemitsu | idemitsu.com | Japan. |
| ENEOS | eneos.co.jp | Japan. |
| LG Chem | lgchem.com | Korea; supplies SKF co-brand. |
| Lubrilog | lubrilog.com | France / Europe; specialty. |
| Carl Bechem | bechem.de | Germany; specialty high-temp. |
| Setral | setral.net | Germany; specialty. |
| CONDAT | condat.fr | France; specialty open-gear / wire-rope. |
| ITW (Rocol, Devcon) | itwprobrands.com | Rocol = UK industrial maintenance. |
| Molykote (DuPont) | molykote.com | Specialty solid / PTFE / MoS2 lubricants. |
| CRC Industries | crcindustries.com | Maintenance greases. |
| Dow / Dow Corning / Molykote | dow.com | Specialty silicone / PFPE. |
| Castrol Industrial (specialty) | castrol.com/industrial | Specialty food-grade (Castrol Optitemp / Variocut). |
| Houghton (now Quaker Houghton) | quakerhoughton.com | Metalworking + industrial greases. |

## Specialty suppliers (high-end / niche)

| Supplier | Primary domain | Notes |
|---|---|---|
| Nyco (NYCO Greases) | nyco.org | Specialty synthetic + ester; strong in aerospace and military. |
| Calwax | calwax.com | Specialty food-grade, NSF H1. |
| Schaeffer Mfg | schaefferoil.com | Specialty food-grade + heavy industrial. |
| Lubrication Engineers | lubricationengineers.com | Heavy industrial; mining / steel. |
| Whitmore Manufacturing | whitmores.com | Open-gear, rail, mining specialty. |
| B'laster (Blaster Chemical) | blastercorp.com | Maintenance, penetrating, marine. |
| Momentive (silicone) | momentive.com | Silicone greases. |
| Chemours (Krytox PFPE) | chemours.com | PFPE greases for oxygen / chemical / vacuum. |

## Search patterns that work well

Use these in `WebFetch` / `firecrawl-search`:

```
"<product name>" PDS site:<supplier-domain>
"<product name>" "technical data sheet" filetype:pdf
"<product name>" grease SDS filetype:pdf
"<product name>" "NLGI" datasheet
"<thickenertype>" "<NLGI grade>" grease PDS site:<supplier-domain>
<OEM> <model> "approved grease" filetype:pdf
DIN 51502 <code> grease equivalent
ISO 6743-9 <class> grease equivalent
NSF H1 grease <application>
```

## Bearing-OEM grease selection tools (authoritative)

| OEM | Tool | URL pattern |
|---|---|---|
| SKF | SKF Bearing Greases selection tool | skf.com → products → lubricants → bearing greases |
| Schaeffler | medias Greases product | medias.schaeffler.com → greases |
| NSK | NSK grease catalogue | nsk.com → products → lubricants |
| NTN-SNR | NTN-SNR grease selection | ntn-snr.com → technical → greases |
| Timken | Timken grease approvals | timken.com → products → grease |
| FAG | (Schaeffler portal) | same as Schaeffler |
| INA | (Schaeffler portal) | same as Schaeffler |

## Application → supplier first-choice cheat sheet

| Application | First-choice supplier brands | Notes |
|---|---|---|
| General rolling-element bearing | Mobilgrease MM 220, Shell Gadus S2 V220 2, Castrol Spheerol LMM, Total Multis EP 2, SKF LGMT 2/3, Arcanol LOAD 220 | Multipurpose lithium 2 — most common product worldwide. |
| Heavy-load / shock | Mobilgrease 532, Shell Gadus S3 V220C 2, Total Ceran XM 220, Castrol Spheerol SX 2, Fuchs Renolit EP 2 | Lithium-complex or calcium-sulfonate, EP additives. |
| High temperature | Mobil Polyrex EM, Shell Gadus S5 T100, Total Ceran HT 200, Klüber Hotemp, SKF LGHP 2 | Polyurea or aluminium-complex or lithium-complex + synthetic base oil. |
| Low temperature | Mobilgrease 33, Shell Gadus S5 V100 2, Castrol Spheerol L 2 LT, SKF LGLT 2 | Synthetic base oil (PAO / ester), low pour point. |
| Wet / water-washout | Mobilgrease BRB 532, Shell Gadus S3 V220C 2, Total Ceran GEP, Caltex Starplex | Calcium-sulfonate or aluminium-complex thickeners dominate. |
| Marine deck equipment | Mobilgrease 532, Shell Gadus S3 V220C 2, Total Ceran XM 220, Whitmore marine series | Water-resistant + corrosion-inhibited. |
| Electric motor bearing | Mobil Polyrex EM 103, Shell Gadus S5 V100 2, SKF LGEP 2 / LGHP 2, Klüber Petamo GHY 133 | Polyurea or lithium-complex; quiet-running. |
| Mining / pinion / shovel | Mobilgrease 532, Shell Gadus S3 V460D 2, Total Ceran XM 460, Whitmore Cynolene | High-viscosity base oil, EP, water-resistant. |
| Wire-rope / dragline | TotalCopal, CONDAT Wire Rope Grease, Whitmore Wire Rope Grease | Adhesive / tacky; open-gear family. |
| Open gear | Mobil Mobilgear OGL, TotalCopal OGH, CONDAT Gear grease, Whitmore Cynolene | Open-gear family (DIN 51502 OG). |
| Centralised lube | Mobil Mobilgrease LC, Shell Gadus S2 V220 00, Total Multis EP 00, SKF LGETM 2 | NLGI 000 / 00 / 0; good pumpability. |
| Food-grade (NSF H1) | Mobil Mobilgrease FM 102, Castrol Optitemp FG, Klüber Klüberbio, Total Nevastane HDM 2 | NSF H1 registration mandatory on PDS. |
| Railway axlebox | Mobil Mobilith SHC 460, Shell Gadus S5 V460, Total Ceran XM 460, Fuchs Renolit CX 460 | AAR M-942 / EN 12081 / EN 12082 approved. |
| Refrigeration compressor | Mobil EAL Arctic 68, Castrol Icematic, Total Planetelf, Fuchs Reniso | Refrigerant-compatible (NH3, CO2, HFC, HFO). |
| Brake caliper pin | Castrol LMX, Total LHM, FTE / ATE-approved greases | High-temp silicone- or PFPE-based. |

## DIN 51502 / ISO 6743-9 quick lookup (use the decoder in sop-flow.md for the full grammar)

| DIN 51502 | ISO 6743-9 | Typical use |
|---|---|---|
| KP 2 N -30 | L-XBCHA 2 | Multipurpose industrial bearing grease |
| KP 2 K -30 | L-XBCHA 2 | Multipurpose industrial bearing grease (corrosion inhibited) |
| KP 2 M -30 | L-XBCHA 2 | Water-resistant bearing grease |
| KP 2 H -30 | L-XBDHB 2 | High-temp industrial bearing grease |
| KPF 2 K -20 | L-XBCIB 2 | Rolling bearing, low-temp, EP |
| KPG 2 N -30 | L-XCCIB 2 | Gear grease (enclosed) |
| K 2 K -30 | L-XABHB 2 | Chassis grease (older DIN code) |

## Industry-standards quick reference

| Body | Standard | What it covers |
|---|---|---|
| ASTM | D217 | Worked penetration → NLGI grade |
| ASTM | D566 / D2265 | Dropping point |
| ASTM | D1264 | Water washout |
| ASTM | D2596 | EP four-ball weld point |
| ASTM | D4048 | Copper-strip corrosion |
| ASTM | D4049 | Water spray-off |
| ASTM | D4950 | Automotive service greases (GC-LB) |
| ASTM | D6185 | Grease compatibility testing |
| DIN | 51502 | Historical European designation code |
| ISO | 6743-9 | Current ISO designation code (supersedes DIN 51502) |
| EN | 12081 | Railway axlebox grease performance class A |
| EN | 12082 | Railway axlebox grease performance class B |
| AAR | M-942 | North American railway axlebox grease spec |
| NSF | H1 / H2 / 3H / HT1 | Food-grade registrations |
| NLGI | GC-LB | Automotive wheel-bearing / chassis service classification |

## Hard rules when matching

- **Application match** — must hold the OEM approval for the named equipment OEM/model.
- **NLGI grade** — must match exactly for sealed-for-life bearings; ±1 grade acceptable for relubricated low-load service.
- **Base-oil ISO VG** — ±1 grade acceptable if all other axes match; for high-DN bearings prefer same or lower.
- **Thickener type** — prefer the **same** thickener family; cross-check the ExxonMobil Generic Compatibility Chart in `sop-flow.md` when thickener family changes. Remove Incompatible (I) candidates.
- **Performance envelope** — must meet or exceed every claim on the incumbent PDS (dropping point, water washout, EP weld, copper corrosion, NSF H1 if required).
- **Speed factor** — if DN or NDm is known from §2a intake, calculate it and confirm the candidate is rated for that speed class.
- **Food-grade** — NSF H1 registration number mandatory on PDS for incidental food contact. No exceptions.
- **Always purge** — even when the chart says Compatible, always purge out the old grease before applying the new one.