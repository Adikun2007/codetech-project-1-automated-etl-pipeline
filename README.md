# CodeTech Internship – Project 1: Automated ETL Pipeline

This repository contains my work for the first project assigned during my CodeTech Internship.

The objective of this project is to build an automated ETL (Extract, Transform, Load) pipeline using Python, Pandas, and scikit-learn.

For this project, I chose to work with the California Housing dataset. Although the internship task did not specify a dataset, I wanted to approach the problem through a realistic business scenario inspired by house price prediction in Gurgaon, India. Since a dedicated Gurgaon housing dataset was not readily available, I used the California dataset as a proxy to understand and implement the complete workflow.

The same ETL approach can later be applied to real housing data from Gurgaon or any other city.

---

## 📥 Dataset

You can download the dataset in either of the following ways:

- Search for **Housing Prices Dataset** on Kaggle and download it manually.
- Or download it directly from:
  https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

---

## 📘 Work Completed So Far

### 📊 `01_Analyzing_data.ipynb`

In this notebook, I performed exploratory data analysis (EDA) to understand the dataset. This included:

- Loading the dataset
- Inspecting feature names and data types
- Generating summary statistics
- Checking for missing values
- Exploring distributions and correlations

This step helped me understand the structure and quality of the data before splitting it.

---

### 🔀 `02_Creating_a_test_set.ipynb`

In this notebook, I implemented a custom function to split the dataset into training and testing sets.

```python
def shuffle_and_split_data(data, test_ratio):
    np.random.seed(42)  # Ensures reproducible random splits
    shuffled_indices = np.random.permutation(len(data))
    test_size = int(len(data) * test_ratio)

    test_indices = shuffled_indices[:test_size]
    train_indices = shuffled_indices[test_size:]

    return data.iloc[train_indices], data.iloc[test_indices]
```

---

### 📌 `03_Stratified_test_spliting.ipynb`

In this notebook, I improved the splitting approach by using `StratifiedShuffleSplit` from scikit-learn.

Created a new column 'income_cat' that categorizes the median_income into five bins. Each bin represents a range of income levels, allowing us to stratify our sampling based on these categories.

```python
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(
    n_splits=1,
    test_size=0.2,
    random_state=42
)

for train_index, test_index in split.split(data, data["income_cat"]):
    strat_train_set = data.loc[train_index]
    strat_test_set = data.loc[test_index]
```

This ensured that the distribution of income categories was preserved in both the training and testing sets, resulting in more representative samples.

---

## 🛠 Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- scikit-learn
- Jupyter Notebook

---

## 📂 Repository Structure

```text
codetech-project-1-automated-etl-pipeline/
│
├── 01_Analyzing_data.ipynb
├── 02_Creating_a_test_set.ipynb
├── 03_Stratified_test_spliting.ipynb
└── README.md
```

---

## 📌 Current Status

Completed so far:

- Exploratory Data Analysis (EDA)
- Manual train-test splitting
- Stratified train-test splitting

Status: In Progress 🚧

---

## 👨‍💻 Author

Aditya Chaudhary  
B.Tech Computer Science Engineering Student  
Data Science and Python Enthusiast  

---