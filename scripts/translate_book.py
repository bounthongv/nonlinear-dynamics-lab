#!/usr/bin/env python3
"""
translate_book.py — Translate the German book to English using Gemini API

Reads the transcribed German text and translates each page to English.
Outputs a parallel English version.
"""

import os
import time
import re
from google import genai
from google.genai import types

SYSTEM_PROMPT = """
You are translating a German physics book on nonlinear dynamics to English.
Translate each page accurately, preserving:
- ALL equations in LaTeX format ($$...$$)
- Figure descriptions and captions
- Section numbers and references
- Scientific terminology correctly

Output format: ## Page [N] followed by the English translation.
"""

def translate_text(client, text, model='gemini-2.5-flash'):
    """Translate a chunk of text using Gemini."""
    prompt = f"Translate the following German text to English. Preserve all LaTeX equations and formatting:\n\n{text}"
    response = client.models.generate_content(
        model=model,
        contents=[prompt],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.1,
            max_output_tokens=8192,
        )
    )
    return response.text


def main():
    api_key = input("Enter your Gemini API key: ").strip()
    
    with open('ocr/book_transcribed.md', 'r', encoding='utf-8') as f:
        german_text = f.read()
    
    # Split by pages
    pages = re.split(r'(## Page \d+)', german_text)
    
    client = genai.Client(api_key=api_key)
    translated_pages = []
    
    # Skip header (first element), then alternate marker/content
    header = pages[0]
    translated_pages.append("# Ordnung und Chaos bei nichtlinearen Schwingungen\n*English Translation*\n\n")
    
    for i in range(1, len(pages), 2):
        marker = pages[i]
        content = pages[i+1] if i+1 < len(pages) else ''
        
        print(f'Translating {marker}...', end=' ', flush=True)
        
        if content.strip():
            try:
                translated = translate_text(client, content, model='gemini-2.5-flash')
                translated_pages.append(f'{marker}\n{translated}')
                print(f'✓ {len(translated)} chars')
            except Exception as e:
                print(f'✗ ERROR: {e}')
                translated_pages.append(f'{marker}\n*[Translation failed]*\n{content}')
        else:
            translated_pages.append(f'{marker}')
            print('(empty)')
        
        time.sleep(2)  # Rate limiting
    
    # Write output
    output = '\n\n'.join(translated_pages)
    with open('ocr/book_transcribed_en.md', 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f'\nDone! English translation saved to ocr/book_transcribed_en.md')
    print(f'Total: {len(output)} chars')


if __name__ == '__main__':
    main()
