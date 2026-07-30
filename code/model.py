"""
model.py

Statistical analysis and classification for MIME-DAR.

Two things happen here, and they answer two different questions:

1. Hypothesis testing (run_feature_ttests) asks: "Are human and
   AI files statistically distinguishable on each feature alone?"
   This uses Welch's t-test, which does not assume equal variance
   between the two groups.

2. Classification (train_and_evaluate) asks: "Can we combine the
   features into a single decision rule that predicts the label?"
   Instead of hand-picking weights (w1, w2, w3) as in the original
   MIME-DAR design sketch, the weights are LEARNED from data via
   logistic regression - this is the empirical replacement for the
   theoretical Weighted Anomaly Scoring Vector (WASV).
"""

from typing import Dict

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

FEATURE_COLUMNS = [
    "indentation_variance",
    "comment_placement_ratio",
    "mixed_line_ending_ratio",
    "trailing_whitespace_ratio",
    "missing_final_newline",
]


def run_feature_ttests(df: pd.DataFrame) -> Dict[str, dict]:
    """
    Run a Welch's t-test on each feature, comparing the human group
    (label == 0) against the AI group (label == 1).

    Returns:
        A dict mapping feature name -> {t_statistic, p_value,
        human_mean, ai_mean}.
    """
    results = {}
    human = df[df["label"] == 0]
    ai = df[df["label"] == 1]

    for feature in FEATURE_COLUMNS:
        t_stat, p_value = stats.ttest_ind(
            human[feature], ai[feature], equal_var=False
        )
        results[feature] = {
            "t_statistic": t_stat,
            "p_value": p_value,
            "human_mean": human[feature].mean(),
            "ai_mean": ai[feature].mean(),
            "significant_at_0.05": bool(p_value < 0.05),
        }

    return results


def train_and_evaluate(df: pd.DataFrame, test_size: float = 0.3, random_state: int = 42) -> dict:
    """
    Train a logistic regression classifier on the feature set and
    evaluate it on a held-out test split.

    Returns:
        A dict containing the learned weights (the empirical WASV),
        the decision threshold, and evaluation metrics.
    """
    X = df[FEATURE_COLUMNS].values
    y = df["label"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # Standardize features so learned coefficients are comparable
    # in magnitude - this makes the weights directly interpretable
    # as relative feature importance.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    clf = LogisticRegression(random_state=random_state)
    clf.fit(X_train_scaled, y_train)

    y_pred = clf.predict(X_test_scaled)

    weights = dict(zip(FEATURE_COLUMNS, clf.coef_[0]))
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    false_positive_rate = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    return {
        "learned_weights": weights,
        "intercept": clf.intercept_[0],
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "false_positive_rate": false_positive_rate,
        "confusion_matrix": {
            "true_negative": int(tn),
            "false_positive": int(fp),
            "false_negative": int(fn),
            "true_positive": int(tp),
        },
        "n_train": len(X_train),
        "n_test": len(X_test),
    }
