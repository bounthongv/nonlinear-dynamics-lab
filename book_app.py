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


def render_book_content(markdown_text):
    """
    Render book content with proper LaTeX handling.

    Splits text around $$...$$ blocks and renders equations with
    st.latex() for proper display, while text goes through st.markdown().
    """
    import re

    # Split by display math $$...$$
    parts = re.split(r'(\$\$.*?\$\$)', markdown_text, flags=re.DOTALL)

    for part in parts:
        if part.startswith('$$') and part.endswith('$$'):
            # Extract the LaTeX inside the delimiters
            latex_content = part[2:-2].strip()
            # Remove any trailing \n and --- separators
            latex_content = latex_content.rstrip('\n')
            if latex_content:
                st.latex(latex_content)
        elif part.strip():
            # Check for inline math and render with markdown
            # Streamlit handles $...$ inline math in markdown
            st.markdown(part, unsafe_allow_html=True)

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
# CHAPTER STRUCTURE — With Hierarchical Table of Contents
# ============================================================

CHAPTERS = [
    {
        'id': 'vorwort',
        'icon': '📖',
        'title': 'Vorwort',
        'pages': [1],
        'toc': [
            ('📖 Vorwort', [1], None, False),
        ],
        'sections': [
            ('Vorwort', [1], None, None),
        ],
    },
    {
        'id': 'ch1',
        'icon': '🔬',
        'title': 'Kapitel I: Zur Physik der nichtlinearen Schwingungen',
        'pages': list(range(2, 16)),
        'toc': [
            ('🔬 Kapitel I', None, None, True),
            ('    1. Behandelte nichtlineare Systeme', None, None, True),
            ('        1.1 Getriebenes mathematisches Pendel', [2, 3], 'pendulum', False),
            ('        1.2 Sinusoidal erregter Federschwinger (Duffing)', [3, 4], 'duffing', False),
            ('        1.3 Pohlsches Rad', [4], 'pendulum', False),
            ('        1.4 Parametrisch getriebenes Pendel', [5], 'pendulum', False),
            ('    2. Nichtlineare Phänomene', None, None, True),
            ('        2.1 Bewegungsgleichung, Phasenraum', [5, 6], 'pendulum', False),
            ('        2.2 Amplitudenabhängigkeit der Periode', [7, 8, 9], 'pendulum', False),
            ('        2.3 Dissipatives System. Attraktor', [10, 11], None, False),
            ('        2.4 Grenzzyklus. Sprungphänomen', [11, 12, 13, 14], 'vdp', False),
            ('        2.5 Stroboskopische Abbildung', [14, 15], 'lorenz', False),
        ],
        'sections': [
            ('Einführung & Pendel', [2, 3, 4], 'pendulum', embedded_pendulum),
            ('Duffing-Oszillator', [3, 4], 'duffing', embedded_duffing),
            ('Phasenraum', [5, 6], 'pendulum', embedded_pendulum),
            ('Amplitudenabhängigkeit', [7, 8, 9], 'pendulum', embedded_pendulum),
            ('Dissipatives System', [10, 11], None, None),
            ('Grenzzyklus & Bistabilität', [11, 12, 13, 14], 'vdp', embedded_vdp),
            ('Stroboskopische Abbildung', [14, 15], 'lorenz', embedded_lorenz),
        ],
    },
    {
        'id': 'ch2',
        'icon': '✏️',
        'title': 'Kapitel II: Aufgaben und Experimente',
        'pages': [16, 17],
        'toc': [
            ('✏️ Kapitel II', None, None, True),
            ('    Aufgabe 1: Freies ungedämpftes Pendel', [16], None, False),
            ('    Aufgabe 2: Phasenportraits und Separatrix', [16], None, False),
            ('    Aufgabe 3: Fixpunkt-Attraktor', [16], None, False),
            ('    Aufgabe 4: Resonanzkurve & Sprungphänomen', [17], None, False),
            ('    Aufgabe 5: Feigenbaum-Kaskade', [17], None, False),
            ('    Aufgabe 6: Lyapunov-Exponent', [17], None, False),
        ],
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
        'icon': '📐',
        'title': 'Kapitel III: Theoretische Grundlagen',
        'pages': list(range(18, 30)),
        'toc': [
            ('📐 Kapitel III', None, None, True),
            ('    i. Lineare vs. Nichtlineare DGLs', [18], None, False),
            ('    ii. Autonomisierung', [18], None, False),
            ('    iii. Phasenraumvolumen', [18], None, False),
            ('    iv. Runge-Kutta Verfahren', [18], None, False),
            ('    v. Coulombsche Reibung', [18], None, False),
        ],
        'sections': [
            ('Lineare vs. Nichtlineare DGLs', [18], None, None),
            ('Runge-Kutta Verfahren', [18], None, None),
        ],
    },
    {
        'id': 'ch4',
        'icon': '📋',
        'title': 'Kapitel IV: Benutzerdokumentation',
        'pages': list(range(30, 64)),
        'toc': [
            ('📋 Kapitel IV', None, None, True),
            ('    Seiten 30–63', [30, 63], None, False),
        ],
        'sections': [],
    },
]

# Map from TOC entry to section for simulation
def find_section_for_toc(chapter, label):
    """Find which section a TOC label belongs to."""
    for sec_title, sec_pages, sim_name, sim_func in chapter['sections']:
        # Check if the label text contains the section title
        if any(word in label for word in sec_title.split()[:3]):
            return (sec_pages, sim_func)
    return (chapter['pages'], None)

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

# --- Table of Contents ---
st.sidebar.markdown("### 📑 Inhaltsverzeichnis")

# Track current selection in session state
if 'toc_selection' not in st.session_state:
    st.session_state.toc_selection = ('vorwort', '📖 Vorwort')

# Build the ToC tree
toc_key_counter = [0]

for ch in CHAPTERS:
    # Chapter header with expander
    with st.sidebar.expander(f"{ch['icon']} {ch['title']}", expanded=(ch['id'] == st.session_state.toc_selection[0])):
        for label, pages, sim_type, is_heading in ch['toc']:
            if is_heading:
                # Section heading (bold, not clickable)
                st.markdown(f"**{label}**")
            else:
                # Leaf item (clickable)
                page_str = f" (S.{pages[0]})" if pages else ""
                btn_label = f"{label}{page_str}"
                if st.button(btn_label, key=f"toc_{ch['id']}_{toc_key_counter[0]}", use_container_width=True):
                    st.session_state.toc_selection = (ch['id'], label)
                toc_key_counter[0] += 1

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tipp:** Klicke auf ein Kapitel oder Thema im Inhaltsverzeichnis.")

# Determine which chapter and page to show
target_chapter_id, target_label = st.session_state.toc_selection
current_chapter = [ch for ch in CHAPTERS if ch['id'] == target_chapter_id][0]

# Find which pages and simulation to show
selected_pages = current_chapter['pages']
selected_sim_func = None

for label, pages, sim_type, is_heading in current_chapter['toc']:
    if label == target_label and pages:
        selected_pages = pages
        # Find the matching simulation
        for sec_title, sec_pages, sim_name, sim_func in current_chapter['sections']:
            if set(sec_pages).intersection(set(pages)):
                if sim_func:
                    selected_sim_func = sim_func
                break
        break

# ============================================================
# MAIN CONTENT
# ============================================================

st.title(f"{current_chapter['icon']} {current_chapter['title']}")

# Load book text
book_text = load_book()

# Get page content
content = get_page_range(book_text, selected_pages[0], selected_pages[-1])
render_book_content(content)

# --- Interactive simulation section ---
sim_section_name = target_label if target_label else current_chapter.get('title', '')

if selected_sim_func:
    st.markdown("---")
    st.subheader("🔬 Interaktive Simulation")
    st.markdown("_Verändere die Parameter und beobachte das Verhalten des Systems in Echtzeit._")
    selected_sim_func(key_suffix=f"_{target_chapter_id}_{selected_pages[0]}")

elif current_chapter['id'] == 'ch2':
    st.markdown("---")
    st.subheader("✏️ Aufgabe — Interaktive Simulation")

    if 'Aufgabe 1' in target_label:
        st.info("**Aufgabe 1:** Variiere θ₀ von 5° bis 175° bei γ=0, notiere die Periode T für jeden Wert. Vergleiche mit T₀=2π√(L/g).")
        col1, col2 = st.columns([1, 1])
        with col1:
            theta0 = st.slider("θ₀ (°)", 5, 175, 45, 1, key="ex1_th")
            show_T = st.checkbox("Zeige T/T₀", True, key="ex1_T")
        with col2:
            gamma = st.slider("Dämpfung γ", 0.0, 0.5, 0.0, 0.01, key="ex1_g")
        theta0_rad = np.radians(theta0)
        t, th, om = sim_pend(theta0_rad, 0.0, 30.0, gamma=gamma)
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(t, th, 'b-', lw=0.6)
        ax.set_xlabel('Zeit (s)'); ax.set_ylabel('φ (rad)')
        ax.set_title(f'Pendel — θ₀={theta0}°')
        ax.grid(alpha=0.3)
        st.pyplot(fig)
        if show_T:
            T_small = small_angle_period()
            actual_T = period_estimate(theta0_rad)
            if actual_T:
                st.metric("T (gemessen)", f"{actual_T:.3f}s", f"{actual_T/T_small:.3f} × T₀")

    elif 'Aufgabe 2' in target_label:
        st.info("**Aufgabe 2:** Finde die Separatrix! Bei φ₀=0, welche φ̇₀ bringt das Pendel genau bis zur oberen Ruhelage (φ=180°)?")
        col1, col2 = st.columns(2)
        with col1:
            theta0 = st.slider("θ₀ (°)", 0, 30, 0, 1, key="ex2_th")
        with col2:
            omega0 = st.slider("φ̇₀ (Anfangsgeschw.)", 0.0, 10.0, 5.0, 0.1, key="ex2_w")
        theta0_rad = np.radians(theta0)
        t, th, om = sim_pend(theta0_rad, omega0, 20.0)
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        axes[0].plot(t, th, 'b-', lw=0.6)
        axes[0].set_xlabel('Zeit'); axes[0].set_ylabel('φ (rad)')
        axes[0].set_title(f'φ₀={theta0}°, φ̇₀={omega0}'); axes[0].grid(alpha=0.3)
        axes[1].plot(th, om, 'r-', lw=0.4)
        axes[1].set_xlabel('φ'); axes[1].set_ylabel('φ̇')
        axes[1].set_title('Phasenportrait'); axes[1].grid(alpha=0.3); axes[1].axis('equal')
        st.pyplot(fig)
        if np.abs(th[-1]) > 0.1:
            st.success("✅ Das Pendel überschlägt — Rotation!")
        else:
            st.warning("⚠️ Das Pendel schwingt — noch keine Rotation")

    elif 'Aufgabe 3' in target_label:
        st.info("**Aufgabe 3:** Beobachte das Schrumpfen des Phasenraumvolumens.")
        col1, col2, col3 = st.columns(3)
        with col1:
            theta0 = st.slider("θ₀ (°)", 10, 179, 90, 1, key="ex3_th")
        with col2:
            gamma = st.slider("Dämpfung b", 0.01, 0.5, 0.05, 0.01, key="ex3_g")
        with col3:
            t_span = st.slider("Zeit (s)", 5, 60, 30, 5, key="ex3_t")
        theta0_rad = np.radians(theta0)
        t, th, om = sim_pend(theta0_rad, 0.0, t_span, gamma=gamma)
        c1, c2 = st.columns(2)
        with c1:
            fig, ax = plt.subplots(figsize=(7, 3))
            ax.plot(t, th, 'b-', lw=0.6)
            ax.set_xlabel('Zeit'); ax.set_ylabel('φ (rad)')
            ax.set_title(f'Gedämpftes Pendel — b={gamma}'); ax.grid(alpha=0.3)
            st.pyplot(fig)
        with c2:
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(th, om, 'r-', lw=0.4)
            ax.set_xlabel('φ'); ax.set_ylabel('φ̇')
            ax.set_title('Spirale zum Fixpunkt')
            ax.grid(alpha=0.3); ax.axis('equal')
            st.pyplot(fig)

    elif 'Aufgabe 4' in target_label:
        st.info("**Aufgabe 4:** Fahre die Resonanzkurve des Duffing-Oszillators.")
        col1, col2 = st.columns(2)
        with col1:
            gamma_f = st.slider("Anregung A", 0.05, 0.5, 0.3, 0.01, key="ex4_g")
            omega_f = st.slider("Frequenz ω", 0.5, 2.0, 1.2, 0.01, key="ex4_w")
        with col2:
            delta = st.slider("Dämpfung δ", 0.05, 0.5, 0.2, 0.01, key="ex4_d")
        t, x, v = sim_duff(0.5, 0.0, 100.0, delta=delta, gamma=gamma_f, omega=omega_f)
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(t[-2000:], x[-2000:], 'b-', lw=0.5)
        ax.set_xlabel('Zeit'); ax.set_ylabel('x')
        ax.set_title(f'Stationäre Schwingung — ω={omega_f:.2f}')
        ax.grid(alpha=0.3)
        st.pyplot(fig)
        amp = (x[-2000:].max() - x[-2000:].min()) / 2
        st.metric("Amplitude", f"{amp:.3f}")

    elif 'Aufgabe 5' in target_label:
        st.info("**Aufgabe 5:** Erhöhe r von 2.5→4.0 und finde die Bifurkationspunkte.")
        col1, col2 = st.columns(2)
        with col1:
            r = st.slider("r", 2.5, 4.0, 3.5, 0.001, key="ex5_r")
        with col2:
            x0 = st.slider("x₀", 0.01, 0.99, 0.5, 0.01, key="ex5_x")
        xs = iterate(x0, r, 200)
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        axes[0].plot(range(50, len(xs)), xs[50:], 'b-', lw=0.6)
        axes[0].set_xlabel('n'); axes[0].set_ylabel('x_n')
        axes[0].set_title(f'Stationär — r={r:.4f}'); axes[0].grid(alpha=0.3)
        axes[0].set_ylim(0, 1)
        axes[1].scatter(range(len(xs)-1), xs[:-1], s=1, alpha=0.5)
        axes[1].set_xlabel('n'); axes[1].set_ylabel('x_n')
        axes[1].set_title('Alle Iterationen'); axes[1].grid(alpha=0.3)
        st.pyplot(fig)
        lyap = lyap_log(r)
        st.metric("Lyapunov-Exponent", f"{lyap:.4f}", delta="CHAOS" if lyap > 0 else "Ordnung", delta_color="inverse")

    elif 'Aufgabe 6' in target_label:
        st.info("**Aufgabe 6:** Starte zwei Trajektorien mit 0.001° Unterschied und beobachte die exponentielle Divergenz!")
        col1, col2 = st.columns(2)
        with col1:
            r = st.slider("r (für Chaos >3.57)", 3.5, 4.0, 3.9, 0.001, key="ex6_r")
        with col2:
            n = st.slider("Iterationen", 20, 100, 50, 5, key="ex6_n")
        xs1 = iterate(0.5000, r, n)
        xs2 = iterate(0.5001, r, n)
        diff = np.abs(xs1 - xs2)
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        axes[0].plot(range(len(xs1)), xs1, 'b-', lw=0.6, label='x₀=0.5000')
        axes[0].plot(range(len(xs2)), xs2, 'r--', lw=0.6, label='x₀=0.5001')
        axes[0].set_xlabel('n'); axes[0].set_ylabel('x_n')
        axes[0].set_title('Zwei benachbarte Trajektorien'); axes[0].legend(); axes[0].grid(alpha=0.3)
        axes[1].semilogy(range(len(diff)), diff + 1e-16, 'k-', lw=0.8)
        axes[1].set_xlabel('n'); axes[1].set_ylabel('|Δx|')
        axes[1].set_title('Exponentielle Divergenz'); axes[1].grid(alpha=0.3)
        st.pyplot(fig)
        st.metric("Endgültige Abweichung", f"{diff[-1]:.6f}", f"Start: 0.0001")

    # Notes section for all exercises
    st.markdown("---")
    st.subheader("📝 Notizen")
    notes = st.text_area("Deine Beobachtungen:", height=150,
                         placeholder="Was hast du beobachtet? Wie verändert sich das System?")
    if notes:
        st.success("Notizen gespeichert (für diese Sitzung).")

# Lorenz attractor special case for chapters that discuss it
if current_chapter['id'] == 'ch1' and 'Stroboskopische' in target_label:
    st.markdown("---")
    st.subheader("🦋 Lorenz-Attraktor")
    embedded_lorenz(key_suffix=f"lor_{selected_pages[0]}")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown(f"""
**Ordnung und Chaos bei nichtlinearen Schwingungen**  
Dr. Bounthong VONGXAYA  
Seiten {selected_pages[0]}–{selected_pages[-1]}
""")
