#  Data Understanding

## Dataset Overview

The dataset used in this project is a comprehensive collection of patient information related to **lung cancer risk**. It contains **1,000 records**, each representing a unique patient, along with **26 columns** detailing:

- Demographic data  
- Lifestyle habits  
- Environmental exposures  
- Genetic predispositions  
- Clinical symptoms  
- Final diagnosis or risk level  

This dataset is specifically designed to support the analysis of potential causes and indicators of lung cancer, thereby facilitating **early risk prediction** through data science and AI techniques.

---

##  Data Source and Context

The dataset includes a diverse set of **health and behavioral attributes**, such as:

- **Demographics**: `Age`, `Gender`  
- **Environmental Factors**: `Air Pollution`, `Occupational Hazards`  
- **Lifestyle Behaviors**: `Alcohol Use`, `Smoking`, `Passive Smoker`, `Balanced Diet`  
- **Genetic and Chronic Conditions**: `Genetic Risk`, `Chronic Lung Disease`, `Obesity`  
- **Symptoms and Clinical Signs**: `Coughing of Blood`, `Chest Pain`, `Shortness of Breath`, `Clubbing of Finger Nails`, etc.

> According to a study published in *Nature Medicine*, air pollution can increase the risk of lung cancer even in **non-smokers**. A 6-year study of over **462,000 people** in China revealed that individuals living in high-pollution areas were more likely to develop lung cancer—particularly among non-smokers and older adults.

This underscores the importance of analyzing a wide array of **non-traditional risk factors**, beyond smoking alone.

---

## 3.3 Key Variables

| **Variable**             | **Type**       | **Description**                                                                 |
|--------------------------|----------------|----------------------------------------------------------------------------------|
| `Age`                    | Numeric        | Age of the patient                                                              |
| `Gender`                 | Categorical    | 0 = Male, 1 = Female                                                            |
| `Air Pollution`          | Ordinal        | Exposure level to polluted air                                                  |
| `Alcohol Use`            | Ordinal        | Frequency or quantity of alcohol consumption                                    |
| `Dust Allergy`           | Ordinal        | Allergy sensitivity to dust                                                     |
| `Occupational Hazards`   | Ordinal        | Exposure to workplace-related health risks                                      |
| `Genetic Risk`           | Ordinal        | Genetic predisposition or family history of lung cancer                         |
| `Chronic Lung Disease`   | Binary         | Presence of chronic lung diseases (e.g., COPD, asthma)                          |
| `Balanced Diet`          | Ordinal        | Quality or consistency of maintaining a balanced diet                           |
| `Obesity`                | Ordinal        | Obesity level or BMI-based classification                                       |
| `Smoking`                | Ordinal        | Direct smoking exposure                                                         |
| `Passive Smoker`         | Ordinal        | Secondhand smoking exposure                                                     |
| `Chest Pain`             | Binary         | Symptom presence: 0 = No, 1 = Yes                                               |
| `Fatigue`                | Binary         | Symptom presence: 0 = No, 1 = Yes                                               |
| `Coughing of Blood`      | Binary         | Symptom presence: 0 = No, 1 = Yes                                               |
| `Shortness of Breath`    | Binary         | Symptom presence: 0 = No, 1 = Yes                                               |
| `Clubbing of Nails`      | Binary         | Symptom presence: 0 = No, 1 = Yes                                               |
| ...                      | ...            | Other relevant symptom indicators                                               |
| `Level`                  | Categorical    | Target variable indicating **lung cancer risk level** (e.g., Low, Medium, High) |

---

This structured dataset enables robust **feature engineering**, **statistical modeling**, and **AI-based classification**, all aimed at **early identification of lung cancer risks**.
