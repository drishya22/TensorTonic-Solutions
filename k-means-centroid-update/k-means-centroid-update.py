import numpy as np

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    Works for any dimensionality.
    """
    
    clusters = {i: [] for i in range(k)}
    
    for i in range(len(assignments)):
        clusters[assignments[i]].append(points[i])
    
    result = []
    
    for i in range(k):
        if len(clusters[i]) == 0:
            result.append([0.0] * len(points[0]))
        else:
            centroid = np.mean(clusters[i], axis=0)
            result.append(centroid.tolist())
    
    return result