import pandas as pd
import geopandas as gpd

# load data
data = pd.read_excel(r"Excel data path")
countries = gpd.read_file(r"Shapefile path")

# only keep some columns
countries = countries[['NUTS_ID', 'geometry']]

# merge on columns
output = pd.merge(countries, data, left_on='NUTS_ID', right_on='NUTS_ID')

# save as shapefile
output.to_file(r"Shapefile output path", encoding='utf-8') 