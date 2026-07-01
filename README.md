<div align="center">

# WEcoS Product Recommendar

**A suite of Distributor Lubricant Engineer (DLE) skills for all the
fluid product categories.**

[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/license-PolyForm--Noncommercial--1.0.0-blue.svg)](LICENSE)
[![Author](https://img.shields.io/badge/author-Aung%20Khaing%20Htun%2C%20CLS-orange.svg)](CONTRIBUTORS.md)
[![AI-assisted](https://img.shields.io/badge/AI--assisted-WEcoS%20Agents%20%C2%B7%20MuleRun%20Agent%20%C2%B7%20Mavis-purple.svg)](CONTRIBUTORS.md)
[![Skills](https://img.shields.io/badge/skills-5-green.svg)](#the-five-skills)

</div>

---

## What is this?

WEcoS Product Recommendar is a suite of five Distributor Lubricant
Engineer (DLE) skills that produce equivalent / alternative lubricant,
coolant, diesel, AdBlue/DEF, and grease recommendations for an incumbent
third-party product. It is the cumulative methodology of **Aung Khaing
Htun, CLS** (STLE Certified Lubrication Specialist), refined through
years of in-the-field experience across commercial bus, heavy-duty
truck, mining, marine, and general industrial applications.

The skills are designed for two audiences:

- **DSRs (Distributor Sales Representatives)** who need to cross-reference
  a competitor product to the right in-house brand / grade, with a
  defensible technical rationale to share with the end customer.
- **End customers** who need a like-for-like equivalent with verified
  approvals against the latest producer PDS / TDS / SDS.

---

## Why does it exist?

Most DLE workflows suffer from three recurring problems:

1. **Stale specifications.** Lubricant producers regularly consolidate,
   rename, or replace SKUs. A 2022 PDS may still be reachable on a
   distributor mirror, but the producer has already moved on. The
   suite enforces a **mandatory product-currency check** before any
   recommendation.
2. **Single-pick recommendations.** The end-customer often wants to know
   not just the equivalent, but the **upgraded** option — and the
   technical reason. The suite defaults to **Standard + Upgraded**
   output for fleet recommendations.
3. **Thickener / chemistry confusion.** Greases look the same on the
   container but behave very differently in service. The suite
   includes a **DIN 51502 / ISO 6743-9 designation decoder** plus the
   ExxonMobil 7×7 thickener compatibility chart (C / M / I matrix)
   so the recommendation is grounded in chemistry, not brand.

---

## The five skills

| # | Skill | Scope | Skill path |
|---|---|---|---|
| 1 | **lubricant-recommender** | Engine oils, gear oils, hydraulic oils, compressor oils, turbine oils, refrigeration-compressor oils, PAG fluids, heat-transfer fluids | `lubricant-recommender/SKILL.md` |
| 2 | **coolant-recommender** | Engine coolants / antifreeze (light-duty, HD diesel, off-highway, marine, stationary gen-set, OEM concentrates) | `coolant-recommender/SKILL.md` |
| 3 | **diesel-recommender** | ULSD / EN 590, off-road / mining / construction diesel, additized premium diesel, marine distillate fuels (ISO 8217 DMA / DMZ / DMB) | `diesel-recommender/SKILL.md` |
| 4 | **adblue-def-recommender** | AdBlue / DEF / ARLA 32 (ISO 22241 AUS 32 urea solution) for SCR-equipped diesel | `adblue-def-recommender/SKILL.md` |
| 5 | **grease-recommender** | Industrial, automotive, food-grade (NSF H1), marine, mining / heavy-load, electric-motor, refrigeration-compressor, central-lube, railway axlebox, high-temperature | `grease-recommender/SKILL.md` |

---

## Quick start

Each skill is a standalone module with the same entry contract: provide
the incumbent product, application, OEM/model, and operating conditions
(where applicable), and the skill produces a **Standard + Upgraded
recommendation** with verified PDS citations.

### 1. Open a skill

```bash
cd lubricant-recommender        # or any of the other 4
cat SKILL.md                     # read the methodology + hard rules
```

### 2. Drive the skill from a MuleRun / WEcoS Agent session

In any WEcoS Agents / MuleRun Agent session, just say:

> *Recommend a Mobil equivalent for **Shell Rimula R5 E 10W-40** for a
> Euro 5 MAN bus operating in Singapore.*

The agent loads the relevant `SKILL.md`, runs §0b currency check,
fetches the producer's current PDS, applies the six-axis filter,
returns tiered Standard + Upgraded picks, and emits a DSR-ready
business email.

### 3. Read the methodology lineage

For a deep dive on **why** the pipeline is the way it is — the hard
rules, the warning matrix, the tiered output structure, the reference-
ledger integration — read:

- `CONTRIBUTORS.md` — per-skill authorship + 2026 methodology extensions
- `NOTICE` — attribution format + AI-assist credits

---

## Repository structure

```
wecos-product-recommendar/
├── LICENSE                      # PolyForm Noncommercial 1.0.0 (master)
├── NOTICE                       # attribution format + AI-assist credits
├── CONTRIBUTORS.md              # per-skill authorship lineage
├── README.md                    # you are here
├── CONTRIBUTING.md              # how to contribute
├── .gitignore                   # exclude /output, /__pycache__, etc.
│
├── lubricant-recommender/
│   ├── SKILL.md                 # 233 lines, methodology + hard rules
│   ├── LICENSE                  # pointer to ../LICENSE
│   ├── references/              # sop-flow.md, supplier_catalogs.md, etc.
│   ├── scripts/                 # render_pdf.py, append_record.py, ...
│   ├── templates/               # report_template.md, ...
│   ├── output/                  # generated recommendations (gitignored)
│   └── requirements.txt
│
├── coolant-recommender/        # same internal layout
├── diesel-recommender/         # same internal layout
├── adblue-def-recommender/     # same internal layout
└── grease-recommender/         # same internal layout
```

---

## Methodology — high-level

Each skill follows the same spine, with branches for the 10 product-line
scenarios inside `grease-recommender`. The full spine is documented in
each `SKILL.md`; the high-level flow is:

```
User request
   │
   ▼
§0  Hard rules (8 mandatory, no exceptions)
   │
   ▼
§0b Product currency check — confirm SKU is current on producer PDS index
   │
   ▼
§2  Intake — incumbent product, application, OEM, operating conditions
   │
   ▼
§3  Fetch incumbent PDS / TDS / SDS — six attributes + DIN/ISO code
   │
   ▼
§4  Sequential filter — application / base oil / ISO VG / NLGI /
                         thickener / performance + OEM approvals
   │                    (DIN/ISO fallback if no 5+ candidate)
   ▼
§6  Special-case warnings — purge-out-old-grease, base-oil vs NLGI,
                            over-greasing, OEM-specific compatibility,
                            vertical-mount NLGI 3, water exposure, ...
   │
   ▼
§0c Tiered output — Standard Y + Upgraded Y+ with technical rationale
                    (drop point, OEM approval set, drain interval)
   │
   ▼
§7  Deliver — chat report + PDF + Excel row
   │
   ▼
§8  Disclaimer appended verbatim
   │
   ▼
§11 Reference-ledger cross-check (MEM-AUNG-YYYY-NNN format)
   │
   ▼
§11b DSR business email (Gemini-style DDMMYY subject, disclaimer verbatim)
```

---

## Source-material lineage

| Era | Source |
|---|---|
| 2024-2025 | Base pack: T-SOP-002-1 / 002-2 / 002-3 / 002-4 / 002-5 series (MuleRun Fluids Suite starter kit) |
| Jul 2026 | Methodology extensions (current session): §0b currency check, §0c tiered output, §11 reference-ledger integration, §11b DSR business email template |
| Jul 2026 | Customer corrections (this session): §6 warning ordering (over-greasing first), §6 vertical-mount NLGI 3, §6 shelf-life advisory (cite PDS, no hardcoding), §6 always-on purge standard phrase, §10/§11 ledger + email template additions |

AI assistance: **WEcoS Agents · MuleRun Agent · Mavis by MiniMax**
(DLR.1 / Mavis, session #414668884336737, Jul 2026).

See `CONTRIBUTORS.md` for the full per-skill lineage.

---

## License

This suite is licensed under the **PolyForm Noncommercial License 1.0.0**.

You are free to:

- Use the skills for personal study, academic research, internal training,
  individual professional use, evaluation, contribution back to the
  upstream project, and integration into non-commercial open-source
  workflows.
- Copy, modify, and improve the skills (with attribution to the original
  author).
- Contribute back to the upstream project via pull request.

You are **not** free to use the suite for commercial purposes (sale, OEM
integration, paid SaaS deployment, etc.) without a separate written
license. See [Commercial licensing](#commercial-licensing) below.

Canonical license text: [polyformproject.org/licenses/noncommercial/1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0)

---

## Commercial licensing

To use the WEcoS Product Recommendar suite in a commercial product, OEM
deployment, paid SaaS workflow, or any revenue-generating context, open
a GitHub Issue at:

> **[github.com/AKHtun/wecos-product-recommendar/issues](https://github.com/AKHtun/wecos-product-recommendar/issues)**

with the **"Commercial licensing"** issue template and we'll get back
to you within 5 business days.

---

## Contributing

We welcome pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for the
PR template, contribution-license agreement, and review process.

In short:

1. **Fork** the repo
2. **Branch** off `main`
3. **Commit** with a clear message naming the skill + the change
4. **Push** and **open a PR** against `main`
5. **Sign off** your commit (`git commit -s`) agreeing to license your
   contribution under the same PolyForm Noncommercial 1.0.0

---

## Trademarks & acknowledgements

All product names, OEM names, and standards-body names mentioned in this
suite (e.g., Mobil, Shell, Caltex, TotalEnergies, SPC, Volvo, MAN, MB,
Mack, Renault, Scania, DAF, IVECO, MTU, Deutz, Caterpillar, Cummins,
Detroit Diesel, ACEA, API, ISO, EN, NEA, ASTM, DIN, IPOS) are the
property of their respective owners and are used here in their
descriptive sense only. No endorsement or affiliation is implied.

Source-material lineage: ExxonMobil Grease Compatibility Paper
(ASTM D6185); DIN 51502 / ISO 6743-9 designation codes; ACEA / API
service categories; EN 590; ISO 22241; Volvo VDS / VOLVO 97718; etc.

---

## Author

**Aung Khaing Htun, CLS** — sole author of the methodology and the
integrated WEcoS Product Recommendar suite.

- GitHub: [github.com/AKHtun](https://github.com/AKHtun)
- Issue tracker: [github.com/AKHtun/wecos-product-recommendar/issues](https://github.com/AKHtun/wecos-product-recommendar/issues)

---

## License at a glance

| Permission | Status |
|---|---|
| Personal study, academic research, internal training | ✅ Yes |
| Individual professional use | ✅ Yes |
| Contribution back to upstream (PR) | ✅ Yes |
| Modification with attribution | ✅ Yes |
| Commercial use (sale, OEM integration, paid SaaS) | ❌ Requires separate written license — open a GitHub Issue |
| Re-licensing under MIT / Apache / similar permissive license | ❌ No |
| Re-licensing under any closed-source commercial license | ❌ No |

See `LICENSE` for the full legal text.