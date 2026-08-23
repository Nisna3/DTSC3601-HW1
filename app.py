import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set_theme(style="whitegrid", palette="Set2")

st.set_page_config(page_title="Iris EDA", page_icon="🌸", layout="wide")

st.title("🌸 Iris Dataset — Exploratory Data Analysis")
st.caption("A quick look at the classic Iris dataset: shape, distributions, and relationships between features.")


@st.cache_data
def load_data():
    return pd.read_csv("Iris.csv")


df = load_data()
features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

tab_overview, tab_distributions, tab_relationships, tab_correlation = st.tabs(
    ["📋 Overview", "📊 Distributions", "🔗 Relationships", "🌡️ Correlation"]
)

with tab_overview:
    st.subheader("Raw Data")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("Shape & Quality")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Rows", df.shape[0])
    m2.metric("Columns", df.shape[1])
    m3.metric("Missing Values", int(df.isnull().sum().sum()))
    m4.metric("Duplicate Rows", int(df.duplicated().sum()))

    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.markdown("**Column Data Types**")
        st.dataframe(df.dtypes.rename("Dtype").astype(str), use_container_width=True)
    with info_col2:
        st.markdown("**Missing Values by Column**")
        st.dataframe(df.isnull().sum().rename("Missing Count"), use_container_width=True)

    stats_col1, stats_col2 = st.columns(2)
    with stats_col1:
        st.markdown("**Summary Statistics**")
        st.dataframe(df.describe(), use_container_width=True)
    with stats_col2:
        st.markdown("**Species Counts**")
        st.dataframe(df["Species"].value_counts(), use_container_width=True)

with tab_distributions:
    st.subheader("Distribution of Each Feature, by Species")
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    for ax, feature in zip(axes.flat, features):
        sns.histplot(data=df, x=feature, hue="Species", kde=True, element="step", ax=ax)
        ax.set_title(feature)
    fig.tight_layout()
    st.pyplot(fig)

    st.subheader("Spread & Outliers, by Species")
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    for ax, feature in zip(axes.flat, features):
        sns.boxplot(data=df, x="Species", y=feature, ax=ax)
        ax.set_title(feature)
    fig.tight_layout()
    st.pyplot(fig)

with tab_relationships:
    st.subheader("Sepal Length vs. Sepal Width, by Species")
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.scatterplot(data=df, x="SepalLengthCm", y="SepalWidthCm", hue="Species", ax=ax)
    ax.set_title("Sepal Length vs Sepal Width by Species")
    fig.tight_layout()
    st.pyplot(fig)

    st.subheader("Pairwise Relationships Between Features")
    pairplot_fig = sns.pairplot(df.drop(columns="Id"), hue="Species", diag_kind="kde", corner=True)
    st.pyplot(pairplot_fig)

with tab_correlation:
    st.subheader("Feature Correlation Matrix")
    corr = df.drop(columns=["Id", "Species"]).corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True, ax=ax)
    ax.set_title("Feature Correlation Matrix")
    fig.tight_layout()
    st.pyplot(fig)
