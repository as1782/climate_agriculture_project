#This python script is for the initial Explatory Data Analsyis section

import matplotlib.pyplot as plt

import seaborn as sns

import pandas as pd

df_with_global_averages = pd.read_csv('dataframe.csv')

global_data = df_with_global_averages[df_with_global_averages['Country'] == 'Global']

#Plots can be made for diffrent regions using the line below, ensure to uncomment the line of code and use the corresponding #Country name as a parameter. For each plot, change the global_data parameter to country_specific_data before running the #code.

#country_specific_data = df_with_global_averages[df_with_global_averages['Country'] == 'China']

#Plot for Tempretrue trends 

plt.figure(figsize=(10, 6))

sns.lineplot(data=global_data, x='Year', y='Annual_Temp')

plt.title('Global Average Temperature Trends Over the Years')

plt.xlabel('Year')

plt.ylabel('Average Annual Temperature (°C)')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

#Plot for Emission trends

plt.figure(figsize=(10, 6))

sns.lineplot(data=global_data, x='Year', y='Annual CO₂ emissions (per capita)')

plt.title('Global CO2 Emissions Per Capita Trends Over the Years')

plt.xlabel('Year')

plt.ylabel('CO2 Emissions Per Capita (t)')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

#Plot for Cereal Yield trends

plt.figure(figsize=(10, 6))

sns.lineplot(data=global_data, x='Year', y='Cereal yield kg per hectar')

plt.title('Global Cereal Yield Trends Over the Years')

plt.xlabel('Year')

plt.ylabel('Cereal Yield (kg per hectare)')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
