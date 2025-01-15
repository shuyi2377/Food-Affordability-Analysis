# Import necessary libraries
import os
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns

data_folder = os.path.join(os.getcwd(), 'data')  # Locate the 'data' folder in the current working directory
file_name = 'food_afford_data.xls'  # Name of the Excel data file
file_path = os.path.join(data_folder, file_name)  # Combine folder and file name to form the full path

# Load the dataset
# Read the dataset from the specified Excel file.
# The sheet name is explicitly provided to ensure the correct data is loaded.
data = pd.read_excel(file_path, sheet_name='Food_afford_cdp_co_region_ca')

#DDo data cleaning and preparation
# Select only the relevant columns needed for the analysis: 'cost_yr', 'median_income', 'affordability_ratio'.
# Drop rows with missing values to avoid errors in subsequent calculations.
analysis_data = data[['cost_yr', 'median_income', 'affordability_ratio']].dropna()

# Calculate cost-to-income ratio
# Create a new column 'cost_ratio' that calculates the ratio of 'cost_yr' (annual food costs)
# to 'median_income' (median income). This ratio measures the proportion of income spent on food.
analysis_data['cost_ratio'] = analysis_data['cost_yr'] / analysis_data['median_income']

# Visualize cost ratio vs. affordability ratio
# Create a scatter plot to visualize the relationship between 'cost_ratio' and 'affordability_ratio'.
# - 'cost_ratio' is plotted on the x-axis (independent variable).
# - 'affordability_ratio' is plotted on the y-axis (dependent variable).
# Use alpha=0.7 for slight transparency and color='blue' for consistent aesthetics.
plt.figure(figsize=(10, 6))  # Define the figure size
sns.scatterplot(
    x='cost_ratio', 
    y='affordability_ratio', 
    data=analysis_data, 
    alpha=0.7, 
    color='blue'
)
plt.title('Relationship between Cost-to-Income Ratio and Food Affordability Ratio', fontsize=14)  # Add a descriptive title
plt.xlabel('Cost-to-Income Ratio', fontsize=12)  # Label the x-axis
plt.ylabel('Affordability Ratio', fontsize=12)  # Label the y-axis
plt.grid(True)  # Add a grid for better readability
plt.show()  # Display the plot

#Group data by cost ratio and calculate group statistics
# Define bins to group the 'cost_ratio' values into specific intervals:
# - e.g., [0, 0.2], [0.2, 0.4], ..., >1.0
# Label the bins for easy interpretation.
bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0, float('inf')]  # Define bin edges
labels = ['0-0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8-1.0', '>1.0']  # Define labels for each bin
analysis_data['cost_ratio_group'] = pd.cut(analysis_data['cost_ratio'], bins=bins, labels=labels)

# Group data by the 'cost_ratio_group' column and calculate the mean 'affordability_ratio' for each group.
group_stats = analysis_data.groupby('cost_ratio_group')['affordability_ratio'].mean().reset_index()

# Visualize group-wise affordability ratio
# Create a bar plot to show the average 'affordability_ratio' for each 'cost_ratio_group'.
# This visualizes how affordability changes with increasing cost-to-income ratio.
plt.figure(figsize=(10, 6))  # Define the figure size
sns.barplot(
    x='cost_ratio_group', 
    y='affordability_ratio', 
    data=group_stats, 
    palette='Blues_d'  # Use a blue gradient palette for aesthetics
)
plt.title('Average Food Affordability Ratio by Cost-to-Income Ratio Group', fontsize=14)  # Add a descriptive title
plt.xlabel('Cost-to-Income Ratio Group', fontsize=12)  # Label the x-axis
plt.ylabel('Average Affordability Ratio', fontsize=12)  # Label the y-axis
plt.grid(True, axis='y')  # Add a horizontal grid for better readability
plt.show()  
