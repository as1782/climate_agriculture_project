#This script is for the Mann-Kendall Trend Test

import pandas as pd

import pymannkendall as mk

df = pd.read_csv('dataframe.csv')

#Ensure to change the key from 'GBR' to the corresponding regional code to perform tests on different regions

uk_data = df[df['Code'] == 'GBR']

#Ensure to change the result variable to the corresponding variable

result_uk = mk.original_test(uk_data['Annual_Temp'])

print(result_uk)

#Trend test for cereal yield trend ensure to change the variables for the corresponding regions

uk_cereal_yield_data = df[df['Code'] == 'GBR']['Cereal yield kg per hectar']

result_cereal_yield = mk.original_test(uk_cereal_yield_data)

print(result_cereal_yield)

#Trend test for CO2 emissions ensure to change the variables for the corresponding regions

uk_co2_emissions_data = df[df['Code'] == 'GBR']['Annual CO₂ emissions (per capita)']

result_co2_emissions = mk.original_test(uk_co2_emissions_data)

print(result_co2_emissions)




