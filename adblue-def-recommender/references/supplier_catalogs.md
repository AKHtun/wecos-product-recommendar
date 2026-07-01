# AdBlue / DEF Supplier Catalog Reference

The DLE agent must let the DSR choose which supplier catalogs to search. The
list below is a *starting* set, not a hardcoded scope — accept any blender or
OEM-branded AdBlue / DEF the DSR names and apply the same PDS / SDS / COA
workflow.

Always prefer the manufacturer's own domain. Reject blogs, distributor
rebrands, and resellers as primary sources. The two regulator-blessed markers
that *must* be on the product page (or in the candidate PDS) are:

- **VDA AdBlue trademark licence** — for any product sold under the AdBlue
  name in EMEA / APAC (search the VDA producer list at vda.de).
- **API Diesel Exhaust Fluid Certification mark** — for any product sold as
  DEF in North America (search the API certified-producers list at
  api.org/DEF).

## Tier-1 majors

| Supplier | Primary domain(s) | Core brand(s) | Region |
|---|---|---|---|
| Yara International | yara.com, air1.com | Air1 AdBlue / DEF | Global; the world's largest AdBlue producer (after acquiring the LaRoche / Qafco assets). |
| BASF | basf.com | AdBlue (BASF) | Global; Tier-1 VDA-licensed. |
| CF Industries | cfindustries.com | DEF (CF Industries), AdBlue (Europe) | North America (largest US producer); global exports. |
| Mitsui Chemicals | mitsuichemicals.com | AdBlue / DEF | Japan, APAC. |
| Borealis | borealisgroup.com | Borstar-class AdBlue | EMEA; some APAC. |
| SK Chemicals | sk.com / SK Geo Centric | SK AdBlue | Korea, APAC. |
| Nissan Chemical | nissanchem.co.jp | AdBlue (Japan) | Japan domestic + APAC export. |
| GreenChem | greenchem-adblue.com | GreenChem AdBlue | EMEA (smaller blender, often bulk supply). |
| Royal Den Hartog | royaldh.com | AdBlue / DEF | Europe / US. |
| Yara Marine Technologies | yara.com/technologies/marine | Yara Marine SCR-grade AdBlue | Marine SCR (IMO Tier III ECA). |
| TotalEnergies | totalenergies.com | TotalEnergies AdBlue / DEF | EMEA. |
| Shell | shell.com | Shell AdBlue / Shell DEF | EMEA, APAC, Americas. |
| ExxonMobil | mobil.com, exxonmobil.com | Mobil AdBlue / DEF | Americas, EMEA. |
| Castrol / BP | castrol.com, bp.com | Castrol DEF, BP AdBlue / DEF | Global. |
| PetroChina (Kunlun) | kunlun-lub.com / petrochina.com.cn | AdBlue (China GB 29518) | China domestic; some export. |
| Sinopec | sinopec.com | AdBlue (China GB 29518) | China domestic; some export. |
| Idemitsu | idemitsu.com | AdBlue (Japan JIS K 2247) | Japan. |
| ENEOS | eneos.co.jp | AdBlue | Japan. |

## Local / regional blenders (accept on request)

| Supplier | Region |
|---|---|
| Yara / Borealis joint ventures (Yara-Sluiskil, Yara-Brunsbüttel) | Europe |
| Kemetyl | Europe (Scandinavia) |
| AD-IT / AlgoChim | Europe (France, Belgium) |
| Adril / Lubrilog | Europe (Spain, Portugal) |
| ADGas / Dieseltec | Latin America (Argentina, Chile) |
| Orica (Australia) | Australia / Pacific |
| Incitec Pivot | Australia |
| Pertamax / Pertamina (Indonesia) | Indonesia |
| Petron Malaysia | Malaysia |

> If the DSR names a blender not on this list, treat the candidate the same
> way: require ISO 22241 part 1 / 2 / 3 / 4 conformance, the appropriate
> regional regulator mark, and explicit OEM approval coverage.

## Search patterns that work well

Use these in `WebFetch` / `firecrawl-search`:

```
"<product name>" PDS site:<supplier-domain>
"<product name>" "technical data sheet" filetype:pdf
"<product name>" AdBlue DEF SDS filetype:pdf
"<supplier>" AdBlue "Certificate of Analysis" filetype:pdf
"Air1" OR "AdBlue" "ISO 22241" certificate filetype:pdf
"<OEM>" "<model>" "AdBlue approval" OR "DEF specification" filetype:pdf
VDA AdBlue licensed producers list
API DEF certified producers list api.org/DEF
```

## OEM-approval quick reference

| OEM family | Where to look | What to check |
|---|---|---|
| Mercedes-Benz trucks (Actros, Antos, Arocs) | bevo.mercedes-benz.com → operating fluids | MB-Approval 325.5 / .6 for AdBlue / DEF |
| VW Group commercial (MAN, Scania) | MAN / Scania service portals | Cross-listed with VDA AdBlue producer list |
| Volvo / Renault Trucks | volvotrucks.com → fluids / impact portal | Volvo STD 417-0001 |
| Iveco / FPT | iveco.com → operating fluids | Cross-listed with VDA AdBlue producer list |
| DAF / PACCAR | daf.com → operating fluids | Cross-listed with VDA AdBlue producer list |
| Cummins (ISB, ISX, X12, X15, L9) | cummins.com → fluids & lubricants | Cummins SB-3-A005 / CES 14603 |
| Detroit Diesel (DD13, DD15, DD16) | Detroit Diesel service portal | 93K217 spec sheet |
| Caterpillar (C13, C15, C18 ACERT marine / gen-set) | cat.com → SEBU6250 fluids reference | Caterpillar SCR-fluids list |
| Marine SCR (Hug Engineering, Yara Marine, Wärtsilä PureNOx) | Class-society databases (DNV, Lloyd's, ABS, BV) | Type approval certificate |
| Passenger-car SCR (VW BlueMotion, MB BlueTec, PSA BlueHDi, FCA, Hyundai-Kia, GM Duramax) | OEM service portals | Cross-listed with VDA AdBlue producer list |

## Regulator-published certified-producer lists (authoritative for fallback)

| Region | List | URL pattern |
|---|---|---|
| EMEA / APAC (AdBlue trademark) | VDA AdBlue licensed producers | https://www.vda.de/en/topics/innovation-and-technology/adblue (look for "AdBlue licensed producers") |
| North America (DEF certification mark) | API certified DEF producers | https://www.api.org/DEF (or search "API Diesel Exhaust Fluid Certification program") |
| Brazil (ARLA 32) | ANP / Inmetro | https://www.gov.br/anp / https://www.inmetro.gov.br |
| Japan | JIS K 2247 producer list | JIS database |
| China | GB 29518-2013 (urea AUS 32) | SAC database |

## ISO 22241 quick reference (use to spot-check any candidate)

| Property | Min | Max | Field tool? |
|---|---|---|---|
| Urea concentration (% w/w) | 31.8 | 33.2 | Refractometer (correlates to RI) |
| Density @ 20 °C (g/cm³) | 1.087 | 1.093 | Hydrometer |
| Refractive index @ 20 °C | 1.381 | 1.384 | Refractometer (fast field check) |
| Alkalinity as NH3 (%) | — | 0.2 | Lab |
| Biuret (%) | — | 0.3 | Lab |
| Aldehydes (mg/kg) | — | 5 | Lab |
| Phosphate (mg/kg) | — | 0.5 | Lab |
| Individual metals Ca / Fe / Na / K / Cu / Zn / Cr / Ni / Al / Mg (each, mg/kg) | — | 0.5 | ICP-OES lab |
| Sum of metals (mg/kg) | — | 1.0 | ICP-OES lab |
| Insolubles (mg/kg) | — | 20 | Lab |

## Storage & shelf-life quick reference

| Storage temperature | Expected shelf-life |
|---|---|
| ≤ 25 °C | 36 months from manufacture |
| 25 – 30 °C | 24 months |
| 30 – 35 °C | 12 months |
| > 35 °C | Rapid hydrolysis — do **not** store |

> DEF freezes at –11 °C; thawing does not harm the chemistry **provided** the
> fluid is still in spec. Always check refractometer / density after thaw
> before use.

## Container / packaging quick reference

| Format | Typical use | Notes |
|---|---|---|
| 10 L can | Workshop top-up / first fill | Retail / garage shelf. |
| 200 L drum | Small fleet | HDPE; sealed cap; check lot number. |
| 1000 L IBC | Mid-size fleet / depot | HDPE cage + pallet; check bottom valve for contamination. |
| Bulk tanker | National distributor / depots | Stainless or HDPE-lined; dedicated DEF hoses. |

## Hard rules when matching

- ISO 22241 part 1 / 2 / 3 / 4 conformance — **mandatory**.
- API DEF mark — **mandatory** for North American sales.
- VDA AdBlue trademark licence — **mandatory** for EMEA / APAC sales under the AdBlue name.
- OEM approval list — must be **explicitly listed** in the candidate PDS, not inferred.
- Density / refractive index must fall in ISO 22241 band; flag any candidate PDS that does not publish these.
- Shelf-life claim must be ≥ 12 months at the customer's expected storage temperature.