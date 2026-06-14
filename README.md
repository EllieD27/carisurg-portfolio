# carisurg-portfolio

> A clinical data portfolio tracking the application of AI and data analysis to surgical triage and emergency care.  
> **Programme:** CariSurg MedTech Pathways 2026 · Mercer General Hospital  
> **Audience:** Clinical reviewers — no coding knowledge required.

---

## What Is This?

This repository is a structured record of weekly clinical data work. Each week produces two outputs: a **notebook** (the analysis) and a **memo** (the plain-English summary of findings). You do not need to open the notebook to understand the conclusions — the memo is written for you.

---

## Contents at a Glance

| Week | Notebook | Memo | Topic |
|------|----------|------|-------|
| 0 | [`notebooks/week-0`](notebooks/) | [`docs/week-0-memo.md`](docs/week-0-memo.md) | Clinical triage data — exploratory analysis, visualisations & triage model design |
| 1 | [`docs/week-1-memo.md`](docs/) | AI-assisted emergency triage |

---

## Where to Start

**If you are a clinical reviewer, start here:**

1. **Week 0 Memo** → `docs/week-0-memo.md`  
   Covers six days of work: data cleaning, clinical visualisations, vital sign overviews, and a prototype digital triage model. No code, no jargon.

2. **Week 1 Memo** → `docs/week-1-memo.md`  
   A structured review of AI-assisted triage in emergency settings — what the evidence suggests and what the limitations are.

The notebooks in `notebooks/` contain the underlying analysis for those who wish to inspect the methodology.

---

## Folder Structure

```
carisurg-portfolio/
├── notebooks/        # Jupyter notebooks — the analysis work
├── docs/             # Memos, proposals, and reports — start here
│   └── images/       # Plot images and screenshots
├── data/             # Raw and cleaned datasets
├── src/              # Reusable code modules (added from Week 8)
├── README.md         # This file — the front door
├── LICENSE           # Terms of use
├── .gitignore        # Files Git does not track
└── requirements.txt  # Exact software versions used
```

---

## How to Read the Memos

Each memo follows the same structure:

- **Background** — why this question matters clinically
- **What the data shows** — key findings in plain language
- **Limitations** — what the analysis cannot tell us
- **Recommendation** — a clear, actionable conclusion

---

## A Note on the Data

All data used in this portfolio is either publicly available or fully anonymised in accordance with NHS information governance standards. No patient-identifiable information is stored in this repository.

---

## Questions?

If anything is unclear or you would like to discuss the findings, please raise an issue via the **Issues** tab at the top of this page, or get in touch directly.
