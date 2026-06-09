# Logistic Regression - Breast Cancer Classification

## Overview
This notebook implements Logistic Regression for binary classification using the Breast Cancer Wisconsin Dataset to predict whether a breast tumor is malignant (0) or benign (1).

## Dataset
- 569 samples, 30 features (radius, texture, perimeter, area, smoothness, etc.)
- Target: 0 = Malignant, 1 = Benign
- Distribution: Malignant 212 (37.3%), Benign 357 (62.7%)

## How Logistic Regression Works
1. Takes linear combination: z = β₀ + β₁x₁ + ... + βₙxₙ
2. Applies sigmoid: P(y=1) = 1 / (1 + e^-z)
3. Classifies using threshold 0.5

## Model Performance
| Metric | Training | Testing |
|--------|----------|---------|
| Accuracy | 96.98% | 94.15% |
| Precision | 97.60% | 92.92% |
| Recall | 97.60% | 98.13% |
| F1-Score | 97.60% | 95.45% |

## Confusion Matrix (Testing Set)
Predicted
Malignant Benign
Actual
Malignant 56 8
Benign 2 105
- True Negatives: 56, False Positives: 8
- False Negatives: 2, True Positives: 105

## What You'll Learn
- Loading and exploring datasets
- Train-test split with stratification
- Logistic Regression implementation
- Evaluation metrics (Accuracy, Precision, Recall, F1-Score)
- Confusion matrix interpretation
- Prediction probabilities

## How to Run
```bash
pip install numpy pandas matplotlib scikit-learn jupyter
jupyter notebook "Logistic Regression.ipynb"

Related Modules

    Linear Regression

    Feature Engineering

    Cross-Validation and Bias-Variance

Last Updated: June 2026

