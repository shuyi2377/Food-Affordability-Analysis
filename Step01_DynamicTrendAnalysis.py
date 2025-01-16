import os  # Import os module for handling file paths
import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import Matplotlib for visualization
import seaborn as sns  # Import Seaborn for advanced visualization

# Define the relative file path
data_folder = os.path.join(os.getcwd(), 'data')  # Locate the 'data' folder in the current directory
file_name = 'food_afford_data.xls'  # File name of the dataset
file_path = os.path.join(data_folder, file_name)  # Construct the full file path

# Verify if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Data file not found at {file_path}. Please check the file name and path.")

# Load the dataset from the specified relative path
data = pd.ExcelFile(file_path)

# Parse the main sheet containing food affordability data
main_data = data.parse('Food_afford_cdp_co_region_ca')

# Filter the relevant columns for analysis
# Selecting 'reportyear', 'race_eth_name', and 'affordability_ratio'
trend_data = main_data[['reportyear', 'race_eth_name', 'affordability_ratio']].copy()

# Focus on a single year for analysis (e.g., "2006-2010")
# Filter the dataset to include only the desired year
single_year_data = trend_data[trend_data['reportyear'] == "2006-2010"]

# Sort data by affordability ratio for better visual clarity
single_year_data = single_year_data.sort_values(by='affordability_ratio', ascending=False)

# Create a bar plot to visualize affordability ratio by race
plt.figure(figsize=(12, 6)) 
sns.barplot(
    data=single_year_data,
    x='affordability_ratio',
    y='race_eth_name',
    hue='race_eth_name',  # Assign 'race_eth_name' to the hue parameter
    dodge=False,  # Avoid bar grouping since hue matches y variable
    palette='muted',  # Use the muted color palette
    legend=False  # Disable the legend as it is redundant
)

# Add titles and labels to the plot
plt.title('Food Affordability Ratio by Race/Ethnicity (2006-2010)', fontsize=14) 
plt.xlabel('Average Affordability Ratio', fontsize=12)  # Label the x-axis
plt.ylabel('Race/Ethnicity', fontsize=12)  # Label the y-axis

# Add gridlines to enhance readability
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add gridlines only for the x-axis

# Adjust layout to ensure no overlapping elements
plt.tight_layout()

# Display the final plot
plt.show()
