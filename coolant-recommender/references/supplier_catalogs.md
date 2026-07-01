# Coolant Supplier Catalog Reference

The DLE agent must let the DSR choose which supplier catalogs to search. The
list below is a starting set, not a hardcoded scope — accept any supplier the
DSR names.

Always prefer the manufacturer's own domain.

## Major coolant suppliers

| Supplier | Primary domain(s) | Core brands |
|---|---|---|
| ExxonMobil | mobil.com, exxonmobil.com | Mobil Antifreeze / Mobil Delvac ELC |
| Shell | shell.com | Shell Rotella ELC, Shell Premium Antifreeze |
| Chevron / Caltex | chevron.com, caltex.com, havoline.com | Havoline XLC, Havoline Universal Extended Life |
| Castrol / BP | castrol.com, bp.com | Castrol Radicool SF / NF, BP Antifreeze |
| TotalEnergies | totalenergies.com | Total Coolelf, Total Glacelf |
| Prestone | prestone.com | Prestone Command HD, Prestone All-Vehicle |
| Old World Industries | owipg.com | Peak, Final Charge, Fleet Charge, Sierra |
| Valvoline | valvolineglobal.com | Zerex G05, Zerex G40, Zerex HD ELC |
| BASF | basf.com | Glysantin G30, G40, G48, G64, G65 |
| Cummins | cummins.com | Fleetguard ES Compleat, OAT ELC |
| OEM concentrates | manufacturer domains | MB Anticorrosion/Antifreeze, VW G12/G13, Volvo VCS, Caterpillar ELC, MAN coolant, MTU MTL 5048 |

## Coolant technology decoder

| Tag | Full name | Inhibitor signature | Typical colours | Service life | Notes |
|---|---|---|---|---|---|
| **IAT** | Inorganic Acid Technology | silicate + borate + nitrite + phosphate | Green, blue | 2 years / 30,000 mi | Legacy. Compatible with older cast-iron / brass systems. |
| **OAT** | Organic Acid Technology | 2-EHA / sebacate, no silicate/phosphate | Orange, red, pink | 5 years / 150,000 mi | VW G12, GM Dex-Cool, Toyota SLLC. |
| **HOAT** | Hybrid OAT | OAT + silicate (no phosphate) | Yellow, turquoise | 5 years / 150,000 mi | VW G05, MB 325.0/.3, Volvo VCS. |
| **NOAT** | NAP-Free OAT (Nitrite-Free) | OAT + nitrite, no silicate / amine / phosphate | Pink, red | 600,000 mi / 12,000 h (HD) | Cummins ES Compleat, Caterpillar ELC. |
| **Si-OAT** | Silicate-fortified OAT | OAT + silicate, no phosphate | Purple / violet | 5 years / 250,000 km | VW G12++ / G13, MB 325.5/.6. |
| **P-OAT** | Phosphate OAT | OAT + phosphate | Pink, blue, red | 5 years | Asian OEMs (Toyota, Honda) when low-silicate is required. |
| **PSI-OAT** | Phosphate + Silicate OAT | OAT + phosphate + silicate | Pink, purple | 5 years | Hyundai / Kia. |

## OEM coolant specification quick reference

| OEM | Spec family | Approved coolant family |
|---|---|---|
| Mercedes-Benz | MB 325.0 / .3 / .5 / .6 | HOAT (G05), Si-OAT (G12++/G13) |
| VW / Audi | TL 774-C (G11), -D/F (G12/G12+), -G (G12++/G13), -J (Si-OAT) | Si-OAT preferred current |
| Volvo Trucks | Volvo VCS / Volvo 1286083 | NOAT extended-life |
| Cummins | CES 14439 (fully formulated) / CES 14603 (ELC OAT) | NOAT |
| Detroit Diesel | Power Cool / Power Cool Plus (7SE-298) | NOAT / OAT |
| Caterpillar | EC-1 (ELC) | NOAT |
| MAN | MAN 324 NF, Si-OAT, Typ NF | NOAT, Si-OAT |
| MTU | MTL 5048 | NOAT |
| Deutz | DQC CB-14 | NOAT/HOAT |
| Toyota | SLLC | P-OAT |
| Hyundai / Kia | MS591-08 | PSI-OAT |

## ASTM / international quick reference

| Spec | Use case |
|---|---|
| ASTM D3306 | Light-duty automotive ethylene-glycol antifreeze |
| ASTM D4985 | Heavy-duty diesel pre-charge (low-silicate) |
| ASTM D6210 | Heavy-duty diesel fully formulated |
| ASTM D6211 | Heavy-duty diesel concentrate |
| BS 6580 | UK automotive |
| JIS K 2234 | Japanese spec |
| SAE J1034 / J1941 / J814 | Performance standards |

## Search patterns

```
"<product>" PDS site:<supplier-domain>
"<product>" "technical data sheet" filetype:pdf
"<product>" coolant antifreeze SDS filetype:pdf
"<OEM>" "<model>" "coolant specification" filetype:pdf
VW TL 774 approved coolants list
Cummins CES 14603 approved coolants list
```
