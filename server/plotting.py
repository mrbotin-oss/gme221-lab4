import matplotlib.pyplot as plt
import numpy as np
from libpysal.weights import lag_spatial


def plot_moran_scatter(gdf, weights, attribute):

    x = gdf[attribute].values

    # spatial lag (neighbors' values)
    lag_x = lag_spatial(weights, x)

    # standardize values (z-score)
    x_std = (x - x.mean()) / x.std()
    lag_x_std = (lag_x - lag_x.mean()) / lag_x.std()

    plt.figure(figsize=(8, 6))

    plt.scatter(x_std, lag_x_std, alpha=0.6)

    # regression line
    b, a = np.polyfit(x_std, lag_x_std, 1)
    plt.plot(x_std, a + b * x_std)

    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')

    plt.title("Moran's I Scatter Plot")
    plt.xlabel("Standardized Values")
    plt.ylabel("Spatial Lag")

    plt.show()