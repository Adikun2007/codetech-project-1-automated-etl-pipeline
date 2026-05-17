import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline


# 1. Load the Dataset
housing = pd.read_csv("../Data/housing.csv")

# 2. Create a stratified train & test set
housing['income_cat'] = pd.cut(housing["median_income"],
                               bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf], 
                               labels=[1, 2, 3, 4, 5])

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index].drop("income_cat", axis=1) # We will work on this data
    strat_test_set = housing.loc[test_index].drop("income_cat", axis=1) # Set aside the test data

# We will work on the copy of training data
housing = strat_train_set.copy()

# 3. Seperate features and labels
housing_labels = housing["median_house_value"].copy() #Labels
housing = housing.drop("median_house_value", axis=1) #Features

# 4. List the numerical and categorical columns
num_attribs = housing.drop("ocean_proximity", axis=1).columns.tolist()
cat_attribs = ["ocean_proximity"]

# 5. Lets make the pipeline

# For numerical columns
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# For categorical columns
cat_pipeline = Pipeline([
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# Construct the full pipeline
full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs)
])

# 6. Transform the data
housing_prepared = full_pipeline.fit_transform(housing)

# 7. Convert to DataFrame
feature_names = full_pipeline.get_feature_names_out()
housing_prepared_df = pd.DataFrame(
    housing_prepared,
    columns=feature_names
)

# 8. Save Final Processed Data to data Folder
housing_prepared_df.to_csv(
    "../Data/housing_prepared.csv",
    index=False
)

print("ETL pipeline completed successfully.")
print("Processed data saved to: ../Data/housing_prepared.csv")
print("Shape of transformed data:", housing_prepared_df.shape)