# Food-Affordability-Analysis
This project aims to analyze food affordability using publicly available data for various regions in California. The analysis explores multiple aspects of food affordability, including its relationship with income, family size, geographic factors, and cost-to-income ratios. The results are visualized using charts, maps, and statistical methods, with all scripts and data structured for reproducibility.

# Data Description
The analysis uses data from an Excel file: food_afford_data.xls. (downloaded from US government data)
Key fields include:
affordability_ratio: Ratio of food costs to income.
median_income: Median income for different regions.
cost_yr: Annual food costs.
ave_fam_size: Average family size in households with children under 18.
CA_RR_Affordability: Regional ratio of food affordability relative to state averages.
county_name: County-level data for geographic mapping.

# Key Libraries:
pandas: Data manipulation
matplotlib: Data visualization
seaborn: Advanced data visualization
scikit-learn: PCA and data preprocessing

# Scripts Introduction
Step01_DynamicTrendAnalysis.py
Purpose: Analyzes trends in food affordability ratios over time and across racial/ethnic groups.
Output: Line plots and grouped bar charts showing trends in affordability ratios.

Step02_RaceIncomeAnalysis.py
Purpose: Explores the relationship between race, income, and affordability.
Analysis:
Median income comparison by race/ethnicity.
Scatter plots with regression lines to show trends.
Output: Grouped bar charts and scatter plots.

Step03_MultiFactorPCA.py
Purpose: Performs principal component analysis (PCA) to understand the contribution of key variables to food affordability.
Analysis:
PCA loadings for key variables like income, family size, and costs.
Pairwise regression analysis between variables and affordability ratio.
Output: Heatmaps for PCA loadings and regression scatter plots.

Step04_CostIncomeAnalysis.py
Purpose: Visualizes food affordability ratios by county in California.
Analysis:
Geographic heatmaps showing regional disparities in affordability.
Output: Heatmaps based on GeoJSON data.

Step05_GeographicMap.py
Purpose: Examines the impact of cost-to-income ratios on affordability.
Analysis:
Scatter plots of cost-to-income ratio vs. affordability ratio.
Grouped bar charts for average affordability by cost ratio bins.
Output: Scatter plots and grouped bar charts.
