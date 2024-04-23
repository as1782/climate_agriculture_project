#This is the python script for the Causual Forest Model

import pandas as pd

from econml.grf import CausalForest

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv('dataframe.csv')

#There is some missing data that we have to account for by deletion

clean_data = data.dropna(subset=['Precipitation mm per year', 'Annual CO₂ emissions (per capita)', 'Annual_Temp', 'Cereal yield kg per hectar'])

#This model has used annual tempretures as treatment variables and precipitation, co2 emissions as covariates to control for and crop yield being outcome variable.
#If you wish to use diffrent variables assign them as follows X = covariates, W = treatment variables (this model is only built for a single treatment variable), y = outcome variable

X = clean_data[['Precipitation mm per year', 'Annual CO₂ emissions (per capita)']]

y = clean_data['Cereal yield kg per hectar']

W = clean_data['Annual_Temp']

causal_forest = CausalForest(n_estimators=100, min_samples_leaf=10, verbose=0, random_state=123)

causal_forest.fit(X, y, W)

predicted_effects = causal_forest.predict(X)

#Causual effect summary table

mean_effect = np.mean(predicted_effects)

median_effect = np.median(predicted_effects)

std_dev_effect = np.std(predicted_effects)

min_effect = np.min(predicted_effects)

max_effect = np.max(predicted_effects)

quantiles_effect = np.quantile(predicted_effects, [0.25, 0.75])

summary_stats = {"Mean": mean_effect, "Median": median_effect, "Standard Deviation": std_dev_effect, "Min": min_effect,
"Max": max_effect, "25th Percentile": quantiles_effect[0], "75th Percentile": quantiles_effect[1]}

for stat, value in summary_stats.items():
    print(f"{stat}: {value}")

#Visual for the causual forest model

plt.figure(figsize=(10, 6))

sns.regplot(x=W, y=predicted_effects, lowess=True, line_kws={'color': 'red'})

plt.xlabel('Annual Temperature (°C)')

plt.ylabel('Estimated Causal Effect on Crop Yield')

plt.title('Causal Effect of Temperature on Crop Yield')

plt.show()
