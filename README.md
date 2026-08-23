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


<img width="1512" height="814" alt="Screenshot 2026-08-22 at 4 48 11 PM" src="https://github.com/user-attachments/assets/7347bcf1-3ca1-4d10-a865-71cc04f702a1" />
<img width="1508" height="807" alt="Screenshot 2026-08-22 at 4 48 21 PM" src="https://github.com/user-attachments/assets/d345e549-93f8-4b92-b044-b7c05ab88899" />
<img width="1512" height="796" alt="Screenshot 2026-08-22 at 4 48 28 PM" src="https://github.com/user-attachments/assets/97fb7629-1ce2-4b9f-b4fe-74727343d179" />
<img width="1486" height="795" alt="Screenshot 2026-08-22 at 4 48 32 PM" src="https://github.com/user-attachments/assets/ecbc6abe-5e03-422e-aa92-95a0cbc8cb9f" />
<img width="1509" height="746" alt="Screenshot 2026-08-22 at 4 48 45 PM" src="https://github.com/user-attachments/assets/04f84ed4-3f86-49d8-8daa-1dcd77a7dc26" />
<img width="1512" height="846" alt="Screenshot 2026-08-22 at 4 48 36 PM" src="https://github.com/user-attachments/assets/64fd60a0-99c2-4d99-95bc-4ab2490d19b3" />



