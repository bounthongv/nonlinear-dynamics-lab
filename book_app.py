"""
book_app.py — Interactive Nonlinear Dynamics Book

A living, interactive version of the 1995 book:
"Ordnung und Chaos bei nichtlinearen Schwingungen"

Features:
- Full book text with chapter navigation
- Embedded interactive simulations alongside the theory
- Exercises that use the simulations for exploration
- Modern Python implementations replacing the original Pascal code

Author: Dr. Bounthong VONGXAYA
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import re

# Import simulation modules
from python.logistic_map import iterate, bifurcation_points, lyapunov_exponent as lyap_log
from python.nonlinear_pendulum import simulate as sim_pend, small_angle_period, period_estimate
from python.lorenz_attractor import simulate as sim_lorenz
from python.duffing_oscillator import simulate as sim_duff, potential
from python.van_der_pol import simulate as sim_vdp

rcParams['figure.dpi'] = 100

# ============================================================
# LOAD BOOK TEXT
# ============================================================

def load_book():
    with open('ocr/book_transcribed.md', 'r', encoding='utf-8') as f:
        return f.read()

def get_page_text(book_text, page_num):
    """Extract content for a specific page number."""
    pattern = rf'## Page {page_num}\n(.*?)(?=\n## Page \d+|\Z)'
    match = re.search(pattern, book_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return '*[Page not found]*'

def get_page_range(book_text, start, end):
    """Get content for a range of pages."""
    parts = []
    for p in range(start, end + 1):
        content = get_page_text(book_text, p)
        if content and content != '*[Page not found]*':
            parts.append(f'## Page {p}\n{content}')
    return '\n\n'.join(parts)

# ============================================================
# SIMULATION WRAPPERS (for embedding in book pages)
# ============================================================

def embedded_pendulum(key_suffix=""):
    """Embedded interactive pendulum simulation."""
    col1, col2, col3 = st.columns(3)
    with col1:
        theta0 = st.slider("θ₀ (°)", 5, 179, 45, 1, key=f"pend_th0_{key_suffix}")
        theta0_rad = np.radians(theta0)
    with col2:
        gamma = st.slider("Dämpfung γ", 0.0, 1.0, 0.0, 0.01, key=f"pend_g_{key_suffix}")
    with col3:
        show_phase = st.checkbox("Phasenportrait", True, key=f"pend_phase_{key_suffix}")

    t, th, om = sim_pend(theta0_rad, 0.0, 20.0, gamma=gamma)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, th, 'b-', linewidth=0.6)
        ax.set_xlabel('Zeit (s)'); ax.set_ylabel('φ (rad)')
        ax.set_title(f'Pendel — θ₀={theta0}°, γ={gamma}')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        if show_phase:
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(th, om, 'r-', linewidth=0.4)
            ax.set_xlabel('φ'); ax.set_ylabel('dφ/dt')
            ax.set_title('Phasenportrait')
            ax.grid(alpha=0.3); ax.axis('equal')
            st.pyplot(fig)

    T_small = small_angle_period()
    actual_T = period_estimate(theta0_rad)
    if actual_T:
        st.info(f"Theoretische Periode (kleine Winkel): {T_small:.3f}s | "
                f"Aktuelle Periode bei θ₀={theta0}°: {actual_T:.3f}s")


def embedded_logistic(key_suffix=""):
    """Embedded logistic map simulation."""
    col1, col2 = st.columns(2)
    with col1:
        r = st.slider("r", 2.5, 4.0, 3.8, 0.01, key=f"log_r_{key_suffix}")
    with col2:
        x0 = st.slider("x₀", 0.01, 0.99, 0.5, 0.01, key=f"log_x0_{key_suffix}")

    xs = iterate(x0, r, 100)
    lyap = lyap_log(r)

    tab1, tab2 = st.tabs(["Zeitreihe", "Cobweb"])
    with tab1:
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(range(len(xs)), xs, 'b-', linewidth=0.6)
        ax.set_xlabel('n'); ax.set_ylabel('x_n')
        ax.set_title(f'Logistische Abbildung — r={r:.4f}')
        ax.set_ylim(-0.05, 1.05); ax.grid(alpha=0.3)
        st.pyplot(fig)
        st.metric("Lyapunov-Exponent", f"{lyap:.4f}",
                  delta="CHAOS" if lyap > 0 else "Ordnung",
                  delta_color="inverse")

    with tab2:
        fig, ax = plt.subplots(figsize=(5, 5))
        xv = np.linspace(0, 1, 200)
        ax.plot(xv, r*xv*(1-xv), 'b-', lw=1.5)
        ax.plot([0,1], [0,1], 'k--', lw=0.8)
        for i in range(min(len(xs)-1, 30)):
            ax.plot([xs[i], xs[i]], [xs[i], xs[i+1]], 'r-', lw=0.3, alpha=0.6)
            ax.plot([xs[i], xs[i+1]], [xs[i+1], xs[i+1]], 'r-', lw=0.3, alpha=0.6)
        ax.set_xlabel('x_n'); ax.set_ylabel('x_{n+1}')
        ax.set_title(f'Cobweb — r={r:.4f}')
        ax.set_xlim(0,1); ax.set_ylim(0,1); ax.grid(alpha=0.3); ax.set_aspect('equal')
        st.pyplot(fig)


def embedded_lorenz(key_suffix=""):
    """Embedded Lorenz attractor."""
    rho = st.slider("ρ", 0.0, 50.0, 28.0, 0.5, key=f"lor_rho_{key_suffix}")
    t, x, y, z = sim_lorenz(1.0, 1.0, 1.0, 40.0, rho=rho)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, 'b-', linewidth=0.4, alpha=0.8)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title(f'Lorenz-Attraktor — ρ={rho}')
    st.pyplot(fig)


def embedded_duffing(key_suffix=""):
    """Embedded Duffing oscillator."""
    col1, col2 = st.columns(2)
    with col1:
        gamma_f = st.slider("γ (Anregung)", 0.0, 0.8, 0.3, 0.01, key=f"duff_g_{key_suffix}")
    with col2:
        delta = st.slider("δ (Dämpfung)", 0.0, 0.5, 0.2, 0.01, key=f"duff_d_{key_suffix}")

    t, x, v = sim_duff(0.5, 0.0, 100.0, delta=delta, gamma=gamma_f, omega=1.2)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot(x[-3000:], v[-3000:], 'r-', linewidth=0.3)
        ax.set_xlabel('x'); ax.set_ylabel("x'")
        ax.set_title('Phasenportrait (stationär)')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(6, 4))
        xp = np.linspace(-2, 2, 200)
        V = potential(xp)
        ax.plot(xp, V, 'b-', lw=2)
        ax.set_xlabel('x'); ax.set_ylabel('V(x)')
        ax.set_title('Potential')
        ax.grid(alpha=0.3)
        st.pyplot(fig)


def embedded_vdp(key_suffix=""):
    """Embedded Van der Pol oscillator."""
    mu = st.slider("μ", 0.0, 8.0, 1.0, 0.1, key=f"vdp_mu_{key_suffix}")
    t, x, v = sim_vdp(0.1, 0.1, 80.0, mu=mu)

    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t, x, 'b-', lw=0.6)
        ax.set_xlabel('Zeit'); ax.set_ylabel('x')
        ax.set_title(f'Van der Pol — μ={mu:.1f}')
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, v, 'r-', lw=0.4)
        ax.set_xlabel('x'); ax.set_ylabel("x'")
        ax.set_title('Grenzzyklus')
        ax.grid(alpha=0.3); ax.axis('equal')
        st.pyplot(fig)


# ============================================================
# CHAPTER STRUCTURE
# ============================================================

CHAPTERS = [
    {
        'id': 'vorwort',
        'title': 'Vorwort',
        'icon': '📖',
        'pages': [1],
        'sim': None,
        'sim_func': None,
    },
    {
        'id': 'ch1',
        'title': 'Kapitel I: Nichtlineare Schwingungen',
        'icon': '🔬',
        'pages': list(range(2, 16)),
        'sections': [
            ('Einführung & Pendel', [2, 3, 4], 'pendulum', embedded_pendulum),
            ('Duffing-Oszillator', [3, 4], 'duffing', embedded_duffing),
            ('Phasenraum', [5, 6], 'pendulum', embedded_pendulum),
            ('Amplitudenabhängigkeit', [7, 8, 9], 'pendulum', embedded_pendulum),
            ('Dissipatives System', [10, 11], None, None),
            ('Grenzzyklus & Bistabilität', [11, 12, 13, 14], 'vdp', embedded_vdp),
            ('Stroboskopische Abbildung', [14, 15], 'pendulum', embedded_pendulum),
        ],
    },
    {
        'id': 'ch2',
        'title': 'Kapitel II: Aufgaben',
        'icon': '✏️',
        'pages': [16, 17],
        'sections': [
            ('Aufgabe 1: Freies Pendel', [16], 'pendulum', embedded_pendulum),
            ('Aufgabe 2: Separatrix', [16], 'pendulum', embedded_pendulum),
            ('Aufgabe 3: Fixpunkt-Attraktor', [16], 'pendulum', embedded_pendulum),
            ('Aufgabe 4: Duffing-Resonanz', [17], 'duffing', embedded_duffing),
            ('Aufgabe 5: Feigenbaum-Kaskade', [17], 'logistic', embedded_logistic),
            ('Aufgabe 6: Lyapunov-Exponent', [17], 'logistic', embedded_logistic),
        ],
    },
    {
        'id': 'ch3',
        'title': 'Kapitel III: Theoretische Grundlagen',
        'icon': '📐',
        'pages': list(range(18, 30)),
        'sections': [
            ('Lineare vs. Nichtlineare DGLs', [18], None, None),
            ('Runge-Kutta Verfahren', [18], None, None),
        ],
    },
    {
        'id': 'ch4',
        'title': 'Kapitel IV: Dokumentation',
        'icon': '📋',
        'pages': list(range(30, 64)),
        'sections': [],
    },
]

# ============================================================
# MAIN APP
# ============================================================

st.set_page_config(page_title="Nichtlineare Schwingungen — Interaktives Buch",
                   page_icon="🌀", layout="wide")

# Sidebar navigation
st.sidebar.title("📗 Nichtlineare\nSchwingungen")
st.sidebar.markdown("*Ordnung und Chaos bei nichtlinearen Schwingungen (1995/2026)*")
st.sidebar.markdown("Dr. Bounthong VONGXAYA")
st.sidebar.markdown("---")

# Chapter selection
chapter_names = {ch['id']: ch for ch in CHAPTERS}
chapter_id = st.sidebar.radio(
    "Kapitel",
    [ch['id'] for ch in CHAPTERS],
    format_func=lambda x: f"{chapter_names[x]['icon']} {chapter_names[x]['title']}"
)

current_chapter = chapter_names[chapter_id]

# Section selection (if applicable)
selected_section = None
selected_pages = current_chapter['pages']
selected_sim_func = None

if 'sections' in current_chapter and current_chapter['sections']:
    section_options = [(None, f"📄 Alle Seiten ({current_chapter['pages'][0]}–{current_chapter['pages'][-1]})")]
    for sec_title, sec_pages, sim_name, sim_func in current_chapter['sections']:
        label = f"{sec_title} (S. {sec_pages[0]})"
        section_options.append(((sec_title, sec_pages, sim_func), label))

    selected = st.sidebar.radio(
        "Abschnitt",
        section_options,
        format_func=lambda x: x[1],
        key="section_select"
    )
    selected_value = selected[0] if selected else None
    if selected_value:
        selected_section = selected_value[0]
        selected_pages = selected_value[1]
        selected_sim_func = selected_value[2]

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tipp:** Ändere die Parameter in den Simulationen und beobachte die Effekte in Echtzeit!")

# ============================================================
# MAIN CONTENT
# ============================================================

st.title(f"{current_chapter['icon']} {current_chapter['title']}")

# Load book text
book_text = load_book()

# Get page content
content = get_page_range(book_text, selected_pages[0], selected_pages[-1])
st.markdown(content)

# --- Interactive simulation section ---
if selected_sim_func:
    st.markdown("---")
    st.subheader("🔬 Interaktive Simulation")
    st.markdown("_Verändere die Parameter und beobachte das Verhalten des Systems in Echtzeit._")
    selected_sim_func(key_suffix=f"_{chapter_id}_{selected_pages[0]}")

elif current_chapter['id'] == 'ch1' and selected_section and 'Pendel' in selected_section:
    st.markdown("---")
    st.subheader("🔬 Interaktive Simulation")
    embedded_pendulum(key_suffix=f"_{chapter_id}_{selected_pages[0]}")

elif current_chapter['id'] == 'ch2':
    st.markdown("---")
    st.subheader("✏️ Aufgabe — Verwende die Simulation zur Bearbeitung")
    st.markdown("""
    **Anleitung:**  
    Ändere die Parameter im Simulator unten, um das in der Aufgabe beschriebene
    Phänomen zu untersuchen. Beobachte die Änderungen in den Diagrammen.
    """)

    if selected_section and '1' in selected_section:
        embedded_pendulum(key_suffix="ex1")
    elif selected_section and '2' in selected_section:
        embedded_pendulum(key_suffix="ex2")
    elif selected_section and '3' in selected_section:
        embedded_pendulum(key_suffix="ex3")
    elif selected_section and '4' in selected_section:
        embedded_duffing(key_suffix="ex4")
    elif selected_section and '5' in selected_section:
        embedded_logistic(key_suffix="ex5")
    elif selected_section and '6' in selected_section:
        embedded_logistic(key_suffix="ex6")

# Lorenz attractor special case for pages that discuss it
if current_chapter['id'] == 'ch1' and selected_section and 'stroboskopisch' in selected_section:
    st.markdown("---")
    st.subheader("🦋 Lorenz-Attraktor")
    embedded_lorenz(key_suffix=f"lor_{selected_pages[0]}")

# ============================================================
# EXERCISE SECTION (for Kapitel II)
# ============================================================

if current_chapter['id'] == 'ch2':
    st.markdown("---")
    st.subheader("📝 Notizen & Lösungen")
    st.markdown("""
    *Hier kannst du deine Beobachtungen notieren.*
    """)
    notes = st.text_area("Deine Notizen:", height=150,
                         placeholder="Was hast du beobachtet? Wie verändert sich das System bei verschiedenen Parametern?")
    if notes:
        st.success("Notizen gespeichert (für diese Sitzung).")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown(f"""
**Ordnung und Chaos bei nichtlinearen Schwingungen**  
Dr. Bounthong VONGXAYA  
Seiten {selected_pages[0]}–{selected_pages[-1]}
""")
