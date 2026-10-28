#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Section:
    number: str
    title: str
    start_line: int


SECTION_HEADING_RE = re.compile(r"^(#{2,6})\s*(\d{1,2}\.\d+)\s*(.*)\s*$")


def _sanitize_filename(name: str) -> str:
    name = name.strip()
    name = re.sub(r"[\\/:*?\"<>|]", "-", name)
    name = re.sub(r"\s+", " ", name)
    return name


def _find_single_md(chapter_dir: Path) -> Path:
    md_files = sorted([p for p in chapter_dir.glob("*.md") if p.name not in (".mathpix_full.md",)])
    if len(md_files) != 1:
        raise RuntimeError(f"Expected exactly 1 markdown file in {chapter_dir}, found {len(md_files)}")
    return md_files[0]


def _parse_sections(lines: list[str]) -> list[Section]:
    sections: list[Section] = []
    for idx, line in enumerate(lines):
        m = SECTION_HEADING_RE.match(line)
        if not m:
            continue
        number = m.group(2)
        raw_title = m.group(3).strip()
        raw_title = re.sub(r"^\s*[\|I]\s*", "", raw_title)
        title = raw_title.strip() or "Section"
        sections.append(Section(number=number, title=title, start_line=idx))
    unique: list[Section] = []
    seen: set[str] = set()
    for s in sections:
        if s.number in seen:
            continue
        seen.add(s.number)
        unique.append(s)
    return unique


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def split_one_chapter_dir(chapter_dir: Path, *, force: bool) -> None:
    chapter_dir = chapter_dir.resolve()
    full_backup = chapter_dir / ".mathpix_full.md"

    if full_backup.exists() and not force:
        return

    main_md = _find_single_md(chapter_dir)
    text = main_md.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    sections = _parse_sections(lines)
    if not sections:
        if not full_backup.exists():
            main_md.rename(full_backup)
            _write_text(main_md, text)
        return

    if not full_backup.exists():
        main_md.rename(full_backup)

    for p in chapter_dir.glob("*.md"):
        if p.name == ".mathpix_full.md":
            continue
        if p.name == main_md.name:
            continue
        p.unlink()

    intro_end = sections[0].start_line
    intro_text = "\n".join(lines[:intro_end]).rstrip() + "\n"

    index_lines = [intro_text.strip(), "", "## Sections", ""]
    section_files: list[tuple[Section, Path]] = []

    for idx, section in enumerate(sections):
        start = section.start_line
        end = sections[idx + 1].start_line if idx + 1 < len(sections) else len(lines)
        chunk = "\n".join(lines[start:end]).rstrip() + "\n"
        filename = _sanitize_filename(f"{section.number} {section.title}.md")
        out_path = chapter_dir / filename
        _write_text(out_path, chunk)
        section_files.append((section, out_path))

    for section, out_path in section_files:
        link = out_path.stem
        index_lines.append(f"- [[{link}]]")

    _write_text(chapter_dir / main_md.name, "\n".join(index_lines).rstrip() + "\n")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Split Mathpix chapter markdown into per-section notes (e.g., 2.1, 2.2).")
    parser.add_argument("--root", required=True, help="Directory containing chapter subfolders.")
    parser.add_argument(
        "--chapter-dir-regex",
        default=r"^(chapter\d+|chapter\d+\.pdf)$",
        help="Regex (case-insensitive) to select chapter directories by name.",
    )
    parser.add_argument("--force", action="store_true", help="Re-split even if .mathpix_full.md already exists.")
    args = parser.parse_args(argv)

    root = Path(args.root).expanduser().resolve()
    chap_re = re.compile(args.chapter_dir_regex, re.IGNORECASE)

    chapter_dirs = sorted([p for p in root.iterdir() if p.is_dir() and chap_re.search(p.name)])
    if not chapter_dirs:
        raise RuntimeError(f"No chapter directories matched under {root}")

    for d in chapter_dirs:
        split_one_chapter_dir(d, force=args.force)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__('sys').argv[1:]))
