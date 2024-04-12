# Climate Agriculture Project

## Introduction

This project uses a Python virtual environment to manage dependencies and requires the installation of R on your machine if you don't already have it. Follow the instructions in Environment Setup to set up your environment. This repository serves as a purpose to display the source code for this project moreover it allows for others to contribute work to this project. 

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
  trend_tests.py]

dataset
  [dataframe.csv]

sources
  [co2_clean.csv
  precipitation_cereal_yield_clean.csv
  temperature_clean.csv]

R_scripts
  [regression_model.R]
     
## Running Instructions

In order to replicate the output. Ensure to have all the required files, in one directory for the ease of replication. Start with booting up python on your machine, then run the summary_analysis.py script first to get the summary table for the dataset. Next for the EDA section run the EDA_visuals.py script to get the graphs. For this section, plots can be made for specific countries, detailed instructions are in the script. Next section is the trend test, this trend test can also be performed on different geographic regions, this the also detailed in the trend_tests.py python script. The next section involves the hypothesis tests which can be run using the hypothesis_test.py script. Lastly for the regression analysis we will be utilising R, ensuring that you have R installed and an IDE for running the regression_model.R script such as Rstudio. Run the script ensuring the right dataset has been selected.

## Data Sources
co2_clean.csv : Global Carbon Budget (2023); Population based on various sources (2023) – with major processing by Our World in Data. “Per capita CO₂ emissions – GCB” [dataset]. Global Carbon Project, “Global Carbon Budget”; Various sources, “Population” [original data]. Retrieved April 8, 2024 from https://ourworldindata.org/grapher/co-emissions-per-capita

precipitation_cereal_yield_clean.csv : https://www.theglobaleconomy.com

temperature_clean.csv : Copernicus Climate Change Service (2024) – with major processing by Our World in Data. “2024” [dataset]. Copernicus Climate Change Service, “ERA5 monthly averaged data on single levels from 1940 to present 2” [original data].

## About
If there are any queries, additions, issues or bugs that could added/fixed regarding this project feel free to fork the repository and send a push request with the changes you seem fit.





