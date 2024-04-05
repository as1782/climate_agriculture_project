# Climate Agriculture Project

## Environment Setup

This project uses a Python virtual environment to manage dependencies. Follow the steps to set up your environment:

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

## Data Sources
co2_clean.csv : Global Carbon Budget (2023), Population based on various sources (2023)

precipitation_cereal_yield_clean.csv : https://www.theglobaleconomy.com

temperature_clean.csv : Copernicus Climate Change Service (2024)







