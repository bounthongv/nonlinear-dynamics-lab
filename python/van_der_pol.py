"""
van_der_pol.py — Van der Pol Oscillator Simulation

The Van der Pol oscillator is a non-conservative oscillator with
nonlinear damping:

    x'' - μ(1 - x²)·x' + x = F·cos(ω·t)

where μ > 0 is the nonlinear damping parameter.

Key phenomena:
    - Self-excited oscillations (limit cycle)
    - Relaxation oscillations (for large μ)
    - Forced chaos (with F > 0)
    - Frequency entrainment

Author: Dr. Bounthong VONGXAYA
Part of: Nonlinear Dynamics Laboratory
"""

import numpy as np


def derivatives(state, t, mu, F, omega):
    """Compute derivatives for the Van der Pol oscillator."""
    x, v = state
    dx = v
    dv = mu * (1 - x**2) * v - x + F * np.cos(omega * t)
    return np.array([dx, dv])


def simulate(x0, v0, t_span, dt=0.01, mu=1.0, F=0.0, omega=0.0):
    """
    Simulate the Van der Pol oscillator using 4th-order Runge-Kutta.

    Parameters:
        x0, v0: Initial displacement and velocity
        t_span: Total simulation time
        dt:     Time step
        mu:     Nonlinear damping parameter
        F:      Forcing amplitude
        omega:  Forcing frequency

    Returns:
        (t, x, v) arrays
    """
    n_steps = int(t_span / dt)
    t = np.linspace(0, t_span, n_steps)

    x = np.empty(n_steps)
    v = np.empty(n_steps)
    x[0], v[0] = x0, v0

    state = np.array([x0, v0])

    for i in range(1, n_steps):
        k1 = derivatives(state, t[i-1], mu, F, omega)
        k2 = derivatives(state + 0.5 * dt * k1, t[i-1] + 0.5 * dt, mu, F, omega)
        k3 = derivatives(state + 0.5 * dt * k2, t[i-1] + 0.5 * dt, mu, F, omega)
        k4 = derivatives(state + dt * k3, t[i-1] + dt, mu, F, omega)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x[i] = state[0]
        v[i] = state[1]

    return t, x, v


def limit_cycle_amplitude(mu):
    """
    Estimate the limit cycle amplitude for unforced Van der Pol.

    For small μ, amplitude ≈ 2.0. For large μ, amplitude ≈ 2.0
    but the waveform becomes highly nonlinear (relaxation oscillation).
    """
    # Simulate long enough to reach limit cycle, measure amplitude
    t, x, v = simulate(0.1, 0.1, 200.0, mu=mu)
    # Take steady state (last half)
    steady = x[len(x)//2:]
    return (np.max(steady) - np.min(steady)) / 2
