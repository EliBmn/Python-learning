# CalibraPhish — Research Progress (18 November 2026)

## Research objective
Risk-calibrated selective automation for multimodal phishing email detection using a vision-language model (Qwen2-VL-2B-Instruct), probability calibration, and a human-review option.

## Earlier pilot (rendered text emails; NOT original email screenshots)
- Dataset: Kaggle phishing-email text corpus; emails rendered as simple images.
- Pilot: 20 samples; accuracy 0.70.
- Main experimental split: 300 balanced samples, with 100 calibration / 100 validation / 100 held-out test.
- Calibration subset (n=100): accuracy 0.57; confusion matrix [[5,43],[0,52]].
- Isotonic regression trained on calibration predictions.
- Validation subset (n=100): accuracy 0.53; confusion matrix [[1,47],[0,52]].
- Validation Brier score: raw 0.4485; isotonic-calibrated 0.2396 (46.6% lower).
- These are preliminary findings on rendered text, not a validated real-screenshot benchmark. Held-out test has not been reported.

## New image dataset preparation
- 51 phishing-themed screenshots from CanIPhish (simulated phishing examples).
- 51 ham emails selected from the Apache SpamAssassin Easy Ham public corpus and rendered as PNG images.
- A 102-image standardized package was prepared (1024 x 768 pixels) with a manifest of sources and labels.
- This is a **preliminary evaluation dataset**, not yet an independently verified benchmark.
- Caution: source/layout confounding remains possible because phishing and benign examples originate from different sources and image creation workflows. Standardized dimensions do not eliminate this bias.
- Do not include obvious category labels such as 'scam' in model-visible screenshots; audit all samples for leakage.

## Current status and next steps
1. Upload the standardized ZIP to Google Drive under CalibraPhish.
2. Restore a working Colab runtime (currently encountering 'Failed to assign a backend').
3. Verify manifest and image counts; visually audit screenshots and remove duplicates/label leakage.
4. Run Qwen2-VL inference on the 102 images and save raw predictions, confidence, latency, and labels to CSV.
5. Create a stratified train/calibration/test protocol and calibrate only on calibration data; avoid tuning on test data.
6. Report accuracy, precision, recall, FPR, Brier score, ECE, coverage-risk curves, and selective automation policies.
7. Preserve source provenance and release permissions; avoid uploading raw email personal data without review.

## Reproducibility note
No Qwen2-VL inference results on the new 102-image set are claimed here. This file records work completed so far and the planned experimental workflow. The image ZIP and model checkpoints are not committed in this update.
