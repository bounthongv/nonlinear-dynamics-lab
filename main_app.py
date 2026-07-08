"""
main_app.py — Nonlinear Dynamics Laboratory
=============================================
Unified web app combining:
  📗 Archive: 1995 German book
  🚀 Modern English Course
  🔬 Interactive Simulation Lab
  ℹ️ About the Author

Author: Dr. Bounthong VONGXAYA
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import re
import os

# Import all simulation modules
from python.logistic_map import iterate, bifurcation_points, lyapunov_exponent as lyap_log
from python.nonlinear_pendulum import simulate as sim_pend, small_angle_period, period_estimate
from python.lorenz_attractor import simulate as sim_lorenz
from python.duffing_oscillator import simulate as sim_duff, potential
from python.van_der_pol import simulate as sim_vdp
from python.double_pendulum import simulate as sim_double

rcParams['figure.dpi'] = 100

st.set_page_config(page_title="Nonlinear Dynamics Laboratory",
                   page_icon="🌀", layout="wide")

# ============================================================
# GLOBAL HELPERS
# ============================================================

def load_book():
    with open('ocr/book_transcribed.md', 'r', encoding='utf-8') as f:
        return f.read()

def get_page_text(book_text, page_num):
    pattern = rf'## Page {page_num}\n(.*?)(?=\n## Page \d+|\Z)'
    match = re.search(pattern, book_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return '*[Page not found]*'

def get_page_range(book_text, start, end):
    parts = []
    for p in range(start, end + 1):
        content = get_page_text(book_text, p)
        if content and content != '*[Page not found]*':
            parts.append(f'## Page {p}\n{content}')
    return '\n\n'.join(parts)
def render_book_content(markdown_text):
    """Render book content with equation support AND figure images."""
    # First split by display math blocks (handles multi-line equations)
    blocks = re.split(r'(\$\$.*?\$\$)', markdown_text, flags=re.DOTALL)
    
    for block in blocks:
        if not block.strip():
            continue
        
        # Check if this is a display equation
        if block.startswith('$$') and block.endswith('$$'):
            latex = block[2:-2].strip().rstrip('\n')
            if latex:
                st.latex(latex)
        else:
            # Process non-equation content line by line
            for line in block.split('\n'):
                if not line.strip():
                    continue
                # Check if this is a figure reference
                img_match = re.match(r'!\[Figure\]\(([^)]+)\)', line.strip())
                if img_match:
                    img_path = img_match.group(1)
                    if os.path.exists(img_path):
                        st.image(img_path, width=600)
                    else:
                        st.markdown(f'*[Figure not available: {img_path}]*')
                else:
                    st.markdown(line, unsafe_allow_html=True)

def styled_plot(fig, title=None):
    if title:
        fig.suptitle(title, fontsize=13, fontweight='bold')
    plt.tight_layout()
    return fig

# ============================================================
# NAVIGATION
# ============================================================

NAV_ITEMS = [
    ("🚀 Modern Course", "course"),
    ("🔬 Simulation Lab", "lab"),
    ("📗 Archive (1995)", "archive"),
    ("📖 About", "about"),
]

st.sidebar.title("🌀 Nonlinear Dynamics")
st.sidebar.markdown("*Laboratory*")
st.sidebar.markdown("Dr. Bounthong VONGXAYA")
st.sidebar.markdown("---")

nav_labels = [item[0] for item in NAV_ITEMS]
nav_ids = [item[1] for item in NAV_ITEMS]
selection = st.sidebar.radio("Section", nav_labels, index=0)
current_page = nav_ids[nav_labels.index(selection)]
st.sidebar.markdown("---")

# ============================================================
# COURSE STRUCTURE (full hierarchical)
# ============================================================

COURSE_CHAPTERS = [
    {
        'id': 'intro',
        'icon': '🎯',
        'title': 'Introduction',
        'subtitle': 'What Are Nonlinear Systems?',
        'content': """
**Nonlinear systems are everywhere.** A pendulum swinging through large angles,
a population with limited resources, weather patterns — all are inherently nonlinear.

| Linear | Nonlinear |
|---|---|
| $$\\ddot{x} + \\omega_0^2 x = 0$$ | $$\\ddot{x} + \\omega_0^2 \\sin x = 0$$ |
| Proportional response | Response depends on state |
| Superposition holds | Superposition fails |

**What you'll explore:**
- Period doubling and bifurcations
- Limit cycles and self-excited oscillations
- Bistability and hysteresis
- Chaos and the butterfly effect

> 📖 **Want to go deeper?** This course is a streamlined introduction. The full theoretical foundation — including detailed derivations, historical context, and 63 pages of in-depth physics — is available in both **German and English** in the **Archive**. Navigate to *📗 Archive (1995)* in the sidebar and toggle between languages.
""",
        'simulation': None,
    },
    {
        'id': 'ch1',
        'icon': '📐',
        'title': 'Chapter 1: Foundations',
        'subtitle': 'Physical Systems & Numerical Methods',
        'sections': [
            {
                'id': 'pendulum',
                'title': '1.1 The Nonlinear Pendulum',
                'content': """
The **mathematical pendulum** is the classic starting point for nonlinear dynamics.

For small angles, $$\\sin\\theta \\approx \\theta$$ gives the linear equation.
But for **large angles**, the full nonlinear equation applies:

$$\\ddot{\\theta} + \\gamma \\dot{\\theta} + \\omega_0^2 \\sin\\theta = F \\cos(\\omega t)$$

**Key insight:** The period now depends on amplitude — impossible in linear systems.
""",
                'simulation': 'pendulum',
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

RK4 is used in all simulations throughout this course.
""",
                'simulation': 'numerics',
            },
            {
                'id': 'phasespace',
                'title': '1.3 Phase Space',
                'content': """
Instead of plotting just $$x(t)$$, we plot **$$x$$ vs $$\\dot{x}$$** — the **phase portrait**.

- **Closed curve** = periodic oscillation
- **Spiral** = damped motion
- **Strange attractor** = chaotic motion
""",
                'simulation': 'phase_space',
            },
            {
                'id': 'duffing_intro',
                'title': '1.4 The Duffing Oscillator',
                'content': """
The Duffing oscillator adds a **nonlinear restoring force**:

$$\\ddot{x} + \\delta \\dot{x} + \\alpha x + \\beta x^3 = \\gamma \\cos(\\omega t)$$

With $$\\alpha < 0, \\beta > 0$$, the system has a **double-well potential**.
""",
                'simulation': 'duffing',
            },
            {
                'id': 'vdp_intro',
                'title': '1.5 The Van der Pol Oscillator',
                'content': """
$$\\ddot{x} - \\mu(1 - x^2)\\dot{x} + x = F \\cos(\\omega t)$$

For $$\\mu > 0$$, the system spontaneously oscillates — producing a stable **limit cycle**.
""",
                'simulation': 'vdp',
            },
        ]
    },
    {
        'id': 'ch2',
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
Fixed point → Period 2 → Period 4 → ... → **Chaos**
""",
                'simulation': 'logistic',
            },
            {
                'id': 'limit_cycles',
                'title': '2.2 Limit Cycles & Relaxation Oscillations',
                'content': """
A **limit cycle** is an isolated closed trajectory — the system settles
into a stable oscillation regardless of initial conditions.

In the Van der Pol oscillator, increasing $$\\mu$$ transforms:
- $$\\mu \\ll 1$$: Nearly sinusoidal
- $$\\mu \\gg 1$$: **Relaxation oscillation** — slow build-up, rapid discharge
""",
                'simulation': 'vdp',
            },
            {
                'id': 'bistability',
                'title': '2.3 Bistability & Hysteresis',
                'content': """
In the Duffing oscillator, **two stable states can coexist** for the same
parameters. Which one the system chooses depends on its history — **hysteresis**.
""",
                'simulation': 'duffing',
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

For $$\\rho > 24.7$$, the trajectory forms a **strange attractor**.
""",
                'simulation': 'lorenz',
            },
            {
                'id': 'sensitivity',
                'title': '2.5 Sensitivity to Initial Conditions',
                'content': """
The **double pendulum** is the most直观 example of sensitive dependence.

Two pendulums starting with a **0.001 radian difference** diverge to
completely different trajectories within seconds.
""",
                'simulation': 'double',
            },
        ]
    },
    {
        'id': 'ch3',
        'icon': '🔬',
        'title': 'Chapter 3: Interactive Lab',
        'subtitle': 'Free Exploration Mode',
        'content': 'Choose any system and explore freely.',
        'sections': [
            {'id': 'lab_pendulum', 'title': 'Pendulum Lab', 'simulation': 'pendulum'},
            {'id': 'lab_duffing', 'title': 'Duffing Lab', 'simulation': 'duffing'},
            {'id': 'lab_vdp', 'title': 'Van der Pol Lab', 'simulation': 'vdp'},
            {'id': 'lab_lorenz', 'title': 'Lorenz Lab', 'simulation': 'lorenz'},
            {'id': 'lab_logistic', 'title': 'Logistic Map Lab', 'simulation': 'logistic'},
            {'id': 'lab_double', 'title': 'Double Pendulum Lab', 'simulation': 'double'},
        ]
    },
]

# ============================================================
# ARCHIVE CHAPTERS (German)
# ============================================================

ARCHIVE_CHAPTERS = [
    {
        'id': 'vorwort',
        'title_de': '📖 Vorwort',
        'title_en': '📖 Foreword',
        'pages': [1],
    },
    {
        'id': 'ch1',
        'title_de': '🔬 Kapitel I: Nichtlineare Schwingungen',
        'title_en': '🔬 Chapter I: Nonlinear Oscillations',
        'pages': list(range(2, 16)),
        'sections': [
            ('1.1 Pendel', [2, 3]),
            ('1.2 Duffing', [3, 4]),
            ('1.3 Phasenraum', [5, 6]),
            ('1.4 Amplitudenabhängigkeit', [7, 8, 9]),
            ('1.5 Dissipatives System', [10, 11]),
            ('1.6 Grenzzyklus', [11, 12, 13, 14]),
            ('1.7 Stroboskopisch', [14, 15]),
        ],
    },
    {
        'id': 'ch2',
        'title_de': '✏️ Kapitel II: Aufgaben',
        'title_en': '✏️ Chapter II: Exercises',
        'pages': [16, 17],
    },
    {
        'id': 'ch3',
        'title_de': '📐 Kapitel III: Grundlagen',
        'title_en': '📐 Chapter III: Foundations',
        'pages': list(range(18, 30)),
    },
    {
        'id': 'ch4',
        'title_de': '📋 Kapitel IV: Dokumentation',
        'title_en': '📋 Chapter IV: Documentation',
        'pages': list(range(30, 64)),
    },
]

# ============================================================
# SIDEBAR NAVIGATION (per-page)
# ============================================================

# Course navigation
if current_page == 'course':
    st.sidebar.markdown("### 📚 Course Contents")
    ch_titles = [f"{ch['icon']} {ch['title']}" for ch in COURSE_CHAPTERS]
    ch_sel = st.sidebar.radio("Chapter", ch_titles, key="course_ch")
    current_ch = [ch for ch in COURSE_CHAPTERS if f"{ch['icon']} {ch['title']}" == ch_sel][0]
    current_section = None
    if 'sections' in current_ch:
        sec_titles = [s['title'] for s in current_ch['sections']]
        sec_sel = st.sidebar.radio("Section", sec_titles, key="course_sec")
        current_section = [s for s in current_ch['sections'] if s['title'] == sec_sel][0]
    st.sidebar.markdown("---")
    st.sidebar.markdown("💡 **Adjust sliders below to explore**")

# Archive navigation
elif current_page == 'archive':
    # Language toggle MUST come first so labels update on same click
    if 'archive_lang' not in st.session_state:
        st.session_state.archive_lang = 'de'
    lang = st.sidebar.radio("Sprache / Language", ["🇩🇪 Deutsch", "🇬🇧 English"],
                           index=0 if st.session_state.archive_lang == 'de' else 1,
                           key="archive_lang_radio")
    st.session_state.archive_lang = 'de' if 'Deutsch' in lang else 'en'
    lang = st.session_state.archive_lang

    # Language-dependent labels (now uses correct lang)
    if lang == 'de':
        nav_title = "📖 Buchnavigation"
        ch_label = "Kapitel"
        sec_label = "Abschnitt"
        all_label = "Alle"
    else:
        nav_title = "📖 Book Navigation"
        ch_label = "Chapter"
        sec_label = "Section"
        all_label = "All"

    st.sidebar.markdown(f"### {nav_title}")
    st.sidebar.markdown("---")

    arch_titles = [ch[f'title_{lang}'] for ch in ARCHIVE_CHAPTERS]
    arch_sel = st.sidebar.radio(ch_label, arch_titles, key="arch_ch")
    current_arch_ch = [ch for ch in ARCHIVE_CHAPTERS if ch[f'title_{lang}'] == arch_sel][0]
    arch_pages = current_arch_ch['pages']
    if 'sections' in current_arch_ch:
        sec_labels = [all_label] + [s[0] for s in current_arch_ch['sections']]
        sec_sel = st.sidebar.radio(sec_label, sec_labels, key="arch_sec")
        if sec_sel != all_label:
            for s_t, s_p in current_arch_ch['sections']:
                if sec_sel == s_t:
                    arch_pages = s_p
                    break
    st.sidebar.markdown("---")

# ============================================================
# SIMULATION RENDERERS
# ============================================================

def sim_pendulum():
    col1, col2, col3 = st.columns(3)
    with col1:
        theta0 = st.slider("θ₀ (°)", 5, 179, 45, 1, key="u_pth")
    with col2:
        gamma = st.slider("Damping γ", 0.0, 1.0, 0.0, 0.01, key="u_pg")
    with col3:
        forcing = st.slider("Forcing F", 0.0, 0.5, 0.0, 0.01, key="u_pf")
    th0_rad = np.radians(theta0)
    t, th, om = sim_pend(th0_rad, 0.0, 20.0, gamma=gamma, F=forcing)
    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, th, 'b-', lw=0.7)
        ax.set_xlabel('Time (s)'); ax.set_ylabel('θ (rad)')
        ax.set_title(f'θ₀ = {theta0}°'); ax.grid(alpha=0.3)
        st.pyplot(fig)
    with c2:
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(th, om, 'r-', lw=0.5)
        ax.set_xlabel('θ'); ax.set_ylabel('dθ/dt')
        ax.set_title('Phase Portrait'); ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)
    if forcing == 0 and gamma == 0:
        actual_T = period_estimate(th0_rad)
        if actual_T:
            st.info(f"Period T = {actual_T:.3f}s (small-angle: {small_angle_period():.3f}s)")

def sim_logistic():
    col1, col2 = st.columns(2)
    with col1:
        r = st.slider("r", 2.5, 4.0, 3.8, 0.01, key="u_lr")
    with col2:
        x0 = st.slider("x₀", 0.01, 0.99, 0.5, 0.01, key="u_lx")
    xs = iterate(x0, r, 100)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(range(len(xs)), xs, 'b-', lw=0.6)
    axes[0].set_xlabel('n'); axes[0].set_ylabel('x_n')
    axes[0].set_title(f'r={r:.4f}'); axes[0].set_ylim(-0.05, 1.05); axes[0].grid(alpha=0.3)
    with st.spinner("Computing bifurcation..."):
        rv = np.linspace(2.5, 4.0, 300)
        rp, xp = bifurcation_points(rv, n_transient=500, n_samples=100)
    axes[1].scatter(rp, xp, s=0.1, c='k', alpha=0.4)
    axes[1].axvline(x=r, color='r', ls='--', lw=1)
    axes[1].set_xlabel('r'); axes[1].set_ylabel('x')
    axes[1].set_title('Bifurcation Diagram'); axes[1].set_xlim(2.5, 4.0); axes[1].set_ylim(-0.05, 1.05); axes[1].grid(alpha=0.3)
    st.pyplot(fig)
    lyap = lyap_log(r)
    st.metric("Lyapunov Exponent", f"{lyap:.4f}", delta="CHAOS" if lyap > 0 else "Periodic", delta_color="inverse")

def sim_lorenz_sim():
    rho = st.slider("ρ", 0.0, 50.0, 28.0, 0.5, key="u_lr_rho")
    t, x, y, z = sim_lorenz(1.0, 1.0, 1.0, 40.0, rho=rho)
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, 'b-', lw=0.4, alpha=0.8)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title(f'Lorenz Attractor — ρ={rho}')
    st.pyplot(fig)
    st.markdown(f"**Regime:** {'Chaos' if rho > 24.7 else 'Stable fixed points'}")

def sim_duffing_sim():
    col1, col2 = st.columns(2)
    with col1:
        gf = st.slider("Forcing γ", 0.0, 0.8, 0.3, 0.01, key="u_dg")
    with col2:
        delta = st.slider("Damping δ", 0.0, 0.5, 0.2, 0.01, key="u_dd")
    t, x, v = sim_duff(0.5, 0.0, 100.0, delta=delta, gamma=gf, omega=1.2)
    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot(x[-3000:], v[-3000:], 'r-', lw=0.3)
        ax.set_xlabel('x'); ax.set_ylabel("x'")
        ax.set_title('Phase Portrait'); ax.grid(alpha=0.3)
        st.pyplot(fig)
    with c2:
        xp = np.linspace(-2, 2, 200)
        V = potential(xp)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(xp, V, 'b-', lw=2)
        ax.set_xlabel('x'); ax.set_ylabel('V(x)')
        ax.set_title('Potential'); ax.grid(alpha=0.3)
        st.pyplot(fig)

def sim_vdp_sim():
    mu = st.slider("μ", 0.0, 8.0, 1.0, 0.1, key="u_vm")
    t, x, v = sim_vdp(0.1, 0.1, 60.0, mu=mu)
    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, x, 'b-', lw=0.6)
        ax.set_xlabel('Time'); ax.set_ylabel('x')
        ax.set_title(f'μ={mu:.1f}'); ax.grid(alpha=0.3)
        st.pyplot(fig)
    with c2:
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, v, 'r-', lw=0.4)
        ax.set_xlabel('x'); ax.set_ylabel("x'")
        ax.set_title('Limit Cycle'); ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)

def sim_double_sim():
    col1, col2 = st.columns(2)
    with col1:
        th1 = st.slider("θ₁₀ (rad)", 0.0, np.pi, np.pi/2, 0.1, key="u_dt1")
    with col2:
        ts = st.slider("Time (s)", 5, 40, 20, 5, key="u_dts")
    _, _, _, _, _, _, _, x2a, y2a = sim_double(th1, 0.0, 0, 0, ts)
    _, _, _, _, _, _, _, x2b, y2b = sim_double(th1+0.001, 0.0, 0, 0, ts)
    diff = np.sqrt((x2a-x2b)**2 + (y2a-y2b)**2)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(x2a, y2a, 'b-', lw=0.4, alpha=0.7, label='θ₁₀')
    axes[0].plot(x2b, y2b, 'r-', lw=0.4, alpha=0.7, label='+0.001')
    axes[0].set_xlabel('x'); axes[0].set_ylabel('y')
    axes[0].set_title('Two Trajectories'); axes[0].legend(fontsize=8); axes[0].axis('equal'); axes[0].grid(alpha=0.3)
    axes[1].semilogy(np.linspace(0, ts, len(diff)), diff+1e-16, 'k-', lw=0.8)
    axes[1].set_xlabel('Time (s)'); axes[1].set_ylabel('Distance')
    axes[1].set_title('Exponential Divergence'); axes[1].grid(alpha=0.3)
    st.pyplot(fig)
    st.info(f"Final separation: {diff[-1]:.4f} (from 0.001) — Butterfly effect!")

def sim_numerics():
    """Euler vs RK4 comparison."""
    st.markdown("**Compare Euler vs Runge-Kutta 4 accuracy**")
    col1, col2 = st.columns(2)
    with col1:
        method = st.selectbox("Method", ["RK4", "Euler", "Both"], key="u_nm")
    with col2:
        h = st.selectbox("Step size h", [0.1, 0.05, 0.02, 0.01], index=2, key="u_nh")

    def euler(y, h):
        x, v = y; return np.array([x + h*v, v - h*x])
    def rk4(y, h):
        def f(s): return np.array([s[1], -s[0]])
        k1 = f(y); k2 = f(y + 0.5*h*k1); k3 = f(y + 0.5*h*k2); k4 = f(y + h*k3)
        return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

    steps = int(20/h)
    t = np.linspace(0, 20, steps)
    x_exact = np.cos(t)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, x_exact, 'k-', lw=1.5, alpha=0.5, label='Exact')

    if method in ['Euler', 'Both']:
        y = np.array([1.0, 0.0]); xe = [y[0]]
        for i in range(1, steps): y = euler(y, h); xe.append(y[0])
        ax.plot(t, xe, 'r-', lw=0.8, label=f'Euler')
    if method in ['RK4', 'Both']:
        y = np.array([1.0, 0.0]); xr = [y[0]]
        for i in range(1, steps): y = rk4(y, h); xr.append(y[0])
        ax.plot(t, xr, 'b--', lw=0.8, label=f'RK4')

    ax.set_xlabel('Time'); ax.set_ylabel('x')
    ax.set_title('Euler vs RK4'); ax.legend(); ax.grid(alpha=0.3)
    st.pyplot(fig)

def sim_phase_space():
    """Phase space demo."""
    col1, col2 = st.columns(2)
    with col1:
        th0 = st.slider("θ₀ (°)", 10, 179, 45, 1, key="u_pth2")
    with col2:
        w0 = st.slider("Initial velocity", 0.0, 5.0, 0.0, 0.1, key="u_pw2")
    th0r = np.radians(th0)
    t, th, om = sim_pend(th0r, w0, 20.0)
    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, th, 'b-', lw=0.7); ax.axhline(y=0, color='gray', ls='--', alpha=0.3)
        ax.set_xlabel('Time (s)'); ax.set_ylabel('θ (rad)')
        ax.set_title('Time Series'); ax.grid(alpha=0.3)
        st.pyplot(fig)
    with c2:
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(th, om, 'r-', lw=0.5)
        ax.scatter(th[0], om[0], c='g', s=50, zorder=5, label='Start')
        ax.scatter(th[-1], om[-1], c='r', s=50, zorder=5, label='End')
        ax.set_xlabel('θ'); ax.set_ylabel('dθ/dt')
        ax.set_title('Phase Portrait'); ax.legend(); ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)

SIM_MAP = {
    'pendulum': sim_pendulum,
    'logistic': sim_logistic,
    'lorenz': sim_lorenz_sim,
    'duffing': sim_duffing_sim,
    'vdp': sim_vdp_sim,
    'double': sim_double_sim,
    'numerics': sim_numerics,
    'phase_space': sim_phase_space,
}

# ============================================================
# PAGE RENDERERS
# ============================================================

def render_course():
    st.title("🚀 Nonlinear Dynamics — Interactive Course")
    st.markdown("**Explore nonlinear phenomena through interactive simulations**")
    st.markdown("---")

    # Show current chapter info
    ch = current_ch
    st.markdown(f"## {ch['icon']} {ch['title']}")
    subtitle = ch.get('subtitle', '')
    if subtitle:
        st.markdown(f"**{subtitle}**")
    st.markdown("---")

    if current_section:
        # Show section content
        sec = current_section
        st.markdown(sec.get('content', ''))
        st.markdown("---")
        sim_id = sec.get('simulation')
        if sim_id and sim_id in SIM_MAP:
            SIM_MAP[sim_id]()
    else:
        # Show chapter overview
        content = ch.get('content', '')
        if content:
            st.markdown(content)
        sim_id = ch.get('simulation')
        if sim_id and sim_id in SIM_MAP:
            st.markdown("---")
            SIM_MAP[sim_id]()

def render_archive():
    lang = st.session_state.get('archive_lang', 'de')
    title = "📗 Ordnung und Chaos bei nichtlinearen Schwingungen"
    subtitle = "*Original German edition (1995) — Deutsch Verlag, Frankfurt am Main*"
    source_file = 'ocr/book_transcribed.md'
    page_label = "Seiten"

    if lang == 'en':
        title = "📗 Order and Chaos in Nonlinear Oscillations"
        subtitle = "*English translation — based on the original German edition (1995)*"
        source_file = 'ocr/book_transcribed_en.md'
        page_label = "Pages"

    st.title(title)
    st.markdown(subtitle)
    st.markdown("---")

    # Try to load the selected language file
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            book_text = f.read()
    except FileNotFoundError:
        if lang == 'en':
            st.info("🌍 English translation is being prepared. Please check back later, or read the original German version.")
            with open('ocr/book_transcribed.md', 'r', encoding='utf-8') as f:
                book_text = f.read()
        else:
            st.error("Book file not found.")
            return

    st.markdown(f"**{arch_sel}** ({page_label} {arch_pages[0]}–{arch_pages[-1]})")

    # Toggle to show original scanned pages
    show_scans = st.checkbox("📄 Show original scanned pages with figures", value=False, key="show_scans")

    # Get content
    content = get_page_range(book_text, arch_pages[0], arch_pages[-1])

    if show_scans:
        # Show scanned images and text in tabs
        tab_text, tab_scans = st.tabs(["📝 Transcribed Text", "📄 Original Scans"])

        with tab_text:
            render_book_content(content)

        with tab_scans:
            st.markdown(f"**Original scanned pages {arch_pages[0]}–{arch_pages[-1]}**")
            for p in arch_pages:
                scan_file = f"scans/pages/page_{p:03d}.png"
                import os
                if os.path.exists(scan_file):
                    st.image(scan_file, caption=f"Original page {p}", use_container_width=True)
                else:
                    st.info(f"Scan for page {p} not available")
    else:
        render_book_content(content)

def render_lab():
    st.title("🔬 Simulation Lab")
    st.markdown("**Full simulation playground — all systems, all controls, no distractions**")
    st.markdown("---")

    lab_systems = [
        ("Pendulum", 'pendulum'),
        ("Logistic Map", 'logistic'),
        ("Lorenz Attractor", 'lorenz'),
        ("Duffing Oscillator", 'duffing'),
        ("Van der Pol", 'vdp'),
        ("Double Pendulum", 'double'),
    ]

    # Sidebar system selector
    st.sidebar.markdown("### 🎛️ Lab Controls")
    lab_sel = st.sidebar.selectbox("System", [s[0] for s in lab_systems], key="lab_sys")
    sim_id = [s[1] for s in lab_systems if s[0] == lab_sel][0]
    st.sidebar.markdown("---")

    # Full parameter controls in sidebar
    if sim_id == 'pendulum':
        st.sidebar.markdown("**Parameters**")
        theta0 = st.sidebar.slider("θ₀ (°)", 5, 179, 45, 1)
        gamma = st.sidebar.slider("Damping γ", 0.0, 1.0, 0.0, 0.01)
        forcing = st.sidebar.slider("Forcing F", 0.0, 1.0, 0.0, 0.01)
        omega_f = st.sidebar.slider("ω (forcing)", 0.5, 2.0, 1.2, 0.01)
        t_span = st.sidebar.slider("Time (s)", 10, 60, 20, 5)
        th0_rad = np.radians(theta0)
        t, th, om = sim_pend(th0_rad, 0.0, t_span, gamma=gamma, F=forcing, omega=omega_f)
        c1, c2 = st.columns(2)
        with c1:
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.plot(t, th, 'b-', lw=0.7)
            ax.set_xlabel('Time (s)'); ax.set_ylabel('θ (rad)')
            ax.set_title(f'Pendulum — θ₀={theta0}°, γ={gamma}'); ax.grid(alpha=0.3)
            st.pyplot(fig)
        with c2:
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(th, om, 'r-', lw=0.5)
            ax.set_xlabel('θ'); ax.set_ylabel('dθ/dt')
            ax.set_title('Phase Portrait'); ax.grid(alpha=0.3); ax.axis('equal')
            st.pyplot(fig)

    elif sim_id == 'logistic':
        r = st.sidebar.slider("r", 2.5, 4.0, 3.8, 0.001)
        x0 = st.sidebar.slider("x₀", 0.01, 0.99, 0.5, 0.01)
        n_iter = st.sidebar.slider("Iterations", 50, 500, 100, 10)
        show_bif = st.sidebar.checkbox("Show bifurcation", True)

        xs = iterate(x0, r, n_iter)
        lyap = lyap_log(r)

        c1, c2 = st.columns(2)
        with c1:
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.plot(range(len(xs)), xs, 'b-', lw=0.6)
            ax.set_xlabel('n'); ax.set_ylabel('x_n')
            ax.set_title(f'Logistic Map — r={r:.4f}')
            ax.set_ylim(-0.05, 1.05); ax.grid(alpha=0.3)
            st.pyplot(fig)
            st.metric("Lyapunov Exponent", f"{lyap:.4f}",
                      delta="CHAOS" if lyap > 0 else "Periodic", delta_color="inverse")
        with c2:
            with st.spinner("Computing..."):
                rv = np.linspace(2.5, 4.0, 400)
                rp, xp = bifurcation_points(rv, n_transient=500, n_samples=100)
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.scatter(rp, xp, s=0.1, c='k', alpha=0.4)
            ax.axvline(x=r, color='r', ls='--', lw=1)
            ax.set_xlabel('r'); ax.set_ylabel('x')
            ax.set_title('Bifurcation Diagram')
            ax.set_xlim(2.5, 4.0); ax.set_ylim(-0.05, 1.05); ax.grid(alpha=0.3)
            st.pyplot(fig)

    elif sim_id == 'lorenz':
        rho = st.sidebar.slider("ρ", 0.0, 50.0, 28.0, 0.5)
        sigma = st.sidebar.slider("σ", 5.0, 20.0, 10.0, 0.5)
        t_s = st.sidebar.slider("Time", 10, 80, 40, 5)
        view_3d = st.sidebar.checkbox("3D view", True)
        view_ts = st.sidebar.checkbox("Time series", True)

        t, x, y, z = sim_lorenz(1.0, 1.0, 1.0, t_s, sigma=sigma, rho=rho)

        if view_3d:
            fig = plt.figure(figsize=(9, 7))
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(x, y, z, 'b-', lw=0.4, alpha=0.8)
            ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
            ax.set_title(f'Lorenz — σ={sigma}, ρ={rho}')
            st.pyplot(fig)
        if view_ts:
            fig, axes = plt.subplots(3, 1, figsize=(10, 5), sharex=True)
            axes[0].plot(t, x, 'b-', lw=0.5); axes[0].set_ylabel('x'); axes[0].grid(alpha=0.3)
            axes[1].plot(t, y, 'g-', lw=0.5); axes[1].set_ylabel('y'); axes[1].grid(alpha=0.3)
            axes[2].plot(t, z, 'r-', lw=0.5); axes[2].set_ylabel('z')
            axes[2].set_xlabel('Time'); axes[2].grid(alpha=0.3)
            st.pyplot(fig)

    elif sim_id == 'duffing':
        gamma_f = st.sidebar.slider("Forcing γ", 0.0, 0.8, 0.3, 0.01)
        delta = st.sidebar.slider("Damping δ", 0.0, 0.5, 0.2, 0.01)
        omega_f = st.sidebar.slider("ω (forcing)", 0.5, 2.0, 1.2, 0.01)
        t_s = st.sidebar.slider("Time", 20, 200, 100, 10)
        show_potential = st.sidebar.checkbox("Show potential", True)

        t, x, v = sim_duff(0.5, 0.0, t_s, delta=delta, gamma=gamma_f, omega=omega_f)

        c1, c2 = st.columns(2)
        with c1:
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.plot(x[-3000:], v[-3000:], 'r-', lw=0.3)
            ax.set_xlabel('x'); ax.set_ylabel("x'")
            ax.set_title('Phase Portrait (steady state)'); ax.grid(alpha=0.3)
            st.pyplot(fig)
        with c2:
            if show_potential:
                xp = np.linspace(-2.5, 2.5, 200)
                V = potential(xp)
                fig, ax = plt.subplots(figsize=(7, 4))
                ax.plot(xp, V, 'b-', lw=2)
                ax.set_xlabel('x'); ax.set_ylabel('V(x)')
                ax.set_title('Potential'); ax.grid(alpha=0.3)
                st.pyplot(fig)

    elif sim_id == 'vdp':
        mu = st.sidebar.slider("μ", 0.0, 10.0, 1.0, 0.1)
        F = st.sidebar.slider("Forcing F", 0.0, 1.0, 0.0, 0.01)
        t_s = st.sidebar.slider("Time", 20, 150, 80, 5)

        t, x, v = sim_vdp(0.1, 0.1, t_s, mu=mu, F=F)

        c1, c2 = st.columns(2)
        with c1:
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.plot(t, x, 'b-', lw=0.6)
            ax.set_xlabel('Time'); ax.set_ylabel('x')
            ax.set_title(f'Van der Pol — μ={mu:.1f}'); ax.grid(alpha=0.3)
            st.pyplot(fig)
        with c2:
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(x, v, 'r-', lw=0.4)
            ax.set_xlabel('x'); ax.set_ylabel("x'")
            ax.set_title('Limit Cycle'); ax.grid(alpha=0.3); ax.axis('equal')
            st.pyplot(fig)

    elif sim_id == 'double':
        th1_0 = st.sidebar.slider("θ₁₀ (rad)", 0.0, np.pi, np.pi/2, 0.1)
        th2_0 = st.sidebar.slider("θ₂₀ (rad)", 0.0, np.pi, 0.0, 0.1)
        t_s = st.sidebar.slider("Time (s)", 5, 60, 30, 5)
        show_traj = st.sidebar.checkbox("Both trajectories", True)

        t, th1, th2, w1, w2, x1, y1, x2, y2 = sim_double(th1_0, th2_0, 0, 0, t_s)
        _, _, _, _, _, _, _, x2b, y2b = sim_double(th1_0+0.001, th2_0, 0, 0, t_s)

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        axes[0].plot(x2, y2, 'b-', lw=0.3, alpha=0.7, label='Primary')
        if show_traj:
            axes[0].plot(x2b, y2b, 'r-', lw=0.3, alpha=0.5, label='+0.001')
        axes[0].scatter([0], [0], color='k', s=30, zorder=5)
        axes[0].set_xlabel('x'); axes[0].set_ylabel('y')
        axes[0].set_title('Trajectory'); axes[0].legend(fontsize=8); axes[0].axis('equal'); axes[0].grid(alpha=0.3)

        diff = np.sqrt((x2-x2b)**2 + (y2-y2b)**2)
        axes[1].semilogy(np.linspace(0, t_s, len(diff)), diff+1e-16, 'k-', lw=0.8)
        axes[1].set_xlabel('Time (s)'); axes[1].set_ylabel('Distance')
        axes[1].set_title('Exponential Divergence'); axes[1].grid(alpha=0.3)
        st.pyplot(fig)

    # Notes
    st.markdown("---")
    st.subheader("📝 Lab Notes")
    st.text_area("Notes", height=100, placeholder="Record your observations here...", key="lab_notes")

def render_about():
    st.title("📖 About")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ## Dr. Bounthong VONGXAYA

        **PhD in Physics** (Magna Cum Laude), TU Dresden, Germany  
        **Master of Science in Physics and Mathematics** (Mention of Excellence), Belarusian State University

        ### Background
        - 40+ years in IT architecture, software development, and education
        - Former Director of IT Center, National University of Laos
        - IT Consultant & Senior Project Manager, APIS Co. Ltd.
        - Author of *"Ordnung und Chaos bei nichtlinearen Schwingungen"* (1995)

        ### Contact
        - Email: bounthongv@gmail.com
        - GitHub: [github.com/bounthongv](https://github.com/bounthongv)
        - LinkedIn: [linkedin.com/in/bounthong-vongxaya](https://linkedin.com/in/bounthong-vongxaya)

        ### Languages
        Lao (native) | English, Russian, German (professional) | Thai (fluent)

        ### Tech Stack
        Python, NumPy, Matplotlib, Streamlit, Gemini AI
        """)

    with col2:
        st.markdown("#### Quick Links")
        st.markdown("- [GitHub Repository](https://github.com/bounthongv/nonlinear-dynamics-lab)")
        st.markdown("- [WorldCat Book Entry](https://search.worldcat.org/title/75499739)")
        st.markdown("---")
        st.markdown("#### Course Syllabus")
        st.markdown("[Download Syllabus](https://github.com/bounthongv/nonlinear-dynamics-lab/blob/main/docs/course_syllabus.md)")

# ============================================================
# DISPATCH
# ============================================================

if current_page == 'course':
    render_course()
elif current_page == 'archive':
    render_archive()
elif current_page == 'lab':
    render_lab()
elif current_page == 'about':
    render_about()

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown("""
**Nonlinear Dynamics Laboratory** — Dr. Bounthong VONGXAYA  
Based on *Ordnung und Chaos bei nichtlinearen Schwingungen* (1995)
""")
