# carisurg-portfolio

> A clinical data portfolio tracking the application of AI and data analysis to surgical triage and emergency care.  
> **Programme:** CariSurg MedTech Pathways 2026 · Mercer General Hospital  
> **Audience:** Clinical reviewers — no coding knowledge required.

---

## What Is This?

This repository is a structured record of weekly clinical data work. Each week produces two outputs: a **notebook** (the analysis) and a **memo** (the plain-English summary of findings). You do not need to open the notebook to understand the conclusions — the memo is written for you.

---
## How to Use This Repository

**For clinical reviewers — no installation needed:**
1. Click any memo link in the table above
2. Read the memo directly in your browser — no coding knowledge required
3. Plot images are saved in `docs/images/` if you wish to view them separately

**For technical reviewers — to run the notebooks locally:**
1. Clone the repository:
```bash
   git clone https://github.com/EllieD27/carisurg-portfolio.git
```
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Open the relevant notebook in `notebooks/` using Jupyter or Google Colab and run each cell sequentially
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

## A Note on the Data

All data used in this portfolio is either publicly available or fully anonymised in accordance with NHS information governance standards. No patient-identifiable information is stored in this repository.

---

## Questions?

If anything is unclear or you would like to discuss the findings, please raise an issue via the **Issues** tab at the top of this page, or get in touch directly.
