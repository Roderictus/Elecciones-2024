# Import necessary libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# Load a sample shapefile

cdmxshp = gpd.read_file("C:\Proyectos\Elecciones-2024\data\shapefiles\CdMx Shp\SECCION_ELECTORAL.shp")

# Display the first few rows of the geodataframe
cdmxshp.head()

# Plot the shapefile
cdmxshp.plot()

