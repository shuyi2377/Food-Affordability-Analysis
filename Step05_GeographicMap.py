import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

# Define the folder containing the dataset and the Excel file name
# os.path.join ensures cross-platform compatibility for path creation

data_folder = os.path.join(os.getcwd(), 'data')  # Path to the 'data' folder
file_name = 'food_afford_data.xls'  # Name of the Excel file
file_path = os.path.join(data_folder, file_name)

# Load the Excel file
data = pd.ExcelFile(file_path)

# Parse the specific sheet containing food affordability data by county
main_data = data.parse('Food_afford_cdp_co_region_ca')  # Parse the relevant sheet

# Select relevant columns: 'county_name' and 'affordability_ratio'
# Drop rows with missing values to ensure data integrity
geo_data = main_data[['county_name', 'affordability_ratio']].dropna()

# Set up relative paths for the GeoJSON file containing California county geometries
project_root = os.getcwd() 
geojson_folder = os.path.join(project_root, 'geo_json')  
geojson_path = os.path.join(geojson_folder, 'california_counties.geojson')  

with open(geojson_path, 'r') as f:
    ca_counties = json.load(f)
    
# Create a dictionary to map each county's name to its affordability ratio
# This ensures easy lookup when matching geographic data with affordability ratios
county_affordability = {
    row['county_name']: row['affordability_ratio']
    for _, row in geo_data.iterrows()
}

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(15, 10))

# Normalize affordability_ratio for coloring
# Normalize maps values to a range between 0 and 1 based on min and max values
norm = Normalize(vmin=min(county_affordability.values()), vmax=max(county_affordability.values()))
cmap = plt.cm.YlOrRd  # Color map (yellow to red)

# Plot each county as a polygon
patches = []
colors = []
for feature in ca_counties['features']:
    county_name = feature['properties']['name']  # Use 'name' as the county identifier
    affordability = county_affordability.get(county_name, None)  # Get affordability ratio
    if affordability is not None:
        polygons = feature['geometry']['coordinates']
        if feature['geometry']['type'] == 'Polygon':
            polygons = [polygons]
        for polygon in polygons:
            poly_patch = Polygon(polygon[0], closed=True, edgecolor='black', linewidth=0.5)
            patches.append(poly_patch)
            colors.append(cmap(norm(affordability)))

# Add all patches to the plot
p = PatchCollection(patches, match_original=True)
p.set_facecolor(colors)
ax.add_collection(p)

# Add a color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, shrink=0.5)
cbar.set_label('Affordability Ratio', fontsize=12)

# Final plot adjustments
ax.set_xlim(-125, -114)  # Longitude bounds for California
ax.set_ylim(32, 42)  # Latitude bounds for California
ax.axis('off')  # Remove axes for cleaner visualization
plt.title('Food Affordability by County in California', fontsize=16)
plt.show()
