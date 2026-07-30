"""
dataset.py

Loads human-written and AI-generated Python files from two folders,
runs the full MIME-DAR pipeline on each (Tier 1 gate, then Tier 2 +
Tier 3 feature extraction), and assembles a labeled pandas DataFrame
ready for statistical analysis and modeling.
"""

import os
import glob

import pandas as pd

from features import extract_features
from tier1 import canonical_verification
from tier3 import extract_environmental_features


def _load_folder(folder_path: str, label: int) -> tuple:
    """
    Read every .py file in a folder, run it through the Tier 1 gate,
    extract Tier 2 + Tier 3 features for files that pass, and tag
    each row with the given label (1 = AI-generated, 0 = human).

    Returns:
        (rows, gate_failures) - rows is a list of feature dicts for
        files that passed Tier 1; gate_failures is a list of dicts
        describing files that were excluded and why.
    """
    rows = []
    gate_failures = []
    filepaths = glob.glob(os.path.join(folder_path, "*.py"))

    for filepath in filepaths:
        gate_result = canonical_verification(filepath)

        if not gate_result["passed"]:
            gate_failures.append({
                "filename": os.path.basename(filepath),
                "reasons": gate_result["reasons"],
            })
            continue

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            source = f.read()

        row = extract_features(source)
        row.update(extract_environmental_features(filepath))
        row["label"] = label
        row["filename"] = os.path.basename(filepath)
        rows.append(row)

    return rows, gate_failures


def build_dataset(human_dir: str, ai_dir: str) -> tuple:
    """
    Build a labeled feature DataFrame from a human-code folder and
    an AI-code folder, running every file through Tier 1 first.

    Args:
        human_dir: Path to folder containing human-written .py files.
        ai_dir: Path to folder containing AI-generated .py files.

    Returns:
        (df, gate_report) where df has one row per file that passed
        Tier 1, with feature columns and a 'label' column (0 = human,
        1 = AI); gate_report contains any Tier 1 failures per class.
    """
    human_rows, human_failures = _load_folder(human_dir, label=0)
    ai_rows, ai_failures = _load_folder(ai_dir, label=1)

    if not human_rows:
        raise ValueError(f"No files in human_dir passed Tier 1: {human_dir}")
    if not ai_rows:
        raise ValueError(f"No files in ai_dir passed Tier 1: {ai_dir}")

    df = pd.DataFrame(human_rows + ai_rows)
    gate_report = {
        "human_failures": human_failures,
        "ai_failures": ai_failures,
    }
    return df, gate_report
