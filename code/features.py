"""
features.py

MIME-DAR Tier 2: Structural Stylometry feature extraction.

Extracts two signals from a Python source file:
  1. Indentation Consistency  - variance in leading-whitespace width
                                 across indented lines
  2. Comment Placement Ratio  - fraction of comments that sit
                                 immediately above a function/class
                                 definition (a "boilerplate" pattern
                                 associated with LLM output)

Each function returns a plain float so results can be dropped
straight into a feature table (see dataset.py).
"""

import io
import tokenize
from typing import List


def _indent_widths(source: str) -> List[int]:
    """Return the leading-whitespace width of every indented line."""
    widths = []
    for line in source.splitlines():
        stripped = line.lstrip(" \t")
        if stripped == "" or stripped == line:
            continue  # blank line or no leading whitespace
        widths.append(len(line) - len(stripped))
    return widths


def indentation_variance(source: str) -> float:
    """
    Measure the statistical variance of indentation widths in a file.

    Human code tends to mix tabs/spaces or drift in width across a
    large file; LLM output tends to be mechanically uniform, which
    shows up as low variance.
    """
    widths = _indent_widths(source)
    if len(widths) < 2:
        return 0.0

    mean_width = sum(widths) / len(widths)
    variance = sum((w - mean_width) ** 2 for w in widths) / len(widths)
    return variance


def comment_placement_ratio(source: str) -> float:
    """
    Measure the fraction of comments that appear directly above a
    function or class definition line.

    A high ratio suggests uniform, boilerplate-style commenting,
    which is associated with LLM-generated code.
    """
    lines = source.splitlines()
    comment_line_numbers = []

    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        for tok in tokens:
            if tok.type == tokenize.COMMENT:
                comment_line_numbers.append(tok.start[0])
    except tokenize.TokenizeError:
        return 0.0

    if not comment_line_numbers:
        return 0.0

    placed_above_def = 0
    for line_no in comment_line_numbers:
        next_line_idx = line_no  # 0-indexed line after the comment
        if next_line_idx < len(lines):
            next_line = lines[next_line_idx].strip()
            if next_line.startswith("def ") or next_line.startswith("class "):
                placed_above_def += 1

    return placed_above_def / len(comment_line_numbers)


def extract_features(source: str) -> dict:
    """
    Run all Tier 2 feature extractors on a source file and return
    a dictionary of feature_name -> value.
    """
    return {
        "indentation_variance": indentation_variance(source),
        "comment_placement_ratio": comment_placement_ratio(source),
    }
