# Building and Sustaining Digital Talent

## Overview
A short plain-English summary of the project.

## Motivation
Why this matters to digital transformation, technical workforce development, and organizations like the U.S. Space Force.

## Research Questions
1. Do active learners report different job satisfaction than non-active learners?
2. Can job satisfaction be predicted from learning pathways and workforce characteristics?
3. Can career change consideration be predicted from learning pathways and workforce characteristics?
4. Which factors appear most important: learning, salary, experience, education, AI attitudes, or workplace characteristics?

## Dataset
Describe the 2025 Stack Overflow Developer Survey:
- number of rows
- number of columns
- key variables
- why it fits the project

## Data Cleaning and Feature Engineering
Explain:
- selected columns
- missing values
- multi-select learning pathway columns
- binary target for career change consideration
- high job satisfaction label, if used
- salary handling / outliers

## Exploratory Data Analysis
Include key plots:
- JobSat distribution
- NewRole distribution
- learning pathway counts
- job satisfaction by active learner status
- career change rate by learning pathway

## Hypothesis Test
State:
- Null hypothesis
- Alternative hypothesis
- Test selected
- Alpha
- Result
- Plain-English interpretation

## Modeling
Separate this into two parts:

### Job Satisfaction Model
Regression model predicting `JobSat`.

### Career Change Consideration Model
Classification model predicting whether someone considered or transitioned into a new career or industry.

## Model Evaluation
Include:
- train/test split or cross-validation
- metrics
- baseline model
- model comparison
- confusion matrix or regression error metrics

## Key Findings
This section should be written for a non-technical reader.

## Military / Workforce Relevance
Connect results back to technical workforce development, Supra Coder, digital transformation, and retention-related workforce outcomes without overclaiming.

## Limitations
Be honest:
- survey data is observational
- not military-specific
- self-reported responses
- job satisfaction is not actual retention
- career change consideration is not the same as attrition

## Future Work
Possible next steps:
- compare with 2024
- build organization-specific survey
- test military workforce data
- improve dashboard
- add SHAP explanations

## Repository Structure
Show folders.

## How to Run
Basic instructions for notebook / Streamlit app.