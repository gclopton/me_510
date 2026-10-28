# PDF processing (bookmarks, splitting, OCR)

This note is a “how I do it” reference for working with large technical PDFs, especially scan-only books where there is no selectable text and no built-in bookmarks. The two most common tasks are (i) adding chapter bookmarks (PDF outline entries) and (ii) splitting a book into cover/front-matter/chapters/back-matter so that later splitting/merging steps do not accidentally glue front matter to Chapter 1.

The tooling assumption for this vault is Python + PyMuPDF (`fitz`). That is enough to inspect, render, bookmark, and split PDFs without Adobe. When a PDF is scan-only, you usually need some form of OCR to reliably read a table-of-contents page; on this machine the most convenient OCR option is typically the Mathpix API (if the `MATHPIX_APP_ID` and `MATHPIX_APP_KEY` environment variables are set).

## Quick decision tree

First determine whether the PDF is text-based or scan-only. In a text-based PDF, `page.get_text("text")` will return non-empty text on normal pages. In a scan-only PDF, it will typically return an empty string on most pages.

If the PDF is text-based, you can often auto-detect chapter headings directly from the extracted text. If the PDF is scan-only, you should plan to drive the process from an existing “Contents” page (render it to an image, then OCR it), or do one manual pass where you record chapter start pages.

## Bookmarks: the essential idea

Bookmarks (outline entries) are a list of triples `(level, title, page)` where `page` is 1-based. You create that list and call `doc.set_toc(toc)` and then save a new copy of the PDF. If you want “Front matter” to be separate from Chapter 1, make it its own top-level bookmark and make “Preface”, “Contents”, etc. children of it.

In scan-only books, the tricky part is not the `set_toc` call; it is mapping printed page numbers from the book’s table of contents onto PDF page numbers. The standard workflow is:

1. Find a printed page number that is unambiguous (often the first chapter start page).
2. Locate that printed page inside the PDF by visual inspection (scroll or search thumbnails).
3. Compute a constant offset
   \[
   \text{pdf\_page} = \text{printed\_page} + \text{offset}.
   \]
4. Apply that offset to every ToC line item.

This “constant offset” approach works well for many scanned books because the scan is a simple linear stack of images.

## Splitting: the essential idea

Splitting is driven by the same “section start page” list you used for bookmarks. If you have section starts at pages
\[
s_1 < s_2 < \cdots < s_n,
\]
then section \(k\) is pages \(s_k\) through \(s_{k+1}-1\) (inclusive), and the last section runs through the final page of the PDF.

## Helper script in this vault

Use `tools/pdf_process.py` for repeatable workflows. It supports:

1. Inspecting a PDF to see whether it is scan-only.
2. Writing bookmarks from a JSON file that lists TOC entries.
3. Splitting a PDF into multiple PDFs from a JSON file that lists section starts.
4. (Optional) OCR of a rendered page via Mathpix to help transcribe a scan-only “Contents” page.

### Minimal bookmark workflow (manual TOC transcription)

1. Create a JSON file that lists bookmark entries, for example:

```json
[
  {"level": 1, "title": "Cover", "page": 1},
  {"level": 1, "title": "Front matter", "page": 2},
  {"level": 2, "title": "Preface", "page": 7},
  {"level": 2, "title": "Contents", "page": 9},
  {"level": 1, "title": "Chapter 1 — …", "page": 11}
]
```

2. Run:

```bash
python3 tools/pdf_process.py bookmark --src "/path/to/book.pdf" --toc-json "/path/to/toc.json"
```

This writes a new file next to the original by default, with a `.bookmarked.pdf` suffix, unless you pass `--out`.

### Minimal split workflow

1. Create a JSON file that lists section starts (1-based pages), for example:

```json
[
  {"title": "00 Cover", "start_page": 1},
  {"title": "01 Front matter", "start_page": 2},
  {"title": "02 Chapter 1", "start_page": 11}
]
```

2. Run:

```bash
python3 tools/pdf_process.py split --src "/path/to/book.pdf" --sections-json "/path/to/sections.json"
```

This writes PDFs into a sibling directory named `<stem>.split/` unless you pass `--out-dir`.

### OCR assist for scan-only “Contents” pages (Mathpix)

If the PDF is scan-only, you can render the contents page to an image and OCR it. The helper script can do that in one step, but it is intentionally opt-in because Mathpix calls cost money.

```bash
python3 tools/pdf_process.py ocr-page \
  --src "/path/to/book.pdf" \
  --page 9 \
  --use-mathpix
```

This prints the recognized text to stdout. From there you either (i) manually copy the chapter list into a JSON TOC file, or (ii) add a small parsing step tailored to the book’s ToC layout.

