import geopandas as gpd 
from sqlalchemy import create_engine 
from spatial_weights import contiguity_weights, knn_weights, distance_weights
from visualization import visualize_neighbors
from moran import calculate_global_morans_I
from esda.moran import Moran_Local
import os
from visualization import visualize_local_moran

host = "localhost" 
port = "5432" 
dbname = "gme221_exer4" 
user = "postgres" 
password = "#Akonaito1234" 

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}" 

engine = create_engine(conn_str) 
sql_query = """ 
SELECT gid, ass_ass_va, ass_market, geom 
FROM public.assessed_parcels; 
""" 
gdf = gpd.read_postgis(sql_query, engine, geom_col="geom") 

# print(gdf.head()) 
# print("CRS:", gdf.crs) 

# spatial weights

w = distance_weights(gdf)

# print("Neighbors:", w.neighbors)

# visualization

# visualize_neighbors(gdf, w)

# Moran Module

attribute = "ass_market" 

moran_I, p_value = calculate_global_morans_I(gdf, w, attribute) 

print("Global Moran's I:", moran_I) 

print("p-value:", p_value)


# Plotting of Moran's I
# from plotting import plot_moran_scatter

# plot_moran_scatter(gdf, w, attribute)

# Local Spatial Autocorrelation

local = Moran_Local(gdf["ass_ass_va"], w) 

gdf["local_I"] = local.Is 
gdf["p_value"] = local.p_sim 

gdf["cluster"] = "Not Significant" 

gdf.loc[(gdf["local_I"] > 0) & (gdf["p_value"] < 0.05), "cluster"] = "Hotspot" 
gdf.loc[(gdf["local_I"] < 0) & (gdf["p_value"] < 0.05), "cluster"] = "Coldspot" 

os.makedirs("output", exist_ok=True) 

gdf.to_file( 
    "output/spatial_clusters.geojson", 
    driver="GeoJSON" 
) 

print("Saved: output/spatial_clusters.geojson")

# Visualize Local Moran's I

visualize_local_moran(gdf) 
