"""
logistic_map.py — Logistic Map Simulation

The logistic map is a classic example of how simple nonlinear equations
can produce complex, chaotic behavior:

    x_{n+1} = r * x_n * (1 - x_n)

Despite its simplicity, it exhibits period doubling, bifurcations, and
deterministic chaos — a core theme of nonlinear dynamics.

Author: Dr. Bounthong VONGXAYA
Part of: Nonlinear Dynamics Laboratory
"""

import numpy as np


def iterate(x0: float, r: float, n: int) -> np.ndarray:
    """
    Iterate the logistic map for n steps.

    Parameters:
        x0: Initial value (0 < x0 < 1)
        r:  Control parameter (0 < r <= 4)
        n:  Number of iterations

    Returns:
        Array of x values from iteration 0 to n
    """
    xs = np.empty(n + 1)
    xs[0] = x0
    for i in range(n):
        xs[i + 1] = r * xs[i] * (1 - xs[i])
    return xs


def bifurcation_points(r_vals: np.ndarray, n_transient: int = 1000,
                       n_samples: int = 200) -> tuple:
    """
    Generate data for a bifurcation diagram.

    For each r value, iterate through a transient period, then collect
    the steady-state x values.

    Parameters:
        r_vals:      Array of r values to scan
        n_transient: Number of initial iterations to discard
        n_samples:   Number of steady-state values to collect

    Returns:
        (r_plot, x_plot) arrays ready for scatter plotting
    """
    r_plot = []
    x_plot = []
    for r in r_vals:
        xs = iterate(0.5, r, n_transient + n_samples)
        # Discard transient, keep steady state
        steady = xs[n_transient:]
        for x in steady:
            r_plot.append(r)
            x_plot.append(x)
    return np.array(r_plot), np.array(x_plot)


def lyapunov_exponent(r: float, n_transient: int = 1000,
                      n_iter: int = 2000) -> float:
    """
    Estimate the Lyapunov exponent for a given r.

    Positive Lyapunov exponent indicates chaos.
    """
    x = 0.5
    lyap = 0.0
    # Transient
    for _ in range(n_transient):
        x = r * x * (1 - x)
    # Compute exponent
    for _ in range(n_iter):
        x = r * x * (1 - x)
        lyap += np.log(abs(r * (1 - 2 * x)))
    return lyap / n_iter
