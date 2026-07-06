"""
Nonlinear Dynamics Laboratory — Interactive Streamlit App

A modern interactive application inspired by the 1995 book:
"Ordnung und Chaos bei nichtlinearen Schwingungen"

Users can explore nonlinear systems in real-time by adjusting parameters
and seeing immediate visual feedback.

Author: Dr. Bounthong VONGXAYA
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Import all simulation modules
from python.logistic_map import iterate, bifurcation_points, lyapunov_exponent as lyap_logistic
from python.nonlinear_pendulum import simulate as sim_pendulum, small_angle_period
from python.lorenz_attractor import simulate as sim_lorenz
from python.duffing_oscillator import simulate as sim_duffing, potential
from python.van_der_pol import simulate as sim_vdp

# Page config
st.set_page_config(
    page_title="Nonlinear Dynamics Laboratory",
    page_icon="🌀",
    layout="wide"
)

rcParams['figure.dpi'] = 100


def plot_timeseries(t, x, title="Time Series"):
    """Plot time series."""
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t, x, 'b-', linewidth=0.6)
    ax.set_xlabel('Time')
    ax.set_ylabel('x')
    ax.set_title(title)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig


def plot_phase(x, v, title="Phase Portrait"):
    """Plot phase portrait."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x, v, 'r-', linewidth=0.4)
    ax.set_xlabel('x')
    ax.set_ylabel("x'")
    ax.set_title(title)
    ax.grid(alpha=0.3)
    ax.axis('equal')
    plt.tight_layout()
    return fig


# ============================================================
# SIDEBAR — System Selection & Parameters
# ============================================================

st.sidebar.title("🌀 Nonlinear Dynamics Lab")
st.sidebar.markdown("---")

system = st.sidebar.selectbox(
    "Select System",
    ["Logistic Map",
     "Nonlinear Pendulum",
     "Lorenz Attractor",
     "Duffing Oscillator",
     "Van der Pol Oscillator"]
)

st.sidebar.markdown("### Parameters")

# ============================================================
# LOGISTIC MAP
# ============================================================

if system == "Logistic Map":
    st.title("Logistic Map")
    st.markdown(r"$$x_{n+1} = r \cdot x_n \cdot (1 - x_n)$$")

    col1, col2, col3 = st.columns(3)

    with col1:
        r = st.slider("r (control parameter)", 2.5, 4.0, 3.8, 0.01)
    with col2:
        x0 = st.slider("x₀ (initial value)", 0.01, 0.99, 0.5, 0.01)
    with col3:
        n_iter = st.slider("Iterations", 50, 500, 100, 10)

    # Compute
    xs = iterate(x0, r, n_iter)
    lyap = lyap_logistic(r)

    # Display
    tab1, tab2, tab3 = st.tabs(["Time Series", "Bifurcation Diagram", "Info"])

    with tab1:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(range(len(xs)), xs, 'b-', linewidth=0.6)
        ax.set_xlabel('n'); ax.set_ylabel('x_n')
        ax.set_title(f'Logistic Map — r = {r:.4f}')
        ax.set_ylim(-0.05, 1.05)
        ax.grid(alpha=0.3)
        st.pyplot(fig)

        st.metric("Lyapunov Exponent", f"{lyap:.4f}",
                  delta="CHAOS" if lyap > 0 else "Order",
                  delta_color="inverse")

    with tab2:
        st.markdown("**Bifurcation Diagram** (full range r = 2.5 to 4.0)")
        with st.spinner("Computing..."):
            r_vals = np.linspace(2.5, 4.0, 300)
            r_plot, x_plot = bifurcation_points(r_vals, n_transient=500, n_samples=100)

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.scatter(r_plot, x_plot, s=0.1, c='k', alpha=0.4)
        ax.axvline(x=r, color='r', linestyle='--', linewidth=1, label=f'r = {r:.2f}')
        ax.set_xlabel('r'); ax.set_ylabel('x')
        ax.set_title('Bifurcation Diagram')
        ax.set_xlim(2.5, 4.0); ax.set_ylim(-0.05, 1.05)
        ax.legend(); ax.grid(alpha=0.3)
        st.pyplot(fig)

    with tab3:
        st.markdown("""
        **About the Logistic Map**

        The logistic map is the simplest equation that demonstrates deterministic chaos:

        - **r < 1**: Population dies out (x → 0)
        - **1 < r < 3**: Stable fixed point
        - **3 < r < 3.45**: Period 2 oscillation
        - **3.45 < r < 3.54**: Period 4
        - **3.57 < r ≤ 4**: Chaos (with periodic windows)

        **Lyapunov Exponent:** λ > 0 = chaos, λ < 0 = order
        """)

# ============================================================
# NONLINEAR PENDULUM
# ============================================================

elif system == "Nonlinear Pendulum":
    st.title("Nonlinear Pendulum")
    st.markdown(r"$$\ddot{\theta} + \gamma \dot{\theta} + \omega_0^2 \sin(\theta) = F \cos(\omega t)$$")

    col1, col2, col3 = st.columns(3)
    with col1:
        theta0 = st.slider("θ₀ (initial angle)", 0.1, 3.0, 1.0, 0.1)
    with col2:
        gamma = st.slider("γ (damping)", 0.0, 2.0, 0.2, 0.01)
    with col3:
        F = st.slider("F (forcing amp.)", 0.0, 2.0, 0.0, 0.01)

    col1, col2, col3 = st.columns(3)
    with col1:
        omega_f = st.slider("ω (forcing freq.)", 0.5, 2.0, 2.0/3.0, 0.01)
    with col2:
        t_span = st.slider("Time span (s)", 10, 100, 50, 5)
    with col3:
        L = st.number_input("Length L (m)", 0.5, 5.0, 1.0, 0.1)

    t, theta, omega = sim_pendulum(theta0, 0.0, t_span, gamma=gamma, L=L, F=F, omega=omega_f)
    T_small = small_angle_period(L=L)

    tab1, tab2 = st.tabs(["Time Series & Phase Portrait", "Info"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.pyplot(plot_timeseries(t, theta, f'Pendulum — θ₀={theta0:.1f}, γ={gamma:.2f}'))
        with c2:
            st.pyplot(plot_phase(theta, omega, 'Phase Portrait'))

        st.markdown(f"""**Small-angle period:** {T_small:.3f} s  
        **Actual period:** varies with amplitude (θ₀={theta0:.1f})""")

    with tab2:
        st.markdown("""
        **About the Nonlinear Pendulum**

        Unlike the simple harmonic oscillator, the real pendulum's period **depends on amplitude**:
        - Small angles: close to 2π√(L/g)
        - Large angles: period increases significantly
        - With damping + forcing: can become chaotic
        """)

# ============================================================
# LORENZ ATTRACTOR
# ============================================================

elif system == "Lorenz Attractor":
    st.title("Lorenz Attractor")
    st.markdown(r"""
    $$
    \begin{align*}
    \frac{dx}{dt} &= \sigma(y - x) \\
    \frac{dy}{dt} &= x(\rho - z) - y \\
    \frac{dz}{dt} &= xy - \beta z
    \end{align*}
    $$
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        rho = st.slider("ρ (Rayleigh number)", 0.0, 50.0, 28.0, 0.5)
    with col2:
        sigma = st.slider("σ (Prandtl number)", 5.0, 20.0, 10.0, 0.5)
    with col3:
        beta = st.slider("β (geometric factor)", 1.0, 4.0, 8.0/3.0, 0.01)

    t_span = st.slider("Time span", 10, 80, 40, 5)

    t, x, y, z = sim_lorenz(1.0, 1.0, 1.0, t_span, sigma=sigma, rho=rho, beta=beta)

    tab1, tab2, tab3 = st.tabs(["3D Attractor", "Time Series", "Info"])

    with tab1:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, 'b-', linewidth=0.4, alpha=0.8)
        ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
        ax.set_title(f'Lorenz Attractor — σ={sigma}, ρ={rho}, β={beta:.3f}')
        st.pyplot(fig)

    with tab2:
        fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
        axes[0].plot(t, x, 'b-', linewidth=0.5); axes[0].set_ylabel('x(t)'); axes[0].grid(alpha=0.3)
        axes[1].plot(t, y, 'g-', linewidth=0.5); axes[1].set_ylabel('y(t)'); axes[1].grid(alpha=0.3)
        axes[2].plot(t, z, 'r-', linewidth=0.5); axes[2].set_ylabel('z(t)'); axes[2].grid(alpha=0.3)
        axes[2].set_xlabel('Time')
        plt.tight_layout()
        st.pyplot(fig)

    with tab3:
        st.markdown("""
        **About the Lorenz Attractor**

        Discovered by Edward Lorenz in 1963 while modeling atmospheric convection:
        - **ρ < 1**: Only one fixed point (origin)
        - **1 < ρ < 24.7**: Two stable fixed points
        - **ρ > 24.7**: Chaos — the butterfly attractor
        - **Higher ρ**: More complex dynamics

        **Classic parameters:** σ=10, β=8/3, ρ=28
        """)

# ============================================================
# DUFFING OSCILLATOR
# ============================================================

elif system == "Duffing Oscillator":
    st.title("Duffing Oscillator")
    st.markdown(r"$$\ddot{x} + \delta \dot{x} + \alpha x + \beta x^3 = \gamma \cos(\omega t)$$")

    col1, col2, col3 = st.columns(3)
    with col1:
        delta = st.slider("δ (damping)", 0.0, 1.0, 0.2, 0.01)
    with col2:
        alpha = st.slider("α (linear stiffness)", -2.0, 2.0, -1.0, 0.1)
    with col3:
        beta_nl = st.slider("β (nonlinear stiffness)", -1.0, 2.0, 1.0, 0.1)

    col1, col2, col3 = st.columns(3)
    with col1:
        gamma_f = st.slider("γ (forcing amp.)", 0.0, 1.0, 0.3, 0.01)
    with col2:
        omega_f = st.slider("ω (forcing freq.)", 0.5, 2.0, 1.2, 0.01)
    with col3:
        t_span = st.slider("Time span", 20, 200, 80, 10)

    t, x, v = sim_duffing(0.5, 0.0, t_span, delta=delta, alpha=alpha,
                          beta=beta_nl, gamma=gamma_f, omega=omega_f)

    tab1, tab2, tab3 = st.tabs(["Phase Portrait", "Time Series", "Info"])

    with tab1:
        # Also show the potential
        c1, c2 = st.columns(2)
        with c1:
            st.pyplot(plot_phase(x, v, f'Duffing — γ={gamma_f:.2f}'))
        with c2:
            x_pot = np.linspace(-2.5, 2.5, 200)
            V = potential(x_pot, alpha=alpha, beta=beta_nl)
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(x_pot, V, 'b-', linewidth=2)
            ax.set_xlabel('x'); ax.set_ylabel('V(x)')
            ax.set_title('Potential')
            ax.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)

    with tab2:
        st.pyplot(plot_timeseries(t, x, f'Duffing — γ={gamma_f:.2f}, δ={delta:.2f}'))

    with tab3:
        st.markdown("""
        **About the Duffing Oscillator**

        A forced nonlinear oscillator with rich dynamics:
        - **Double-well potential** (α < 0, β > 0): two stable equilibria
        - **Intrawell**: trapped in one well (low forcing)
        - **Cross-well**: jumps between wells (high forcing → chaos)
        - **Bistability**: two stable solutions can coexist
        """)

# ============================================================
# VAN DER POL
# ============================================================

elif system == "Van der Pol Oscillator":
    st.title("Van der Pol Oscillator")
    st.markdown(r"$$\ddot{x} - \mu(1 - x^2)\dot{x} + x = F\cos(\omega t)$$")

    col1, col2, col3 = st.columns(3)
    with col1:
        mu = st.slider("μ (nonlinear damping)", 0.0, 10.0, 1.0, 0.1)
    with col2:
        F = st.slider("F (forcing amp.)", 0.0, 2.0, 0.0, 0.01)
    with col3:
        omega_f = st.slider("ω (forcing freq.)", 0.5, 2.0, 1.2, 0.01)

    t_span = st.slider("Time span", 20, 200, 80, 10)

    t, x, v = sim_vdp(0.1, 0.1, t_span, mu=mu, F=F, omega=omega_f)

    tab1, tab2, tab3 = st.tabs(["Phase Portrait", "Time Series", "Info"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.pyplot(plot_phase(x, v, f'Van der Pol — μ={mu:.1f}'))
        with c2:
            # Show convergence to limit cycle from different starting points
            _, x2, v2 = sim_vdp(3.0, 0.0, t_span, mu=min(mu, 5.0), F=F, omega=omega_f)
            fig, ax = plt.subplots(figsize=(6, 5))
            ax.plot(x, v, 'b-', linewidth=0.4, label='x₀=0.1')
            ax.plot(x2, v2, 'r-', linewidth=0.4, alpha=0.5, label='x₀=3.0')
            ax.set_xlabel('x'); ax.set_ylabel("x'")
            ax.set_title('Limit Cycle Convergence')
            ax.legend(fontsize=8); ax.grid(alpha=0.3); ax.axis('equal')
            plt.tight_layout()
            st.pyplot(fig)

    with tab2:
        st.pyplot(plot_timeseries(t, x, f'Van der Pol — μ={mu:.1f}'))

    with tab3:
        st.markdown("""
        **About the Van der Pol Oscillator**

        The classic self-excited oscillator:
        - **μ = 0**: Simple harmonic oscillator
        - **0 < μ < 1**: Nearly sinusoidal limit cycle
        - **μ > 1**: Relaxation oscillations (slow-fast dynamics)
        - **Large μ**: Sharp spikes followed by slow recovery
        - **With forcing**: Can become chaotic
        """)

# ============================================================
# FOOTER
# ============================================================

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Nonlinear Dynamics Laboratory**  
Dr. Bounthong VONGXAYA  
*Based on the 1995 book "Ordnung und Chaos bei nichtlinearen Schwingungen"*
""")
