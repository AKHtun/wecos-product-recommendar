# Supplier Catalog Reference

The DLE agent must let the DSR choose which supplier catalogs to search. The
list below is a *starting* set, not a hardcoded scope — accept any supplier the
DSR names and apply the same PDS/SDS workflow.

Always prefer the manufacturer's own domain. Reject blogs, distributor
rebrands, and resellers as primary sources.

## Tier-1 majors

| Supplier | Primary domain(s) | Product-finder / equivalents URL | PDS naming convention |
|---|---|---|---|
| ExxonMobil | mobil.com, exxonmobil.com | https://www.mobil.com/en/lubricants/for-businesses/product-cross-reference | "Mobil <product> Product Data Sheet" |
| Shell | shell.com | https://www.shell.com/business-customers/lubricants-for-business/lubematch.html | "<product> Technical Data Sheet" |
| Chevron / Caltex | chevronlubricants.com, caltex.com | https://www.chevronlubricants.com/en_us/home/products-services/product-finder.html | "Chevron <product> Product Data Sheet" |
| Castrol | castrol.com | https://www.castrol.com/en/global/home/lubricants/product-search.html | "Castrol <product> Technical Data Sheet" |
| TotalEnergies | totalenergies.com, lubricants.totalenergies.com | https://lubricants.totalenergies.com/business/product-finder | "<product> Technical Data Sheet" |

## Tier-2 / regional (accept on request)

| Supplier | Primary domain |
|---|---|
| BP | bp.com |
| Fuchs | fuchs.com |
| Petronas Lubricants | pli-petronas.com |
| Idemitsu | idemitsu.com |
| Eni / Agip | eni.com |
| Repsol | repsol.com |
| Sinopec Lubricant | lubricant.sinopec.com |
| PetroChina (Kunlun) | kunlun-lub.com |
| Phillips 66 / Conoco / 76 | phillips66lubricants.com |
| Valvoline | valvolineglobal.com |
| Pennzoil / Quaker State | pennzoil.com, quakerstate.com |
| Klüber Lubrication (specialty / grease) | klueber.com |
| Mobil Industrial / Mobilgrease specialty pages | mobil.com |

## Search patterns that work well

Use these in `WebFetch` / `firecrawl-search`:

```
"<product name>" PDS site:<supplier-domain>
"<product name>" "technical data sheet" filetype:pdf
"<product name>" SDS filetype:pdf
"<product name>" cross reference equivalents
<OEM> <model> "approved lubricants" filetype:pdf
<OEM> <model> "service manual" lubricant specification
```

## OEM lubricant specification pages

| OEM | Approvals chart / where to look |
|---|---|
| Mercedes-Benz | bevo.mercedes-benz.com |
| MAN | man-engines.com → lubricant approval list (MAN 270, 271, 3477, 3677, etc.) |
| Volvo | volvotrucks.com → Volvo VDS-4.5 / VDS-5 |
| Cummins | cumminsfiltration.com → CES specifications (CES 20086, 20092, etc.) |
| Caterpillar | cat.com → SEBU6250 fluids reference |
| Allison | allisontransmission.com → TES 295 / TES 668 list |
| ZF | zf.com → TE-ML approval lists |
| JCB | jcb.com |
| Deutz | deutz.com → DQC oil quality classes |
| Renault Trucks | renault-trucks.com → RLD-3, RLD-4 |

## Industry-standards quick reference

| Body | Common spec families |
|---|---|
| API | Service (SP/SN/CK-4/CJ-4/FA-4), Gear (GL-4/GL-5/MT-1) |
| ACEA | A/B (gasoline/diesel light-duty), C (catalyst-compatible), E (heavy-duty) |
| ISO | VG (industrial visc grade), 11158 hydraulic, 6743 lubricant classification |
| DIN | 51524 hydraulic (HL/HLP/HVLP), 51517 gear (CLP) |
| AGMA | 9005 industrial gear lubricants |
| JASO | MA / MA2 / MB (motorcycle), DH-1 / DH-2 (HD diesel Japan) |
| NLGI | Grease consistency 000–6 |
| NSF | H1 (incidental food contact), H2, 3H |
| SAE | J300 engine viscosity, J306 gear viscosity |
