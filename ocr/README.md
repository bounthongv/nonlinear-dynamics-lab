# Transcribe Pages Using AI Vision

Tesseract OCR cannot handle the Fraktur font in this book. **AI vision models can.**

## Recommended Workflow

Use a vision-capable AI (Claude, GPT-4o, Gemini) to transcribe each page.

### Prompt Template

Copy this prompt and send it with each page image:

> **Prompt:**
> This is a scanned page from my 1995 German book 'Ordnung und Chaos bei nichtlinearen Schwingungen'. Transcribe ALL text exactly in German. Preserve equations in LaTeX format ($$...$$). Mark illegible words as [illegible]. Output as ## Page [N].
>
> For each figure, note its number and caption, and describe what it shows (plot type, axes, key features). Mark figure locations as: ![Figure X.Y: brief description]

### Batch Strategy

| Batch | Pages | Est. Time |
|---|---|---|
| 1 | 1–6 (Title, TOC) | ~10 min |
| 2 | 7–16 (Ch 1-2) | ~15 min |
| 3 | 17–26 (Ch 2-3) | ~15 min |
| 4 | 27–36 (Ch 3) | ~15 min |
| 5 | 37–46 (Ch 4) | ~15 min |
| 6 | 47–54 (Ch 4, appendices) | ~10 min |

Total: ~80 min of transcription work.

### Files Ready

- **Full PDF:** `scans/book_full.pdf` (54 pages)
- **Individual page images:** `scans/pages/page_001.png` through `page_054.png`

### After Transcription

Save the output as `ocr/book_transcribed.md`
Then we can proceed to:
- Convert to LaTeX
- Extract equations for Python simulation
- Rebuild each chapter as a Jupyter notebook
