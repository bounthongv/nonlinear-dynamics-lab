"""
plot_logistic.py — Visualization of the Logistic Map

Produces three classic plots:
1. Time series for different r values
2. Bifurcation diagram
3. Lyapunov exponent vs r
"""

import numpy as np
import matplotlib.pyplot as plt
from logistic_map import iterate, bifurcation_points, lyapunov_exponent


def plot_time_series(ax, r: float, n: int = 100, x0: float = 0.5):
    """Plot time series for a given r."""
    xs = iterate(x0, r, n)
    ax.plot(range(len(xs)), xs, 'b-', linewidth=0.8)
    ax.set_title(f'r = {r:.2f}')
    ax.set_xlabel('n')
    ax.set_ylabel('x_n')
    ax.set_ylim(-0.05, 1.05)
    ax.grid(alpha=0.3)


def plot_bifurcation(ax, r_min: float = 2.5, r_max: float = 4.0,
                     n_points: int = 2000):
    """Plot bifurcation diagram."""
    r_vals = np.linspace(r_min, r_max, n_points)
    r_plot, x_plot = bifurcation_points(r_vals)
    ax.scatter(r_plot, x_plot, s=0.1, c='k', alpha=0.5)
    ax.set_xlabel('r')
    ax.set_ylabel('x')
    ax.set_title('Bifurcation Diagram')
    ax.set_xlim(r_min, r_max)
    ax.set_ylim(-0.05, 1.05)


def plot_lyapunov(ax, r_min: float = 2.5, r_max: float = 4.0,
                  n_points: int = 500):
    """Plot Lyapunov exponent vs r."""
    r_vals = np.linspace(r_min, r_max, n_points)
    lyap = [lyapunov_exponent(r) for r in r_vals]
    ax.plot(r_vals, lyap, 'r-', linewidth=0.8)
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlabel('r')
    ax.set_ylabel('λ')
    ax.set_title('Lyapunov Exponent')
    ax.set_xlim(r_min, r_max)


def show_all():
    """Generate all three plots."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Time series for different r regimes
    regimes = [(2.5, 'Fixed point'), (3.2, 'Period 2'),
               (3.5, 'Period 4'), (3.9, 'Chaos')]

    for i, (r_val, label) in enumerate(regimes):
        ax = axes[0, 0] if i == 0 else (
            axes[0, 1] if i == 1 else (
                axes[1, 0] if i == 2 else axes[1, 1]))
        plot_time_series(ax, r_val, n=80)
        ax.set_title(f'r = {r_val:.1f} — {label}')

    plt.tight_layout()
    plt.savefig('../docs/logistic_map_timeseries.png', dpi=150)
    plt.show()

    # Bifurcation diagram
    fig, ax = plt.subplots(figsize=(12, 6))
    plot_bifurcation(ax)
    plt.tight_layout()
    plt.savefig('../docs/bifurcation_diagram.png', dpi=300)
    plt.show()

    # Lyapunov exponent
    fig, ax = plt.subplots(figsize=(10, 5))
    plot_lyapunov(ax)
    plt.tight_layout()
    plt.savefig('../docs/lyapunov_exponent.png', dpi=150)
    plt.show()


if __name__ == '__main__':
    show_all()
