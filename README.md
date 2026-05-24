# carisurg-portfolio

# README — Mercer General Hospital Project

This portfolio is dedicated to the CariSurg MedTech Pathways 2026 Programme, where AI is incorporated into Healthcare.

This repository records all task deliverables from Week 0 (out of 13 weeks).

---

# Day 1 Task

## Objective

This project utilises Python to perfom data cleaning on a given dataset.
The Day 1 task deliverable involves updating the "Gender" column to ensure accuracy and consistency.

Initially, the dataset had inconsistent entries in classifying a patient's gender. 
Therefore, the data was reviewed and cleaned by grouping each gender into 2 distinctive categories instead of 6, which now promotes consistency and better understandibility, especially for the system.

The results of the refined **Gender** column is classified as:
- Male   = 1
- Female = 0

---

## Dataset/Input

**File used:** `EmergencyTriageDataset_Reduced_Dirty.csv`

---

## Subtasks Performed

- Loaded dataset using Pandas
- Inspected dirty gender values
- Uniformized inconsistent text entries
- Encoded cleaned values numerically
- Verified cleaned dataset output

---

## Technologies Used

- Python
- Google Colab
- Pandas

---

## Output

The cleaned dataset now contains standardized numerical gender values suitable for:
- Data analysis
- Machine learning
- Statistical modeling

---

# Day 2 Task

## Objective:
The Day 2 task deliverable involves cleaning the "Pulse" column to ensure proper representation of all pulse values data.

This project focused on continuing foundational data cleaning techniques in Python, specifically working with the **Pulse** column from the same Emergency Department dataset.

The process began with practicing on the GCS dataset to become familiar with the general cleaning workflow, especially the use of median imputation for skewed data.

The Pulse column cleaning process included:
- Inspecting pulse row data
- Checking unique value counts
- Reviewing value frequencies
- Identifying invalid or non-numeric entries

After understanding the dataset structure, non-numeric values were converted into numeric format and a valid pulse range of 20 to 250 was established.

Next, logical masks ( `df.loc` ) were then used to scan the column for values outside the valid boundary, and any unrealistic values were replaced with `NaN` placeholders.

Since the dataset showed signs of outliers through even the extreme minimum and maximum values, the **median** was selected as the most appropriate imputation method.

Finally, a visualization graph was drafted to better observe the cleaned dataset and improve interpretability.
---

## Dataset/Input

**File used:** `EmergencyTriageDataset_Reduced_Dirty.csv`

---

## Tasks Performed

- Explored Pulse column values
- Counted unique and frequent entries
- Converted invalid values to numeric
- Applied logical masking using `df.loc`
- Replaced impossible values with `NaN`
- Imputed missing values using the median
- Visualized cleaned Pulse data

---

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib

---

## Final Result

The resulting dataset achieved a final `NaN` count of **0** after successful median imputation.

The Pulse column was fully cleaned, standardized, and prepared for:
- Statistical analysis
- Visualization
- Machine learning workflows
- Further healthcare data processing

---

# Day 3 Task

## Objective:
The Day 3 task deliverable involves deriving clinical meaningful plots from the given Emergency Triage Dataset
This deliverable consists of 3 plots:

1. ## Scatter Plot: DBP vs Age

- *Clinical question: Do older patients tend to present with higher or lower diastolic blood pressure (DBP) values in the Mercer General ED dataset?*
- This plot compares patient age and diastolic blood pressure.
- A reference line was added at `DBP = 80 mmHg` to indicate the average Diastolic Blood Pressure value.
- The scatter plot helps identify trends, clustering, and possible outliers across different age groups.
- For instance, at early ages, the clusters were lighter and had a wider distribution as opposed to the region between ages 65 to 90 & DBP between 50 and 80, where the heaviest cluster is observed. This shows that as patients get older, their Diastolic Blood Pressure has a tendancy to drop below the 80 ; indicating that they are more prone to *cardiovascular risk.*

<img width="790" height="390" alt="image" src="https://github.com/user-attachments/assets/1b578724-2d5c-482e-8b16-a84b1d620db5" />
dbp_vs_age.png


## Histogram: Distribution of Pulse Values

- *Clinical question: What is the distribution of pulse rates among patients in the Mercer General ED dataset?*
- This plot shows how pulse values are distributed across the cleaned dataset and helps determine common pulse ranges.
- Clinical reference lines was added at `Pulse = 60 bpm` and  `Pulse = 100 bpm` to indicate the normal heart rate range.
- Two (2) other clinical reference lines were added indicating danger ranges: <60 (Bradycardia) and >100 (Tachycardia) respectfully.

<img width="790" height="390" alt="image" src="https://github.com/user-attachments/assets/93c8fbe5-0403-455e-8327-34772e05f4db" />
 pulse_histogram.png
 

3. ## Scatter Plot: DBP vs Pulse

- *Clinical question: Do patients with lower diastolic blood pressure tend to present with elevated pulse rates that may suggest physiological stress or compensation?*
- This plot compares diastolic blood pressure and pulse rate.
- Clinical reference lines were added at:
  - `Lower Pulse Limit = 60 bpm`
  - `Upper Pulse Limit = 100 bpm`
  - `Normal Adult DBP - 80 mmHg`
- These thresholds help highlight patients who may fall into a possible clinical review zone where they can be susceptible to heart failure or cardiovascular diseases.

<img width="790" height="390" alt="image" src="https://github.com/user-attachments/assets/69b630aa-70b7-463f-aa31-4ce596506acb" />
dbp_vs_pulse.png 

The main clinical considerations included:

- `DBP < 80 mmHg` may suggest hypotension or reduced perfusion.
- `Pulse > 100 bpm` may suggest tachycardia.
- Scatter plots were used to explore possible relationships between variables such as age, DBP, and pulse.
- Histograms were used to visualise the distribution of individual vital signs.

Abnormal values were not automatically treated as errors because emergency department patients may present with genuinely abnormal vital signs.

# Submission Evidence

The repository includes:

- Evidence that the required histogram and scatter plots were successfully produced
- Clinical annotations and reference lines included in the visualisations
- Saved plot images generated from the notebook


## Author:

Eliana Dookhoo
