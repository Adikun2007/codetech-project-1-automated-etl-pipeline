# ⚙️ Python Source Code – Automated ETL Pipeline

This folder contains the final Python implementation of my CodeTech Internship Project 1: Automated ETL Pipeline.

After working through each preprocessing stage in Jupyter Notebooks, I consolidated the complete workflow into a single production-ready script: `main.py`.

The script automates the entire ETL process using `pandas`, `NumPy`, and key scikit-learn modules such as `StratifiedShuffleSplit`, `SimpleImputer`, `OneHotEncoder`, `StandardScaler`, `Pipeline`, and `ColumnTransformer`.

---

## 📖 Development Journey

To build this solution, I first explored and validated every preprocessing step individually:

- Exploratory Data Analysis (EDA)
- Manual and stratified train-test splitting
- Missing value handling
- Categorical encoding
- Feature scaling
- Pipeline construction

After confirming that each component worked correctly, I integrated them into one automated Python script that processes the dataset end to end.

---

## 🐍 `main.py` – Workflow Overview

The script executes the following steps automatically:

### 1. Load the Dataset
Reads the raw housing dataset from the `Data/` directory using Pandas.

### 2. Create Income Categories
Uses `pd.cut()` to discretize `median_income` into bins for stratified sampling.

### 3. Perform Stratified Train-Test Split
Uses `StratifiedShuffleSplit` to preserve the distribution of income categories.

### 4. Select Training Data
Creates a copy of the training set for preprocessing while keeping the test set untouched.

### 5. Separate Features and Labels
Splits `median_house_value` (target) from the predictor features.

### 6. Identify Numerical and Categorical Columns
Separates numerical attributes from the `ocean_proximity` categorical feature.

### 7. Build Numerical Pipeline
Uses `SimpleImputer(strategy="median")` and `StandardScaler()`.

### 8. Build Categorical Pipeline
Uses `OneHotEncoder(handle_unknown="ignore")`.

### 9. Construct the Full ETL Pipeline
Combines both pipelines using `ColumnTransformer`.

### 10. Transform and Save the Data
Applies the pipeline, converts the result to a DataFrame, and saves it as `housing_prepared.csv`.

---

## 📂 Input and Output

### Input
- `../Data/housing.csv`

### Output
- `../Data/housing_prepared.csv`

---

## 🚀 How to Run

```bash
python main.py
```

---

## 🛠 Technologies and Libraries

- Python
- Pandas
- NumPy
- scikit-learn
  - `StratifiedShuffleSplit`
  - `SimpleImputer`
  - `OneHotEncoder`
  - `StandardScaler`
  - `Pipeline`
  - `ColumnTransformer`

---

## ✅ Final Outcome

Running main.py transforms raw housing data into a clean, standardized, one-hot-encoded, machine-learning-ready dataset in a single command.

This script represents the final automated ETL solution developed through a structured, step-by-step data science workflow.

---
