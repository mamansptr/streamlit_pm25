import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# run in terminal: streamlit run dashboard.py

# load dataframe from google drive
import io
import requests
import pandas as pd

# Public link to the file hosted on cloud storage
file_url = "https://drive.google.com/file/d/1xXBK4ilP7sGmShvDpL1WTOqtgHa753AF/view?usp=sharing"

# Download the file using requests library
response = requests.get(file_url)

# Check if the download was successful
if response.status_code == 200:
    try:
        # Read the content of the response as a file-like object
        content = io.StringIO(response.text)
        
        # Read the CSV file into a DataFrame
        merged_df = pd.read_csv(content, encoding='utf-8')
        
        # Display the DataFrame in Streamlit
        st.write(merged_df)
    except Exception as e:
        st.error(f"Error reading CSV file: {str(e)}")
else:
    st.error("Failed to download the file. Please check the file URL.")
    
# Group by year and station, calculate mean PM2.5, and reset index
mean_by_year_and_station = merged_df.groupby(['year', 'station'])['PM2.5'].mean().reset_index()

# Pivot the dataframe to have years as rows, stations as columns, and mean PM2.5 values as values
pivot_mean = mean_by_year_and_station.pivot(index='year', columns='station', values='PM2.5').fillna(0)

# Plot the heatmap
st.subheader('Mean PM2.5 by Year and Station (Heatmap)')
selected_year = st.slider('Select Year', min_value=min(merged_df['year']), max_value=max(merged_df['year']), value=min(merged_df['year']))
filtered_data = pivot_mean[pivot_mean.index == selected_year]
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(filtered_data, cmap='viridis', annot=True, fmt=".2f", vmin=60, vmax=110, ax=ax)
ax.set_xlabel('Station')
ax.set_ylabel('Year')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Using Line Plot
st.subheader('Mean PM2.5 by Year and Station (Line Plot)')
selected_stations = st.multiselect('Select Stations', list(pivot_mean.columns), default=list(pivot_mean.columns))
fig, ax = plt.subplots(figsize=(12, 8))
for station in selected_stations:
    ax.plot(pivot_mean.index, pivot_mean[station], label=station)
ax.set_xlabel('Year')
ax.set_ylabel('Mean PM2.5')
ax.legend()
st.pyplot(fig)

# using Bar Plot
st.subheader('Mean PM2.5 by Station (Bar Plot)')
selected_year = st.slider('Select Year', min_value=min(merged_df['year']), max_value=max(merged_df['year']), value=min(merged_df['year']), key='barplot_year_slider')
filtered_data = mean_by_year_and_station[mean_by_year_and_station['year'] == selected_year]
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(data=filtered_data, x='station', y='PM2.5', ci=None, ax=ax)
ax.set_xlabel('Station')
ax.set_ylabel('Mean PM2.5')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)
