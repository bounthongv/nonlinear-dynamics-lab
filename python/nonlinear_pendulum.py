"""
nonlinear_pendulum.py — Nonlinear Pendulum Simulation

The nonlinear pendulum is governed by:

    θ'' + γ·θ' + ω₀²·sin(θ) = F·cos(ω·t)

where:
    θ    = angular displacement
    γ    = damping coefficient
    ω₀   = natural frequency (√(g/L))
    F    = forcing amplitude
    ω    = forcing frequency

Unlike the small-angle approximation (θ'' + ω₀²·θ = 0),
the full nonlinear equation exhibits:
    - Amplitude-dependent period
    - Anharmonic oscillations
    - Chaotic motion (with damping + forcing)

Author: Dr. Bounthong VONGXAYA
Part of: Nonlinear Dynamics Laboratory
"""

import numpy as np


def derivatives(state, t, gamma, omega0_sq, F, omega):
    """
    Compute derivatives for the forced, damped pendulum.

    state = [θ, θ']  (angular displacement, angular velocity)

    Returns [θ', θ''].
    """
    theta, omega_vel = state
    dtheta = omega_vel
    domega = -gamma * omega_vel - omega0_sq * np.sin(theta) + F * np.cos(omega * t)
    return np.array([dtheta, domega])


def simulate(theta0, omega0, t_span, dt=0.01,
             gamma=0.0, L=1.0, g=9.81, F=0.0, omega=0.0):
    """
    Simulate the nonlinear pendulum using 4th-order Runge-Kutta.

    Parameters:
        theta0: Initial angular displacement (radians)
        omega0: Initial angular velocity (rad/s)
        t_span: Total simulation time (seconds)
        dt:     Time step (seconds)
        gamma:  Damping coefficient
        L:      Pendulum length (m)
        g:      Gravitational acceleration (m/s²)
        F:      Forcing amplitude
        omega:  Forcing frequency (rad/s)

    Returns:
        (t, theta, omega_vel) arrays
    """
    omega0_sq = g / L
    n_steps = int(t_span / dt)
    t = np.linspace(0, t_span, n_steps)

    theta = np.empty(n_steps)
    omega_vel = np.empty(n_steps)
    theta[0] = theta0
    omega_vel[0] = omega0

    state = np.array([theta0, omega0])

    for i in range(1, n_steps):
        # Runge-Kutta 4th order
        k1 = derivatives(state, t[i-1], gamma, omega0_sq, F, omega)
        k2 = derivatives(state + 0.5 * dt * k1, t[i-1] + 0.5 * dt,
                         gamma, omega0_sq, F, omega)
        k3 = derivatives(state + 0.5 * dt * k2, t[i-1] + 0.5 * dt,
                         gamma, omega0_sq, F, omega)
        k4 = derivatives(state + dt * k3, t[i-1] + dt,
                         gamma, omega0_sq, F, omega)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        theta[i] = state[0]
        omega_vel[i] = state[1]

    return t, theta, omega_vel


def period_estimate(theta0, L=1.0, g=9.81, t_max=50.0, dt=0.01):
    """
    Estimate the oscillation period for a given initial amplitude.

    Uses zero-crossing detection. Returns None if period cannot be found.
    """
    t, theta, _ = simulate(theta0, 0.0, t_max, dt, L=L, g=g)

    # Find zero crossings
    zero_crossings = []
    for i in range(1, len(theta)):
        if theta[i-1] <= 0 and theta[i] > 0:
            zero_crossings.append(t[i])

    if len(zero_crossings) >= 3:
        # Average period from multiple cycles
        periods = np.diff(zero_crossings)
        return np.mean(periods)
    return None


def small_angle_period(L=1.0, g=9.81):
    """Small-angle approximation period."""
    return 2 * np.pi * np.sqrt(L / g)
