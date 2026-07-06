#!/usr/bin/env python3
"""
Split scanned A4 page images (containing two book pages side-by-side)
into individual left/right pages, reorder correctly, and output as PDF.

Usage:
    python split_pages.py input.pdf --output output.pdf
    python split_pages.py input.pdf --output output.pdf --dpi 600

Requirements:
    pip install pymupdf Pillow
"""

import os
import argparse
import fitz  # PyMuPDF


def split_pdf(input_path, output_path, dpi=300):
    """Split each A4 page into left and right halves, preserving order."""
    doc = fitz.open(input_path)
    out_doc = fitz.open()

    width = doc[0].rect.width
    height = doc[0].rect.height
    mid = width / 2

    print(f"Processing {len(doc)} pages at {width:.0f}x{height:.0f}")

    for i, page in enumerate(doc):
        # Left half
        left_rect = fitz.Rect(0, 0, mid, height)
        left_pix = page.get_pixmap(dpi=dpi, clip=left_rect)
        left_page = out_doc.new_page(width=mid, height=height)
        left_page.insert_image(left_page.rect, pixmap=left_pix)

        # Right half
        right_rect = fitz.Rect(mid, 0, width, height)
        right_pix = page.get_pixmap(dpi=dpi, clip=right_rect)
        right_page = out_doc.new_page(width=mid, height=height)
        right_page.insert_image(right_page.rect, pixmap=right_pix)

    out_doc.save(output_path, garbage=4, deflate=True)
    out_doc.close()
    doc.close()

    total = len(out_doc)
    print(f"Done. Created {total} individual pages → {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split scanned A4 book pages")
    parser.add_argument("input", help="Input PDF (A4 with two book pages)")
    parser.add_argument("--output", "-o", default="split_output.pdf", help="Output PDF")
    parser.add_argument("--dpi", type=int, default=300, help="Output DPI (default: 300)")
    args = parser.parse_args()

    split_pdf(args.input, args.output, args.dpi)
