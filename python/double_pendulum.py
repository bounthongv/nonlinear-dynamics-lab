"""
double_pendulum.py — Double Pendulum Simulation

The double pendulum is one of the simplest physical systems that exhibits
deterministic chaos. Two pendulums connected end-to-end produce motion
that is exquisitely sensitive to initial conditions.

State: [θ₁, θ₂, ω₁, ω₂]
Derived using Lagrangian mechanics with matrix formulation for stability.

Author: Dr. Bounthong VONGXAYA
Part of: Nonlinear Dynamics Laboratory
"""

import numpy as np


def derivatives(state, m1, m2, L1, L2, g):
    """
    Compute derivatives using the mass-matrix formulation.

    [M] [α₁, α₂]ᵀ = [F₁, F₂]ᵀ

    where M is the mass matrix and F contains the remaining terms.
    """
    theta1, theta2, omega1, omega2 = state
    delta = theta1 - theta2
    M = m1 + m2

    # Mass matrix
    M11 = M * L1**2
    M12 = m2 * L1 * L2 * np.cos(delta)
    M21 = M12  # symmetric
    M22 = m2 * L2**2

    # Right-hand side (derived from Euler-Lagrange equations)
    F1 = (-m2 * L1 * L2 * omega2**2 * np.sin(delta)
          - M * g * L1 * np.sin(theta1))
    F2 = (m2 * L1 * L2 * omega1**2 * np.sin(delta)
          - m2 * g * L2 * np.sin(theta2))

    # Solve 2x2 system using Cramer's rule
    det = M11 * M22 - M12 * M21
    alpha1 = (F1 * M22 - M12 * F2) / det
    alpha2 = (M11 * F2 - F1 * M21) / det

    return np.array([omega1, omega2, alpha1, alpha2])


def simulate(theta1_0, theta2_0, omega1_0, omega2_0,
             t_span, dt=0.001, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
    """
    Simulate the double pendulum using 4th-order Runge-Kutta.

    Parameters:
        theta1_0, theta2_0: Initial angles (radians, 0 = hanging down)
        omega1_0, omega2_0: Initial angular velocities
        t_span: Total simulation time
        dt: Time step (use small value, e.g. 0.001 for accuracy)
        m1, m2: Masses of the two bobs
        L1, L2: Lengths of the two arms
        g: Gravitational acceleration

    Returns:
        (t, theta1, theta2, omega1, omega2, x1, y1, x2, y2)
    """
    n_steps = int(t_span / dt)
    t = np.linspace(0, t_span, n_steps)

    theta1 = np.empty(n_steps)
    theta2 = np.empty(n_steps)
    omega1 = np.empty(n_steps)
    omega2 = np.empty(n_steps)

    theta1[0] = theta1_0
    theta2[0] = theta2_0
    omega1[0] = omega1_0
    omega2[0] = omega2_0

    state = np.array([theta1_0, theta2_0, omega1_0, omega2_0])

    for i in range(1, n_steps):
        k1 = derivatives(state, m1, m2, L1, L2, g)
        k2 = derivatives(state + 0.5 * dt * k1, m1, m2, L1, L2, g)
        k3 = derivatives(state + 0.5 * dt * k2, m1, m2, L1, L2, g)
        k4 = derivatives(state + dt * k3, m1, m2, L1, L2, g)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        theta1[i] = state[0]
        theta2[i] = state[1]
        omega1[i] = state[2]
        omega2[i] = state[3]

    # Convert to Cartesian coordinates
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    return t, theta1, theta2, omega1, omega2, x1, y1, x2, y2


def energy(theta1, theta2, omega1, omega2, m1=1.0, m2=1.0,
           L1=1.0, L2=1.0, g=9.81):
    """
    Compute total energy (should be conserved).

    Returns (KE, PE, total) arrays.
    """
    # Kinetic energy of mass 1
    KE1 = 0.5 * m1 * (L1 * omega1)**2

    # Velocity of mass 2 squared
    v2_sq = (L1 * omega1)**2 + (L2 * omega2)**2 + 2 * L1 * L2 * omega1 * omega2 * np.cos(theta1 - theta2)
    KE2 = 0.5 * m2 * v2_sq
    KE = KE1 + KE2

    # Potential energy (zero at pivot height)
    PE = -(m1 + m2) * g * L1 * np.cos(theta1) - m2 * g * L2 * np.cos(theta2)

    return KE, PE, KE + PE
