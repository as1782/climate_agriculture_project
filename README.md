# Climate Agriculture Project

## Introduction

This project uses a python virtual environment to manage dependencies and requires the installation of R, an IDE such as R Studio and python on your machine if you don't already have it. Follow the instructions in Environment Setup to set up your environment. This repository serves as a purpose to display the source code for this project moreover it allows for others to contribute work to this project. 

## Environment Setup

Follow the steps to set up your environment:

1. **Clone the Repository**
First, clone the project repository to your local machine:
https://github.com/as1782/climate_agriculture_project.git
cd climate_agriculture_project

2. **Create and Activate the Virtual Environment**
Ensure you have `virtualenv` installed. If not, install it using pip:
pip install virtualenv

Create a new virtual environment named `venv`:
virtualenv venv

Activate the virtual environment:

- On macOS and Linux:
source venv/bin/activate

- On Windows:
venv\Scripts\activate

3. **Install Required Packages**
Install all dependencies listed in `requirements.txt`:
pip install -r requirements.txt

4. **Deactivating the Virtual Environment**
When you're done working, you can deactivate the virtual environment by running:
deactivate

## Repo Overview

README.md

venv

requirements.txt  

python_scripts
  [EDA_visuals.py
  hypothesis_test.py
  summary_analysis.py
  trend_tests.py regression_model.py]

dataset
  [dataframe.csv]

sources
  [co2_clean.csv
  precipitation_cereal_yield_clean.csv
  temperature_clean.csv]

R_scripts
  [regression_model.R]
     
## Running Instructions
To generate the expected results, please follow the steps outlined below. Ensure that all necessary files are placed within the same directory to facilitate straightforward replication.

### Data Summary
1. To obtain a summary table of the dataset, execute the summary_analysis.py script. This script will output a comprehensive overview of the data at hand.

### Exploratory Data Analysis (EDA)
2. Execute the EDA_visuals.py script to produce the required graphical representations for the exploratory analysis. This script allows the creation of plots tailored to specific countries. For detailed instructions, please refer to the comments within the script itself.

### Trend Analysis
3. To conduct trend analysis on various geographic regions, execute the trend_tests.py script. Detailed guidelines for conducting these tests are included within the script.

### Hypothesis Testing
4. For hypothesis testing, execute the hypothesis_test.py script. This will carry out the necessary statistical tests as per the hypotheses defined.

### Regression Analysis 
5. Run the regression_model.R script on an IDE suitable for running R scripts. Make certain that the correct dataset is loaded before executing the script.

### Alternative Regression Analysis in Python
6. If you prefer using Python, an equivalent regression_model.py script is provided. This script replicates the regression model in the Python environment. Execute this script if you opt for a Python-based analysis.

## Data Sources
co2_clean.csv : Global Carbon Budget (2023); Population based on various sources (2023) – with major processing by Our World in Data. “Per capita CO₂ emissions – GCB” [dataset]. Global Carbon Project, “Global Carbon Budget”; Various sources, “Population” [original data]. Retrieved April 8, 2024 from https://ourworldindata.org/grapher/co-emissions-per-capita

precipitation_cereal_yield_clean.csv : https://www.theglobaleconomy.com

temperature_clean.csv : Copernicus Climate Change Service (2024) – with major processing by Our World in Data. “2024” [dataset]. Copernicus Climate Change Service, “ERA5 monthly averaged data on single levels from 1940 to present 2” [original data].

## About
If there are any queries, additions, issues or bugs that could added/fixed regarding this project feel free to fork the repository and send a push request with the changes you seem fit.





