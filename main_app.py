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
    parts = re.split(r'(\$\$.*?\$\$)', markdown_text, flags=re.DOTALL)
    for part in parts:
        if part.startswith('$$') and part.endswith('$$'):
            latex = part[2:-2].strip().rstrip('\n')
            if latex:
                st.latex(latex)
        elif part.strip():
            st.markdown(part, unsafe_allow_html=True)

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
    ("📗 Archive (1995)", "archive"),
    ("🔬 Simulation Lab", "lab"),
    ("ℹ️ About", "about"),
]

st.sidebar.title("🌀 Nonlinear Dynamics")
st.sidebar.markdown("*Laboratory*")
st.sidebar.markdown("Dr. Bounthong VONGXAYA")
st.sidebar.markdown("---")

nav_labels = [item[0] for item in NAV_ITEMS]
nav_ids = [item[1] for item in NAV_ITEMS]
selection = st.sidebar.radio("", nav_labels, index=0)
current_page = nav_ids[nav_labels.index(selection)]
st.sidebar.markdown("---")

# ============================================================
# TAB: MODERN COURSE (English, streamlined)
# ============================================================

COURSE_SECTIONS = [
    {
        'id': 'intro',
        'title': 'Introduction',
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
""",
        'sim': None,
    },
    {
        'id': 'pendulum',
        'title': '1. The Nonlinear Pendulum',
        'content': """
For small angles, $$\\sin\\theta \\approx \\theta$$ gives the linear equation.
For **large angles**, the full nonlinear equation:

$$\\ddot{\\theta} + \\gamma \\dot{\\theta} + \\omega_0^2 \\sin\\theta = F \\cos(\\omega t)$$

**Key insight:** The period now depends on amplitude — impossible in linear systems.
""",
        'sim': 'pendulum',
    },
    {
        'id': 'bifurcation',
        'title': '2. Bifurcations & Chaos',
        'content': """
The **logistic map** shows period doubling to chaos:

$$x_{n+1} = r \\cdot x_n \\cdot (1 - x_n)$$

As $$r$$ increases: Fixed point → Period 2 → Period 4 → ... → **Chaos**
""",
        'sim': 'logistic',
    },
    {
        'id': 'lorenz',
        'title': '3. The Lorenz Attractor',
        'content': """
$$\\begin{aligned}
\\dot{x} &= \\sigma(y - x) \\\\
\\dot{y} &= x(\\rho - z) - y \\\\
\\dot{z} &= xy - \\beta z
\\end{aligned}$$

For $$\\rho > 24.7$$, the trajectory forms a **strange attractor** — bounded but never repeating.
""",
        'sim': 'lorenz',
    },
    {
        'id': 'duffing',
        'title': '4. Duffing Oscillator',
        'content': """
$$\\ddot{x} + \\delta \\dot{x} + \\alpha x + \\beta x^3 = \\gamma \\cos(\\omega t)$$

With $$\\alpha < 0, \\beta > 0$$: **double-well potential**, bistability, hysteresis.
""",
        'sim': 'duffing',
    },
    {
        'id': 'vdp',
        'title': '5. Van der Pol Oscillator',
        'content': """
$$\\ddot{x} - \\mu(1 - x^2)\\dot{x} + x = F \\cos(\\omega t)$$

For $$\\mu > 0$$: **self-excited oscillations** and stable limit cycles.
""",
        'sim': 'vdp',
    },
    {
        'id': 'double',
        'title': '6. Double Pendulum',
        'content': """
Two pendulums connected end-to-end. **Deterministic chaos** in action —
a 0.001 rad difference leads to completely different trajectories within seconds.
""",
        'sim': 'double',
    },
]

# ============================================================
# ARCHIVE CHAPTERS (German)
# ============================================================

ARCHIVE_CHAPTERS = [
    {
        'id': 'vorwort',
        'title': '📖 Vorwort',
        'pages': [1],
    },
    {
        'id': 'ch1',
        'title': '🔬 Kapitel I: Nichtlineare Schwingungen',
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
        'title': '✏️ Kapitel II: Aufgaben',
        'pages': [16, 17],
    },
    {
        'id': 'ch3',
        'title': '📐 Kapitel III: Grundlagen',
        'pages': list(range(18, 30)),
    },
    {
        'id': 'ch4',
        'title': '📋 Kapitel IV: Dokumentation',
        'pages': list(range(30, 64)),
    },
]

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

SIM_MAP = {
    'pendulum': sim_pendulum,
    'logistic': sim_logistic,
    'lorenz': sim_lorenz_sim,
    'duffing': sim_duffing_sim,
    'vdp': sim_vdp_sim,
    'double': sim_double_sim,
}

# ============================================================
# PAGE RENDERERS
# ============================================================

def render_course():
    st.title("🚀 Nonlinear Dynamics — Interactive Course")
    st.markdown("**Explore nonlinear phenomena through interactive simulations**")
    st.markdown("---")

    for sec in COURSE_SECTIONS:
        st.subheader(sec['title'])
        st.markdown(sec['content'])
        if sec['sim'] and sec['sim'] in SIM_MAP:
            st.markdown("---")
            SIM_MAP[sec['sim']]()
        st.markdown("---")

def render_archive():
    st.title("📗 Ordnung und Chaos bei nichtlinearen Schwingungen")
    st.markdown("*Original German edition (1995)*")
    st.markdown("---")

    book_text = load_book()
    book_nav = st.sidebar.radio("Chapter", [ch['title'] for ch in ARCHIVE_CHAPTERS], key="arch_nav")
    current_ch = [ch for ch in ARCHIVE_CHAPTERS if ch['title'] == book_nav][0]

    # Section selector for Kapitel I
    pages = current_ch['pages']
    if 'sections' in current_ch:
        sec_labels = ["All pages"] + [s[0] for s in current_ch['sections']]
        sec_sel = st.sidebar.radio("Section", sec_labels, key="arch_sec")
        if sec_sel != "All pages":
            for sec_title, sec_pages in current_ch['sections']:
                if sec_sel == sec_title:
                    pages = sec_pages
                    break

    st.markdown(f"**{book_nav}** (pages {pages[0]}–{pages[-1]})")
    content = get_page_range(book_text, pages[0], pages[-1])
    render_book_content(content)

def render_lab():
    st.title("🔬 Simulation Lab")
    st.markdown("**Free exploration — choose any system and play with parameters**")
    st.markdown("---")

    lab_systems = [
        ("Pendulum", 'pendulum'),
        ("Logistic Map", 'logistic'),
        ("Lorenz Attractor", 'lorenz'),
        ("Duffing Oscillator", 'duffing'),
        ("Van der Pol", 'vdp'),
        ("Double Pendulum", 'double'),
    ]

    selected_lab = st.selectbox("Select System", [s[0] for s in lab_systems], key="lab_sel")
    sim_id = [s[1] for s in lab_systems if s[0] == selected_lab][0]

    st.markdown("---")
    if sim_id in SIM_MAP:
        SIM_MAP[sim_id]()

    st.markdown("---")
    st.subheader("📝 Lab Notes")
    st.text_area("Your observations:", height=120, placeholder="What did you discover?")

def render_about():
    st.title("ℹ️ About")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ## Dr. Bounthong VONGXAYA

        **PhD in Physics** (Magna Cum Laude), TU Dresden, Germany  
        **Master of Science in Physics and Mathematics** (Mention of Excellence), Belarusian State University

        This interactive laboratory is based on my 1995 book  
        *"Ordnung und Chaos bei nichtlinearen Schwingungen"*
        (Deutsch Verlag, Frankfurt am Main).

        ### Academic Background
        - 40+ years in IT architecture, software development, and education
        - Former Director of IT Center, National University of Laos
        - IT Consultant & Senior Project Manager, APIS Co. Ltd.

        ### What This Project Does
        The original 1994 Pascal simulations have been rebuilt in modern Python,
        creating an interactive educational platform for nonlinear dynamics.

        ### Contact
        - Email: bounthongv@gmail.com
        - GitHub: [github.com/bounthongv](https://github.com/bounthongv)
        - LinkedIn: [linkedin.com/in/bounthong-vongxaya](https://linkedin.com/in/bounthong-vongxaya)

        ### Languages
        Lao (native) | English, Russian, German (professional) | Thai (fluent)
        """)

    with col2:
        st.markdown("""
        #### Quick Links
        - [GitHub Repository](https://github.com/bounthongv/nonlinear-dynamics-lab)
        - [WorldCat Book Entry](https://search.worldcat.org/title/75499739)

        #### Tech Stack
        - Python, NumPy, Matplotlib
        - Streamlit (web framework)
        - Gemini AI (OCR transcription)
        - RK4 numerical integration
        """)

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
