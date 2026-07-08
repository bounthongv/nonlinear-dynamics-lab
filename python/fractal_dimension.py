"""
fractal_dimension.py — Correlation dimension (D2) for strange attractors

The correlation dimension measures the fractal dimension of a strange attractor
using the Grassberger-Procaccia algorithm.

    D2 = lim_{r→0} d(log C(r)) / d(log r)

where C(r) is the correlation integral: fraction of point pairs within distance r.
"""

import numpy as np

def correlation_dimension(data, r_min=None, r_max=None, n_r=50):
    """
    Estimate the correlation dimension D2 of a time series or trajectory.
    
    Parameters:
        data: array of shape (n_points, n_dimensions)
        r_min, r_max: distance range for scaling region
        n_r: number of distance values
    
    Returns:
        D2: correlation dimension estimate
        r_vals: distance values
        C_r: correlation integral values
    """
    n = len(data)
    if n > 2000:
        # Subsample for performance
        idx = np.linspace(0, n-1, 2000, dtype=int)
        data = data[idx]
        n = 2000
    
    # Compute pairwise distances (sample for large n)
    max_pairs = 50000
    pairs = min(n * (n-1) // 2, max_pairs)
    
    if n > 200:
        # Random sampling of pairs
        distances = []
        for _ in range(pairs):
            i, j = np.random.randint(0, n, 2)
            if i != j:
                d = np.sqrt(np.sum((data[i] - data[j])**2))
                distances.append(d)
        distances = np.array(distances)
    else:
        # Full pair computation
        distances = []
        for i in range(n):
            for j in range(i+1, n):
                d = np.sqrt(np.sum((data[i] - data[j])**2))
                distances.append(d)
        distances = np.array(distances)
    
    if len(distances) == 0:
        return 0, [], []
    
    # Distance range for scaling region
    if r_min is None:
        r_min = distances.min() + 1e-10
    if r_max is None:
        r_max = distances.max()
    
    r_vals = np.logspace(np.log10(r_min), np.log10(r_max), n_r)
    
    # Correlation integral C(r) = fraction of pairs with distance < r
    C_r = np.array([np.mean(distances < r) for r in r_vals])
    
    # Find scaling region (linear part in log-log)
    log_r = np.log10(r_vals)
    log_C = np.log10(np.maximum(C_r, 1e-16))
    
    # Use middle 60% for slope estimation
    mid_start = int(n_r * 0.2)
    mid_end = int(n_r * 0.8)
    
    if mid_end - mid_start < 3:
        return 0, r_vals, C_r
    
    slope, intercept = np.polyfit(log_r[mid_start:mid_end], log_C[mid_start:mid_end], 1)
    
    return slope, r_vals, C_r


def fractal_dimension_of_lorenz(t, x, y, z):
    """
    Estimate fractal dimension of the Lorenz attractor.
    Expected: D2 ≈ 2.06 for the classic Lorenz attractor.
    """
    data = np.column_stack([x, y, z])
    D2, r_vals, C_r = correlation_dimension(data)
    return D2


def fractal_dimension_of_duffing(t, x, v):
    """
    Estimate fractal dimension of Duffing oscillator attractor.
    """
    data = np.column_stack([x, v])
    D2, r_vals, C_r = correlation_dimension(data)
    return D2
