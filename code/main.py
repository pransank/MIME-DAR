"""
main.py

Runs the full MIME-DAR pipeline end to end:

  1. Tier 1 - Canonical Verification: gate out corrupted/mislabeled
     files before deeper analysis                          (tier1.py)
  2. Load remaining human and AI Python files, extract
     Tier 2 (structural stylometry) and Tier 3 (environmental
     artifact) features                          (dataset.py, features.py, tier3.py)
  3. Test whether each feature statistically separates
     the two groups (Welch's t-test)                        (model.py)
  4. Train a logistic regression classifier and evaluate
     it on a held-out test split                            (model.py)
  5. Print a summary you can drop directly into the
     paper's Results section

Usage:
    python main.py --human_dir path/to/human_python --ai_dir path/to/ai_python
"""

import argparse

from dataset import build_dataset
from model import run_feature_ttests, train_and_evaluate, FEATURE_COLUMNS


def print_section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Run the MIME-DAR pipeline.")
    parser.add_argument("--human_dir", required=True, help="Folder of human-written .py files")
    parser.add_argument("--ai_dir", required=True, help="Folder of AI-generated .py files")
    args = parser.parse_args()

    print_section("1. TIER 1 - CANONICAL VERIFICATION (GATE)")
    df, gate_report = build_dataset(args.human_dir, args.ai_dir)

    n_human_fail = len(gate_report["human_failures"])
    n_ai_fail = len(gate_report["ai_failures"])
    print(f"Human files failing Tier 1: {n_human_fail}")
    for failure in gate_report["human_failures"]:
        print(f"  - {failure['filename']}: {failure['reasons']}")
    print(f"AI files failing Tier 1: {n_ai_fail}")
    for failure in gate_report["ai_failures"]:
        print(f"  - {failure['filename']}: {failure['reasons']}")
    if n_human_fail == 0 and n_ai_fail == 0:
        print("All files passed Tier 1. Proceeding to Tier 2 / Tier 3 analysis.")

    print_section("2. LOADING DATASET (Tier 2 + Tier 3 features)")
    print(f"Loaded {len(df)} files total: "
          f"{(df['label'] == 0).sum()} human, {(df['label'] == 1).sum()} AI")
    print(df[["filename"] + FEATURE_COLUMNS + ["label"]])

    print_section("3. HYPOTHESIS TESTING (Welch's t-test per feature)")
    ttest_results = run_feature_ttests(df)
    for feature, result in ttest_results.items():
        print(f"\nFeature: {feature}")
        print(f"  Human mean : {result['human_mean']:.6f}")
        print(f"  AI mean    : {result['ai_mean']:.6f}")
        print(f"  t-statistic: {result['t_statistic']:.4f}")
        print(f"  p-value    : {result['p_value']:.6f}")
        print(f"  Significant at alpha=0.05: {result['significant_at_0.05']}")

    print_section("4. LOGISTIC REGRESSION CLASSIFICATION")
    eval_results = train_and_evaluate(df)
    print(f"Train size: {eval_results['n_train']}  |  Test size: {eval_results['n_test']}")
    print(f"\nLearned weights (standardized, i.e. the empirical WASV):")
    for feature, weight in eval_results["learned_weights"].items():
        print(f"  {feature}: {weight:.4f}")
    print(f"  intercept: {eval_results['intercept']:.4f}")

    print(f"\nAccuracy : {eval_results['accuracy']:.3f}")
    print(f"Precision: {eval_results['precision']:.3f}")
    print(f"Recall   : {eval_results['recall']:.3f}")
    print(f"False Positive Rate: {eval_results['false_positive_rate']:.3f}")
    print(f"\nConfusion matrix: {eval_results['confusion_matrix']}")

    print_section("DONE")
    print("Copy the numbers above into your paper's Results section.")


if __name__ == "__main__":
    main()
