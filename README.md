# Predicting Staffing Strain in U.S. Public Schools

## Overview
This project predicts staffing strain in U.S. public schools using education and socioeconomic data from NCES EDGE and the American Community Survey (ACS) between 2017 and 2023. 

Staffing strain is defined in terms of student-teacher ratios and modeled using demographic, grade composition, and community economic indicators. The objective is to identify schools at risk and determine which factors most strongly contribute to staffing shortages.

## Live Streamlit Dashboard
https://strain-risk-capstone.streamlit.app/

An interactive Streamlit dashboard was developed to explore multi-year staffing strain predictions and generate executive-style summaries of long-term risk trajectories at the school level.

<img width="1794" height="672" alt="image" src="https://github.com/user-attachments/assets/5c74dcef-fa1e-4a75-995b-c05f3265ff79" />

<img width="1786" height="654" alt="image" src="https://github.com/user-attachments/assets/ac76c7d9-7db4-4865-8bab-884d5ff16410" />
Example dashboard output showing predicted multi-year staffing strain trajectory and executive trend assessment.

## Research Question and Objective
Can we predict whether a school is experiencing staffing strain based on demographic and economic factors?

## Definition of Staffing Strain
Staffing strain is defined using the NCES student-teacher ratio variable:

STURATIO > 20

Schools exceeding this threshold are labeled as experiencing staffing strain for 10th Street School.

## Data Sources
Datasets used:
* NCES EDGE K-12 School Locations (school-level staffing, poverty rates, demographics, and enrollment data)
* American Community Survey (ACS) (community-level economic indicators)

Years Covered:
2017–2023 (Excluding 2019)

NCES provided enrollment counts, teacher counts, grade-level composition, and student demographics. ACS provided surrounding socioeconomic indicators such as household income, employment status, and public assistance participation. 

## Target Variable
Binary classification variable:
staffing_strain = 1 if student_teacher_ratio > 20
staffing_strain = 0 otherwise

## Features Used
Example predictors include:
* grade-level enrollment ratios
* ethnicity proportions
* median_household_income
* unemployment indicators
* food assistance participation

## Modeling Approach
Model used:
* XGBoost
* Random Forest Classifier

Evaluation Metrics:
* ROC-AUC
* Precision
* Recall

## Results
Both XGBoost and Random Forest achieved strong classification performance in identifying high-risk staffing environments, with ROC-AUC values of .91 and .92 respectively. 

## Key Findings
Grade-level composition had the greatest influence on staffing load, especially the ratio of lower-grade students.

Socioeconomic conditions, including household earnings and food assistance participation, were the second strongest predictors.

Racial demographic composition also contributed to prediction performance, though with a smaller influence compared to grade structure and economic indicators.

## Streamlit Dashboard

An interactive Streamlit dashboard was developed to explore staffing strain predictions across U.S. public schools.

The dashboard allows users to:

- evaluate predicted staffing strain probability across five observed years
- visualize risk trajectories
- identify peak-risk years and long-term trend changes
- review multi-year average strain estimates
- generate summaries of staffing strain patterns
- interact with an AI-assisted policy interpretation component for trend analysis

The interface supports exploratory policy-style analysis by translating model predictions into interpretable risk trends for decision-making contexts.


## Tech Stack
* Python (pandas, scikit-learn)
* PostgreSQL
* SQL
* NCES EDGE API
* ACS Census API
* Streamlit
* XGBoost
* Random Forest

## How to Run the Project 
- git clone repo
- pip install requirements.txt
- run notebooks

## Contributers
- Caleb Combs
- Scott Whitfield
- Johnny Tu
