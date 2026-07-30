"""
tier3.py

MIME-DAR Tier 3: Environmental Artifact Profiling (Python edition).

The original MIME-DAR design scanned for background application
metadata (e.g. Microsoft Office fields) as evidence a file was
touched by a real desktop application. That design was scoped to
Excel; since this study's empirical scope was narrowed to Python
only (see paper Methodology), Tier 3 is redefined here around the
equivalent traces real text editors and human typing habits leave
in plain-text source files:

  1. Mixed line endings    - humans (especially switching between
                              Windows/Unix editors, or copy-pasting
                              from different sources) often produce
                              files that mix \\r\\n and \\n. LLM
                              output is uniformly one style.
  2. Trailing whitespace    - humans frequently leave trailing spaces
                              on lines by accident. LLM output is
                              typically clean of trailing whitespace.
  3. Missing final newline  - many editors leave a file without a
                              trailing newline at EOF depending on
                              how it was saved; LLM output tends to
                              consistently end with one.

This is a redesign of the original Excel-metadata Tier 3, not the
original feature set - state this explicitly in the paper.
"""

from typing import List


def _read_raw_bytes(filepath: str) -> bytes:
    """Read a file in binary mode to preserve original line endings."""
    with open(filepath, "rb") as f:
        return f.read()


def mixed_line_ending_ratio(raw: bytes) -> float:
    """
    Return the fraction of newlines that belong to the minority
    line-ending style.

    0.0 means the file uses exactly one style consistently.
    Values above 0.0 mean the file mixes \\r\\n and \\n.
    """
    crlf_count = raw.count(b"\r\n")
    total_newlines = raw.count(b"\n")
    lf_only_count = total_newlines - crlf_count

    if total_newlines == 0:
        return 0.0

    minority = min(crlf_count, lf_only_count)
    return minority / total_newlines


def trailing_whitespace_ratio(raw: bytes) -> float:
    """Return the fraction of non-empty lines that end in trailing whitespace."""
    text = raw.decode("utf-8", errors="ignore")
    lines = text.splitlines()
    non_empty_lines = [line for line in lines if line.strip() != ""]

    if not non_empty_lines:
        return 0.0

    trailing_count = sum(1 for line in non_empty_lines if line != line.rstrip(" \t"))
    return trailing_count / len(non_empty_lines)


def missing_final_newline(raw: bytes) -> float:
    """Return 1.0 if the file does not end with a newline, else 0.0."""
    if len(raw) == 0:
        return 0.0
    return 0.0 if raw.endswith(b"\n") else 1.0


def extract_environmental_features(filepath: str) -> dict:
    """Run all Tier 3 feature extractors on a file and return a dict."""
    raw = _read_raw_bytes(filepath)
    return {
        "mixed_line_ending_ratio": mixed_line_ending_ratio(raw),
        "trailing_whitespace_ratio": trailing_whitespace_ratio(raw),
        "missing_final_newline": missing_final_newline(raw),
    }
