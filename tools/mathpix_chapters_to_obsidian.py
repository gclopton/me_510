#!/usr/bin/env python3
from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


API_BASE = "https://api.mathpix.com/v3"


@dataclass(frozen=True)
class SourcePdf:
    path: Path
    chapter_hint: str


def _headers() -> dict[str, str]:
    app_id = os.environ.get("MATHPIX_APP_ID", "").strip()
    app_key = os.environ.get("MATHPIX_APP_KEY", "").strip()
    if not app_id or not app_key:
        raise RuntimeError("Missing Mathpix credentials: set MATHPIX_APP_ID and MATHPIX_APP_KEY.")
    return {"app_id": app_id, "app_key": app_key}


def _request_json(method: str, url: str, body: bytes | None = None, content_type: str | None = None) -> Any:
    headers = dict(_headers())
    if content_type:
        headers["Content-Type"] = content_type
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read()
    return json.loads(raw.decode("utf-8"))


def _request_bytes(method: str, url: str) -> bytes:
    req = urllib.request.Request(url, headers=_headers(), method=method)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def _multipart_form(fields: dict[str, str], files: dict[str, tuple[str, bytes, str]]) -> tuple[bytes, str]:
    boundary = "----mathpixform-" + datetime.now().strftime("%Y%m%d%H%M%S%f")
    crlf = "\r\n"
    parts: list[bytes] = []
    for name, value in fields.items():
        parts.append(f"--{boundary}{crlf}".encode())
        parts.append(f'Content-Disposition: form-data; name="{name}"{crlf}{crlf}'.encode())
        parts.append(value.encode())
        parts.append(crlf.encode())
    for name, (filename, content, mimetype) in files.items():
        parts.append(f"--{boundary}{crlf}".encode())
        parts.append(
            f'Content-Disposition: form-data; name="{name}"; filename="{filename}"{crlf}'.encode()
        )
        parts.append(f"Content-Type: {mimetype}{crlf}{crlf}".encode())
        parts.append(content)
        parts.append(crlf.encode())
    parts.append(f"--{boundary}--{crlf}".encode())
    body = b"".join(parts)
    return body, f"multipart/form-data; boundary={boundary}"


def _normalize_for_obsidian(text: str) -> str:
    return (
        text.replace(r"\(", "$")
        .replace(r"\)", "$")
        .replace(r"\[", "$$")
        .replace(r"\]", "$$")
    )


def _sanitize_name(name: str) -> str:
    name = name.strip()
    name = re.sub(r"[\\/*?\"<>|]", "-", name)
    name = re.sub(r"\s+", " ", name)
    return name


def _clean_heading_text(text: str) -> str:
    text = re.sub(r"<br\s*/?>", " ", text)
    text = text.replace(r"$\mathrm{O}(N)$", "O(N)")
    text = re.sub(r"\\mathrm\{([^}]*)\}", r"\1", text)
    text = text.replace("$", "")
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _list_chapter_pdfs(src_dir: Path) -> list[SourcePdf]:
    pdfs = sorted([p for p in src_dir.iterdir() if p.is_file() and p.suffix.lower() == ".pdf"])
    sources: list[SourcePdf] = []
    for p in pdfs:
        chapter_hint = p.stem
        sources.append(SourcePdf(path=p, chapter_hint=chapter_hint))
    return sources


def _filter_sources(
    sources: list[SourcePdf], *, include_regex: str | None, exclude_regex: str | None
) -> list[SourcePdf]:
    include = re.compile(include_regex, re.IGNORECASE) if include_regex else None
    exclude = re.compile(exclude_regex, re.IGNORECASE) if exclude_regex else None
    kept: list[SourcePdf] = []
    for s in sources:
        name = s.path.name
        if include and not include.search(name):
            continue
        if exclude and exclude.search(name):
            continue
        kept.append(s)
    return kept


def _submit_pdf(pdf_path: Path) -> str:
    pdf_bytes = pdf_path.read_bytes()
    options = {"math_inline_delimiters": ["$", "$"]}
    body, ctype = _multipart_form(
        fields={"options_json": json.dumps(options)},
        files={"file": (pdf_path.name, pdf_bytes, "application/pdf")},
    )
    result = _request_json("POST", f"{API_BASE}/pdf", body=body, content_type=ctype)
    pdf_id = result.get("pdf_id")
    if not isinstance(pdf_id, str) or not pdf_id:
        raise RuntimeError(f"Unexpected submission response: keys={sorted(result.keys())}")
    return pdf_id


def _wait_complete(pdf_id: str, *, label: str) -> None:
    attempt = 0
    while True:
        attempt += 1
        status = _request_json("GET", f"{API_BASE}/pdf/{pdf_id}")
        st = status.get("status")
        if st == "completed":
            return
        if st in ("error", "failed"):
            raise RuntimeError(f"Mathpix conversion failed for {label}: {json.dumps(status)[:500]}")
        percent = status.get("percent_done")
        if isinstance(percent, (int, float)):
            print(f"Converting {label} … {percent}%")
        else:
            print(f"Converting {label} … (status: {st})")
        time.sleep(2 if attempt < 10 else 5)


def _download_best_zip(pdf_id: str) -> tuple[bytes, str]:
    candidates = [
        ("md.zip", "md.zip"),
        ("mmd.zip", "mmd.zip"),
    ]
    for ext, label in candidates:
        try:
            data = _request_bytes("GET", f"{API_BASE}/pdf/{pdf_id}.{ext}")
            return data, label
        except urllib.error.HTTPError as e:
            if e.code in (404, 400):
                continue
            raise
    raise RuntimeError("No markdown zip format available (tried md.zip and mmd.zip).")


def _extract_markdown_zip(zip_bytes: bytes, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        zf.extractall(dest_dir)
    md_files = sorted(dest_dir.rglob("*.md"))
    if not md_files:
        raise RuntimeError(f"No .md found after extracting into {dest_dir}")
    return md_files[0]


def _rewrite_md_in_place(md_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    text = _normalize_for_obsidian(text)
    md_path.write_text(text, encoding="utf-8")


def _extract_title_hint(md_path: Path) -> str | None:
    lines = md_path.read_text(encoding="utf-8", errors="replace").splitlines()
    headings = [
        _clean_heading_text(re.sub(r"^#+\s*", "", ln))
        for ln in lines[:160]
        if ln.lstrip().startswith("#")
    ]
    headings = [h for h in headings if h]

    numeric_heading = re.compile(r"^(\d{1,2}(?:\.\d+)?)$")
    skip_titles = {"summary", "abstract"}

    for i, heading in enumerate(headings):
        m = numeric_heading.fullmatch(heading)
        if not m:
            continue
        num = m.group(1)
        if num.endswith(".0"):
            num = num[:-2]
        for nxt in headings[i + 1 : i + 6]:
            lower = nxt.lower()
            if numeric_heading.fullmatch(nxt):
                continue
            if lower in skip_titles or lower.startswith("part "):
                continue
            return f"{num} {_sanitize_name(nxt)}"

    for heading in headings:
        lower = heading.lower()
        if lower.startswith("overview of chapters "):
            return _sanitize_name(heading)
        if lower == "contents":
            return "Contents"
        if lower == "preface":
            return "Preface"
        if lower in {"acknowledgments", "acknowledgements"}:
            return "Acknowledgments"
        if lower == "dedication":
            return "Dedication"
        if lower in {"notation", "list of notation"}:
            return "List of Notation"
        if "basic theory and practical methods" in lower:
            return "Title Page and Copyright"
    return None


def _load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def convert_one(src: SourcePdf, out_root: Path, state: dict[str, Any], *, force: bool) -> None:
    key = str(src.path)
    existing = state.get(key, {})
    pdf_id = existing.get("pdf_id") if isinstance(existing, dict) else None

    if not isinstance(pdf_id, str) or not pdf_id:
        print(f"Submitting {src.path.name} …")
        pdf_id = _submit_pdf(src.path)
        state[key] = {"pdf_id": pdf_id, "submitted_at": datetime.now().isoformat()}

    _wait_complete(pdf_id, label=src.path.name)

    zip_bytes, zip_kind = _download_best_zip(pdf_id)
    with tempfile.TemporaryDirectory(prefix="mathpix_extract_") as tmp:
        tmp_dir = Path(tmp)
        md_path = _extract_markdown_zip(zip_bytes, tmp_dir)
        _rewrite_md_in_place(md_path)

        final_name = _extract_title_hint(md_path) or _sanitize_name(src.chapter_hint)
        final_dir = out_root / final_name

        if final_dir.exists() and not force:
            print(f"Skipping (exists): {final_dir}")
            state[key] = {**state.get(key, {}), "out_dir": str(final_dir), "zip_kind": zip_kind}
            return

        if final_dir.exists() and force:
            shutil.rmtree(final_dir)

        final_dir.mkdir(parents=True, exist_ok=True)

        for item in tmp_dir.iterdir():
            shutil.move(str(item), str(final_dir / item.name))

        md_files = list(final_dir.glob("*.md"))
        if md_files:
            main_md = md_files[0]
            desired = final_dir / f"{final_name}.md"
            if main_md != desired:
                if desired.exists():
                    desired.unlink()
                main_md.rename(desired)

        state[key] = {
            **state.get(key, {}),
            "out_dir": str(final_dir),
            "zip_kind": zip_kind,
            "completed_at": datetime.now().isoformat(),
        }
        print(f"Wrote: {final_dir}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Convert already-split chapter PDFs via Mathpix /v3/pdf into Obsidian-friendly Markdown."
    )
    parser.add_argument("--src-dir", required=True, help="Directory containing chapter PDFs (not front/back matter).")
    parser.add_argument("--out-dir", required=True, help="Destination directory inside the Obsidian vault.")
    parser.add_argument(
        "--include-regex",
        default=None,
        help="Only convert PDFs whose filename matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--exclude-regex",
        default=None,
        help="Skip PDFs whose filename matches this regex (case-insensitive).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output chapter folders.",
    )
    args = parser.parse_args(argv)

    src_dir = Path(args.src_dir).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    state_path = out_dir / ".mathpix_state.json"
    state = _load_state(state_path)

    sources = _list_chapter_pdfs(src_dir)
    sources = _filter_sources(sources, include_regex=args.include_regex, exclude_regex=args.exclude_regex)
    if not sources:
        raise RuntimeError(f"No PDFs found in {src_dir}")

    for src in sources:
        convert_one(src, out_dir, state, force=args.force)
        _save_state(state_path, state)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(os.sys.argv[1:]))
