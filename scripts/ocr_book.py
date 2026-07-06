#!/usr/bin/env python3
"""
ocr_book.py — OCR Pipeline for Fraktur Font Book

Processes scanned pages of the 1995 book:
"Ordnung und Chaos bei nichtlinearen Schwingungen"

Uses Tesseract with Fraktur script support for German text.
Outputs cleaned markdown with preserved page structure.

Usage:
    python scripts/ocr_book.py --input scans/book_full.pdf --output ocr/
"""

import os
import argparse
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import fitz  # PyMuPDF


def preprocess_image(img):
    """Preprocess scanned page for better OCR accuracy."""
    # Convert to grayscale
    img = img.convert('L')

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

    # Sharpen
    img = img.filter(ImageFilter.SHARPEN)

    # Adaptive threshold using local mean
    # Convert to binary with high contrast
    img = img.point(lambda x: 0 if x < 160 else 255)

    return img


def ocr_page(img, lang='deu+script/Fraktur'):
    """
    OCR a single page image.

    Uses German language + Fraktur script model.
    Falls back to German-only if Fraktur fails.
    """
    try:
        text = pytesseract.image_to_string(img, lang=lang, config='--psm 6')
        return text
    except Exception:
        # Fallback without Fraktur
        text = pytesseract.image_to_string(img, lang='deu', config='--psm 6')
        return text


def extract_images_from_pdf(pdf_path, output_dir, dpi=300):
    """Extract all pages from PDF as images."""
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    paths = []

    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(dpi=dpi)
        img_path = os.path.join(output_dir, f'page_{i+1:03d}.png')
        pix.save(img_path)
        paths.append(img_path)
        print(f'  Extracted page {i+1}/{len(doc)}')

    doc.close()
    return paths


def process_book(pdf_path, output_dir, dpi=300,
                 ocr_lang='deu+script/Fraktur'):
    """
    Full pipeline: extract → preprocess → OCR → save as markdown.
    """
    print(f'Processing book: {pdf_path}')
    print(f'Output directory: {output_dir}')

    # Create output directories
    images_dir = os.path.join(output_dir, 'images')
    text_dir = os.path.join(output_dir, 'text')
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(text_dir, exist_ok=True)

    # Step 1: Extract PDF pages as images
    print('\nStep 1: Extracting pages...')
    img_paths = extract_images_from_pdf(pdf_path, images_dir, dpi)

    # Step 2: OCR each page
    print(f'\nStep 2: OCR with language: {ocr_lang}')
    all_text = []
    for i, img_path in enumerate(img_paths):
        print(f'  OCR page {i+1}/{len(img_paths)}...', end=' ')
        img = Image.open(img_path)
        img_processed = preprocess_image(img)

        # Save processed version
        proc_path = os.path.join(output_dir, 'processed',
                                 f'page_{i+1:03d}_processed.png')
        os.makedirs(os.path.dirname(proc_path), exist_ok=True)
        img_processed.save(proc_path)

        # OCR
        text = ocr_page(img_processed, ocr_lang)

        # Save individual page text
        text_path = os.path.join(text_dir, f'page_{i+1:03d}.txt')
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(text)

        all_text.append((i+1, text))
        print(f'{len(text)} chars')

    # Step 3: Assemble markdown
    print('\nStep 3: Assembling markdown...')
    md_path = os.path.join(output_dir, 'book_ocr_output.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('# Ordnung und Chaos bei nichtlinearen Schwingungen\n')
        f.write('*OCR output from scanned book*\n\n')
        f.write('---\n\n')

        for page_num, text in all_text:
            f.write(f'## Page {page_num}\n\n')
            f.write(text.strip())
            f.write('\n\n---\n\n')

    print(f'\nDone! Markdown saved to: {md_path}')
    print(f'Total pages: {len(img_paths)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='OCR pipeline for Fraktur font book')
    parser.add_argument('--input', '-i', required=True,
                        help='Input PDF path')
    parser.add_argument('--output', '-o', default='ocr_output',
                        help='Output directory')
    parser.add_argument('--dpi', type=int, default=300,
                        help='Scan DPI for extraction')
    parser.add_argument('--lang', default='deu+script/Fraktur',
                        help='Tesseract language')

    args = parser.parse_args()
    process_book(args.input, args.output, args.dpi, args.lang)
