# Handover Document — CariSurg Triage Model
*Draft outline — Week 8 Interim Submission. Final version due Tuesday.*

## 1. Project Summary
*(one paragraph — what it does, for whom)*
> This project trains and evaluates ED triage-severity (ESI) classification models on the Yale
> EMMLC dataset (55,121 encounters), for Mercer General Hospital's Clinical AI & Innovation Unit.
> The goal is a passive decision-support tool that flags likely ESI-1 (immediate resuscitation)
> patients alongside nurse triage assessment, addressing the extreme class imbalance (0.14% of
> encounters) that causes standard models to miss critical patients entirely.

## 2. Final-Model Decision
*(which model won + one sentence on why — no hedging)*
> **We ship Random Forest + ESI-1 threshold tuning for Phase 3.** It raises ESI-1 Recall from
> 0.500 (baseline) to 0.750 — 12 of 16 critical patients caught vs 8 of 16 — at Medium
> interpretability and a training/inference cost Mercer General's infrastructure can absorb.
>
> Full reasoning: [`docs/decisions/2026-week-7-decision-journal.pdf`](docs/decisions/2026-week-7-decision-journal.pdf)
> Full audit table: [`docs/model-selection.md`](docs/model-selection.md)

## 3. How to Run
```bash
git clone <repo-url>
cd carisurg-triage
pip install -r requirements.txt
python scripts/train.py --config config.yaml
```
*(TODO: pin exact library versions in requirements.txt before final submission — see Task 1, "Get all versions of libraries used")*

## 4. Where the Data Lives
- File: `data/yaleemmlc_admissionprediction_triage.csv` (git-ignored — not committed to the repo)
- Governance: de-identified Yale New Haven Hospital data — **de-identified does not mean
  ungoverned.** Must not be redistributed outside the CariSurg MedTech Pathways programme.
  Access restricted to programme students and tutors.
- *(TODO before final: confirm and state exact access/storage policy with programme admin)*

## 5. Known Limitations
*(3 honest, specific bullets — not performatively humble)*
- **Single-site data → distribution shift likely.** All results are from a US academic hospital
  (Yale New Haven); Mercer General's patient population (higher dengue/NCD burden, different
  arrival patterns) has not yet been validated against this model (Yang et al., 2024).
- **ESI-1 recall (0.750) is support, not replace.** 4 of 16 critical patients in the test set are
  still missed — this must remain a passive decision-support signal alongside nurse judgement,
  never an autonomous triage decision.
- **Demographic features excluded by design (fairness).** Race, ethnicity, gender, etc. are not
  used as model inputs, given the Week 5 documented triage-allocation disparity — this protects
  against a specific bias pathway but has not been validated as sufficient on its own.

## 6. Who to Ask
*(TODO before final: names/contacts for model, data, and clinical questions)*
- Model/code questions: Eliana Dookhoo (student author)
- Data governance: Martina Griffith, Clinical IT Lead
- Clinical interpretation: Dr. De Freitas, ED Board

---
*This content also seeds README.md — see Tutorial 4, "one page, this content also seeds your README."*
