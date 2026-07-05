# Feasibility Memo Outline: AI-Assisted ED Triage Predictive Modelling
**To:** Dr. De Fretias & Emergency Department Board  
**From:** Medical Data Science Lead  
**Date:** July 4, 2026  

## 1. One-Sentence Verdict
We recommend proceeding with model development using the 225-feature Electronic Health Record (EHR) dataset, subject to critical workflow mitigations for systematic triage variance and data sparsity.

## 2. Dataset Executive Summary
* **Cohort Scale:** 55,121 total unique Emergency Department presentation entries.
* **Feature Dimensionality:** 225 clinical and systemic variables (including demographics, vital logs, and chief complaints).
* **Target Label Profile:** Class distribution is heavily centered on ESI level 3 (27,010 records), followed by ESI level 2 (17,924 records), with critical acuity (ESI level 1) making up less than 0.15% of records.

## 3. Top 3 Data Quality Concerns
1. **Severe Chief Complaint Sparsity:** 149 out of 200 diagnostic feature checkmarks (74.5%) exhibit a baseline prevalence lower than 0.5%, implying a severe risk of high dimensionality with minimal statistical signals.
2. **Vital Sign Estimation Noise:** Critical inputs like Respiratory Rate (`triage_vital_rr`) show an identical artificial median of 18 breaths per minute across all 5 acuity classes, showing data entry shortcuts at triage.
3. **Data Completeness Variances:** Systemic missingness signatures in diagnostic variables like fingerstick glucose testing (`triage_glucose`) track selectively against patient acuity rather than random technical faults.

## 4. Top 3 Reasons to Proceed
1. **Strong Predictor Separation Signals:** High-acuity markers such as Oxygen Saturation (`triage_vital_o2`) exhibit robust class variance and direct correlation with critical triage tracking.
2. **Vast Sample Coverage:** A volume of over 55,000 observations provides sufficient sample depth to train neural network architectures safely without sudden validation collapse.
3. **High Clinical Redundancy/Coherence:** Key symptomatic indicator flags (e.g., `cc_chestpain`) automatically capture priority risk vectors—steering almost 60% of associated records safely into urgent ESI 2 categories.

## 5. Algorithmic Guardrails & Caveats
* **Mitigating Demographic Disparities:** Raw data shows structural variance across ethnic categories (e.g., Black cohorts allocated to lower-urgency ESI 4 categories at nearly double the rate of White cohorts). Models will incorporate fairness constraints to avoid reinforcing historical triage disparities.
* **Imputation Limits:** Missing vital signs must be handled using robust column-wise medians bounded strictly by physiological limits (e.g., WHO ETAT guidelines) rather than aggressive standard algorithmic interpolations.