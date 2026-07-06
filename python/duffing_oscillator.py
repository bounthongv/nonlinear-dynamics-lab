"""
duffing_oscillator.py — Duffing Oscillator Simulation

The Duffing oscillator is a forced nonlinear oscillator:

    x'' + δ·x' + α·x + β·x³ = γ·cos(ω·t)

where:
    δ = damping coefficient
    α = linear stiffness
    β = nonlinear stiffness (β > 0: hardening, β < 0: softening)
    γ = forcing amplitude
    ω = forcing frequency

Phenomena exhibited:
    - Double-well oscillations (α > 0, β < 0)
    - Amplitude jump resonance
    - Period-doubling route to chaos
    - Strange attractors
    - Coexisting attractors (bistability)

Author: Dr. Bounthong VONGXAYA
Part of: Nonlinear Dynamics Laboratory
"""

import numpy as np


def derivatives(state, t, delta, alpha, beta, gamma, omega):
    """
    Compute derivatives for the Duffing oscillator.

    state = [x, x']  (displacement, velocity)
    """
    x, v = state
    dx = v
    dv = -delta * v - alpha * x - beta * x**3 + gamma * np.cos(omega * t)
    return np.array([dx, dv])


def simulate(x0, v0, t_span, dt=0.01,
             delta=0.2, alpha=-1.0, beta=1.0, gamma=0.3, omega=1.2):
    """
    Simulate the Duffing oscillator using 4th-order Runge-Kutta.

    Parameters:
        x0, v0: Initial displacement and velocity
        t_span: Total simulation time
        dt:     Time step
        delta:  Damping coefficient
        alpha:  Linear stiffness
        beta:   Nonlinear stiffness
        gamma:  Forcing amplitude
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
        k1 = derivatives(state, t[i-1], delta, alpha, beta, gamma, omega)
        k2 = derivatives(state + 0.5 * dt * k1, t[i-1] + 0.5 * dt,
                         delta, alpha, beta, gamma, omega)
        k3 = derivatives(state + 0.5 * dt * k2, t[i-1] + 0.5 * dt,
                         delta, alpha, beta, gamma, omega)
        k4 = derivatives(state + dt * k3, t[i-1] + dt,
                         delta, alpha, beta, gamma, omega)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x[i] = state[0]
        v[i] = state[1]

    return t, x, v


def frequency_response(alpha=-1.0, beta=1.0, delta=0.2, gamma=0.3,
                       omega_range=(0.5, 2.0), n_points=200,
                       n_periods=50, dt=0.01):
    """
    Compute the frequency response (amplitude vs forcing frequency).

    For each frequency, simulates and records the steady-state amplitude.

    Returns:
        (omega_vals, amplitudes) arrays
    """
    omegas = np.linspace(omega_range[0], omega_range[1], n_points)
    amplitudes = []

    for om in omegas:
        T = 2 * np.pi / om
        # Simulate for many periods to reach steady state, then measure
        t_span = n_periods * T
        t, x, v = simulate(0.0, 0.0, t_span, dt,
                           delta=delta, alpha=alpha, beta=beta,
                           gamma=gamma, omega=om)
        # Take last few periods
        steady = x[-int(5 * T / dt):]
        amp = (np.max(steady) - np.min(steady)) / 2
        amplitudes.append(amp)

    return omegas, np.array(amplitudes)


def potential(x, alpha=-1.0, beta=1.0):
    """Compute the Duffing potential V(x) = α·x²/2 + β·x⁴/4."""
    return 0.5 * alpha * x**2 + 0.25 * beta * x**4
