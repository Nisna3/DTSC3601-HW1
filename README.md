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


<img width="1512" height="814" alt="Screenshot 2026-08-22 at 4 48 11 PM" src="https://github.com/user-attachments/assets/ea29f9b9-42a7-4162-8f7a-77c82132a5b6" />
<img width="1508" height="807" alt="Screenshot 2026-08-22 at 4 48 21 PM" src="https://github.com/user-attachments/assets/fb6c4b99-b887-4e40-a5bd-c7d37989baa8" />
<img width="1512" height="796" alt="Screenshot 2026-08-22 at 4 48 28 PM" src="https://github.com/user-attachments/assets/5187b5ed-9385-4bfe-86a8-28f7fdaff14c" />
<img width="1486" height="795" alt="Screenshot 2026-08-22 at 4 48 32 PM" src="https://github.com/user-attachments/assets/3c58d876-95c7-47bd-a773-ef93ec289674" />
<img width="1512" height="846" alt="Screenshot 2026-08-22 at 4 48 36 PM" src="https://github.com/user-attachments/assets/c44c4eec-7450-4cfd-a4b9-fe6b61a293fe" />
<img width="1509" height="746" alt="Screenshot 2026-08-22 at 4 48 45 PM" src="https://github.com/user-attachments/assets/604a4b4b-d769-437e-bd13-9850f19f751d" />








