#!/usr/bin/env python3
"""
transcribe_with_gemini.py — Transcribe scanned book pages using Gemini Vision API

Processes all 54 pages of the Fraktur-font book using Google's Gemini API,
which handles Fraktur text far better than traditional OCR.

Usage:
    python scripts/transcribe_with_gemini.py --api-key YOUR_KEY
    python scripts/transcribe_with_gemini.py --api-key YOUR_KEY --pages 1-10

Requires:
    pip install google-genai
    Gemini API key (get from https://aistudio.google.com/apikey)
"""

import os
import sys
import argparse
import time
import json
from pathlib import Path
from google import genai
from google.genai import types


# Gemini works best with system instruction + image
SYSTEM_INSTRUCTION = """
You are transcribing a scanned German book on nonlinear dynamics from 1995.
The book uses Fraktur (blackletter) font which is difficult for traditional OCR.

Your task: Transcribe every page exactly as written, in German.
Preserve ALL content: text, equations, figure captions, page numbers, footnotes.

RULES:
1. Transcribe ALL text exactly — do NOT summarize or skip anything
2. Mathematical equations MUST be in LaTeX format ($$...$$ or $...$)
3. Preserve the original German spelling and formatting
4. If a word is illegible, mark it as [illegible]
5. Include page numbers as ## Page [N]
6. Separate sections with horizontal lines ---
7. Output ONLY the markdown transcription, no commentary
"""


def load_page_image(page_num, pages_dir='scans/pages'):
    """Load a page image file."""
    path = os.path.join(pages_dir, f'page_{page_num:03d}.png')
    if not os.path.exists(path):
        raise FileNotFoundError(f'Page not found: {path}')
    return path


def transcribe_page(client, page_num, model='gemini-2.5-flash'):
    """Transcribe a single page using Gemini Vision."""
    image_path = load_page_image(page_num)

    # Read the image file
    with open(image_path, 'rb') as f:
        image_bytes = f.read()

    prompt = f"Transcribe page {page_num} of the German book 'Ordnung und Chaos bei nichtlinearen Schwingungen'. Output as markdown with ## Page {page_num} header and LaTeX for equations."

    response = client.models.generate_content(
        model=model,
        contents=[
            types.Content(
                role='user',
                parts=[
                    types.Part.from_bytes(data=image_bytes, mime_type='image/png'),
                    types.Part(text=prompt),
                ]
            )
        ],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.1,
            max_output_tokens=8192,
        )
    )

    text = response.text
    return text


def transcribe_batch(api_key, page_range, model='gemini-2.5-flash',
                     output_dir='ocr', delay=2):
    """
    Transcribe a range of pages and save to markdown.

    Args:
        api_key: Gemini API key
        page_range: tuple (start, end) inclusive
        model: Gemini model name
        output_dir: output directory
        delay: seconds between API calls (avoid rate limits)
    """
    client = genai.Client(api_key=api_key)
    start, end = page_range

    os.makedirs(output_dir, exist_ok=True)

    all_text = []
    total = end - start + 1

    for i, page_num in enumerate(range(start, end + 1)):
        print(f'[{i+1}/{total}] Transcribing page {page_num}...', end=' ', flush=True)

        try:
            text = transcribe_page(client, page_num, model)

            # Save individual page
            page_file = os.path.join(output_dir, f'page_{page_num:03d}.md')
            with open(page_file, 'w', encoding='utf-8') as f:
                f.write(text)

            all_text.append((page_num, text))
            print(f'✓ {len(text)} chars')

        except Exception as e:
            print(f'✗ ERROR: {e}')
            all_text.append((page_num, f'*[Transcription failed for page {page_num}]*'))

        # Delay between calls (avoid rate limits)
        if i < total - 1:
            time.sleep(delay)

    # Assemble full markdown
    print(f'\nAssembling full transcription...')
    md_path = os.path.join(output_dir, 'book_transcribed.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('# Ordnung und Chaos bei nichtlinearen Schwingungen\n')
        f.write('*Transcribed with Gemini Vision from scanned book*\n\n')

        for page_num, text in all_text:
            f.write(text.strip())
            f.write('\n\n---\n\n')

    print(f'\nDone! Full transcription saved to: {md_path}')
    print(f'Total pages transcribed: {len(all_text)}')


def main():
    parser = argparse.ArgumentParser(
        description='Transcribe book pages using Gemini Vision API')
    parser.add_argument('--api-key', required=True,
                        help='Gemini API key')
    parser.add_argument('--pages', default='1-54',
                        help='Page range to transcribe (e.g. "1-10" or "1-54")')
    parser.add_argument('--model', default='gemini-2.5-flash',
                        help='Gemini model (gemini-2.5-flash or gemini-2.5-pro)')
    parser.add_argument('--output', default='ocr',
                        help='Output directory')
    parser.add_argument('--delay', type=int, default=2,
                        help='Delay between API calls in seconds')

    args = parser.parse_args()

    # Parse page range
    try:
        parts = args.pages.split('-')
        start, end = int(parts[0]), int(parts[1])
    except:
        print('Error: pages must be in format "start-end" (e.g. 1-54)')
        sys.exit(1)

    if start < 1 or end > 54 or start > end:
        print('Error: page range must be between 1 and 54')
        sys.exit(1)

    transcribe_batch(args.api_key, (start, end), args.model, args.output, args.delay)


if __name__ == '__main__':
    main()
