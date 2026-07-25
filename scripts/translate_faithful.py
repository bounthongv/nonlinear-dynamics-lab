#!/usr/bin/env python3
"""
translate_faithful.py — Faithful English translation of verified German text.

Reads the German markdown (verified correct) and translates each page
faithfully using Gemini API. Preserves ALL structure, equations,
section numbers, and figure markers exactly.
"""

import re
import time
import sys
from google import genai
from google.genai import types

SYSTEM_PROMPT = """You are translating a German physics textbook to English.
You must follow these rules STRICTLY:

1. Translate ONLY the visible text — do NOT add, remove, or restructure ANY content.
2. Preserve ALL LaTeX equations exactly as they are ($$...$$).
3. Preserve ALL section headings, numbering, and hierarchy (#, ##, ###, etc.).
4. Preserve ALL figure markers ![Figure ...] exactly as they are.
5. Preserve ALL page markers (## Page N).
6. Keep the same paragraph structure and ordering.
7. Use correct physics terminology.
8. Do NOT invent new sections, objectives, or content that isn't in the original.
9. If there is a caption in German after a figure, translate the caption but keep the figure marker.

The original text is from "Ordnung und Chaos bei nichtlinearen Schwingungen"
by Dr. Bounthong VONGXAYA. Translate it faithfully."""

def main():
    api_key = input("Enter Gemini API key: ").strip()
    
    with open('ocr/book_transcribed.md', 'r', encoding='utf-8') as f:
        german_text = f.read()
    
    # Split into pages
    pages = re.split(r'(## Page \d+)', german_text)
    
    client = genai.Client(api_key=api_key)
    
    # Process pages one at a time
    translated_pages = []
    translated_pages.append("# Ordnung und Chaos bei nichtlinearen Schwingungen\n*Faithful English Translation*\n\n---\n\n")
    
    for i in range(1, len(pages), 2):
        marker = pages[i]
        content = pages[i+1] if i+1 < len(pages) else ''
        
        if content.strip():
            print(f'Translating {marker}...', end=' ', flush=True)
            
            prompt = f"""Translate this page from the book faithfully.
German text:
{content}

Remember: translate ONLY what is written. Do not add or change anything."""

            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[prompt],
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.0,
                        max_output_tokens=8192,
                    )
                )
                translated = response.text
                
                # Verify structure preserved
                de_sections = len(re.findall(r'^###', content, re.MULTILINE))
                en_sections = len(re.findall(r'^###', translated, re.MULTILINE))
                
                if abs(de_sections - en_sections) > 2:
                    print(f'⚠️ Section count mismatch: DE={de_sections}, EN={en_sections}')
                    # Try again with stricter prompt
                    retry_prompt = f"""STRICT TRANSLATION ONLY — do not change structure.

Original German:
{content}

Translate to English, keeping EXACTLY the same number of headings, paragraphs, and equations."""
                    
                    response2 = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[retry_prompt],
                        config=types.GenerateContentConfig(
                            system_instruction="You are a literal translator. Do not rewrite or restructure.",
                            temperature=0.0,
                            max_output_tokens=8192,
                        )
                    )
                    translated = response2.text
                    print(f'✓ (retry)')
                else:
                    print(f'✓')
                    
            except Exception as e:
                print(f'✗ ERROR: {e}')
                translated = f'*[Translation failed]*\n\n{content}'
            
            translated_pages.append(f'{marker}\n{translated}')
        else:
            translated_pages.append(marker)
            print(f'{marker} (empty)')
        
        time.sleep(2)  # Rate limit
    
    # Write output
    output = '\n\n'.join(translated_pages)
    with open('ocr/book_transcribed_en.md', 'w', encoding='utf-8') as f:
        f.write(output)
    
    # Verify
    de_pages = len(re.findall(r'## Page \d+', german_text))
    en_pages = len(re.findall(r'## Page \d+', output))
    
    print(f'\n{"="*50}')
    print(f'Translation complete!')
    print(f'German pages: {de_pages}')
    print(f'English pages: {en_pages}')
    print(f'English file: ocr/book_transcribed_en.md')
    print(f'Total chars: {len(output)}')

if __name__ == '__main__':
    main()
