# PM2.5 Air Quality Index - Data Analysis 
This analysis aims to understand the PM2.5 air quality index in several station in Beijing from 2013 to 2017. We use data from public (https://github.com/marceloreis/HTI/tree/master)

# Project Structure
dashboard/: This directory contains dashboard.py which is used to create dashboards of data analysis results.
data/: Directory containing the raw CSV data files.
notebook.ipynb: This file is used to perform data analysis.
README.md: This documentation file.

# Installation
1. Clone this this repository to your local machine: git clone https://github.com/mamansptr/streamlit_pm25.git
2. Go to the project directory: cd streamlit_pm25
3. Install the required Python packages by running: pip install -r requirements.txt

# Usage
1. Data Wrangling: Data wrangling scripts are available in the notebook.ipynb file to prepare and clean the data.
2. Exploratory Data Analysis (EDA): Explore and analyze the data using the provided Python scripts. EDA insights can guide your understanding of air quality data.
3. Visualization: Run the Streamlit dashboard for interactive data exploration: streamlit run dashboard.py
Access the dashboard in your web browser at http://localhost:8501
