from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "stackoverflow_2025_project_cleaned.csv"

LEARNING_COLS = {
    "Online courses/certifications": "learned_online_courses",
    "School/university": "learned_school",
    "Coding bootcamp": "learned_bootcamp",
    "AI tools": "learned_ai",
    "Technical documentation": "learned_docs",
    "On-the-job/colleague": "learned_on_job",
    "Books": "learned_books",
    "Videos": "learned_videos"
}

st.set_page_config(
    page_title="Building Digital Talent",
    page_icon="📊",
    layout="wide"
)

def inject_custom_css():
    st.markdown(
        """
        <style>
        /* Main app background */
        .stApp {
            background-color: #F4F7FA;
        }

        /* Main content container */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1150px;
        }

        .dashboard-header {
    background-color: #0B2F3A;
    color: #F4F7FA;
    padding: 1.5rem 2rem;
    border-radius: 18px;
    margin-bottom: 2rem;
    border-bottom: 5px solid #0B7285;
    box-shadow: 0 4px 14px rgba(16, 42, 67, 0.18);
}

    .dashboard-title {
        font-size: 2.6rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin-bottom: 0.35rem;
    }

    .dashboard-subtitle {
        font-size: 1.25rem;
        font-weight: 600;
        color: #D9EAF2;
        margin-bottom: 0.75rem;
    }

    .dashboard-description {
        font-size: 1rem;
        color: #BFD7E2;
        max-width: 950px;
        line-height: 1.6;
    }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #0B2F3A;
        }

        section[data-testid="stSidebar"] * {
            color: #F4F7FA;
        }

        /* Headings */
        h1 {
            color: #102A43;
            font-weight: 800;
        }

        h2, h3 {
            color: #173B4D;
            font-weight: 700;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #FFFFFF;
            border: 1px solid #D9E2EC;
            padding: 1rem;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(16, 42, 67, 0.08);
        }

        div[data-testid="stMetricLabel"] {
            color: #52616B;
        }

        div[data-testid="stMetricValue"] {
            color: #0B7285;
            font-weight: 800;
        }

        /* Info / warning boxes */
        div[data-testid="stAlert"] {
            border-radius: 12px;
        }

        /* Dataframes */
        div[data-testid="stDataFrame"] {
            border-radius: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

inject_custom_css()

st.markdown(
    """
    <div class="dashboard-header">
        <div class="dashboard-title">Building Digital Talent</div>
        <div class="dashboard-subtitle">
            What Developer Career Data Reveals About Training Investment
        </div>
        <div class="dashboard-description">
            This dashboard explores how developer learning pathways, job satisfaction,
            AI attitudes, and workforce characteristics relate to career change consideration.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)



@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()
filtered_df=df.copy()


st.sidebar.header("Building Digital Talent")

# filtered_df = df.copy()

# remote_options = ["All"] + sorted(df["RemoteWork"].dropna().unique().tolist())
# selected_remote = st.sidebar.selectbox("Remote work setting", remote_options)

# ai_options = ["All"] + sorted(df["AISelect"].dropna().unique().tolist())
# selected_ai = st.sidebar.selectbox("AI usage", ai_options)

# career_options = {
#     "All": "All",
#     "No career change considered": 0,
#     "Considered or transitioned careers": 1
# }
# selected_career_label = st.sidebar.selectbox(
#     "Career mobility group",
#     list(career_options.keys())
# )

# if selected_remote != "All":
#     filtered_df = filtered_df[filtered_df["RemoteWork"] == selected_remote]

# if selected_ai != "All":
#     filtered_df = filtered_df[filtered_df["AISelect"] == selected_ai]

# if selected_career_label != "All":
#     filtered_df = filtered_df[
#         filtered_df["career_change_considered"] == career_options[selected_career_label]
#     ]

# st.markdown("## Executive Overview")

# total_responses = len(filtered_df)
# job_sat_responses = filtered_df["JobSat"].notna().sum()
# career_target_responses = filtered_df["career_change_considered"].notna().sum()
# career_change_rate = filtered_df["career_change_considered"].mean() * 100

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("Filtered responses", f"{total_responses:,}")
# col2.metric("JobSat responses", f"{job_sat_responses:,}")
# col3.metric("Career mobility responses", f"{career_target_responses:,}")

# if pd.notna(career_change_rate):
#     col4.metric("Career change considered", f"{career_change_rate:.1f}%")
# else:
#     col4.metric("Career change considered", "N/A")
    
# tab1, tab2, tab3, tab4, tab5 = st.tabs([
#     "Executive Overview",
#     "Learning Pathways",
#     "Job Satisfaction",
#     "Career Mobility Model",
#     "Pathway Deep Dive"
# ])

section = st.sidebar.radio(
    "Section",
    [
        "Executive Overview",
        "Learning Pathways",
        "Job Satisfaction",
        "Career Mobility Model",
        "Pathway Deep Dive"
    ]
)

if section == "Executive Overview":
    st.markdown("### Executive Overview")
    total_responses = len(df)
    job_sat_responses = df["JobSat"].notna().sum()
    career_target_responses = df["career_change_considered"].notna().sum()
    career_change_rate = df["career_change_considered"].mean() * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total responses", f"{total_responses:,}")
    col2.metric("JobSat responses", f"{job_sat_responses:,}")
    col3.metric("Career mobility responses", f"{career_target_responses:,}")
    col4.metric("Career change considered", f"{career_change_rate:.1f}%")

    # st.write("Data preview")
    # st.dataframe(df.head())

    st.info(
        """
    Job satisfaction was clearly lower among respondents who had considered or transitioned careers,
    but job satisfaction itself was difficult to predict from broad survey variables. Career change
    consideration showed more useful group-level signal, especially when combined with career stage,
    compensation, AI concern, learning pathways, and workplace context.
        """
    )

    st.markdown("### How to Use This Dashboard")

    st.write(
    """
    Use the navigation panel on the left to move through the analysis:

    - **Learning Pathways** shows how respondents reported learning to code.
    - **Job Satisfaction** compares satisfaction patterns across career mobility groups.
    - **Career Mobility Model** summarizes model performance, probability bands, and sensitivity checks.
    - **Pathway Deep Dive** explores structured, self-directed, AI-assisted, and workplace learning pathways.
    """
)

    st.warning(
    """
    This dashboard uses public survey data from Stack Overflow. Findings should be interpreted
    as associations, not causal claims, and should not be used to assess individual workers.
    """
)
    


elif section == "Learning Pathways":
    st.markdown("### Learning Pathways")
    st.write(
        """
        This section explores how respondents reported learning to code.
        Respondents could select multiple pathways, so counts overlap.
        """
    )

    learning_counts = pd.DataFrame({
        "Learning pathway": LEARNING_COLS.keys(),
        "Count": [df[col].sum() for col in LEARNING_COLS.values()]
    }).sort_values("Count", ascending=True)

    fig = go.Figure(
        go.Bar(
            x=learning_counts["Count"],
            y=learning_counts["Learning pathway"],
            orientation="h"
        )
    )

    fig.update_layout(
        title="Most Common Learning Pathways",
        xaxis_title="Number of respondents",
        yaxis_title="Learning pathway",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Learning Pathway Mix")

    top_pathways = learning_counts.sort_values("Count", ascending=False).copy()

    fig = go.Figure(
        go.Pie(
            labels=top_pathways["Learning pathway"],
            values=top_pathways["Count"],
            hole=0.45
        )
    )

    fig.update_layout(
    title="Share of Reported Learning Pathway Selections",
    height=500,
    plot_bgcolor="#FFFFFF",
    paper_bgcolor="#FFFFFF"
)

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
    "Because respondents could select multiple learning pathways, this chart represents share of selections, not share of people."
)

elif section == "Job Satisfaction":
    st.markdown("### Job Satisfaction")
    st.write(
        """
        This page compares job satisfaction patterns across respondents.
        One of the clearest descriptive findings is that respondents who had
        not considered or transitioned careers reported higher job satisfaction
        than those who had.
        """
    )

    # JobSat distribution
    st.markdown("### Job Satisfaction Distribution")

    jobsat_counts = (
        df["JobSat"]
        .dropna()
        .value_counts()
        .sort_index()
        .reset_index()
    )

    jobsat_counts.columns = ["JobSat", "Count"]

    fig = go.Figure(
        go.Bar(
            x=jobsat_counts["JobSat"],
            y=jobsat_counts["Count"]
        )
    )

    fig.update_layout(
        title="Distribution of Job Satisfaction Scores",
        xaxis_title="Job satisfaction score",
        yaxis_title="Number of respondents",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    # JobSat by career change group
    st.markdown("### Job Satisfaction by Career Mobility Group")

    jobsat_group = (
        df.dropna(subset=["JobSat", "career_change_considered"])
        .groupby("career_change_considered")["JobSat"]
        .agg(["count", "mean", "median"])
        .reset_index()
    )

    jobsat_group["Career mobility group"] = jobsat_group["career_change_considered"].map({
        0: "No career change considered",
        1: "Considered or transitioned careers"
    })

    col1, col2 = st.columns(2)

    no_change_mean = jobsat_group.loc[
        jobsat_group["career_change_considered"] == 0, "mean"
    ].values[0]

    considered_mean = jobsat_group.loc[
        jobsat_group["career_change_considered"] == 1, "mean"
    ].values[0]

    col1.metric("No career change considered", f"{no_change_mean:.2f}")
    col2.metric("Considered or transitioned careers", f"{considered_mean:.2f}")

    fig = go.Figure(
        go.Bar(
            x=jobsat_group["Career mobility group"],
            y=jobsat_group["mean"],
            text=jobsat_group["mean"].round(2),
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Average Job Satisfaction by Career Mobility Group",
        xaxis_title="Career mobility group",
        yaxis_title="Average JobSat",
        height=450
    )

    fig.update_yaxes(range=[0, 10])

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        Respondents who had not considered or transitioned careers reported
        higher average job satisfaction. However, the regression models later
        showed that job satisfaction itself was difficult to predict from the
        available survey variables.
        """
    )

    

elif section == "Career Mobility Model":
    st.markdown("### Career Mobility Model")
    st.write(
        """
        This page summarizes the classification model used to predict whether a respondent
        had considered or transitioned into a new career or industry. The model should not
        be interpreted as predicting individual career behavior. Instead, it is useful for
        identifying group-level workforce patterns.
        """
    )

    # ------------------------------------------------------------
    # Model performance table
    # ------------------------------------------------------------
    st.markdown("### Model Performance")

    model_results = pd.DataFrame({
        "Model": [
            "Full Model",
            "No Salary",
            "Development-Focused",
            "No Salary/Experience/AIThreat"
        ],
        "Accuracy": [0.592, 0.586, 0.575, 0.558],
        "Precision": [0.598, 0.593, 0.589, 0.565],
        "Recall": [0.764, 0.762, 0.722, 0.818],
        "F1": [0.670, 0.667, 0.649, 0.668],
        "ROC-AUC": [0.612, 0.607, 0.590, 0.564]
    })

    st.dataframe(
        model_results.style.format({
            "Accuracy": "{:.3f}",
            "Precision": "{:.3f}",
            "Recall": "{:.3f}",
            "F1": "{:.3f}",
            "ROC-AUC": "{:.3f}"
        }),
        use_container_width=True
    )

    st.info(
        """
        The full model performed best, but the ROC-AUC was about 0.61.
        That means the model had useful but modest signal. It is better for
        identifying broad patterns than for predicting what any one person will do.
        """
    )

    # ------------------------------------------------------------
    # Probability bands
    # ------------------------------------------------------------
    st.markdown("### Probability Bands")

    st.write(
        """
        To make the model easier to interpret, predicted probabilities were grouped
        into lower, middle, and higher probability bands. The chart below shows the
        actual observed career change consideration rate within each band.
        """
    )

    band_df = pd.DataFrame({
        "Probability Band": ["Lower", "Middle", "Higher"],
        "Observed Career Change Rate": [30.5, 52.5, 66.0],
        "Respondents": [354, 5176, 1576]
    })

    col1, col2, col3 = st.columns(3)

    col1.metric("Lower band", "30.5%")
    col2.metric("Middle band", "52.5%")
    col3.metric("Higher band", "66.0%")

    fig = go.Figure(
        go.Bar(
            x=band_df["Probability Band"],
            y=band_df["Observed Career Change Rate"],
            text=band_df["Observed Career Change Rate"],
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Observed Career Change Consideration by Probability Band",
        xaxis_title="Predicted probability band",
        yaxis_title="Observed career change consideration rate (%)",
        height=450
    )

    fig.update_yaxes(range=[0, 100])

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        """
        This is one of the strongest dashboard findings: the model separated respondents
        into groups with meaningfully different observed career change consideration rates.
        """
    )

    # ------------------------------------------------------------
    # Sensitivity checks
    # ------------------------------------------------------------
    st.markdown("### Sensitivity Checks")

    st.write(
        """
        Several versions of the model were compared to test whether performance depended
        on salary, career experience, or AI threat perception.
        """
    )

    sensitivity_df = pd.DataFrame({
        "Model": [
            "Full Model",
            "No Salary",
            "Development-Focused",
            "No Salary/Experience/AIThreat"
        ],
        "ROC-AUC": [0.612, 0.607, 0.590, 0.564]
    })

    fig = go.Figure(
        go.Bar(
            x=sensitivity_df["Model"],
            y=sensitivity_df["ROC-AUC"],
            text=sensitivity_df["ROC-AUC"].round(3),
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Model Performance After Removing Key Feature Groups",
        xaxis_title="Model version",
        yaxis_title="ROC-AUC",
        height=450
    )

    fig.update_yaxes(range=[0.5, 0.65])

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        Removing salary alone barely changed model performance. Removing salary and
        experience reduced performance more noticeably. Removing AI threat perception
        reduced ROC-AUC further. This suggests career change consideration was not
        explained by one factor alone. It reflected a mix of compensation, career stage,
        AI-related concern, learning pathways, and workplace context.
        """
    )

    st.markdown("### Scenario Explorer")

        # ------------------------------------------------------------
    # AI Threat Breakdown
    # ------------------------------------------------------------
    st.markdown("### AI Threat Perception and Career Change Consideration")

    st.write(
        """
        AI threat perception was one of the more important signals in the model.
        This chart shows the observed career change consideration rate by AI threat response.
        """
    )

    ai_threat_df = (
        df.dropna(subset=["AIThreat", "career_change_considered"])
        .groupby("AIThreat")["career_change_considered"]
        .agg(["count", "mean"])
        .reset_index()
    )

    ai_threat_df["Career change rate"] = ai_threat_df["mean"] * 100

    ai_threat_df = ai_threat_df.sort_values(
        "Career change rate",
        ascending=True
    )

    fig = go.Figure(
        go.Bar(
            x=ai_threat_df["Career change rate"],
            y=ai_threat_df["AIThreat"],
            orientation="h",
            text=ai_threat_df["Career change rate"].round(1),
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Career Change Consideration by AI Threat Perception",
        xaxis_title="Career change consideration rate (%)",
        yaxis_title="AI threat response",
        height=450,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF"
    )

    fig.update_xaxes(range=[0, 80])

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        Respondents who viewed AI as a threat to future opportunities had a higher observed
        career change consideration rate. This reinforces the model sensitivity finding that
        AI-related concern carried meaningful signal.
        """
    )
    #____________TEST______________________________-



    plot_df = df.dropna(subset=["AIThreat", "career_change_considered", "YearsCode_clean"]).copy()

    

    agg = plot_df.groupby("AIThreat").agg(
        rate=("career_change_considered", lambda s: s.mean() * 100),
        avg_experience=("YearsCode_clean", "mean"),
    ).reset_index()

    fig = go.Figure(go.Scatter(
        x=agg["rate"], y=agg["AIThreat"], mode="markers+text",
        text=agg["rate"].round(1), textposition="top center",
        marker=dict(size=28, color=agg["avg_experience"], colorscale="Viridis",
                    colorbar=dict(title="Avg. years coding"), line=dict(width=1, color="white")),
    ))
    fig.update_layout(title="Career Change Rate by AI Threat Perception (colored by avg. experience)",
                    xaxis_title="Career change consideration rate (%)", height=420)
    st.plotly_chart(fig, use_container_width=True)

    #_________________-EndTEST____________________

    # ------------------------------------------------------------
    # Scenario Explorer
    # ------------------------------------------------------------
    st.markdown("### Career Mobility Band Explorer")

    st.write(
        """
        This interactive demo shows how a few broad workforce signals can be translated
        into lower, middle, or higher career mobility bands. It is not the trained model
        and should not be used to assess real individuals.
        """
    )

    st.warning(
        """
        Demonstration only: this explorer uses simplified scoring logic based on the
        project findings. It is meant to show how a dashboard could support workforce
        planning conversations, not individual prediction.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        years_code = st.slider(
            "Years coding",
            min_value=0,
            max_value=20,
            value=5
        )

        ai_threat = st.selectbox(
            "AI threat perception",
            sorted(df["AIThreat"].dropna().unique().tolist())
        )

    with col2:
        selected_pathways = st.multiselect(
            "Learning pathways",
            list(LEARNING_COLS.keys()),
            default=["Online courses/certifications"]
        )

    # Simplified scoring logic for demo purposes
    score = 0
    band_basis = []

    if years_code <= 5:
        score += 1
        band_basis.append("Earlier career stage")
    elif years_code >= 20:
        score -= 1
        band_basis.append("More experienced career stage")

    if "Yes" in ai_threat:
        score += 2
        band_basis.append("Reports AI as a threat to future opportunities")
    elif "Not sure" in ai_threat:
        score += 1
        band_basis.append("Uncertain about AI's impact on future opportunities")

    if "Coding bootcamp" in selected_pathways:
        score += 1
        band_basis.append("Reported coding bootcamp pathway")

    if "Online courses/certifications" in selected_pathways:
        score += 1
        band_basis.append("Reported online courses/certifications")

    if "AI tools" in selected_pathways:
        score += 1
        band_basis.append("Reported AI-assisted learning")

    # Map simplified score to the same bands used in the model results
    if score <= 1:
        band = "Lower"
        observed_rate = 30.5
        message = (
            "This scenario falls into a lower mobility signal band. In the held-out "
            "test set, the lower probability band had an observed career change "
            "consideration rate of about 30.5%."
        )
    elif score <= 3:
        band = "Middle"
        observed_rate = 52.5
        message = (
            "This scenario falls into a middle mobility signal band. In the held-out "
            "test set, the middle probability band had an observed career change "
            "consideration rate of about 52.5%."
        )
    else:
        band = "Higher"
        observed_rate = 66.0
        message = (
            "This scenario falls into a higher mobility signal band. In the held-out "
            "test set, the higher probability band had an observed career change "
            "consideration rate of about 66.0%."
        )

    st.markdown("#### Scenario Output")

    out1, out2 = st.columns(2)

    out1.metric("Mobility signal band", band)
    out2.metric("Observed band rate", f"{observed_rate:.1f}%")

    if band == "Lower":
        st.success(message)
    elif band == "Middle":
        st.info(message)
    else:
        st.warning(message)

    st.markdown("#### Band Basis")

    if band_basis:
        for item in band_basis:
            st.write(f"- {item}")
    else:
        st.write("- No major elevated mobility signals selected")

    st.caption(
        """
        This explorer is intentionally simple. It uses the same lower, middle, and higher
        probability bands from the model results, but it does not run the trained random
        forest classifier.
        """
    )

elif section == "Pathway Deep Dive":
    st.markdown("### Pathway Deep Dive")
    st.write(
        """
        This section takes a closer look at learning pathways. The main dashboard
        treats all learning pathways as overlapping signals, but this page explores
        whether structured pathways and self-directed pathways show different patterns.
        """
    )

    st.warning(
        """
        Important: learning pathways overlap. A respondent could report using
        documentation, videos, AI tools, online courses, and bootcamps. These comparisons
        are descriptive, not causal.
        """
    )

    # ------------------------------------------------------------
    # Define pathway groups
    # ------------------------------------------------------------
    structured_cols = [
        "learned_online_courses",
        "learned_school",
        "learned_bootcamp"
    ]

    self_directed_cols = [
        "learned_docs",
        "learned_books",
        "learned_videos"
    ]

    ai_cols = [
        "learned_ai"
    ]

    workplace_cols = [
        "learned_on_job"
    ]

    pathway_group_df = df.copy()

    pathway_group_df["Structured learning"] = (
        pathway_group_df[structured_cols].sum(axis=1) > 0
    ).astype(int)

    pathway_group_df["Self-directed learning"] = (
        pathway_group_df[self_directed_cols].sum(axis=1) > 0
    ).astype(int)

    pathway_group_df["AI-assisted learning"] = (
        pathway_group_df[ai_cols].sum(axis=1) > 0
    ).astype(int)

    pathway_group_df["Workplace learning"] = (
        pathway_group_df[workplace_cols].sum(axis=1) > 0
    ).astype(int)

    pathway_groups = [
        "Structured learning",
        "Self-directed learning",
        "AI-assisted learning",
        "Workplace learning"
    ]

    # ------------------------------------------------------------
    # Pathway group summary
    # ------------------------------------------------------------
    st.markdown("### Learning Pathway Group Summary")

    group_summary = []

    for group in pathway_groups:
        group_data = pathway_group_df[pathway_group_df[group] == 1]

        group_summary.append({
            "Pathway group": group,
            "Respondents": len(group_data),
            "Avg JobSat": group_data["JobSat"].mean(),
            "Career change rate": group_data["career_change_considered"].mean() * 100
        })

    group_summary = pd.DataFrame(group_summary)

    st.dataframe(
        group_summary.style.format({
            "Respondents": "{:,}",
            "Avg JobSat": "{:.2f}",
            "Career change rate": "{:.1f}%"
        }),
        use_container_width=True
    )

    # ------------------------------------------------------------
    # Career change rate by pathway group
    # ------------------------------------------------------------
    st.markdown("### Career Change Consideration by Pathway Group")

    fig = go.Figure(
        go.Bar(
            x=group_summary["Pathway group"],
            y=group_summary["Career change rate"],
            text=group_summary["Career change rate"].round(1),
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Career Change Consideration Rate by Learning Pathway Group",
        xaxis_title="Learning pathway group",
        yaxis_title="Career change consideration rate (%)",
        height=450
    )

    fig.update_yaxes(range=[0, 100])

    st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------------------
    # Bootcamp spotlight
    # ------------------------------------------------------------
    st.markdown("### Bootcamp Spotlight")

    bootcamp_df = df[df["learned_bootcamp"] == 1]
    non_bootcamp_df = df[df["learned_bootcamp"] == 0]

    bootcamp_count = len(bootcamp_df)
    bootcamp_jobsat = bootcamp_df["JobSat"].mean()
    bootcamp_career_rate = bootcamp_df["career_change_considered"].mean() * 100

    non_bootcamp_jobsat = non_bootcamp_df["JobSat"].mean()
    non_bootcamp_career_rate = non_bootcamp_df["career_change_considered"].mean() * 100

    col1, col2, col3 = st.columns(3)

    col1.metric("Bootcamp respondents", f"{bootcamp_count:,}")
    col2.metric("Bootcamp Avg JobSat", f"{bootcamp_jobsat:.2f}")
    col3.metric("Bootcamp career change rate", f"{bootcamp_career_rate:.1f}%")

    bootcamp_compare = pd.DataFrame({
        "Group": ["Reported bootcamp", "Did not report bootcamp"],
        "Avg JobSat": [bootcamp_jobsat, non_bootcamp_jobsat],
        "Career change rate": [bootcamp_career_rate, non_bootcamp_career_rate]
    })

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=bootcamp_compare["Group"],
            y=bootcamp_compare["Career change rate"],
            text=bootcamp_compare["Career change rate"].round(1),
            textposition="outside",
            name="Career change rate"
        )
    )

    fig.update_layout(
        title="Career Change Consideration: Bootcamp vs. Non-Bootcamp",
        xaxis_title="Group",
        yaxis_title="Career change consideration rate (%)",
        height=450
    )

    fig.update_yaxes(range=[0, 100])

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        Bootcamp respondents are interesting because bootcamps are a more structured,
        intensive learning pathway. However, bootcamp participation was much less common
        than documentation, videos, AI tools, or online courses. This makes it useful as
        a spotlight finding, not the center of the entire project.
        """
    )

    st.markdown("### Pathway Outcome Heatmap")

    heatmap_df = group_summary.set_index("Pathway group")[
        ["Avg JobSat", "Career change rate"]
    ].copy()

    # Scale JobSat to percent-like scale so it can sit beside career rate visually
    heatmap_df["Avg JobSat"] = heatmap_df["Avg JobSat"] * 10

    fig = go.Figure(
        data=go.Heatmap(
            z=heatmap_df.values,
            x=["Avg JobSat scaled 0-100", "Career change rate"],
            y=heatmap_df.index,
            text=heatmap_df.round(1).values,
            texttemplate="%{text}",
            colorscale="Blues"
        )
    )

    fig.update_layout(
        title="Learning Pathway Groups Compared Across Outcomes",
        height=450,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Average JobSat is multiplied by 10 so it can be visually compared on a 0-100 scale."
    )

    st.markdown("### Learning Pathways by Coding Experience")

    st.write(
        """
        This view compares how respondents with different levels of coding experience
        reported learning to code. Values represent the percent of respondents within
        each experience group who reported using each learning pathway.
        """
    )

    experience_pathway_df = df.dropna(subset=["YearsCode_clean"]).copy()

    experience_pathway_df["Experience group"] = pd.cut(
        experience_pathway_df["YearsCode_clean"],
        bins=[0, 2, 5, 10, 50],
        labels=["0-2 years", "3-5 years", "6-10 years", "11+ years"],
        include_lowest=True
    )

    learning_summary = []

    for exp_group in ["0-2 years", "3-5 years", "6-10 years", "11+ years"]:
        group_df = experience_pathway_df[
            experience_pathway_df["Experience group"] == exp_group
        ]
        
        for pathway_label, pathway_col in LEARNING_COLS.items():
            learning_summary.append({
                "Experience group": exp_group,
                "Learning pathway": pathway_label,
                "Percent using pathway": group_df[pathway_col].mean() * 100
            })

    learning_summary_df = pd.DataFrame(learning_summary)

    fig = go.Figure()

    for exp_group in ["0-2 years", "3-5 years", "6-10 years", "11+ years"]:
        group_data = learning_summary_df[
            learning_summary_df["Experience group"] == exp_group
        ]
        
        fig.add_trace(
            go.Bar(
                x=group_data["Percent using pathway"],
                y=group_data["Learning pathway"],
                name=exp_group,
                orientation="h"
            )
        )

    fig.update_layout(
        barmode="group",
        title="Learning Pathways by Coding Experience Group",
        xaxis_title="Percent of respondents using pathway",
        yaxis_title="Learning pathway",
        height=650,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF"
    )

    fig.update_xaxes(range=[0, 100])

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Respondents could select multiple learning pathways, so percentages do not sum to 100%."
    )


    st.markdown("### Newer vs. Experienced Coders")

    compare_df = df.dropna(subset=["YearsCode_clean"]).copy()

    compare_df = compare_df[
        (compare_df["YearsCode_clean"] <= 2) |
        (compare_df["YearsCode_clean"] >= 11)
    ].copy()

    compare_df["Experience category"] = np.where(
        compare_df["YearsCode_clean"] <= 2,
        "Newer coders (0-2 years)",
        "Experienced coders (11+ years)"
    )

    compare_summary = []

    for exp_group in ["Newer coders (0-2 years)", "Experienced coders (11+ years)"]:
        group_df = compare_df[compare_df["Experience category"] == exp_group]
        
        for pathway_label, pathway_col in LEARNING_COLS.items():
            compare_summary.append({
                "Experience category": exp_group,
                "Learning pathway": pathway_label,
                "Percent using pathway": group_df[pathway_col].mean() * 100
            })

    compare_summary_df = pd.DataFrame(compare_summary)

    fig = go.Figure()

    for exp_group in ["Newer coders (0-2 years)", "Experienced coders (11+ years)"]:
        group_data = compare_summary_df[
            compare_summary_df["Experience category"] == exp_group
        ]
        
        fig.add_trace(
            go.Bar(
                x=group_data["Percent using pathway"],
                y=group_data["Learning pathway"],
                name=exp_group,
                orientation="h"
            )
        )

    fig.update_layout(
        barmode="group",
        title="Learning Pathways: Newer vs. Experienced Coders",
        xaxis_title="Percent using pathway",
        yaxis_title="Learning pathway",
        height=650,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF"
    )

    fig.update_xaxes(range=[0, 100])

    st.plotly_chart(fig, use_container_width=True)

    st.info(
    """
    Learning pathways appear to shift with experience. Newer coders reported higher use of
    structured learning pathways such as school, bootcamps, and online courses, while more
    experienced coders showed stronger reliance on technical documentation, books, and
    workplace learning. This suggests that training investment may need to vary by career stage.
    """
)








