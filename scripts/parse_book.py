#!/usr/bin/env python3
"""
parse_book.py — Parse the transcribed book markdown into chapter structure.

Outputs a Python module with chapter data that can be imported by the book app.
"""

import re

def parse_book(md_path):
    """Parse the transcribed book into structured chapters."""
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split by page markers
    pages = re.split(r'(## Page \d+)', text)
    # First element is header, then alternating marker/content
    page_data = []
    for i in range(1, len(pages), 2):
        marker = pages[i]
        content = pages[i+1] if i+1 < len(pages) else ''
        page_num = int(re.search(r'\d+', marker).group())
        page_data.append((page_num, marker + '\n' + content.strip()))

    # Define chapter boundaries based on known structure
    chapters = [
        {
            'id': 'foreword',
            'title': 'Vorwort',
            'pages': [1],
            'simulation': None,
            'exercises': []
        },
        {
            'id': 'ch1',
            'title': 'Kapitel I: Zur Physik der nichtlinearen Schwingungen',
            'subsections': [
                {'id': 'ch1_intro', 'title': 'Einführung', 'pages': [2]},
                {'id': 'ch1_pendulum', 'title': '1.1 Getriebenes mathematisches Pendel', 'pages': [2, 3, 4, 5]},
                {'id': 'ch1_duffing', 'title': '1.2 Duffing-Oszillator', 'pages': [3, 4]},
                {'id': 'ch1_pohl', 'title': '1.3 Pohlsches Rad', 'pages': [4]},
                {'id': 'ch1_parametric', 'title': '1.4 Parametrisch getriebenes Pendel', 'pages': [5]},
                {'id': 'ch1_phase', 'title': '2.1 Phasenraum', 'pages': [5, 6]},
                {'id': 'ch1_period', 'title': '2.2 Amplitudenabhängigkeit der Periode', 'pages': [7, 8, 9]},
                {'id': 'ch1_dissipative', 'title': '2.3 Dissipatives System. Attraktor', 'pages': [10, 11]},
                {'id': 'ch1_limitcycle', 'title': '2.4 Grenzzyklus. Sprungphänomen', 'pages': [11, 12, 13, 14]},
                {'id': 'ch1_poincare', 'title': '2.5 Stroboskopische Abbildung. Seltsamer Attraktor', 'pages': [14, 15]},
            ],
            'pages': list(range(2, 16)),
            'simulation': 'pendulum',
            'exercises': []
        },
        {
            'id': 'ch2',
            'title': 'Kapitel II: Aufgaben und Experimente',
            'subsections': [
                {'id': 'ch2_intro', 'title': 'Einführung', 'pages': [16]},
                {'id': 'ch2_aufgabe1', 'title': 'Aufgabe 1: Freies ungedämpftes Pendel', 'pages': [16]},
                {'id': 'ch2_aufgabe2', 'title': 'Aufgabe 2: Phasenportraits und Separatrix', 'pages': [16]},
                {'id': 'ch2_aufgabe3', 'title': 'Aufgabe 3: Fixpunkt-Attraktor', 'pages': [16]},
                {'id': 'ch2_aufgabe4', 'title': 'Aufgabe 4: Resonanzkurve und Sprungphänomen', 'pages': [17]},
                {'id': 'ch2_aufgabe5', 'title': 'Aufgabe 5: Feigenbaum-Kaskade', 'pages': [17]},
                {'id': 'ch2_aufgabe6', 'title': 'Aufgabe 6: Lyapunov-Exponent', 'pages': [17]},
            ],
            'pages': [16, 17],
            'simulation': 'all',
            'exercises': [1, 2, 3, 4, 5, 6]
        },
        {
            'id': 'ch3',
            'title': 'Kapitel III: Theoretische Grundlagen',
            'subsections': [
                {'id': 'ch3_linear', 'title': 'i. Lineare vs. Nichtlineare DGLs', 'pages': [18]},
                {'id': 'ch3_autonomous', 'title': 'ii. Autonomisierung', 'pages': [18]},
                {'id': 'ch3_volume', 'title': 'iii. Phasenraumvolumen', 'pages': [18]},
                {'id': 'ch3_rk4', 'title': 'iv. Runge-Kutta Verfahren', 'pages': [18]},
                {'id': 'ch3_coulomb', 'title': 'v. Coulombsche Reibung', 'pages': [18]},
            ],
            'pages': list(range(18, 30)),
            'simulation': None,
            'exercises': []
        },
        {
            'id': 'ch4',
            'title': 'Kapitel IV: Benutzerdokumentation',
            'pages': list(range(30, 64)),
            'simulation': None,
            'exercises': []
        }
    ]

    # Build a page lookup
    page_lookup = {num: content for num, content in page_data}

    # Verify coverage
    covered = set()
    for ch in chapters:
        for p in ch.get('pages', []):
            covered.add(p)
    all_pages = set(p for p, _ in page_data)
    missing = all_pages - covered

    return {
        'chapters': chapters,
        'page_lookup': page_lookup,
        'total_pages': len(page_data),
        'missing_pages': sorted(missing)
    }


if __name__ == '__main__':
    result = parse_book('ocr/book_transcribed.md')
    print(f'Parsed {result["total_pages"]} pages into {len(result["chapters"])} chapters')
    if result['missing_pages']:
        print(f'Missing pages: {result["missing_pages"]}')
    else:
        print('All pages covered!')
    for ch in result['chapters']:
        subs = ch.get('subsections', [])
        sim = ch.get('simulation', 'none')
        print(f'  {ch["title"]}: {len(ch["pages"])} pages, {len(subs)} sections, sim={sim}')
