#This python script is for the initial Explatory Data Analsyis section

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df_with_global_averages = pd.read_csv('updated_final_dataframe.csv')
global_data = df_with_global_averages[df_with_global_averages['Country'] == 'Global']

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
plt.ylabel('CO2 Emissions Per Capita')
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
