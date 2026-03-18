from libpysal.weights import Rook, KNN, DistanceBand 

def contiguity_weights(gdf): # Rook - based on shared borders
    return Rook.from_dataframe(gdf)

def knn_weights(gdf, k=4): # KNN (k-nearest neighbors) - based on closest points
    coords = [(geom.centroid.x, geom.centroid.y) for geom in gdf.geometry] 
    return KNN(coords, k=k) 

def distance_weights(gdf, threshold=20): # DistanceBand - based on distance threshold
    coords = [(geom.centroid.x, geom.centroid.y) for geom in gdf.geometry]
    return DistanceBand(coords, threshold=threshold)