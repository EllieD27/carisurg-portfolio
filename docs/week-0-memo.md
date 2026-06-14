# Week 0 Memo — Clinical Triage Data: Exploratory Analysis

**Programme:** CariSurg MedTech Pathways 2026  
**Project:** Mercer General Hospital — Emergency Department Triage  
**Author:** Eliana Dookhoo  
**Dataset:** `EmergencyTriageDataset_Reduced_Dirty.csv`

---

## Overview

This memo documents all Week 0 deliverables across six days. The work focused on cleaning and exploring Mercer General's Emergency Department triage dataset, producing clinical visualisations, and designing a prototype digital triage model. The full analysis code is available in `notebooks/week-0`.

---

## Day 1 — Gender Column Cleaning

### Objective
Standardise inconsistent entries in the **Gender** column to ensure accuracy and consistency across the dataset.

### What Was Done
The dataset initially contained six inconsistent categories for patient gender. These were reviewed, cleaned, and consolidated into two clearly defined categories:

| Label | Encoded Value |
|-------|--------------|
| Male | 1 |
| Female | 0 |

### Tasks Performed
- Loaded dataset using Pandas
- Inspected dirty gender values
- Standardised inconsistent text entries
- Encoded cleaned values numerically
- Verified cleaned dataset output

### Technologies Used
Python · Google Colab · Pandas

---

## Day 2 — Pulse Column Cleaning

### Objective
Clean the **Pulse** column to ensure proper representation of all pulse values in the dataset.

### What Was Done
The process began with practice on the GCS dataset to establish familiarity with the general cleaning workflow, particularly the use of median imputation for skewed data.

For the Pulse column:
- A valid pulse range of **20 to 250 bpm** was established
- Logical masks (`df.loc`) were used to identify values outside this boundary
- Unrealistic values were replaced with `NaN` placeholders
- The **median** was selected as the most appropriate imputation method, given the presence of outliers even at the extreme minimum and maximum values
- A visualisation graph was produced to aid interpretability

### Tasks Performed
- Explored Pulse column values
- Counted unique and frequent entries
- Converted invalid values to numeric format
- Applied logical masking using `df.loc`
- Replaced impossible values with `NaN`
- Imputed missing values using the median
- Visualised cleaned Pulse data

### Final Result
The resulting dataset achieved a final `NaN` count of **0** after successful median imputation. The Pulse column was fully cleaned and prepared for statistical analysis, visualisation, and machine learning workflows.

### Technologies Used
Python · Google Colab · Pandas · NumPy · Matplotlib

---

## Day 3 — Clinical Visualisations

### Objective
Derive clinically meaningful plots from the Emergency Triage Dataset to support clinical interpretation.

---

### Plot 1 — Scatter Plot: DBP vs Age

**Clinical question:** Do older patients tend to present with higher or lower diastolic blood pressure (DBP) in the Mercer General ED dataset?

- Compares patient age against diastolic blood pressure
- A reference line was added at `DBP = 80 mmHg` to indicate the average adult diastolic blood pressure
- The plot helps identify trends, clustering, and possible outliers across age groups

**Key finding:** Younger patients show a wider, lighter distribution. The heaviest cluster appears between ages 65–90 with DBP between 50–80 mmHg, suggesting that older patients tend to present with diastolic blood pressure below 80 mmHg — indicating increased susceptibility to cardiovascular risk.

*(See: `docs/images/dbp_vs_age.png`)*

---

### Plot 2 — Histogram: Distribution of Pulse Values

**Clinical question:** What is the distribution of pulse rates among patients in the Mercer General ED dataset?

- Shows how pulse values are distributed across the cleaned dataset
- Clinical reference lines added at:
  - `60 bpm` — lower boundary of normal heart rate
  - `100 bpm` — upper boundary of normal heart rate
  - Danger zones indicated for **Bradycardia** (<60 bpm) and **Tachycardia** (>100 bpm)

*(See: `docs/images/pulse_histogram.png`)*

---

### Plot 3 — Scatter Plot: DBP vs Pulse

**Clinical question:** Do patients with lower diastolic blood pressure tend to present with elevated pulse rates suggesting physiological stress or compensation?

- Compares diastolic blood pressure against pulse rate
- Clinical reference lines added at:
  - `Lower Pulse Limit = 60 bpm`
  - `Upper Pulse Limit = 100 bpm`
  - `Normal Adult DBP = 80 mmHg`
- Thresholds highlight a potential clinical review zone for patients susceptible to heart failure or cardiovascular disease

*(See: `docs/images/dbp_vs_pulse.png`)*

---

### Clinical Considerations
- `DBP < 80 mmHg` may suggest hypotension or reduced perfusion
- `Pulse > 100 bpm` may suggest tachycardia
- Abnormal values were not automatically treated as errors — ED patients may present with genuinely abnormal vital signs

---

## Day 4 — Vital Sign Overview: Heart Rate

### Definition
Heart rate is the number of times a person's heart contracts and beats per minute (bpm). The heart beats to supply oxygen throughout the body, adapting its rate based on the body's needs at any given moment. This behaviour can provide critical information about cardiovascular function and overall physiological condition.

Heart rate is measured by locating the pulse — the arterial pulsation transmitted to the skin surface at points of compression. Common pulse sites include the temporal artery (forehead), facial artery (jaw), carotid artery (neck), and radial artery (wrist).

### Normal Ranges
| Category | Pulse Range |
|----------|-------------|
| Normal adult | 60–100 bpm |
| Bradycardia | < 60 bpm |
| Tachycardia | > 100 bpm |

### Clinical Relevance to Triage
Heart rate is one of the primary vital signs used in triage to identify patients experiencing stress, shock, infection, and other critical conditions requiring immediate care.

*Reference: Mandal, A. (2023). What is Heart Rate? News Medical Life Sciences. https://www.news-medical.net/health/What-is-Heart-Rate.aspx*

---

## Day 5 — Vital Sign Overview: Cholesterol

### Definition
Cholesterol is a type of fat found in the blood, primarily produced by the liver. It serves important functions including hormone production and vitamin D synthesis.

### Key Components

| Component | Role |
|-----------|------|
| HDL (High-Density Lipoprotein) — "good cholesterol" | Carries excess cholesterol away from the blood back to the liver for breakdown; protective of heart and vessels |
| LDL (Low-Density Lipoprotein) — "bad cholesterol" | When elevated, can accumulate in blood vessels and contribute to stroke, heart disease, and dementia |
| Total Cholesterol | Combined HDL and LDL measurement |

### Normal Ranges
Cholesterol is measured in milligrams per decilitre (mg/dL). The desirable total cholesterol level is less than **200 mg/dL**. Higher values indicate increased risk of heart disease and stroke.

### Clinical Relevance to Triage
Abnormal cholesterol levels are not typically treated as an acute emergency, but provide important background information about a patient's long-term cardiovascular risk and overall health status.

*Reference: Alzheimer's Research UK. Cholesterol and Dementia Risk. https://www.alzheimersresearchuk.org/dementia-information/dementia-risk/cholesterol-and-dementia-risk/*

---

## Day 6 — Digital Triage Model: Pseudocode and System Design

### Objective
Design a pseudocode model describing how a digital triaging system would work and how patients are categorised into respective risk levels.

---

## ED Triage Pseudocode Attempt and System Explanation: 

START

Receive patient data:
   - Age
   - Temperature
   - Pulse
   - Blood Pressure
   - Respiratory Rate
   - Oxygen Saturation
   - GCS Score
   - Reported Symptoms

Check for missing or invalid data
   IF critical data is missing:
       Flag patient for manual nurse review

Evaluate vital signs against clinical thresholds

IF:
   GCS <= 8
   OR Oxygen Saturation < 90
   OR Pulse > 130
   OR Systolic BP < 90
THEN:
   Assign Risk Level = CRITICAL

ELSE IF:
   Temperature >= 38
   OR Pulse > 100
   OR DBP < 60
THEN:
   Assign Risk Level = HIGH

ELSE IF:
   Mildly abnormal vitals detected
THEN:
   Assign Risk Level = MODERATE

ELSE:
   Assign Risk Level = LOW
Store patient results in database

Send triage category to ED dashboard

END

## System Explanation 

The proposed digital triaging system is designed to assist emergency department staff by rapidly processing patient information and assigning a clinical risk category. The system begins by collecting patient demographic information and vital signs, including temperature, pulse, blood pressure, oxygen saturation, respiratory rate, and Glasgow Coma Scale (GCS) score. These measurements are commonly used during emergency department triage to assess patient stability and urgency of care.
Once the patient data is received, the system information is validated and cleaned to identify and rectify missing or abnormal entries. If critical information is unavailable, the patient is flagged for direct nurse review to reduce the risk of incorrect automated categorisation.
The system then compares the patient’s vital signs against predefined clinical thresholds. Patients with severely abnormal measurements, such as very low GCS scores, extremely low oxygen saturation, severe hypotension, or dangerously elevated pulse rates, are categorised as critical priority cases requiring immediate medical attention. Patients with moderately abnormal vital signs are categorised into high or moderate risk groups depending on the severity of the findings.
After processing the data, the system assigns a final triage category and stores the information in the hospital database. The assigned risk level can then be displayed on the emergency department dashboard to support nurses and physicians in prioritising patient care efficiently.

---

*Week 0 · CariSurg MedTech Pathways 2026 · Mercer General Hospital Project*