# 📘 Jupyter Notebooks – Step-by-Step Development of the Automated ETL Pipeline

This folder contains the complete step-by-step development process I followed to solve CodeTech Internship Project 1: Automated ETL Pipeline.

Instead of directly writing a single Python script, I first worked through each preprocessing stage individually using Jupyter Notebooks. This helped me understand the purpose and implementation of every ETL component before combining them into a fully automated Python script.

---

## 🎯 Internship Problem Statement

The task assigned by CodeTech was to build an automated ETL pipeline that:

- Extracts data from a CSV file
- Cleans and preprocesses the data
- Handles missing values
- Encodes categorical variables
- Scales numerical features
- Produces transformed data ready for analysis or machine learning

---

## 🧠 Dataset Selection and Project Mindset

To solve this problem, I used the California Housing dataset.

Although the dataset contains housing information from California, I treated it as a realistic housing analytics project similar to predicting property prices in Indian cities such as Gurgaon, Noida, or Delhi.

My objective was to understand how raw housing data can be transformed into clean, structured, and machine-learning-ready data through an automated ETL pipeline.

---

## 📂 Step-by-Step Notebook Workflow

### 📊 01_Analyzing_Data.ipynb
Explored the dataset structure, data types, summary statistics, and missing values.

### 🔀 02_Creating_a_Test_Set_Using_Python_Function.ipynb
Built a custom Python function to manually split the dataset into training and testing sets.

### 📌 03_Creating_a_Test_Set_Using_StratifiedShuffleSplit.ipynb
Used scikit-learn's StratifiedShuffleSplit to preserve income category distributions.

### 📈 04_Visualizing_the_Data.ipynb
Created visualizations to identify important patterns and correlations.

### 🧹 05_Further_Preprocessing.ipynb
Handled missing values using SimpleImputer.

### 🏷️ 06_Handling_Categorical_Values.ipynb
Encoded the ocean_proximity categorical feature using One-Hot Encoding.

### ⚖️ 07_Feature_Scaling.ipynb
Standardized numerical features using StandardScaler.

### ⚙️ 08_Creating_an_Automated_Pipeline.ipynb
Combined all preprocessing steps into a reusable scikit-learn Pipeline and ColumnTransformer.

---

## 🐍 Final Python Implementation

After understanding and validating each step through Jupyter Notebooks, I consolidated the complete workflow into a standalone Python script:

Python_src/main.py

This script:

- Loads the raw housing dataset
- Performs stratified train-test splitting
- Handles missing values
- Encodes categorical features
- Scales numerical columns
- Executes the full ETL pipeline automatically
- Saves the transformed output as `housing_prepared.csv` in the `data/` folder

---

## 📁 Folder Structure

    project-1/
    │
    ├── data/
    │   ├── housing.csv
    │   └── housing_prepared.csv
    │
    ├── notebooks/
    │   ├── 01_Analyzing_Data.ipynb
    │   ├── 02_Creating_a_Test_Set_Using_Python_Function.ipynb
    │   ├── 03_Creating_a_Test_Set_Using_StratifiedShuffleSplit.ipynb
    │   ├── 04_Visualizing_the_Data.ipynb
    │   ├── 05_Further_Preprocessing.ipynb
    │   ├── 06_Handling_Categorical_Values.ipynb
    │   ├── 07_Feature_Scaling.ipynb
    │   ├── 08_Creating_an_Automated_Pipeline.ipynb
    │   └── README.md
    │
    └── Python_src/
        └── main.py

---

## 📥 Loading the Dataset in Notebooks

Since the notebooks are located inside the `notebooks/` folder, the dataset is loaded using:

```python
housing = pd.read_csv("../Data/housing.csv")
```
---

## 🚀 Outcome

By working through these notebooks step by step, I developed a strong understanding of the ETL process and successfully built a fully automated pipeline that transforms raw housing data into clean, machine-learning-ready data.

---

👨‍💻 Author

Aditya Chaudhary
B.Tech Computer Science Engineering Student
Data Science and Python Enthusiast