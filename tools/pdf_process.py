#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import fitz  # PyMuPDF


@dataclass(frozen=True)
class TocEntry:
    level: int
    title: str
    page: int  # 1-based


@dataclass(frozen=True)
class SectionStart:
    title: str
    start_page: int  # 1-based


def _read_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _unique_path(path: str) -> str:
    if not os.path.exists(path):
        return path
    root, ext = os.path.splitext(path)
    for k in range(2, 50):
        candidate = f"{root}.v{k}{ext}"
        if not os.path.exists(candidate):
            return candidate
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{root}.{ts}{ext}"


def _sanitize_filename(name: str) -> str:
    name = name.strip()
    name = re.sub(r'[\\/:*?"<>|]', "-", name)
    name = re.sub(r"\s+", " ", name)
    return name


def _as_toc_entries(obj: Any) -> list[TocEntry]:
    if not isinstance(obj, list):
        raise ValueError("TOC JSON must be a list of objects")
    entries: list[TocEntry] = []
    for idx, row in enumerate(obj):
        if not isinstance(row, dict):
            raise ValueError(f"TOC entry {idx} must be an object")
        level = int(row["level"])
        title = str(row["title"])
        page = int(row["page"])
        if level < 1:
            raise ValueError(f"TOC entry {idx} has invalid level: {level}")
        if page < 1:
            raise ValueError(f"TOC entry {idx} has invalid page: {page}")
        entries.append(TocEntry(level=level, title=title, page=page))
    return entries


def _as_section_starts(obj: Any) -> list[SectionStart]:
    if not isinstance(obj, list):
        raise ValueError("Sections JSON must be a list of objects")
    sections: list[SectionStart] = []
    for idx, row in enumerate(obj):
        if not isinstance(row, dict):
            raise ValueError(f"Section {idx} must be an object")
        title = str(row["title"])
        start_page = int(row["start_page"])
        if start_page < 1:
            raise ValueError(f"Section {idx} has invalid start_page: {start_page}")
        sections.append(SectionStart(title=title, start_page=start_page))
    sections = sorted(sections, key=lambda s: s.start_page)
    return sections


def cmd_inspect(args: argparse.Namespace) -> int:
    doc = fitz.open(args.src)
    try:
        toc = doc.get_toc()
        has_toc = bool(toc)
        print(f"pages: {doc.page_count}")
        print(f"has_toc: {has_toc}")
        sample_pages = args.sample_pages
        if sample_pages is None:
            sample_pages = [1, 2, 3, 10, 20, 50, 100, 200, 400, doc.page_count]
        sample_pages = [p for p in sample_pages if 1 <= p <= doc.page_count]
        # Deduplicate while preserving order.
        seen: set[int] = set()
        sample_pages = [p for p in sample_pages if not (p in seen or seen.add(p))]
        print("sample_text_chars:")
        for p in sample_pages:
            text = doc.load_page(p - 1).get_text("text").strip()
            print(f"  p{p}: {len(text)}")
        return 0
    finally:
        doc.close()


def cmd_bookmark(args: argparse.Namespace) -> int:
    toc_entries = _as_toc_entries(_read_json(args.toc_json))
    toc = [[e.level, e.title, e.page] for e in toc_entries]

    src = args.src
    doc = fitz.open(src)
    try:
        for e in toc_entries:
            if e.page > doc.page_count:
                raise ValueError(f"Bookmark page out of range: {e.title} -> {e.page} (max {doc.page_count})")
        doc.set_toc(toc)

        out = args.out
        if out is None:
            base_dir = os.path.dirname(src)
            stem = os.path.splitext(os.path.basename(src))[0]
            out = os.path.join(base_dir, f"{stem}.bookmarked.pdf")
        out = _unique_path(out)
        doc.save(out)
        print(out)
        return 0
    finally:
        doc.close()


def _iter_ranges(sections: list[SectionStart], page_count: int) -> Iterable[tuple[str, int, int]]:
    if not sections:
        return
    if sections[0].start_page != 1:
        raise ValueError("First section start_page must be 1")
    starts = [s.start_page for s in sections]
    if starts != sorted(starts):
        raise ValueError("Section starts must be sorted by start_page")
    for idx, section in enumerate(sections):
        start = section.start_page
        end = (sections[idx + 1].start_page - 1) if idx + 1 < len(sections) else page_count
        if end < start:
            raise ValueError(f"Bad range for {section.title}: {start}-{end}")
        yield (section.title, start, end)


def cmd_split(args: argparse.Namespace) -> int:
    sections = _as_section_starts(_read_json(args.sections_json))

    src = args.src
    doc = fitz.open(src)
    try:
        for s in sections:
            if s.start_page > doc.page_count:
                raise ValueError(
                    f"Section start out of range: {s.title} -> {s.start_page} (max {doc.page_count})"
                )

        out_dir = args.out_dir
        if out_dir is None:
            base_dir = os.path.dirname(src)
            stem = os.path.splitext(os.path.basename(src))[0]
            out_dir = os.path.join(base_dir, f"{stem}.split")
        Path(out_dir).mkdir(parents=True, exist_ok=True)

        written = 0
        for title, start, end in _iter_ranges(sections, doc.page_count):
            out_name = _sanitize_filename(title) + ".pdf"
            out_path = os.path.join(out_dir, out_name)
            out_path = _unique_path(out_path)
            new = fitz.open()
            new.insert_pdf(doc, from_page=start - 1, to_page=end - 1)
            new.save(out_path)
            new.close()
            written += 1
        print(out_dir)
        print(f"files: {written}")
        return 0
    finally:
        doc.close()


def _mathpix_headers() -> dict[str, str]:
    app_id = os.environ.get("MATHPIX_APP_ID", "").strip()
    app_key = os.environ.get("MATHPIX_APP_KEY", "").strip()
    if not app_id or not app_key:
        raise RuntimeError("Mathpix credentials missing: set MATHPIX_APP_ID and MATHPIX_APP_KEY")
    return {"app_id": app_id, "app_key": app_key}


def _mathpix_ocr_png(png_bytes: bytes) -> str:
    import urllib.request

    payload = {
        "src": "data:image/png;base64," + base64.b64encode(png_bytes).decode("ascii"),
        "formats": ["text"],
        "ocr": ["math", "text"],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.mathpix.com/v3/text",
        data=data,
        headers={**_mathpix_headers(), "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read()
    result = json.loads(body.decode("utf-8"))
    text = result.get("text")
    if not isinstance(text, str):
        raise RuntimeError(f"Unexpected Mathpix response keys: {sorted(result.keys())}")
    return text


def cmd_ocr_page(args: argparse.Namespace) -> int:
    if not args.use_mathpix:
        raise RuntimeError("Refusing to OCR without --use-mathpix (Mathpix calls cost money).")

    doc = fitz.open(args.src)
    try:
        if not (1 <= args.page <= doc.page_count):
            raise ValueError(f"--page must be between 1 and {doc.page_count}")
        page = doc.load_page(args.page - 1)
        zoom = float(args.zoom)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        text = _mathpix_ocr_png(pix.tobytes("png"))
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")
        return 0
    finally:
        doc.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf_process.py",
        description="Bookmark and split PDFs using PyMuPDF; optional OCR via Mathpix for scan-only pages.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_inspect = sub.add_parser("inspect", help="Print quick stats and sample text lengths.")
    p_inspect.add_argument("--src", required=True, help="Source PDF path.")
    p_inspect.add_argument(
        "--sample-pages",
        nargs="+",
        type=int,
        default=None,
        help="1-based pages to sample for extracted text length.",
    )
    p_inspect.set_defaults(func=cmd_inspect)

    p_bookmark = sub.add_parser("bookmark", help="Write bookmarks from a TOC JSON file.")
    p_bookmark.add_argument("--src", required=True, help="Source PDF path.")
    p_bookmark.add_argument("--toc-json", required=True, help="JSON list of {level,title,page}.")
    p_bookmark.add_argument("--out", default=None, help="Output PDF path (defaults to <stem>.bookmarked.pdf).")
    p_bookmark.set_defaults(func=cmd_bookmark)

    p_split = sub.add_parser("split", help="Split into multiple PDFs from a sections JSON file.")
    p_split.add_argument("--src", required=True, help="Source PDF path.")
    p_split.add_argument("--sections-json", required=True, help="JSON list of {title,start_page}.")
    p_split.add_argument("--out-dir", default=None, help="Output directory (defaults to <stem>.split/).")
    p_split.set_defaults(func=cmd_split)

    p_ocr = sub.add_parser("ocr-page", help="Render a page and OCR it via Mathpix.")
    p_ocr.add_argument("--src", required=True, help="Source PDF path.")
    p_ocr.add_argument("--page", required=True, type=int, help="1-based page to OCR.")
    p_ocr.add_argument("--zoom", default="2.0", help="Render zoom factor (e.g. 2.0).")
    p_ocr.add_argument(
        "--use-mathpix",
        action="store_true",
        help="Actually call Mathpix (opt-in; costs money).",
    )
    p_ocr.set_defaults(func=cmd_ocr_page)

    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

