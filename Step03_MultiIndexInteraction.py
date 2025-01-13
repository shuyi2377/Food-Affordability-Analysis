import os
import pandas as pd
#import seaborn to visualize the relationship between variables and the affordability_ratio
#also to interpret the contribution of each variable to the principal components
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Define the relative file path
data_folder = os.path.join(os.getcwd(), 'data')  # Locate the 'data' folder in the current directory
file_name = 'food_afford_data.xls'  # Name of the Excel data file
file_path = os.path.join(data_folder, file_name)  # Construct the full relative file path

# Load the Excel file
data = pd.ExcelFile(file_path)  # Load the Excel file using pandas' ExcelFile for multi-sheet support
main_data = data.parse('Food_afford_cdp_co_region_ca')  # Parse the relevant sheet

# Preprocess the data
# Select relevant columns and drop missing values
analysis_data = main_data[['affordability_ratio', 'median_income', 'ave_fam_size', 'cost_yr', 'CA_RR_Affordability']].dropna()

# Standardize numerical data for PCA
# Standardizing 'median_income', 'ave_fam_size', 'cost_yr', 'CA_RR_Affordability'
scaler = StandardScaler()
numeric_data = analysis_data[['median_income', 'ave_fam_size', 'cost_yr', 'CA_RR_Affordability']]
scaled_data = scaler.fit_transform(numeric_data)

# Perform PCA
# Initialize PCA and fit the standardized data
pca = PCA(n_components=2)  # Extract the top 2 principal components
pca.fit(scaled_data)

# Extract PCA loadings (components) for each variable
loadings = pd.DataFrame(
    pca.components_.T,
    columns=['PC1', 'PC2'],
    index=['median_income', 'ave_fam_size', 'cost_yr', 'CA_RR_Affordability']
)

# Visualize PCA loadings as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(loadings, annot=True, cmap='coolwarm', cbar=True)
plt.title('PCA Loadings: Contribution of Variables to Principal Components', fontsize=14)
plt.xlabel('Principal Components', fontsize=12)
plt.ylabel('Variables', fontsize=12)
plt.tight_layout()
plt.show()

# Pairwise regression analysis with affordability_ratio
plt.figure(figsize=(12, 10))
for i, column in enumerate(['median_income', 'ave_fam_size', 'cost_yr', 'CA_RR_Affordability']):
    plt.subplot(2, 2, i + 1)
    sns.regplot(data=analysis_data, x=column, y='affordability_ratio', line_kws={'color': 'red'}, scatter_kws={'alpha': 0.6})
    plt.title(f'Relationship between {column} and Affordability Ratio', fontsize=10)
    plt.xlabel(column, fontsize=8)
    plt.ylabel('Affordability Ratio', fontsize=8)
    plt.tight_layout()
plt.show()
