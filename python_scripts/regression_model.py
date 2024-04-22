#This script is for the regression model analysis for those who feel more comfortable using python

import statsmodels.api as sm

import pandas as pd

#Ensure the path to the dataframe is correct before importing the csv file

df = pd.read_csv('dataframe.csv')

df_clean = df.dropna()

Y = df_clean['Cereal yield kg per hectar']

X = df_clean[['Precipitation mm per year', 'Annual CO₂ emissions (per capita)', 'Annual_Temp']]

X = sm.add_constant(X)

model = sm.OLS(Y, X).fit()

model.summary()


