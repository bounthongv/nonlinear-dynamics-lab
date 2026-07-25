#!/usr/bin/env python3
"""
translate_remaining.py — Translate remaining pages 20-63 and merge.

Reads German text, translates pages 20-63 literally,
then merges with existing pages 1-19 from the current English file.
"""

import re, time, sys
from google import genai
from google.genai import types

def main():
    api_key = sys.argv[1]
    
    with open('ocr/book_transcribed.md', 'r', encoding='utf-8') as f:
        german = f.read()
    with open('ocr/book_transcribed_en.md', 'r', encoding='utf-8') as f:
        current_en = f.read()
    
    pages = re.split(r'(## Page \d+)', german)
    client = genai.Client(api_key=api_key)
    
    # Process only pages 20+
    new_parts = []
    new_parts.append("# Ordnung und Chaos bei nichtlinearen Schwingungen\n*English Translation*\n\n---\n\n")
    
    for i in range(1, len(pages), 2):
        marker = pages[i]
        content = pages[i+1] if i+1 < len(pages) else ''
        page_num = int(re.search(r'\d+', marker).group())
        
        if page_num < 20:
            # Keep existing English translation from current file
            en_start = current_en.find(f'\n## Page {page_num}\n')
            if en_start < 0:
                en_start = current_en.find(f'## Page {page_num}\n')
            en_end = current_en.find(f'\n## Page {page_num + 1}\n')
            if en_start >= 0:
                existing = current_en[en_start:en_end].strip() if en_end >= 0 else current_en[en_start:].strip()
                new_parts.append(existing)
                print(f'{marker} (keeping existing)')
                continue
        
        # Check if page is already properly translated in current file
        en_start = current_en.find(f'## Page {page_num}\n')
        if en_start >= 0:
            en_end = current_en.find(f'\n## Page {page_num + 1}\n')
            block = current_en[en_start:en_end] if en_end >= 0 else current_en[en_start:]
            # Skip if it's already a proper translation (not an error marker)
            if '*[Quota' not in block and '*[Not yet' not in block and '*[Error' not in block:
                new_parts.append(block.strip())
                print(f'{marker} (keeping existing)')
                continue
        
        if content.strip():
            print(f'{marker}...', end=' ', flush=True)
            try:
                resp = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[f'Translate to English. Keep all LaTeX ($$), headings (#), and figure markers (![...]) exactly as-is. Translate only the text between them.\n\n{content}'],
                    config=types.GenerateContentConfig(temperature=0.0, max_output_tokens=8192)
                )
                t = resp.text
                print(f'✓')
            except Exception as e:
                msg = str(e)
                if 'RESOURCE_EXHAUSTED' in msg or '429' in msg:
                    print(f'\n⚠️ QUOTA at {marker}')
                    new_parts.append(f'{marker}\n*[Quota exceeded]*\n\n{content}')
                    # Queue remaining
                    for j in range(i+2, len(pages), 2):
                        m = pages[j]; c = pages[j+1] if j+1 < len(pages) else ''
                        new_parts.append(f'{m}\n*[Not yet translated]*\n\n{c}')
                    break
                else:
                    print(f'✗ {str(e)[:60]}')
                    t = f'*[Error]*\n\n{content}'
            
            new_parts.append(f'{marker}\n{t}')
        else:
            new_parts.append(marker)
        
        time.sleep(2)
    
    result = '\n\n'.join(new_parts)
    with open('ocr/book_transcribed_en.md', 'w', encoding='utf-8') as f:
        f.write(result)
    
    final = len(re.findall(r'## Page \d+', result))
    print(f'\nDone! {final} pages ({len(result)} chars)')

if __name__ == '__main__':
    main()
