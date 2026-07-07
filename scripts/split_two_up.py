#!/usr/bin/env python3
"""
split_two_up.py — Detect and split 2-up scanned pages into individual pages.

Some scanned pages contain two book pages side-by-side.
This script detects them by aspect ratio and splits accordingly.
"""

import os, sys
from PIL import Image
from pathlib import Path


def is_two_up(img, aspect_threshold=0.8):
    """
    Detect if a page is 2-up (two book pages on one scan).
    Book pages are typically more square (wider) than a full A4.
    """
    w, h = img.size
    aspect = w / h  # width / height
    # A4 portrait is ~0.707. Two book pages side-by-side is wider.
    return aspect > aspect_threshold


def split_page(img, output_dir, base_name):
    """Split a 2-up page into left and right halves."""
    w, h = img.size
    mid = w // 2

    left = img.crop((0, 0, mid, h))
    right = img.crop((mid, 0, w, h))

    left.save(os.path.join(output_dir, f'{base_name}_a.png'))
    right.save(os.path.join(output_dir, f'{base_name}_b.png'))
    return True


def process_pages(input_dir, output_dir):
    """Process all pages: detect 2-up, split if needed, copy if single."""
    os.makedirs(output_dir, exist_ok=True)
    files = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])

    two_up_count = 0
    single_count = 0
    page_counter = 1

    print(f'Processing {len(files)} pages from {input_dir}')
    print()

    for fname in files:
        path = os.path.join(input_dir, fname)
        img = Image.open(path)
        w, h = img.size

        if is_two_up(img):
            # Split into two pages
            mid = w // 2
            left = img.crop((0, 0, mid, h))
            right = img.crop((mid, 0, w, h))
            left.save(os.path.join(output_dir, f'book_page_{page_counter:03d}.png'))
            page_counter += 1
            right.save(os.path.join(output_dir, f'book_page_{page_counter:03d}.png'))
            page_counter += 1
            two_up_count += 1
            print(f'  {fname}: SPLIT ({w}x{h}) → 2 book pages')
        else:
            # Single book page — copy as-is
            img.save(os.path.join(output_dir, f'book_page_{page_counter:03d}.png'))
            page_counter += 1
            single_count += 1
            print(f'  {fname}: COPY ({w}x{h}) → 1 book page')

    print(f'\nDone! Created {page_counter - 1} book pages')
    print(f'  Split (2-up): {two_up_count}')
    print(f'  Copied (single): {single_count}')


if __name__ == '__main__':
    input_dir = sys.argv[1] if len(sys.argv) > 1 else 'scans/pages'
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'scans/book_pages'
    process_pages(input_dir, output_dir)
