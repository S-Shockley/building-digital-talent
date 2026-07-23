
<h1 align="center">Building Digital Talent</h1>
<p align="center">
  What Developer Career Data Reveals About Training Investment
</p>

<p align="center">
  <img src="img/top_pic3.png">
</p>

<p align="center">
  An analysis of software developer learning pathways, job satisfaction, AI attitudes, and career-change consideration
</p>

## Project Overview <a id="top"></a>

Digital transformation is often discussed in terms of tools, platforms, automation, and artificial intelligence. However, none of those investments create lasting value without people who can build, adapt, and apply technical skills in mission-relevant ways.

Using the 2025 Stack Overflow Developer Survey, this analysis explores how software professionals report learning technical skills and how those learning pathways relate to job satisfaction, AI concern, and career-change consideration. The central question is: **when organizations invest in technical training, how do they make sure that learning turns into applied capability?**

The analysis uses a large public developer workforce dataset as an exploratory stand-in, not as a direct measure of military or government personnel. Findings should be interpreted as broad, self-reported associations, not causal proof and not individual-level prediction.

## Motivation

Organizations are investing in technical training to support digital transformation, automation, software development, data analysis, and AI adoption. Training is important, but course completion alone does not guarantee mission impact. A person can complete a course, earn a certification, or learn a new tool and still return to a role where the skill is not used.

The motivation for this project is to examine the space between learning and application. For leaders, the practical issue is not only what training to fund. It is also how to time training, how to connect it to mission-relevant work, and how to create a credible next step for people who are building valuable technical skills.

A key leadership takeaway from the analysis is:

> **Training builds capability, but timing and opportunity determine whether the organization captures it.**

## Table of Contents

1. [Dataset Description](#dataset-description)
2. [Questions Explored](#questions-explored)
3. [Tools and Technologies](#tools-and-technologies)
4. [Repository Structure](#repository-structure)
5. [Analytical Approach](#analytical-approach)
6. [Data Preparation](#data-preparation)
7. [Exploratory Data Analysis](#exploratory-data-analysis)
8. [Modeling](#modeling)
9. [Dashboard Prototype](#dashboard-prototype)
10. [Key Findings](#key-findings)
11. [Leadership Implications](#leadership-implications)
12. [Limitations](#limitations)
13. [Future Research](#future-research)

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
- Career-change consideration

The dataset is based on self-reported survey responses from people who chose to participate. It does not represent the military workforce or any specific organization. Results should be interpreted as broad patterns among survey respondents, not direct conclusions about all software professionals, government employees, or military personnel.

## Questions Explored

This analysis focuses on questions related to technical workforce development:

1. Which learning pathways are most common among software professionals?
2. Are learning pathways associated with differences in job satisfaction?
3. How does job satisfaction relate to career-change consideration?
4. Can job satisfaction be predicted from learning pathways and workforce characteristics?
5. Can career-change consideration be predicted using learning pathways, experience, compensation, AI attitudes, and workplace characteristics?
6. Which broad feature groups appear most important in the career-change consideration model?
7. Does the career-change consideration model still perform when salary, experience, or AI threat perception are removed?
8. How could the findings support a future workforce planning dashboard or decision-support prototype?

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Git/GitHub

## Repository Structure

```text
building-digital-talent/
├── app/
│   └── app.py
├── data/
│   ├── raw/
│   └── processed/
├── img/
├── notebooks/
│   ├── 01_data_check_edited.ipynb
│   ├── 02_eda_edited.ipynb
│   ├── 03_hypothesis_test_edited.ipynb
│   └── 04_modeling.ipynb
├── src/
└── README.md
```

## Analytical Approach

This project followed a structured data science workflow, beginning with data cleaning and exploratory analysis, then moving into hypothesis testing, predictive modeling, and dashboard development.

The analysis was organized across four main notebooks:

#### [Data Preparation](notebooks/01_data_check_edited.ipynb)

- Imported the 2025 Stack Overflow Developer Survey data
- Selected project-relevant columns
- Reviewed missing values
- Cleaned numeric experience fields
- Created a log-transformed salary feature
- Created binary learning pathway flags
- Created a job satisfaction outcome variable
- Created a career-change consideration target variable

#### [Exploratory Data Analysis](notebooks/02_eda_edited.ipynb)

- Examined job satisfaction distribution
- Compared job satisfaction by career-change consideration group
- Reviewed learning pathway frequencies
- Compared career-change consideration rates across learning pathways
- Reviewed salary distribution and outliers
- Explored relationships among experience, AI attitudes, work setting, and career-change consideration

#### [Modeling](notebooks/04_modeling.ipynb)

- Built regression models to predict job satisfaction
- Built classification models to predict career-change consideration
- Compared logistic regression and random forest classification models
- Evaluated model performance using accuracy, precision, recall, F1 score, and ROC-AUC
- Created model score bands to evaluate whether predicted probabilities separated groups with different observed career-change consideration rates
- Ran sensitivity checks by removing salary, experience, and AI threat perception

<p align="right">
  <a href="#top">⬆ Back to Top</a>
</p>

## Data Preparation

The raw survey dataset contained many columns that were not needed for this project, so the analysis began by selecting variables related to learning pathways, workforce background, job satisfaction, career-change consideration, compensation, and AI-related attitudes.

Several features were engineered for analysis:

- `YearsCode_clean`: cleaned numeric version of years coding
- `WorkExp_clean`: cleaned numeric version of work experience
- `log_salary`: log-transformed annual compensation to reduce the influence of salary outliers
- `high_job_sat`: binary indicator for higher job satisfaction
- `career_change_considered`: binary target variable indicating whether a respondent considered or transitioned into a new career or industry
- Learning pathway flags, including:
  - online courses/certifications
  - school/university
  - coding bootcamp
  - AI tools
  - technical documentation
  - colleague or on-the-job learning
  - books/physical media
  - videos

Learning pathway variables were not mutually exclusive. Respondents could report multiple ways of learning to code, so these variables should be interpreted as overlapping learning signals rather than separate categories.

## Exploratory Data Analysis

Exploratory analysis showed that job satisfaction was generally high among respondents who answered the job satisfaction question. However, job satisfaction differed noticeably by career-change consideration group.

```text
No career change considered:
Mean JobSat = 7.79
Median JobSat = 8

Considered or transitioned careers:
Mean JobSat = 6.70
Median JobSat = 7
```

Career-change consideration also varied across learning pathways and AI threat perception. Respondents who viewed AI as a threat to future opportunities had a higher observed career-change consideration rate than respondents who did not.

```text
Career-change consideration by AI threat perception:
Not worried about AI: 50.1%
Not sure: 57.6%
Worried about AI: 68.1%
```

This pattern does not prove that AI concern causes career-change consideration. However, it suggests that AI adoption should be treated as a leadership and workforce issue, not only a technical tools rollout.

## Modeling

### Job Satisfaction Regression

Regression models were used to test whether job satisfaction could be predicted from learning pathways and broad workforce characteristics. Model performance was weak.

```text
Linear Regression:
MAE = 1.469
RMSE = 1.943
R² = 0.049

Random Forest Regressor:
MAE = 1.474
RMSE = 1.953
R² = 0.039

Expanded Linear Model with Developer Type:
MAE = 1.464
RMSE = 1.936
R² = 0.056
```

These results suggest that job satisfaction was difficult to predict from the available survey variables. Important drivers of job satisfaction may include factors not measured in this dataset, such as manager quality, team culture, workload, mission fit, organizational climate, or local leadership conditions.

### Career-Change Consideration Classification

The main classification target was `career_change_considered`:

```text
0 = did not report career-change consideration
1 = reported career-change consideration or career/role transition
```

Logistic regression and random forest classification models were compared. The random forest classifier performed slightly better overall and was used for the main classification results.

```text
Random Forest Classifier:
Accuracy = 0.592
Precision = 0.598
Recall = 0.764
F1 = 0.670
ROC-AUC = 0.612

Logistic Regression:
Accuracy = 0.584
Precision = 0.602
Recall = 0.692
F1 = 0.644
ROC-AUC = 0.604
```

The classification model found modest signal. A ROC-AUC near 0.61 is better than random guessing, but not strong enough for individual prediction. The model is best interpreted as group-level pattern recognition, not a tool to predict what any one person will do.

### Model Score Bands

To make the classification results easier to interpret, predicted probabilities from the held-out test set were grouped into lower, middle, and higher model score bands.

```text
Lower band: 30.5% observed career-change consideration
Middle band: 52.5% observed career-change consideration
Higher band: 66.0% observed career-change consideration
```

These bands are an interpretation step. They are not official categories and should not be used to label individuals. The bands show that when the model assigned higher scores, those groups had higher observed career-change consideration rates. This supports the conclusion that career-change consideration had detectable group-level structure in the survey data.

### Feature Group Importance

Random forest feature importances were grouped into broader workforce categories.

```text
Experience & Compensation: 33.1%
AI Use & Attitudes: 24.6%
Learning Pathways: 17.4%
Work Setting: 16.2%
Education: 8.8%
```

The strongest signal came from experience and compensation, followed by AI use and attitudes. Learning pathways mattered, but they did not explain career-change consideration by themselves. This supports the broader interpretation that training decisions should be considered alongside career stage, marketability, AI concern, workplace context, and opportunity.

### Sensitivity Checks

Several model versions were tested to see whether performance depended heavily on salary, experience, or AI threat perception.

```text
Full Model ROC-AUC: 0.612
No Salary ROC-AUC: 0.607
Development-Focused ROC-AUC: 0.590
No Salary/Experience/AIThreat ROC-AUC: 0.564
```

Removing salary alone only slightly reduced performance. Removing salary and experience reduced performance more noticeably. Removing AI threat perception reduced performance further. This suggests career-change consideration was not explained by one factor alone. It reflected a mix of compensation, career stage, AI attitudes, learning pathways, work setting, and education.

<p align="right">
  <a href="#top">⬆ Back to Top</a>
</p>

## Dashboard Prototype

A Streamlit dashboard was developed as a companion product for exploring the analysis. The dashboard includes:

- An executive overview with key dataset metrics
- A training explorer for comparing observed outcomes by learning pathway
- Job satisfaction visualizations
- Model results, including performance metrics, model score bands, and sensitivity checks
- A pathway deep dive comparing structured, self-directed, AI-assisted, and workplace learning pathways
- A prototype workforce signal explorer

The dashboard is intended to support exploration and discussion, not personnel assessment. The workforce signal explorer is a prototype only. It does not run the trained random forest model live. Instead, it demonstrates how a future decision-support tool could allow leaders to explore broad workforce signals such as experience, AI concern, and learning pathways.

## Key Findings

1. **Job satisfaction was lower among respondents who reported career-change consideration.**

   Respondents who had not considered a career change reported higher average job satisfaction than those who had considered or transitioned careers.

2. **Job satisfaction was difficult to predict from broad survey variables.**

   Regression models had low explanatory power, suggesting that job satisfaction may depend on factors not captured in the survey.

3. **Career-change consideration showed modest but useful group-level signal.**

   The random forest classifier was not strong enough for individual prediction, but it did identify broad patterns associated with career-change consideration.

4. **Experience and compensation carried the strongest model signal.**

   This suggests that career-change consideration is partly connected to career stage and market position. Training can increase capability, but compensation and experience may influence where that capability goes next.

5. **AI concern was a notable pattern worth deeper investigation.**

   Respondents who viewed AI as a threat to future opportunities reported higher career-change consideration rates. This suggests AI adoption should be paired with role clarity, expectations, and mission-relevant examples of how the tools will be used.

6. **Learning pathways matter, but they are not the whole story.**

   Learning pathways were associated with different workforce patterns, but career-change consideration reflected a broader mix of experience, compensation, AI attitudes, work setting, and education.

## Leadership Implications

The analysis does not tell leaders exactly why someone is considering a career change, and it should not be used to label individuals. Its value is that it identifies patterns that are strong enough to support deeper workforce questions.

For leaders investing in digital talent, the practical implication is to treat technical training as part of a broader talent-development system. Training should be connected to mission demand, timing, role clarity, and follow-on opportunity.

Leaders could use this type of analysis to ask:

- After someone completes technical training, what mission problem, project, role, or responsibility will use that skill?
- Are people being trained close enough to a real mission need that they can apply the skill quickly?
- Are newer, mid-career, and experienced personnel receiving training pathways that fit their career stage and needs?
- Are people learning AI tools without also receiving clarity on how AI changes their role, expectations, and future value?
- Are technically skilled and experienced people given a credible reason to keep growing inside the organization?
- After training, do people have access to mentors, tools, data, permissions, and supervisor support to actually use the skill?

The recommended next step is to build a training-to-application plan before assigning or funding training. That plan should identify the skill being developed, the mission need it supports, the project or role where it will be used, the expected timeline for applying it, and the supervisor or mentor responsible for follow-through.

## Limitations

This analysis has several important limitations:

- The dataset is observational and self-reported.
- The survey does not represent the military workforce or any specific organization.
- Learning pathways overlap, so pathway comparisons are descriptive rather than mutually exclusive.
- Career-change consideration is not the same as actual retention, attrition, or turnover.
- The model identifies associations, not causes.
- The classification model performance was modest and should not be used for individual prediction.
- Salary data had substantial missingness and may not be comparable across countries, roles, or labor markets.
- The survey does not directly measure follow-on assignments, supervisor support, mission alignment, training timing, or whether respondents actually used new skills after training.

## Future Research

Future work could strengthen this analysis by using organizational data that more directly measures training investment and workforce outcomes. Useful next steps include:

- Linking training completion to follow-on assignments, projects, or role changes
- Measuring whether trained personnel actually use new skills after training
- Comparing training timing against mission demand or project availability
- Adding measures of supervisor support, role clarity, team climate, and workload
- Studying AI adoption with more detailed measures of role impact, confidence, and perceived future value
- Tracking actual retention, attrition, internal movement, or career progression over time
- Evaluating whether different career stages benefit from different training pathways
- Developing and validating a real workforce decision-support model using organization-specific data

## Conclusion

This analysis found that career-change consideration among survey respondents was associated with more than learning pathway alone. Experience and compensation carried the strongest model signal, followed by AI use and attitudes, learning pathways, work setting, and education. The model was not strong enough for individual prediction, but it did show that career-change consideration had detectable group-level patterns.

For leaders, the main takeaway is that technical training should not be treated as course completion alone. Training builds capability, but timing and opportunity determine whether the organization captures it. To connect learning to what comes next, leaders should define the mission need, identify the follow-on work, clarify how new skills fit the role, and create a credible path for continued growth.

<p align="right">
  <a href="#top">⬆ Back to Top</a>
</p>
