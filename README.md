# GmE 221 – Laboratory 4: Spatial Statistics: Spatial Autocorrelation and Cluster Detection

# Overview
- This laboratory extends the analytical pipeline estblished in Laboratory 3. The focus shifts toward spatial statistical analysis. Instead of asking how mgeometry is constructed, we now ask if spatial values are randomly distributed, clustered, or dispersed across space?

# Environment Setup
- Python, GeoPandas, PySAL, Matplotlib, GitHub (PostGIS for storage only) 

# How to Run
- Activate the virtual environment
- Confirm PostGIS Database Setup
- Construct spatial weightsmatrices that degine neighborhod relationships
- Compute Global Moran's I to measure overall spatial autocorellation
- Compute Local Moran's I to identify spatial clusters.
- Detect hotspot and coldspot
- Visualize spatial statistical patterns
- Export spatial statistical results

# Output
- GeoJSON Output File 
- Local Moran's I Cluster Map
- Spatial Weights Graph Visualization

# Required Reflection - D. Interpreting the Neighborhood Structure
1. How does the spatial weights graph represent neighborhood relationships? Explain how parcel centroids and connecting lines correspond to nodes and edges in a spatial network.  
- Based on our previous lesson, the spatial weights graph represents neighborhood relationships by converting spatial features into a network structure. Each parcel centroid acts as a node, while the lines connecting centroids represent edges that define which parcels are considered neighbors. 
2. Change the spatial weights method and rerun the visualization. Compare the following methods: 
- contiguity weights - there are no changes because this is based on shared boundaries between parcels.
- K-nearest neighbors (KNN) - each parcel connects to a fixed number of nearest parcels based on the value of K.
- distance-based weights - this is based on the specified distance threshold.
3. Modify the parameter of one method. 
- Increasing the distance thrsehold shows more network resulting in more lines shown in the figure generated based on our 30 distance threshold.
4. Does increasing K or distance create a denser spatial network? 
- Increasing our distance shows a very dense green cluster in our graph especially in the area where each parcel is small. As discused on our previous lesson, increasing distance potentially increased Moran’s I which just mean stronger clustering.
5. Which spatial weights method do you think best represents the spatial relationships of parcels in your dataset? 
- Among the three methods, only contiguity weights remain consistent because they do not rely on adjustable parameters. Instead, they are based purely on the geometry of the parcels. This preserves the true geographic structure of the dataset, making contiguity weights the most appropriate method for representing spatial relationships between parcels.
6. Why is it important to visualize spatial weights before computing Moran’s I? 
- Visualizing spatial weights is important because it ensures that the neighborhood structure is correct before analysis. By visualizing the graph, errors in connectivity can be detected early, preventing incorrect conclusions in spatial statistics.

# Required Reflection - E. Global Autocorrelation 
1. What does positive Moran’s I indicate?
- ass_ass_va shows a slightly higer Moran's I and a positive Moran’s I indicates spatial clustering, meaning parcels with similar values (high or low) are located near each other.
2. Why is the p-value required for interpretation? 
- The p-value is needed to determine if the result is statistically significant.
3. What would Moran’s I near zero suggest? 
- A Moran's I near zero suggest a random spatial pattern, meaning there is no clear clustering or dispersion in the data.
4. What is the role of the attribute in computing Moran’s I?
- The choice of attribute matters because different attributes have different spatial patterns. When processing the same attribute, ass_ass_va shows a stronger clustering compare to ass_market that are a bit more spread out.
5. How the spatial autocorrelation result might change when a different attribute is analyzed. 
- Changing the attributes result in a different Moran’s I values and interpretations.
6. Why Moran’s I requires both a spatial weights matrix and an attribute variable. 
- Attribute variable provides the value needed for comparison, without the attribute there is nothing to analyze. While spatial weights matrix defines who is the neighbor which defines the relationships.

# Required Reflection - F. Interpreting Local Spatial Autocorrelation
1. What is the difference between Global Moran’s I and Local Moran’s I?
- Moran's I comes in two types, the Global and Local. Global Moran's I measures spatial autocorrelation for the entire dataset. It gives one value that summarizes whether the data is clustered, dispersed, or random. While, Local Moran’s I measures spatial autocorrelation at the individual parcel level. It identifies specific locations where clustering or outliers occur.
2. How are hotspots and coldspots identified using Local Moran’s I?
- Hotspots and coldspots are identified using both the Local Moran’s I value and the p-value. 
- Hotspot are high values surrounded by high values. Their Local Moran's I should  be greater than zero and p-value is less than 0.05. 
- Coldspot are low values surrounded by low values. Their Local Moran's I should be less than zero and p-value is less than 0.05.
3. Where do hotspots appear in your dataset? 
- Hotspot which are the red parcels are mainly concentrated in the central portion of the map, the possible explanation for this is that these areas are likely more developed and located near main roads or accesible areas that may have higher land demand or better infrastructure.
4. Where do coldspots appear in your dataset?
-  Blue parcels are the coldspots which are mostly found in the lower right side of the map and are scattered near the edges. These areas may be less developed and farther from main road which means lower economic activity that may result in clusters of lower parcel values.
5. Did you observe any spatial outliers? 
- A spatial outlier occurs when a parcel has a value very different from its neighbors. There are parcels that are among the red parcels and vice versa, which means that a high value parcel is surrounded by a low value neighbor and also vice versa. The possible reason for this is the data may be inconsistent or there's a suddden change of land value or there is a unique landuse for that parcel.
6. How does changing the spatial weights method affect Local Moran’s I results? 
- Hotspot and coldspot locations can change when using a different spatial weights method. This can make our cluster smaller or larger or a few hotspots/coldspots may appear or disappear.
- Changing the parameter of the spatial weights affect the result of Local Moran's I. After increasing the threshold for our Distance, more parcels are defined as hotspot. 
7. How does changing the attribute affect the spatial clusters?
- Changing the attribute changes the spatial clusters because each variable has a different value distribution, which affects how parcels relate to their neighbors in Local Moran’s I analysis.