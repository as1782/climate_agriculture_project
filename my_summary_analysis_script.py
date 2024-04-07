#This is the python script for the initial summary analysis of the final_dataframe.csv file

import pandas as pd

df = pd.read_csv('final_dataframe.csv')

summary_statistics = df.describe(include='all')

missing_data = df.isnull().sum()

print(f"Missing data points: {missing_data}")

print(summary_statistics)

