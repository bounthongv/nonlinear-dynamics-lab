"""
lorenz_attractor.py — Lorenz System Simulation

The Lorenz system is a set of three coupled ODEs that exhibit
deterministic chaos for certain parameter values:

    dx/dt = σ(y - x)
    dy/dt = x(ρ - z) - y
    dz/dt = xy - βz

where:
    σ = Prandtl number
    ρ = Rayleigh number (control parameter)
    β = geometric factor

Classic chaotic parameters: σ=10, β=8/3, ρ=28

Author: Dr. Bounthong VONGXAYA
Part of: Nonlinear Dynamics Laboratory
"""

import numpy as np


def derivatives(state, sigma, rho, beta):
    """Compute derivatives for the Lorenz system."""
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])


def simulate(x0, y0, z0, t_span, dt=0.01,
             sigma=10.0, rho=28.0, beta=8.0/3.0):
    """
    Simulate the Lorenz system using 4th-order Runge-Kutta.

    Parameters:
        x0, y0, z0: Initial conditions
        t_span:     Total simulation time
        dt:         Time step
        sigma, rho, beta: System parameters

    Returns:
        (t, x, y, z) arrays
    """
    n_steps = int(t_span / dt)
    t = np.linspace(0, t_span, n_steps)

    x = np.empty(n_steps)
    y = np.empty(n_steps)
    z = np.empty(n_steps)
    x[0], y[0], z[0] = x0, y0, z0

    state = np.array([x0, y0, z0])

    for i in range(1, n_steps):
        # RK4
        k1 = derivatives(state, sigma, rho, beta)
        k2 = derivatives(state + 0.5 * dt * k1, sigma, rho, beta)
        k3 = derivatives(state + 0.5 * dt * k2, sigma, rho, beta)
        k4 = derivatives(state + dt * k3, sigma, rho, beta)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x[i], y[i], z[i] = state

    return t, x, y, z


def lyapunov_exponents(sigma=10.0, rho=28.0, beta=8.0/3.0,
                       n_transient=10000, n_iter=20000, dt=0.01):
    """
    Estimate the largest Lyapunov exponent (λ_max).

    Positive λ_max indicates chaos. Uses the standard method of
    tracking divergence of nearby trajectories.
    """
    # Reference trajectory
    state = np.array([1.0, 1.0, 1.0])

    # Transient
    for _ in range(n_transient):
        k1 = derivatives(state, sigma, rho, beta)
        k2 = derivatives(state + 0.5 * dt * k1, sigma, rho, beta)
        k3 = derivatives(state + 0.5 * dt * k2, sigma, rho, beta)
        k4 = derivatives(state + dt * k3, sigma, rho, beta)
        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    # Perturbation vector
    w = np.array([1.0, 0.0, 0.0])
    lyap = 0.0

    for _ in range(n_iter):
        k1 = derivatives(state, sigma, rho, beta)
        k2 = derivatives(state + 0.5 * dt * k1, sigma, rho, beta)
        k3 = derivatives(state + 0.5 * dt * k2, sigma, rho, beta)
        k4 = derivatives(state + dt * k3, sigma, rho, beta)
        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

        # Jacobian of Lorenz system at current state
        x, y, z = state
        J = np.array([[-sigma, sigma, 0],
                       [rho - z, -1, -x],
                       [y, x, -beta]])
        w = w + dt * J @ w
        # Renormalize
        norm = np.linalg.norm(w)
        w = w / norm
        lyap += np.log(norm)

    return lyap / (n_iter * dt)
