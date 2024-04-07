#This python script is for the hypothesis test to see if extreme climate change affects crop yield

import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('updated_final_dataframe.csv')
affected_countries = ['PHL']
affected_data = df[df['Code'].isin(affected_countries)]
pre_eruption_year = 1990 
post_eruption_year = 1992
pre_eruption_data = affected_data[affected_data['Year'] <= pre_eruption_year]
post_eruption_data = affected_data[affected_data['Year'] >= post_eruption_year]
t_stat, p_value = stats.ttest_ind(
...     pre_eruption_data['Cereal yield kg per hectar'],
...     post_eruption_data['Cereal yield kg per hectar'],
...     equal_var=False)
print(f'T-statistic: {t_stat}, P-value: {p_value}')
