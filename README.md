# 🏠 CodeTech Internship – Project 1: Automated ETL Pipeline for Housing Data

This repository contains my submission for Project 1 of the CodeTech Internship Program.

The objective of this project was to design and implement an automated ETL (Extract, Transform, Load) pipeline using Python and scikit-learn.

To solve this problem, I used the California Housing dataset as a realistic case study to understand how raw housing data can be transformed into a clean, structured, and machine-learning-ready dataset.

---

## 🎯 Project Motivation

Housing prices are influenced by many factors such as income levels, number of rooms, population density, and geographic location.

In rapidly developing cities like Gurgaon, understanding these relationships can help buyers, sellers, and analysts make better real estate decisions.

Since a large, clean Gurgaon housing dataset was not readily available, I used the California Housing dataset as a practical substitute to build and validate the complete ETL workflow.

The same approach can later be applied to real housing data from Gurgaon or any other city.

---

## 📂 Repository Structure

```text
project-1/
│
├── Data/
│   ├── housing.csv
│   ├── housing_prepared.csv
│   └── data_README.md
│
├── Jupyter_Notebook/
│   ├── 01_Analyzing_data.ipynb
│   ├── 02_Creating_a_test_set.ipynb
│   ├── 03_Stratified_test_spliting.ipynb
│   ├── 04_Visualizing_the_data.ipynb
│   ├── 05_Further_Preprocessing&Handling_Missing_Values.ipynb
│   ├── 06_Handling_categorical_values.ipynb
│   ├── 07_Feature_Scaling.ipynb
│   ├── 08_sklearn_pipelines.ipynb
│   └── README.md
│
├── Python_src/
│       ├── main.py
│       └── src_README.md
│
└── README.md
```

---

## 📘 Project Workflow

### 1. Data Understanding
Explored the dataset and studied feature distributions, correlations, and missing values.

### 2. Train-Test Splitting
Created both manual and stratified train-test splits.

### 3. Data Visualization
Visualized important patterns and relationships.

### 4. Data Cleaning
Handled missing numerical values.

### 5. Categorical Encoding
Converted categorical attributes using One-Hot Encoding.

### 6. Feature Scaling
Standardized numerical features.

### 7. Pipeline Automation
Combined all preprocessing steps into a reusable ETL pipeline.

### 8. Export Processed Data
Saved the transformed dataset for future machine learning tasks.

---

## ⚙️ Final Python Script

The final implementation is located in:

```text
Python_src/main.py
```

This script automates the complete ETL workflow and saves the processed output to:

```text
Data/housing_prepared.csv
```

---

## 📊 Dataset Source

The dataset used in this project was downloaded from Kaggle:

https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

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
- Jupyter Notebook

---

## 🚀 How to Run the Project

Navigate to the Python source folder and execute:

```bash
python main.py
```

---

## ✅ Final Outcome

This project demonstrates a complete end-to-end ETL workflow for housing data.

Starting from raw CSV data, the pipeline automatically:

- Loads the dataset
- Performs stratified sampling
- Cleans missing values
- Encodes categorical features
- Scales numerical attributes
- Produces a machine-learning-ready dataset

The final output is a clean and fully transformed dataset ready for downstream analysis and predictive modeling.

---

## 👨‍💻 Author

Aditya Chaudhary<br>  
B.Tech Computer Science Engineering Student<br>  
Data Science and Python Enthusiast  

---