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


---

# Day 4 Task

## Objective
The Day 4 task deliverable involves writing a summarized description of chosen vital sign: Heart Rate:

## Heart Rate

According to `Dr. Mandal (2023)`, the heart rate is defined as *the number of times a person’s heart contracts and beats per minute (bpm).* The heart essentially beats to supply oxygen throughout the whole body. Based on the need for oxygen in each situation or state, the heart rate would adapt to suit. The heart’s beating behaviour can provide critical information about the cardiovascular function and also overall psychological condition. 
Heart rate is usually measured by finding the pulse in the body. This pulse rate is felt at any part of the body where the arterial pulsation is transmitted to the skin surface, especially when compressed. Some of the main pulse sites include: *temporal artery by the forehead sides, facial artery at the angle of the jaws, carotid artery in the neck*, and also the *radial artery by the wrist.*
In a normal adult, the average pulse range is from 60 to 100 bpm. Therefore, pulses below 60 can signify *bradycardia* and pulses above 100bpm can signify *tachycardia*. With reference to triaging, the heart rate is one of the main vitals used to help identify patients experiencing stress, shock, infection, and other critical medical conditions needing immediate care.


*Reference source:
https://www.news-medical.net/health/What-is-Heart-Rate.aspx*

---

# Day 5 Task

## Objective
The Day 5 task deliverable involves writing a summarized description of any unmentioned vital sign: Cholesterol:

## Cholesterol
Cholesterol is *a type of fat that is found in the blood, most of which is produced by the liver*. This serves many important functions such as *producing hormones* and also *vitamin D*. Cholesterol also consists of different components. For instance, *High-Density Lipoprotein (HDL)* also known as *‘good cholesterol’* carries extra cholesterol away from the blood and cells, back to the liver which breaks it down, assisting with the protection of the heart and blood vessels; *Low-Density Lipoprotein (LDL)*, also known as *‘bad cholesterol’* can lead to serious health problems like stroke, heart disease, and dementia, when too much clogs the blood vessels; and then the total cholesterol which is the HDL and LDL combined.
Cholesterol levels are usually measured in *milligrams per decilitre (mg/dL)* and are used to assess cardiovascular health. The desirable total cholesterol level is averaged to be less than ***200 mg/dL***. Higher values would then indicate there is increased heart disease and stroke. Therefore, in reference to triaging, abnormal cholesterol levels are not usually treated as an ‘urgent’ emergency, but they can provide important background information about a patient’s long-term cardiovascular risk and overall health status.



*Reference source:
https://www.alzheimersresearchuk.org/dementia-information/dementia-risk/cholesterol-and-dementia-risk/#:~:text=Having%20high%20cholesterol%20in%20our,people%20who%20develop%20it%20now.*

---

# Day 6 Task

## Objective
The Day 6 task deliverable involves the final deliverable which is writing a pseudocode that describes how a digital triaging model will work and how patients are categorized into respective risk levels. A combination of pseudocode and explanations were done to effectively display the information:

## ED Triage Pseudocode Attempt and System Explanation: 

<img width="585" height="582" alt="image" src="https://github.com/user-attachments/assets/a9cb7ad2-f4a1-4325-8252-2bdea5948de3" />
<img width="529" height="636" alt="image" src="https://github.com/user-attachments/assets/1dd92f4b-a995-4004-b110-db35abfb6b54" />
<img width="467" height="245" alt="image" src="https://github.com/user-attachments/assets/e6313edb-4e2e-491d-94a3-5a08e6d16a9a" />


## System Explanation 
The proposed digital triaging system is designed to assist emergency department staff by rapidly processing patient information and assigning a clinical risk category. The system begins by collecting patient demographic information and vital signs, including temperature, pulse, blood pressure, oxygen saturation, respiratory rate, and Glasgow Coma Scale (GCS) score. These measurements are commonly used during emergency department triage to assess patient stability and urgency of care.
Once the patient data is received, the system information is validated and cleaned to identify and rectify missing or abnormal entries. If critical information is unavailable, the patient is flagged for direct nurse review to reduce the risk of incorrect automated categorisation.
The system then compares the patient’s vital signs against predefined clinical thresholds. Patients with severely abnormal measurements, such as very low GCS scores, extremely low oxygen saturation, severe hypotension, or dangerously elevated pulse rates, are categorised as critical priority cases requiring immediate medical attention. Patients with moderately abnormal vital signs are categorised into high or moderate risk groups depending on the severity of the findings.
After processing the data, the system assigns a final triage category and stores the information in the hospital database. The assigned risk level can then be displayed on the emergency department dashboard to support nurses and physicians in prioritising patient care efficiently.


## Author:

Eliana Dookhoo
