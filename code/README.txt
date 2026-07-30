MIME-DAR Full Pipeline (Tier 1 + Tier 2 + Tier 3)
===================================================

FILES:
  tier1.py      - Tier 1: Canonical Verification (pass/fail gate, NOT a
                  classifier feature - matches original design "files
                  that pass proceed to Tier 2")
  features.py   - Tier 2: Structural Stylometry (indentation_variance,
                  comment_placement_ratio)
  tier3.py      - Tier 3: Environmental Artifact Profiling, REDESIGNED
                  for Python (mixed_line_ending_ratio,
                  trailing_whitespace_ratio, missing_final_newline).
                  NOTE: original design was Excel-metadata based - this
                  is a stated redesign, say so explicitly in your paper.
  dataset.py    - runs Tier 1 gate, then Tier 2 + Tier 3 extraction,
                  builds labeled feature table
  model.py      - Welch's t-tests per feature + logistic regression
                  classifier (learned weights = empirical WASV)
  main.py       - runs everything end to end, prints results

INCLUDED:
  ai_python/    - your 30 AI-generated Python files

WHAT TO DO:
  1. Add your human_python/ folder (your 30 real GitHub files) at the
     same level as ai_python/, inside this mimedar/ folder.
  2. From inside mimedar/:
       pip install pandas scikit-learn scipy --break-system-packages
       python3 main.py --human_dir human_python --ai_dir ai_python
  3. Section 1 of the output shows the Tier 1 gate results - report
     how many files (if any) were excluded and why, in your Methodology.
  4. Sections 3-4 give you real t-test and classification numbers for
     ALL FIVE features now (2 Tier 2 + 3 Tier 3) - copy these into
     Results. Report every feature's p-value honestly, even if most
     aren't significant - that's a real finding, not a failure.

WRITE THIS DOWN FOR YOUR PAPER:
  - Tier 1 is a gate, not a scored feature - explain this design choice
    matches your original architecture description.
  - Tier 3 was redesigned from Excel-metadata to Python-environmental-
    artifacts because the study's empirical scope narrowed to Python
    only. State this as a deliberate scope decision, not an oversight.
