import pandas as pd
import pgeocode
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Load data
data = pd.read_csv('data.csv')

# Initialize pgeocode for UK postcodes
nomi = pgeocode.Nominatim('gb')

# Function to get latitude and longitude
def get_coordinates(postcode):
    result = nomi.query_postal_code(postcode)
    return result.latitude, result.longitude

# Extract coordinates
data[['latitude', 'longitude']] = data['Postcode'].apply(lambda x: pd.Series(get_coordinates(x)))

# Drop rows with missing values
data = data.dropna(subset=['latitude', 'longitude'])

# Group by latitude and longitude, and sum the frequencies for each group
data_grouped = data.groupby(['latitude', 'longitude'], as_index=False)['Frequency'].sum()

# Convert to a GeoDataFrame
gdf = gpd.GeoDataFrame(data_grouped, geometry=gpd.points_from_xy(data_grouped['longitude'], data_grouped['latitude']), crs="EPSG:4326")

# Reproject to a Web Mercator projection (for contextily basemaps)
gdf = gdf.to_crs(epsg=3857)

# Directly proportional scaling (adjust scale factor as needed)
scale_factor = 0.03
gdf['scaled_size'] = gdf['Frequency'] * scale_factor

# Plot map
fig, ax = plt.subplots(figsize=(12, 10))
gdf.plot(ax=ax, markersize=gdf['scaled_size'], alpha=0.7, color='blue', edgecolor='black')

# Add basemap
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

# Add labels
for idx, row in gdf.iterrows():
    ax.annotate(f"{row['Frequency']}",  # Added £ symbol
                xy=(row['geometry'].x, row['geometry'].y), 
                xytext=(5, 5), 
                textcoords="offset points", 
                ha='center', 
                fontsize=8, 
                color='red', 
                fontweight='bold')

# Formatting
ax.set_axis_off()
plt.title('Event Frequency by Postcode (Directly Proportional Bubble Size)')

# Show plot
plt.show()
