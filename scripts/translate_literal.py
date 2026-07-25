#!/usr/bin/env python3
"""
translate_literal.py — Ultra-literal page-by-page translation.

Splits German text into pages, sends each page to Gemini with
minimalistic prompt. No context about the book. Just: translate this.
"""

import re, time, sys
from google import genai
from google.genai import types

def main():
    api_key = sys.argv[1] if len(sys.argv) > 1 else input("Enter API key: ")
    
    with open('ocr/book_transcribed.md', 'r', encoding='utf-8') as f:
        german = f.read()
    
    pages = re.split(r'(## Page \d+)', german)
    client = genai.Client(api_key=api_key)
    
    output_parts = []
    output_parts.append("# Ordnung und Chaos bei nichtlinearen Schwingungen\n*English Translation*\n\n---\n\n")
    
    for i in range(1, len(pages), 2):
        marker = pages[i]
        content = pages[i+1] if i+1 < len(pages) else ''
        
        if content.strip():
            print(f'{marker}...', end=' ', flush=True)
            
            try:
                # Minimal prompt - just translate
                resp = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[f'Translate to English. Keep all LaTeX ($$), headings (#), and figure markers (![...]) exactly as-is. Translate only the text between them.\n\n{content}'],
                    config=types.GenerateContentConfig(temperature=0.0, max_output_tokens=8192)
                )
                t = resp.text
                
                # Verify: count heading markers
                de_hash = content.count('###')
                en_hash = t.count('###')
                de_eq = content.count('$$')
                en_eq = t.count('$$')
                
                if abs(de_hash - en_hash) > 3:
                    print(f'⚠️ headings: {de_hash}→{en_hash}')
                    # Retry with even stricter prompt
                    resp2 = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[f'LITERAL TRANSLATION ONLY. Do not add or change anything.\n\n{content}'],
                        config=types.GenerateContentConfig(temperature=0.0, max_output_tokens=8192)
                    )
                    t = resp2.text
                    print('(retried)')
                else:
                    print(f'✓')
                    
            except Exception as e:
                msg = str(e)
                if 'RESOURCE_EXHAUSTED' in msg or '429' in msg:
                    print(f'\n⚠️ QUOTA EXHAUSTED at {marker}')
                    output_parts.append(f'{marker}\n*[Quota exceeded - resume later]*\n\n{content}')
                    remaining = 1
                    for j in range(i+2, len(pages), 2):
                        m = pages[j]
                        c = pages[j+1] if j+1 < len(pages) else ''
                        output_parts.append(f'{m}\n*[Not yet translated]*\n\n{c}')
                        remaining += 1
                    print(f'Remaining pages queued: {remaining}')
                    break
                else:
                    print(f'✗ {str(e)[:50]}')
                    t = f'*[Translation error]*\n\n{content}'
            
            output_parts.append(f'{marker}\n{t}')
        else:
            output_parts.append(marker)
        
        time.sleep(2)
    
    # Write output
    result = '\n\n'.join(output_parts)
    with open('ocr/book_transcribed_en.md', 'w', encoding='utf-8') as f:
        f.write(result)
    
    final_pages = len(re.findall(r'## Page \d+', result))
    print(f'\nDone! {final_pages} pages in ocr/book_transcribed_en.md ({len(result)} chars)')

if __name__ == '__main__':
    main()
