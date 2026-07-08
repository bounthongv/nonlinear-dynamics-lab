#!/usr/bin/env python3
"""
regenerate_figures.py — Recreate all book figures using modern Python.

The original 1995 book had ~25 figures (schematics + mathematical plots).
This script regenerates the mathematical plots using our Python simulations.
Schematic diagrams are kept from the original scans.

Author: Nonlinear Dynamics Lab — Dr. Bounthong VONGXAYA
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Arc, FancyArrowPatch
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from python.nonlinear_pendulum import simulate as sim_pend, small_angle_period, period_estimate

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs', 'figures')
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 10

def save(name):
    path = os.path.join(OUTPUT_DIR, name)
    plt.savefig(path, bbox_inches='tight', dpi=150)
    plt.close()
    print(f'  ✓ {name}')
    return name

# ============================================================
# Chapter I: Schematic diagrams (from scans)
# These are kept as original scanned images — not regenerated.
# ============================================================

# ============================================================
# Figure 2.1: 3D Phase Trajectory of Driven Pendulum
# ============================================================
def fig_2_1():
    """3D phase trajectory in (φ, Ω, ψ) space."""
    print('Figure 2.1: 3D Phase Trajectory')
    t, th, om = sim_pend(1.5, 0.0, 40.0, gamma=0.1, F=0.3, omega=1.2)
    psi = 1.2 * t
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(th, om, psi, 'b-', lw=0.5, alpha=0.8, label='Trajectory')
    ax.plot(th, om, np.full_like(psi, psi.min()), 'gray', lw=0.3, alpha=0.4, label='Projection')
    ax.set_xlabel('φ'); ax.set_ylabel('Ω'); ax.set_zlabel('ψ = ωt')
    ax.set_title('Figure 2.1: Phase Trajectory in 3D Phase Space')
    ax.legend(fontsize=8)
    save('fig_2_1_3d_trajectory.png')

# ============================================================
# Figure 2.2.1a: Small-angle time series
# ============================================================
def fig_2_2_1a():
    """Small-angle pendulum — near-harmonic oscillation."""
    print('Figure 2.2.1a: Small-angle time series')
    t, th, om = sim_pend(np.radians(10), 0.0, 10.0)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, np.degrees(th), 'b-', lw=0.8)
    ax.set_xlabel('Time t (s)'); ax.set_ylabel('φ (degrees)')
    ax.set_title('Figure 2.2.1a: Small-angle oscillation (θ₀ = 10°)')
    ax.grid(alpha=0.3)
    save('fig_2_2_1a_small_angle.png')

# ============================================================
# Figure 2.2.1b: Large-angle time series
# ============================================================
def fig_2_2_1b():
    """Large-angle pendulum — anharmonic, period depends on amplitude."""
    print('Figure 2.2.1b: Large-angle time series')
    t, th, om = sim_pend(np.radians(120), 0.0, 10.0)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, np.degrees(th), 'b-', lw=0.8)
    ax.set_xlabel('Time t (s)'); ax.set_ylabel('φ (degrees)')
    ax.set_title('Figure 2.2.1b: Large-angle oscillation (θ₀ = 120°)')
    ax.grid(alpha=0.3)
    save('fig_2_2_1b_large_angle.png')

# ============================================================
# Figure 2.2.2: Pendulum near 180° (plateau behavior)
# ============================================================
def fig_2_2_2():
    """Near-inverted pendulum — long dwell time at the top."""
    print('Figure 2.2.2: Near 180° oscillation')
    t, th, om = sim_pend(np.radians(179.9), 0.0, 15.0)
    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    axes[0].plot(t, np.degrees(th), 'b-', lw=0.7)
    axes[0].set_ylabel('φ (degrees)')
    axes[0].set_title('Figure 2.2.2: Amplitude near 179.9°')
    axes[0].grid(alpha=0.3)
    axes[1].plot(t, om, 'r-', lw=0.7)
    axes[1].set_xlabel('Time t (s)'); axes[1].set_ylabel('dφ/dt')
    axes[1].grid(alpha=0.3)
    save('fig_2_2_2_near_180.png')

# ============================================================
# Figure 2.2.3: Phase portrait ensemble (separatrix)
# ============================================================
def fig_2_2_3():
    """Phase portrait showing oscillations, rotations, and separatrix."""
    print('Figure 2.2.3: Phase portrait ensemble')
    fig, ax = plt.subplots(figsize=(7, 5))
    initial_conditions = [
        (np.radians(30), 0), (np.radians(90), 0), (np.radians(150), 0),
        (np.radians(179), 0), (0, 1.5), (0, 2.5), (0, 3.5), (0, 5.0)
    ]
    for th0, w0 in initial_conditions:
        t, th, om = sim_pend(th0, w0, 30.0)
        label = f'θ₀={int(np.degrees(th0))}°' if th0 > 0.1 else f'φ̇₀={w0}'
        ax.plot(th, om, lw=0.5, alpha=0.7, label=label)
    ax.set_xlabel('φ'); ax.set_ylabel('dφ/dt')
    ax.set_title('Figure 2.2.3: Phase Trajectories of Free Pendulum')
    ax.legend(fontsize=7, ncol=2); ax.grid(alpha=0.3); ax.axis('equal')
    save('fig_2_2_3_phase_portrait_ensemble.png')

# ============================================================
# Figure 2.3.1a: Damped oscillation
# ============================================================
def fig_2_3_1a():
    """Free damped pendulum — exponential decay."""
    print('Figure 2.3.1a: Damped oscillation')
    t, th, om = sim_pend(np.radians(60), 0.0, 15.0, gamma=0.1)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, np.degrees(th), 'b-', lw=0.8)
    ax.set_xlabel('Time t (s)'); ax.set_ylabel('φ (degrees)')
    ax.set_title('Figure 2.3.1a: Damped Pendulum (b = 0.1)')
    ax.grid(alpha=0.3)
    save('fig_2_3_1a_damped_oscillation.png')

# ============================================================
# Figure 2.3.1b: Damped phase portrait (spiral to fixed point)
# ============================================================
def fig_2_3_1b():
    """Damped phase portrait — spiral attractor."""
    print('Figure 2.3.1b: Damped phase portrait')
    t, th, om = sim_pend(np.radians(90), 0.0, 40.0, gamma=0.15)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(th, om, 'r-', lw=0.4, alpha=0.7)
    ax.scatter(0, 0, c='k', s=50, zorder=5, label='Fixed point attractor')
    ax.set_xlabel('φ'); ax.set_ylabel('dφ/dt')
    ax.set_title('Figure 2.3.1b: Damped Trajectories Spiraling to Fixed Point')
    ax.legend(); ax.grid(alpha=0.3); ax.axis('equal')
    save('fig_2_3_1b_damped_spiral.png')

# ============================================================
# Figure 2.4.1a: Forced pendulum — transient to steady state
# ============================================================
def fig_2_4_1a():
    """Forced damped pendulum: transient and steady state."""
    print('Figure 2.4.1a: Forced pendulum transient')
    # Parameters from the book: m=0.2, l=0.25, ω_A=4.176, b=0.02, A=0.29
    t, th, om = sim_pend(0.0, 0.0, 30.0, gamma=0.02, F=0.29, omega=4.176, L=0.25)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, np.degrees(th), 'b-', lw=0.6)
    ax.axvline(x=10, color='r', ls='--', alpha=0.5, label='Transient → Steady state')
    ax.set_xlabel('Time t (s)'); ax.set_ylabel('φ (degrees)')
    ax.set_title('Figure 2.4.1a: Forced Pendulum — Transient and Steady State')
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    save('fig_2_4_1a_forced_transient.png')

# ============================================================
# Figure 2.4.1b: Trajectory winding onto limit cycle
# ============================================================
def fig_2_4_1b():
    """Phase portrait showing transient spiraling onto limit cycle."""
    print('Figure 2.4.1b: Winding onto limit cycle')
    t, th, om = sim_pend(0.0, 0.0, 40.0, gamma=0.02, F=0.29, omega=4.176, L=0.25)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(th, om, 'r-', lw=0.3, alpha=0.6)
    ax.set_xlabel('φ'); ax.set_ylabel('dφ/dt')
    ax.set_title('Figure 2.4.1b: Phase Trajectory Winding onto Limit Cycle')
    ax.grid(alpha=0.3); ax.axis('equal')
    save('fig_2_4_1b_winding_limit_cycle.png')

# ============================================================
# Figure 2.4.1c: Clean limit cycle
# ============================================================
def fig_2_4_1c():
    """Steady-state limit cycle (after transient removed)."""
    print('Figure 2.4.1c: Clean limit cycle')
    t, th, om = sim_pend(1.0, 0.0, 60.0, gamma=0.02, F=0.29, omega=4.176, L=0.25)
    # Take last 20 seconds
    idx = np.where(t > 40)[0]
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(th[idx], om[idx], 'r-', lw=0.6)
    ax.set_xlabel('φ'); ax.set_ylabel('dφ/dt')
    ax.set_title('Figure 2.4.1c: Limit Cycle (Steady State)')
    ax.grid(alpha=0.3); ax.axis('equal')
    save('fig_2_4_1c_limit_cycle.png')

# ============================================================
# Figure 2.4.2: Resonance curves (amplitude vs frequency)
# ============================================================
def fig_2_4_2():
    """Resonance curves for different forcing amplitudes."""
    print('Figure 2.4.2: Resonance curves')
    omega_range = np.linspace(3.0, 5.0, 60)
    amplitudes = [0.1, 0.2, 0.29, 0.4]
    colors = ['b', 'g', 'r', 'm']

    fig, ax = plt.subplots(figsize=(8, 5))
    for A_val, color in zip(amplitudes, colors):
        amps = []
        for w in omega_range:
            t, th, om = sim_pend(0.5, 0.0, 80.0, gamma=0.02, F=A_val, omega=w, L=0.25)
            amp = np.max(np.abs(th[-2000:]))
            amps.append(amp)
        ax.plot(omega_range, amps, '-', color=color, lw=1.5, label=f'A = {A_val} Nm')

    ax.set_xlabel('Forcing frequency ω (rad/s)')
    ax.set_ylabel('Amplitude (rad)')
    ax.set_title('Figure 2.4.2: Resonance Curves for Different Excitation Amplitudes')
    ax.legend(); ax.grid(alpha=0.3)
    save('fig_2_4_2_resonance_curves.png')

# ============================================================
# Figure 2.4.3a/b: Bistability — two coexisting attractors
# ============================================================
def fig_2_4_3():
    """Bistability: two stable oscillations for same parameters."""
    print('Figure 2.4.3: Bistability')
    # Duffing oscillator with two different initial conditions
    from python.duffing_oscillator import simulate as sim_duff
    _, x1, v1 = sim_duff(0.5, 0.0, 150.0, gamma=0.35, omega=1.2)
    _, x2, v2 = sim_duff(-0.5, 0.0, 150.0, gamma=0.35, omega=1.2)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(x1[-3000:], v1[-3000:], 'b-', lw=0.5)
    axes[0].set_xlabel('x'); axes[0].set_ylabel("x'")
    axes[0].set_title('Figure 2.4.3a: x₀ = 0.5 (Right Well)')
    axes[0].grid(alpha=0.3)

    axes[1].plot(x2[-3000:], v2[-3000:], 'r-', lw=0.5)
    axes[1].set_xlabel('x'); axes[1].set_ylabel("x'")
    axes[1].set_title('Figure 2.4.3b: x₀ = -0.5 (Left Well)')
    axes[1].grid(alpha=0.3)

    save('fig_2_4_3_bistability.png')

# ============================================================
# Figure 3.x: Lorenz attractor (if referenced)
# ============================================================
def fig_lorenz():
    """Classic Lorenz butterfly."""
    print('Figure Lorenz: Butterfly attractor')
    from python.lorenz_attractor import simulate as sim_lorenz
    t, x, y, z = sim_lorenz(1.0, 1.0, 1.0, 40.0, rho=28.0)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, 'b-', lw=0.3, alpha=0.7)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Lorenz Attractor (σ = 10, ρ = 28, β = 8/3)')
    save('fig_lorenz_attractor.png')


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print('=' * 50)
    print('Regenerating book figures with modern Python')
    print('=' * 50)

    # Chapter I: Schematic diagrams — skipped (keep originals)
    print('\n[Chapter I] Schematic diagrams — using original scans')

    # Chapter II: Mathematical plots
    print('\n[Chapter II] Mathematical plots — regenerating...')
    fig_2_1()
    fig_2_2_1a()
    fig_2_2_1b()
    fig_2_2_2()
    fig_2_2_3()
    fig_2_3_1a()
    fig_2_3_1b()
    fig_2_4_1a()
    fig_2_4_1b()
    fig_2_4_1c()
    fig_2_4_2()
    fig_2_4_3()

    # Additional
    print('\n[Additional] Other systems...')
    fig_lorenz()

    print(f'\nDone! All figures saved to: {OUTPUT_DIR}')
    import glob
    files = glob.glob(os.path.join(OUTPUT_DIR, '*.png'))
    print(f'Total: {len(files)} figures generated')
