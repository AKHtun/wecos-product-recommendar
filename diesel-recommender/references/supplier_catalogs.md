# Diesel Fuel Supplier Catalog Reference

The DLE agent must let the DSR choose which supplier catalogs to search. The
list below is a starting set, not a hardcoded scope — accept any supplier or
local refiner the DSR names.

Always prefer the manufacturer's / refiner's own domain.

## Major diesel suppliers

| Supplier | Primary domain(s) | Core diesel brands |
|---|---|---|
| ExxonMobil | mobil.com, exxonmobil.com | Mobil Diesel Efficient, Synergy Diesel Efficient, Mobil Diesel |
| Shell | shell.com | Shell V-Power Diesel, Shell FuelSave Diesel, Shell GTL Fuel, Shell Marine Gasoil |
| Chevron | chevron.com | Chevron Techron Premium Diesel, Chevron Diesel No. 2 |
| Caltex | caltex.com | Caltex Diesel with Techron D, Caltex Premium Diesel |
| Castrol / BP | bp.com, castrol.com | BP Ultimate Diesel, BP Diesel, BP Marine Distillate |
| TotalEnergies | totalenergies.com | Total Excellium Diesel, Total Diesel, Total Marine Fuels |
| Petronas | petronas.com, petronas.com.my | Petronas Dynamic Diesel Euro 5, Petronas Dynamic Diesel Euro 2M |
| Sinopec | sinopec.com | Sinopec Diesel #0 / #-10 / #-20 (China GB 19147) |
| PetroChina | petrochina.com.cn | PetroChina Diesel |
| Idemitsu | idemitsu.com | Idemitsu Diesel (Japan JIS K 2204) |
| ENEOS | eneos.co.jp | ENEOS Diesel (Japan) |
| Reliance | ril.com | HP Power Diesel, BS-VI ULSD |
| Local refiners | refiner domain | Singapore EMA, Malaysia Petronas refineries, Indonesia Pertamina (Dexlite, Pertamina Dex) |

## Sulfur tier quick reference

| Region / Spec | Maximum sulfur | Typical fuel |
|---|---|---|
| EU EN 590 | 10 ppm | Automotive diesel |
| US ASTM D975 S15 | 15 ppm | On-road diesel |
| US ASTM D975 S500 | 500 ppm | Off-road (legacy) |
| Japan JIS K 2204 | 10 ppm | Automotive diesel |
| China GB 19147 (VI) | 10 ppm | Automotive |
| Singapore SS EN 590 | 10 ppm | Automotive |
| Malaysia Euro 5 | 10 ppm | Automotive |
| IMO MARPOL — ECA | 1,000 ppm (0.1 %) | Marine |
| IMO MARPOL — Global | 5,000 ppm (0.5 %) | Marine VLSFO |
| Mining / off-grid (variable) | up to 5,000 ppm | Where permitted only |

## Emission-tier compatibility

| OEM tier | DPF | SCR / DEF | EGR | Max permissible sulfur |
|---|---|---|---|---|
| Euro 6 (on-road) | Yes | Yes | Yes | 10 ppm |
| Euro 5 (on-road) | Yes | Optional | Yes | 10 ppm (best) / 50 ppm legacy |
| Euro 4 | No | No | Yes | 50 ppm |
| EPA Tier 4 Final (off-road) | Yes | Yes | Yes | 15 ppm (ULSD S15) |
| EPA Tier 3 / Interim 4 | Optional | Optional | Yes | 500 ppm permitted on legacy |
| Stage V (EU off-road) | Yes | Yes | Yes | 10 ppm |
| IMO Tier III (marine) | — | Yes (NOx) | — | ECA fuel rules apply |
| IMO Tier II | — | No | — | Global / ECA cap applies |

## Cold-flow grades

| Grade | CFPP target | Typical use |
|---|---|---|
| Summer | -5 °C | Tropical, subtropical |
| Winter | -20 °C | Continental winters |
| Arctic / Class 0–4 | -32 °C to -44 °C | High-latitude winter |
| Kerosene-blended | down to -50 °C | Extreme cold |

## Additized premium diesel — typical claims

| Brand | Claims |
|---|---|
| Shell V-Power Diesel | Detergent, friction modifier, cetane improver, corrosion inhibitor |
| BP Ultimate Diesel | ACTIVE detergent technology, lubricity, cetane improver |
| Total Excellium Diesel | Detergent, anti-corrosion, anti-foam |
| Caltex Diesel with Techron D | Detergent, deposit cleanup, corrosion inhibitor |
| Mobil Diesel Efficient | Detergent, cetane improver, lubricity, anti-foam |
| Petronas Dynamic Diesel | Detergent, lubricity, corrosion inhibitor |

## Standards quick reference

| Spec | Use case |
|---|---|
| EN 590 | EU automotive diesel |
| ASTM D975 | US diesel (Grade 1-D / 2-D, S15 / S500 / S5000) |
| ISO 8217 | Marine fuels (DMA / DMZ / DMB / RMG / RMK) |
| JIS K 2204 | Japan automotive diesel |
| GB 19147 | China automotive diesel |
| SS EN 590 | Singapore automotive diesel |
| AS 3570 | Australia automotive diesel |
| IS 1460 | India diesel (BS-VI) |

## Search patterns

```
"<product>" PDS site:<supplier-domain>
"<product>" "technical data sheet" filetype:pdf
"<refiner>" "<grade>" "Certificate of Analysis" filetype:pdf
"<refiner>" diesel "typical properties" filetype:pdf
EN 590 winter grade CFPP specification
ISO 8217 DMA marine gas oil specification
IMO 2020 ECA sulfur limit
```
