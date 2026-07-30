"""
tier1.py

MIME-DAR Tier 1: Canonical Verification.

This is a fast, low-resource gate that mimics traditional MIME-style
file validation. It does NOT try to detect AI-generated content -
its only job is to catch files that are corrupted, mislabeled, or
not what they claim to be, before they reach the deeper Tier 2/3
analysis. This matches the original design: "Files that pass proceed
to Tier 2."

A file that fails Tier 1 is excluded from the dataset used for
classification, the same way a file that fails a MIME/magic-number
check would be excluded by traditional security tooling.
"""

import ast
import mimetypes
import os


def canonical_verification(filepath: str) -> dict:
    """
    Run fast structural checks on a file before deeper analysis.

    Returns:
        A dict with 'passed' (bool) and 'reasons' (list of str)
        describing any checks that failed.
    """
    reasons = []

    # Check 1: file extension
    _, ext = os.path.splitext(filepath)
    if ext != ".py":
        reasons.append(f"unexpected extension '{ext}', expected '.py'")

    # Check 2: MIME type sniffing via extension - a stand-in for the
    # magic-number check traditional MIME classifiers perform
    guessed_type, _ = mimetypes.guess_type(filepath)
    if guessed_type is not None and "python" not in guessed_type and "text" not in guessed_type:
        reasons.append(f"unexpected MIME type '{guessed_type}'")

    # Check 3: file is non-empty
    if os.path.getsize(filepath) == 0:
        reasons.append("file is empty")

    # Check 4: file parses as syntactically valid Python
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            source = f.read()
        ast.parse(source)
    except SyntaxError as exc:
        reasons.append(f"syntax error: {exc}")
    except (OSError, UnicodeDecodeError) as exc:
        reasons.append(f"could not read file: {exc}")

    return {
        "passed": len(reasons) == 0,
        "reasons": reasons,
    }
