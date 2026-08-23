# Iris EDA

Exploratory data analysis of the classic [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set), available both as a Jupyter notebook and an interactive Streamlit app.

## Contents

- `Iris.csv` — the dataset (150 rows: sepal/petal length & width, plus species).
- `eda_iris.ipynb` — notebook walking through the analysis step by step.
- `app.py` — Streamlit app presenting the same analysis interactively.

## What's covered

- Dataset shape, column types, missing values, and duplicate rows
- Summary statistics and species counts
- Feature distributions by species (histograms, boxplots)
- Relationships between features (scatter plot, pairplot)
- Feature correlation matrix

## Running

Install dependencies:

```bash
uv sync
```

Launch the Streamlit app:

```bash
streamlit run app.py
```

Or explore the notebook directly in Jupyter:

```bash
jupyter notebook eda_iris.ipynb
```
