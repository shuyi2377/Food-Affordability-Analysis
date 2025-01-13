# Import necessary libraries
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the relative file path
data_folder = os.path.join(os.getcwd(), 'data')  # Locate the 'data' folder in the current directory
file_name = 'food_afford_data.xls' 
file_path = os.path.join(data_folder, file_name)  # Construct the full relative file path

# Load the Excel file
data = pd.ExcelFile(file_path)  # Load the Excel file using pandas' ExcelFile for multi-sheet support

# Parse the relevant sheet
main_data = data.parse('Food_afford_cdp_co_region_ca')  # Parse the sheet with relevant data

# Preprocess the data
# Select relevant columns and drop rows with missing values
analysis_data = main_data[['race_eth_name', 'median_income', 'affordability_ratio']].dropna()

# Define custom colors for high contrast (for third chart)
hue_colors = {
    'AIAN': 'red',
    'Asian': 'blue',
    'AfricanAm': 'green',
    'Latino': 'orange',
    'White': 'purple',
    'NHOPI': 'brown',
    'Multiple': 'pink',
    'Other': 'gray',
    'Total': 'black'
}

# Plot 1: Bar plot for Median Income by Race/Ethnicity
plt.figure(figsize=(10, 6))  # Set figure size for the bar plot
sns.barplot(
    data=analysis_data.groupby('race_eth_name', as_index=False)['median_income'].median(),
    x='median_income',
    y='race_eth_name',
    palette='muted'  # Use a muted color palette for aesthetics
)
plt.title('Median Income by Race/Ethnicity', fontsize=14)  # Add a title
plt.xlabel('Median Income', fontsize=12)  # Label the x-axis
plt.ylabel('Race/Ethnicity', fontsize=12)  # Label the y-axis
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add gridlines along the x-axis
plt.tight_layout()  # Adjust layout for better spacing
plt.show() 

# Plot 2: Scatter plot for Income vs Food Affordability Ratio by Race/Ethnicity
plt.figure(figsize=(12, 6))  # Set figure size for the scatter plot
sns.scatterplot(
    data=analysis_data,
    x='median_income',
    y='affordability_ratio',
    hue='race_eth_name',
    palette='Set2',  # Use a Set2 color palette for better distinction
    alpha=0.8  # Adjust transparency for better visibility of overlapping points
)
plt.title('Income vs Food Affordability Ratio by Race/Ethnicity', fontsize=14)  # Add a title
plt.xlabel('Median Income', fontsize=12)  # Label the x-axis
plt.ylabel('Food Affordability Ratio', fontsize=12)  # Label the y-axis
plt.grid(True)  # Add gridlines for better visual clarity
plt.tight_layout()  # Adjust layout for better spacing
plt.show() 

# Plot 3: Trend line plot for Income vs Food Affordability Ratio(show trends mainly)
sns.lmplot(
    data=analysis_data,
    x='median_income',  # Independent variable: income
    y='affordability_ratio',  # Dependent variable: affordability ratio
    hue='race_eth_name',  # Grouping variable: race
    palette=hue_colors,  # Apply the custom high-contrast colors
    aspect=1.5,  # Set aspect ratio for better readability
    ci=None,  # Disable confidence intervals for a cleaner plot
    scatter=False,  # Remove scatter points from the plot
    line_kws={'linewidth': 2}  # Set the line width for better visibility
)
plt.title('Income vs Food Affordability Ratio Trends by Race/Ethnicity', fontsize=14)  # Add a descriptive title
plt.xlabel('Median Income', fontsize=12)  # Label the x-axis for income
plt.ylabel('Food Affordability Ratio', fontsize=12)  # Label the y-axis for affordability ratio
plt.tight_layout()  # Ensure proper spacing
plt.show()  
