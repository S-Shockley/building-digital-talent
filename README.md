
<h1 align="center">Building Digital Talent</h1>
<p align="center">
  What Developer Career Data Reveals About Training Investment
</p>

<p align="center">
  <img src="img/top_pic3.png">
</p>

<p align="center">
  An analysis of software developer learning pathways, job satisfaction, and career change consideration
</p>

## Project Overview <a id="top"></a>

Organizations increasingly depend on technical talent to support digital transformation, automation, software development, and data-driven decision-making. However, leaders often face difficult choices about how to build and sustain that talent: formal education, online courses, certifications, coding bootcamps, AI-assisted learning, self-directed study, and on-the-job experience may all contribute differently to workforce outcomes.

Using the 2025 Stack Overflow Developer Survey, this project analyzes how software professionals build technical skills and how learning pathways relate to job satisfaction and career change consideration.

The goal of this project is to identify workforce patterns that may inform digital talent development and training investment decisions. Since this analysis uses an observational public survey dataset, findings should be interpreted as associations rather than direct cause-and-effect relationships.


## Motivation

In my current role as an Operations Research Analyst supporting digital transformation efforts, I am interested in how organizations can build, retain, and grow technical talent. Digital transformation depends not only on tools and platforms, but also on people who can learn, adapt, and apply technical skills in mission-relevant ways.

This dataset does not represent the military or my workplace directly. However, it provides a useful public workforce dataset for exploring questions that are relevant to technical workforce development, including how people learn to code, what factors relate to job satisfaction, and which characteristics are associated with career change consideration.


## Table of Contents

1. [Dataset Description](#dataset-description)
2. [Questions Explored](#questions-explored)
3. [Tools and Technologies](#tools-and-technologies)
4. [Analytical Approach](#analytical-approach)
5. [Data Preparation](#data-preparation)
6. [Exploratory Data Analysis](#exploratory-data-analysis)
7. [Hypothesis Testing](#hypothesis-testing)
8. [Modeling](#modeling)
9. [Findings](#findings)
10. [Limitations](#limitations)
11. [Future Research](#future-research)

## Dataset Description

This project uses the 2025 Stack Overflow Developer Survey, a public survey dataset containing responses from approximately 49,000 software professionals and learners.

Dataset Source: [Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/)

Key areas used in this analysis include:

- Learning pathways
- Education level
- Years of coding experience
- Work experience
- Compensation
- Remote, hybrid, or in-person work setting
- Organization size
- AI usage
- AI threat perception
- Job satisfaction
- Career change consideration

Data Considerations:

The dataset is based on survey responses, so results reflect self-reported information from respondents who chose to participate. The dataset does not represent the military workforce or any specific organization. Findings should be interpreted as broad workforce patterns among survey respondents, not as direct conclusions about all software professionals or government technical talent.


## Questions Explored

This analysis focuses on questions related to technical workforce development:

1. Which learning pathways are most common among software professionals?
2. Are learning pathways associated with differences in job satisfaction?
3. How does job satisfaction relate to career change consideration?
4. Can job satisfaction be predicted from learning pathways and workforce characteristics?
5. Can career change consideration be predicted using learning pathways, experience, compensation, AI attitudes, and workplace characteristics?
6. Does the career change model still perform when salary, experience, or AI threat perception are removed?


## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Git/GitHub


## Analytical Approach

This project followed a structured data science workflow, beginning with data cleaning and exploratory analysis, then moving into hypothesis testing and predictive modeling.

The analysis was organized across four main notebooks:

#### [Data Preparation](notebooks/01_data_check_edited.ipynb)

- Imported the 2025 Stack Overflow Developer Survey data
- Selected project-relevant columns
- Reviewed missing values
- Cleaned numeric experience fields
- Created a log-transformed salary feature
- Created binary learning pathway flags
- Created a job satisfaction outcome variable
- Created a career change consideration target variable

#### [Exploratory Data Analysis](notebooks/02_eda_edited.ipynb)

- Examined job satisfaction distribution
- Compared job satisfaction by career change consideration group
- Reviewed learning pathway frequencies
- Compared career change consideration rates across learning pathways
- Reviewed salary distribution and outliers
- Explored relationships between experience, AI attitudes, work setting, and career change consideration

#### [Hypothesis Testing](notebooks/03_hypothesis_test_edited.ipynb)

- Tested whether respondents who used online courses or certifications reported different average job satisfaction than those who did not
- Used Welch’s t-test because the two groups had different sample sizes and potentially different variances
- Used a Mann-Whitney U test as a robustness check for the bounded 0–10 job satisfaction scale

#### [Modeling](notebooks/04_modeling.ipynb)

- Built regression models to predict job satisfaction
- Built classification models to predict career change consideration
- Compared logistic regression and random forest classification models
- Evaluated model performance using accuracy, precision, recall, F1 score, and ROC-AUC
- Created probability bands to evaluate group-level career mobility patterns
- Ran sensitivity checks by removing salary, experience, and AI threat perception

<p align="right">
  <a href="#top">⬆ Back to Top</a>
</p>


## Data Preparation

The raw survey dataset contained many columns that were not needed for this project, so the analysis began by selecting variables related to learning pathways, workforce background, job satisfaction, career change consideration, compensation, and AI-related attitudes.

Several features were engineered for analysis:

- `YearsCode_clean`: cleaned numeric version of years coding
- `WorkExp_clean`: cleaned numeric version of work experience
- `log_salary`: log-transformed annual compensation to reduce the effect of salary outliers
- `high_job_sat`: binary indicator for higher job satisfaction
- `career_change_considered`: binary target variable indicating whether a respondent considered or transitioned into a new career or industry
- Learning pathway flags, including:
  - online courses/certifications
  - school/university
  - coding bootcamp
  - AI coding tools
  - technical documentation
  - colleague or on-the-job learning
  - books/physical media
  - videos

Learning pathway variables were not mutually exclusive. Respondents could report multiple ways of learning to code, so these variables should be interpreted as overlapping learning signals rather than separate categories.


## Exploratory Data Analysis

Exploratory analysis showed that job satisfaction was generally high among respondents who answered the job satisfaction question. However, job satisfaction differed noticeably by career change consideration group.

Respondents who had not considered or transitioned careers reported higher job satisfaction than respondents who had considered or transitioned careers.

```text
No career change considered:
Mean JobSat = 7.79
Median JobSat = 8

Considered or transitioned careers:
Mean JobSat = 6.70
Median JobSat = 7