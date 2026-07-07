"""
course_app.py — Modern Interactive Course on Nonlinear Dynamics

A clean, English-language, simulation-first learning experience.
Extracts essential theory from the 1995 book and pairs it with
interactive Python simulations.

Author: Dr. Bounthong VONGXAYA
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import time

# Import simulation modules
from python.logistic_map import iterate, bifurcation_points, lyapunov_exponent as lyap_log
from python.nonlinear_pendulum import simulate as sim_pend, small_angle_period, period_estimate
from python.lorenz_attractor import simulate as sim_lorenz
from python.duffing_oscillator import simulate as sim_duff, potential
from python.van_der_pol import simulate as sim_vdp
from python.double_pendulum import simulate as sim_double

rcParams['figure.dpi'] = 100
rcParams['font.size'] = 11

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(page_title="Nonlinear Dynamics — Interactive Course",
                   page_icon="🌀", layout="wide")

# ============================================================
# HELPER: Consistent Plot Styling
# ============================================================

def styled_fig(fig, title=None):
    """Apply consistent styling to figures."""
    if title:
        fig.suptitle(title, fontsize=13, fontweight='bold')
    return fig

# ============================================================
# CHAPTER DEFINITIONS
# ============================================================

CHAPTERS = [
    {
        'id': 'intro',
        'icon': '🎯',
        'title': 'Introduction',
        'subtitle': 'What Are Nonlinear Systems?',
        'content': """
        **Nonlinear systems are everywhere.**

        Most of the real world is nonlinear. A pendulum swinging through large angles,
        a population fluctuating with limited resources, weather patterns, heartbeats,
        stock markets — all are inherently nonlinear.

        **Linear vs. Nonlinear**

        | Linear | Nonlinear |
        |---|---|
        | $$\\ddot{x} + \\omega_0^2 x = 0$$ | $$\\ddot{x} + \\omega_0^2 \\sin x = 0$$ |
        | Proportional response | Response depends on state |
        | Superposition holds | Superposition fails |
        | Predictable, periodic | Can be chaotic |

        **What makes nonlinear dynamics fascinating?**
        - Simple equations can produce incredibly complex behavior
        - Deterministic systems can be unpredictable (chaos)
        - The same system can exhibit completely different behaviors depending on parameters

        In this course, you'll explore these phenomena through interactive simulations.
        """,
        'simulation': None,
    },
    {
        'id': 'ch1_foundations',
        'icon': '📐',
        'title': 'Chapter 1: Foundations',
        'subtitle': 'Physical Systems & Numerical Methods',
        'sections': [
            {
                'id': 'pendulum',
                'title': '1.1 The Nonlinear Pendulum',
                'content': """
                The **mathematical pendulum** is the classic starting point for nonlinear dynamics.

                For small angles, $$\\sin\\theta \\approx \\theta$$, giving the linear equation:
                $$\\ddot{\\theta} + \\omega_0^2 \\theta = 0$$

                But for **large angles**, the full nonlinear equation applies:
                $$\\ddot{\\theta} + \\gamma \\dot{\\theta} + \\omega_0^2 \\sin\\theta = F \\cos(\\omega t)$$

                **Key insight:** The period now depends on amplitude — something impossible in linear systems.
                """,
                'simulation': 'pendulum_basic',
            },
            {
                'id': 'numerics',
                'title': '1.2 Numerical Integration',
                'content': """
                Most nonlinear equations cannot be solved analytically. We use **numerical methods**.

                **Euler Method** (simplest):
                $$y_{n+1} = y_n + h \\cdot f(t_n, y_n)$$

                **Runge-Kutta 4** (workhorse):
                $$\\begin{aligned}
                k_1 &= h f(t_n, y_n) \\\\
                k_2 &= h f(t_n + \\frac{h}{2}, y_n + \\frac{k_1}{2}) \\\\
                k_3 &= h f(t_n + \\frac{h}{2}, y_n + \\frac{k_2}{2}) \\\\
                k_4 &= h f(t_n + h, y_n + k_3)
                \\end{aligned}$$

                RK4 is the method used in all simulations throughout this course.
                """,
                'simulation': 'numerics_compare',
            },
            {
                'id': 'phasespace',
                'title': '1.3 Phase Space',
                'content': """
                Instead of plotting just $$x(t)$$, we plot **$$x$$ vs $$\\dot{x}$$** — this is the **phase portrait**.

                Each point represents the complete state of the system. The trajectory through
                phase space reveals:
                - **Fixed points** (where the system comes to rest)
                - **Limit cycles** (stable periodic orbits)
                - **Strange attractors** (chaotic orbits)
                """,
                'simulation': 'phase_space',
            },
            {
                'id': 'duffing_intro',
                'title': '1.4 The Duffing Oscillator',
                'content': """
                The Duffing oscillator adds a **nonlinear restoring force**:
                $$\\ddot{x} + \\delta \\dot{x} + \\alpha x + \\beta x^3 = \\gamma \\cos(\\omega t)$$

                With $$\\alpha < 0, \\beta > 0$$, the system has a **double-well potential** —
                the particle can oscillate in one well or jump between wells.
                """,
                'simulation': 'duffing_intro',
            },
            {
                'id': 'vdp_intro',
                'title': '1.5 The Van der Pol Oscillator',
                'content': """
                The Van der Pol oscillator demonstrates **self-excited oscillations**:
                $$\\ddot{x} - \\mu(1 - x^2)\\dot{x} + x = F \\cos(\\omega t)$$

                For $$\\mu > 0$$, the system spontaneously oscillates — energy is pumped
                into the system at small amplitudes and dissipated at large amplitudes,
                producing a stable **limit cycle**.
                """,
                'simulation': 'vdp_intro',
            },
        ]
    },
    {
        'id': 'ch2_phenomena',
        'icon': '🌀',
        'title': 'Chapter 2: Phenomena',
        'subtitle': 'Explore Nonlinear Behavior Through Simulations',
        'sections': [
            {
                'id': 'bifurcation',
                'title': '2.1 Bifurcations & Period Doubling',
                'content': """
                The **logistic map** is the simplest system showing period doubling:

                $$x_{n+1} = r \\cdot x_n \\cdot (1 - x_n)$$

                As $$r$$ increases from 2.5 to 4.0, the system undergoes:
                - **Fixed point** → **Period 2** → **Period 4** → ... → **Chaos**

                The ratio of successive bifurcation intervals approaches the **Feigenbaum constant** $$\\delta \\approx 4.669$$ — universal across all period-doubling systems.
                """,
                'simulation': 'bifurcation',
            },
            {
                'id': 'limit_cycles',
                'title': '2.2 Limit Cycles & Relaxation Oscillations',
                'content': """
                A **limit cycle** is an isolated closed trajectory — the system settles
                into a stable oscillation regardless of initial conditions.

                In the Van der Pol oscillator, increasing $$\\mu$$ transforms:
                - $$\\mu \\ll 1$$: Nearly sinusoidal oscillation
                - $$\\mu \\gg 1$$: **Relaxation oscillation** — slow build-up, rapid discharge
                """,
                'simulation': 'limit_cycles',
            },
            {
                'id': 'bistability',
                'title': '2.3 Bistability & Hysteresis',
                'content': """
                In the Duffing oscillator, **two stable states can coexist** for the same
                parameters. Which one the system chooses depends on its history.

                This is **hysteresis** — the system remembers its past.

                As you sweep the forcing frequency up and down, the amplitude follows
                different paths, creating a **jump phenomenon**.
                """,
                'simulation': 'bistability',
            },
            {
                'id': 'chaos',
                'title': '2.4 Chaos & the Butterfly Effect',
                'content': """
                The **Lorenz system** is the most famous example of deterministic chaos:

                $$\\begin{aligned}
                \\dot{x} &= \\sigma(y - x) \\\\
                \\dot{y} &= x(\\rho - z) - y \\\\
                \\dot{z} &= xy - \\beta z
                \\end{aligned}$$

                For $$\\rho > 24.7$$, the trajectory forms a **strange attractor** — \
                bounded but never repeating. Small differences grow exponentially:
                the **butterfly effect**.
                """,
                'simulation': 'chaos',
            },
            {
                'id': 'sensitivity',
                'title': '2.5 Sensitivity to Initial Conditions',
                'content': """
                The **double pendulum** is the most直观 example of sensitive dependence.

                Two pendulums starting with a **0.001 radian difference** diverge to
                completely different trajectories within seconds.

                This is the defining feature of chaos: **deterministic equations, unpredictable outcomes**.
                """,
                'simulation': 'sensitivity',
            },
        ]
    },
    {
        'id': 'ch3_lab',
        'icon': '🔬',
        'title': 'Chapter 3: Interactive Lab',
        'subtitle': 'Free Exploration Mode',
        'content': """
        Choose any system and explore freely. Change parameters, switch between
        visualizations, and discover nonlinear phenomena on your own terms.
        """,
        'sections': [
            {
                'id': 'lab_pendulum',
                'title': 'Pendulum Lab',
                'simulation': 'lab_pendulum',
            },
            {
                'id': 'lab_duffing',
                'title': 'Duffing Lab',
                'simulation': 'lab_duffing',
            },
            {
                'id': 'lab_vdp',
                'title': 'Van der Pol Lab',
                'simulation': 'lab_vdp',
            },
            {
                'id': 'lab_lorenz',
                'title': 'Lorenz Lab',
                'simulation': 'lab_lorenz',
            },
            {
                'id': 'lab_logistic',
                'title': 'Logistic Map Lab',
                'simulation': 'lab_logistic',
            },
            {
                'id': 'lab_double',
                'title': 'Double Pendulum Lab',
                'simulation': 'lab_double',
            },
        ]
    },
    {
        'id': 'about',
        'icon': 'ℹ️',
        'title': 'About',
        'subtitle': 'Author & Background',
        'content': f"""
        This interactive course is based on the 1995 book
        **"Ordnung und Chaos bei nichtlinearen Schwingungen"**
        by Dr. Bounthong VONGXAYA.

        **Author:**
        - PhD in Physics (Magna Cum Laude), TU Dresden, Germany
        - Master of Science in Physics and Mathematics (Mention of Excellence), Belarusian State University
        - 40+ years in IT architecture, software development, and education

        **Technology:**
        All simulations run in real-time using Python + Streamlit.
        Source code available at: [github.com/bounthongv/nonlinear-dynamics-lab](https://github.com/bounthongv/nonlinear-dynamics-lab)
        """,
        'simulation': None,
    },
]

# ============================================================
# SIMULATION FUNCTIONS
# ============================================================

def sim_pendulum_basic():
    """Interactive pendulum demonstrating amplitude-dependent period."""
    st.markdown("### 🔬 Interactive: Nonlinear Pendulum")
    col1, col2, col3 = st.columns(3)
    with col1:
        theta0 = st.slider("Initial angle θ₀ (°)", 5, 179, 45, 1)
    with col2:
        damping = st.slider("Damping γ", 0.0, 1.0, 0.0, 0.01)
    with col3:
        forcing = st.slider("Forcing F", 0.0, 0.5, 0.0, 0.01)

    theta0_rad = np.radians(theta0)
    t, th, om = sim_pend(theta0_rad, 0.0, 20.0, gamma=damping, F=forcing)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, th, 'b-', lw=0.7)
        ax.set_xlabel('Time (s)'); ax.set_ylabel('θ (rad)')
        ax.set_title(f'Time Series — θ₀ = {theta0}°')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(th, om, 'r-', lw=0.5)
        ax.set_xlabel('θ'); ax.set_ylabel('dθ/dt')
        ax.set_title('Phase Portrait')
        ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)

    if forcing == 0 and damping == 0:
        actual_T = period_estimate(theta0_rad)
        T0 = small_angle_period()
        if actual_T:
            st.info(f"📊 **Period:** T = {actual_T:.3f}s  |  Small-angle approx: T₀ = {T0:.3f}s  |  Ratio: {actual_T/T0:.3f}×")


def sim_numerics_compare():
    """Compare Euler vs RK4."""
    st.markdown("### 🔬 Interactive: Euler vs. Runge-Kutta 4")
    st.markdown("Compare the accuracy of different numerical methods.")
    col1, col2 = st.columns(2)
    with col1:
        method = st.selectbox("Method", ["RK4", "Euler", "Both"], key="num_method")
    with col2:
        step_size = st.selectbox("Step size h", [0.1, 0.05, 0.02, 0.01, 0.005], index=3)

    # Simple test: integrate harmonic oscillator
    def euler_step(y, h, omega=1.0):
        x, v = y
        return np.array([x + h * v, v - h * omega**2 * x])

    def rk4_step(y, h, omega=1.0):
        x, v = y
        def f(state):
            return np.array([state[1], -omega**2 * state[0]])
        k1 = f(y)
        k2 = f(y + 0.5 * h * k1)
        k3 = f(y + 0.5 * h * k2)
        k4 = f(y + h * k3)
        return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

    t_max = 20.0
    steps = int(t_max / step_size)
    t = np.linspace(0, t_max, steps)

    # Analytical solution
    x_exact = np.cos(t)  # x₀ = 1, v₀ = 0

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, x_exact, 'k-', lw=1.5, alpha=0.5, label='Exact')

    if method in ['Euler', 'Both']:
        y = np.array([1.0, 0.0])
        x_euler = [y[0]]
        for i in range(1, steps):
            y = euler_step(y, step_size)
            x_euler.append(y[0])
        ax.plot(t, x_euler, 'r-', lw=0.8, label=f'Euler (h={step_size})')

    if method in ['RK4', 'Both']:
        y = np.array([1.0, 0.0])
        x_rk4 = [y[0]]
        for i in range(1, steps):
            y = rk4_step(y, step_size)
            x_rk4.append(y[0])
        ax.plot(t, x_rk4, 'b--', lw=0.8, label=f'RK4 (h={step_size})')

    ax.set_xlabel('Time'); ax.set_ylabel('x')
    ax.set_title('Numerical Integration Comparison')
    ax.legend(); ax.grid(alpha=0.3)
    st.pyplot(fig)

    st.markdown("""
    **Observations:**
    - Euler diverges quickly — it's only first-order accurate
    - RK4 stays close to the exact solution even with large step sizes
    - All our simulations use RK4 for accuracy
    """)


def sim_phase_space():
    """Demonstrate phase space concept."""
    st.markdown("### 🔬 Interactive: Phase Space Visualization")
    col1, col2 = st.columns(2)
    with col1:
        theta0 = st.slider("θ₀ (°)", 10, 179, 45, 1, key="ps_th")
    with col2:
        omega0 = st.slider("Initial velocity", 0.0, 5.0, 0.0, 0.1, key="ps_w")

    theta0_rad = np.radians(theta0)
    t, th, om = sim_pend(theta0_rad, omega0, 20.0)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, th, 'b-', lw=0.7)
        ax.axhline(y=0, color='gray', ls='--', alpha=0.3)
        ax.set_xlabel('Time (s)'); ax.set_ylabel('θ (rad)')
        ax.set_title('Time Series — θ(t)')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(th, om, 'r-', lw=0.5)
        ax.scatter(th[0], om[0], c='g', s=50, zorder=5, label='Start')
        ax.scatter(th[-1], om[-1], c='r', s=50, zorder=5, label='End')
        ax.set_xlabel('θ'); ax.set_ylabel('dθ/dt')
        ax.set_title('Phase Portrait')
        ax.legend(); ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)

    st.markdown("""
    **The phase portrait reveals:**
    - **Closed curve** = periodic oscillation
    - **Spiral** = damped motion
    - Each point is a complete system state
    """)


# --- Brief intro simulations for Chapter 1 ---

def sim_duffing_intro():
    st.markdown("### 🔬 Interactive: Duffing Double-Well")
    col1, col2 = st.columns(2)
    with col1:
        gamma_f = st.slider("Forcing γ", 0.0, 0.6, 0.3, 0.01, key="di_g")
    with col2:
        alpha_v = st.selectbox("α (stiffness)", [-1.0, -0.5, 0.0, 0.5, 1.0], index=0, key="di_a")

    t, x, v = sim_duff(0.5, 0.0, 80.0, alpha=alpha_v, gamma=gamma_f, omega=1.2)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot(x[-3000:], v[-3000:], 'r-', lw=0.4)
        ax.set_xlabel('x'); ax.set_ylabel("x'")
        ax.set_title('Phase Portrait')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        xp = np.linspace(-2.5, 2.5, 200)
        V = potential(xp, alpha=alpha_v)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(xp, V, 'b-', lw=2)
        ax.set_xlabel('x'); ax.set_ylabel('V(x)')
        ax.set_title('Potential Energy')
        ax.grid(alpha=0.3)
        for vv in [-1, 0, 1]:
            ax.axvline(x=vv, color='gray', ls=':', alpha=0.3)
        st.pyplot(fig)


def sim_vdp_intro():
    st.markdown("### 🔬 Interactive: Van der Pol Limit Cycle")
    mu = st.slider("μ (nonlinear damping)", 0.0, 5.0, 1.0, 0.1, key="vdp_i")
    t, x, v = sim_vdp(0.1, 0.1, 60.0, mu=mu)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, x, 'b-', lw=0.6)
        ax.set_xlabel('Time'); ax.set_ylabel('x')
        ax.set_title(f'Van der Pol — μ = {mu:.1f}')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, v, 'r-', lw=0.4)
        ax.set_xlabel('x'); ax.set_ylabel("x'")
        ax.set_title('Limit Cycle')
        ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)


# --- Chapter 2 simulations ---

def sim_bifurcation():
    st.markdown("### 🔬 Interactive: Period-Doubling Route to Chaos")

    # Bifurcation diagram
    st.markdown("**Bifurcation Diagram** — sweeps r from 2.5 to 4.0")
    with st.spinner("Computing..."):
        r_vals = np.linspace(2.5, 4.0, 400)
        r_plot, x_plot = bifurcation_points(r_vals, n_transient=500, n_samples=100)

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.scatter(r_plot, x_plot, s=0.1, c='k', alpha=0.4)
    ax.set_xlabel('Control parameter r')
    ax.set_ylabel('Steady-state x')
    ax.set_title('Bifurcation Diagram — Logistic Map')
    ax.set_xlim(2.5, 4.0); ax.set_ylim(-0.05, 1.05)
    ax.grid(alpha=0.3)

    # Interactive marker
    r_marker = st.slider("r", 2.5, 4.0, 3.5, 0.01, key="bf_r")
    ax.axvline(x=r_marker, color='r', ls='--', lw=1.5)
    st.pyplot(fig)

    # Time series at selected r
    xs = iterate(0.5, r_marker, 100)
    fig2, ax2 = plt.subplots(figsize=(10, 3))
    ax2.plot(range(len(xs)), xs, 'b-', lw=0.6)
    ax2.set_xlabel('n'); ax2.set_ylabel('x_n')
    ax2.set_title(f'Time Series at r = {r_marker:.4f}')
    ax2.set_ylim(-0.05, 1.05); ax2.grid(alpha=0.3)
    st.pyplot(fig2)

    lyap = lyap_log(r_marker)
    st.metric("Lyapunov Exponent", f"{lyap:.4f}",
              delta="CHAOTIC" if lyap > 0 else "Periodic",
              delta_color="inverse")


def sim_limit_cycles():
    st.markdown("### 🔬 Interactive: From Sine Waves to Relaxation Oscillations")
    mu = st.slider("μ", 0.1, 10.0, 1.0, 0.1, key="lc_mu")
    t, x, v = sim_vdp(0.1, 0.1, 80.0, mu=mu)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, x, 'b-', lw=0.6)
        ax.set_xlabel('Time'); ax.set_ylabel('x')
        ax.set_title(f'μ = {mu:.1f}')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, v, 'r-', lw=0.4)
        ax.set_xlabel('x'); ax.set_ylabel("x'")
        ax.set_title('Limit Cycle')
        ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)

    st.markdown(f"""
    **Regime:** {'Nearly sinusoidal' if mu < 1 else 'Relaxation oscillation' if mu > 3 else 'Transition'}
    """)


def sim_bistability():
    st.markdown("### 🔬 Interactive: Duffing Bistability")
    col1, col2 = st.columns(2)
    with col1:
        gamma_f = st.slider("Forcing amplitude γ", 0.2, 0.6, 0.35, 0.01, key="bs_g")
    with col2:
        omega_f = st.slider("Forcing frequency ω", 0.5, 2.0, 1.2, 0.01, key="bs_w")

    # Two different initial conditions
    _, x1, v1 = sim_duff(0.5, 0.0, 100.0, gamma=gamma_f, omega=omega_f)
    _, x2, v2 = sim_duff(-0.5, 0.0, 100.0, gamma=gamma_f, omega=omega_f)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(x1[-3000:], v1[-3000:], 'b-', lw=0.4, label='x₀ = 0.5')
    axes[0].set_xlabel('x'); axes[0].set_ylabel("x'")
    axes[0].set_title('Starting in Right Well')
    axes[0].legend(); axes[0].grid(alpha=0.3)

    axes[1].plot(x2[-3000:], v2[-3000:], 'r-', lw=0.4, label='x₀ = -0.5')
    axes[1].set_xlabel('x'); axes[1].set_ylabel("x'")
    axes[1].set_title('Starting in Left Well')
    axes[1].legend(); axes[1].grid(alpha=0.3)

    st.pyplot(fig)

    st.markdown("""
    **Notice:** Same parameters, different initial conditions → **different stable states!**
    This is **bistability** — two coexisting attractors.
    """)


def sim_chaos():
    st.markdown("### 🔬 Interactive: Lorenz Butterfly")
    rho = st.slider("ρ (Rayleigh number)", 0.0, 50.0, 28.0, 0.5, key="ch_rho")
    t, x, y, z = sim_lorenz(1.0, 1.0, 1.0, 40.0, rho=rho)

    tab1, tab2 = st.tabs(["3D Attractor", "Time Series"])
    with tab1:
        fig = plt.figure(figsize=(9, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, 'b-', lw=0.4, alpha=0.8)
        ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
        ax.set_title(f'Lorenz Attractor — ρ = {rho}')
        st.pyplot(fig)

    with tab2:
        fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
        axes[0].plot(t, x, 'b-', lw=0.5); axes[0].set_ylabel('x(t)'); axes[0].grid(alpha=0.3)
        axes[1].plot(t, y, 'g-', lw=0.5); axes[1].set_ylabel('y(t)'); axes[1].grid(alpha=0.3)
        axes[2].plot(t, z, 'r-', lw=0.5); axes[2].set_ylabel('z(t)')
        axes[2].set_xlabel('Time'); axes[2].grid(alpha=0.3)
        st.pyplot(fig)

    st.markdown(f"""
    **Regime:** {'Chaos (strange attractor)' if rho > 24.7 else 'Stable fixed points'}
    """)


def sim_sensitivity():
    st.markdown("### 🔬 Interactive: Exponential Divergence")
    col1, col2 = st.columns(2)
    with col1:
        th1_0 = st.slider("θ₁₀ (rad)", 0.0, np.pi, np.pi/2, 0.1, key="se_th1")
    with col2:
        t_span = st.slider("Time (s)", 5, 40, 20, 5, key="se_t")

    # Two nearly identical starts
    t, _, _, _, _, _, _, x2a, y2a = sim_double(th1_0, 0.0, 0, 0, t_span)
    t, _, _, _, _, _, _, x2b, y2b = sim_double(th1_0 + 0.001, 0.0, 0, 0, t_span)

    diff = np.sqrt((x2a - x2b)**2 + (y2a - y2b)**2)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(x2a, y2a, 'b-', lw=0.4, alpha=0.7, label='θ₁₀')
    axes[0].plot(x2b, y2b, 'r-', lw=0.4, alpha=0.7, label='θ₁₀ + 0.001')
    axes[0].set_xlabel('x'); axes[0].set_ylabel('y')
    axes[0].set_title('Two Trajectories')
    axes[0].legend(fontsize=8); axes[0].axis('equal'); axes[0].grid(alpha=0.3)

    axes[1].semilogy(t, diff + 1e-16, 'k-', lw=0.8)
    axes[1].set_xlabel('Time (s)'); axes[1].set_ylabel('Distance')
    axes[1].set_title('Exponential Divergence')
    axes[1].grid(alpha=0.3)

    st.pyplot(fig)

    st.info(f"""
    **Final separation:** {diff[-1]:.4f} (from initial 0.001)
    This is the **butterfly effect** in action!
    """)


# --- Lab simulations (free exploration) ---

def lab_pendulum():
    sim_pendulum_basic()

def lab_duffing():
    sim_duffing_intro()

def lab_vdp():
    sim_vdp_intro()

def lab_lorenz():
    sim_chaos()

def lab_logistic():
    sim_bifurcation()

def lab_double():
    sim_sensitivity()


# ============================================================
# SIMULATION DISPATCH
# ============================================================

SIM_DISPATCH = {
    'pendulum_basic': sim_pendulum_basic,
    'numerics_compare': sim_numerics_compare,
    'phase_space': sim_phase_space,
    'duffing_intro': sim_duffing_intro,
    'vdp_intro': sim_vdp_intro,
    'bifurcation': sim_bifurcation,
    'limit_cycles': sim_limit_cycles,
    'bistability': sim_bistability,
    'chaos': sim_chaos,
    'sensitivity': sim_sensitivity,
    'lab_pendulum': lab_pendulum,
    'lab_duffing': lab_duffing,
    'lab_vdp': lab_vdp,
    'lab_lorenz': lab_lorenz,
    'lab_logistic': lab_logistic,
    'lab_double': lab_double,
}


# ============================================================
# APP LAYOUT
# ============================================================

# Sidebar navigation
st.sidebar.title("🌀 Nonlinear Dynamics")
st.sidebar.markdown("*Interactive Course*")
st.sidebar.markdown("Dr. Bounthong VONGXAYA")
st.sidebar.markdown("---")

# Chapter selector
chap_ids = [ch['id'] for ch in CHAPTERS]
chap_labels = [f"{ch['icon']} {ch['title']}" for ch in CHAPTERS]
selected_idx = st.sidebar.radio("", chap_labels, index=0)
selected_id = chap_ids[chap_labels.index(selected_idx)]
current = [ch for ch in CHAPTERS if ch['id'] == selected_id][0]

# Section selector (if chapter has sections)
selected_section = None
if 'sections' in current and current['sections']:
    sec_labels = [s['title'] for s in current['sections']]
    selected_sec_title = st.sidebar.radio("Section", sec_labels, key="sec_select")
    selected_section = [s for s in current['sections'] if s['title'] == selected_sec_title][0]

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** Adjust parameters in each simulation to explore the phenomena.")

# ============================================================
# MAIN CONTENT
# ============================================================

# Header
st.title(f"{current['icon']} {current['title']}")
st.markdown(f"**{current.get('subtitle', '')}**")
st.markdown("---")

# Render content
if selected_section:
    # Show section content
    content = selected_section.get('content', '')
    if content:
        st.markdown(content)
        st.markdown("---")

    # Run simulation if specified
    sim_id = selected_section.get('simulation')
    if sim_id and sim_id in SIM_DISPATCH:
        SIM_DISPATCH[sim_id]()
        st.markdown("---")

    # Add notes to Chapter 3 lab sections
    if current['id'] == 'ch3_lab':
        st.subheader("📝 Lab Notes")
        st.text_area("Your observations:", height=120,
                     placeholder="What did you discover? Record your findings here.")

else:
    # Show chapter-level content
    content = current.get('content', '')
    if content:
        st.markdown(content)

    # Run chapter-level simulation if specified
    sim_id = current.get('simulation')
    if sim_id and sim_id in SIM_DISPATCH:
        SIM_DISPATCH[sim_id]()

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown("""
*Nonlinear Dynamics — Interactive Course*  
Dr. Bounthong VONGXAYA  
Based on "Ordnung und Chaos bei nichtlinearen Schwingungen" (1995)
""")
