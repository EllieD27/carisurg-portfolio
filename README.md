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


## Author:

Eliana Dookhoo
