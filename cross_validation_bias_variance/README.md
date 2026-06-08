# Cross-Validation and Bias-Variance Tradeoff

## What this notebook covers

**Part 1: Cross-Validation**
- Compare 5-fold vs 10-fold cross-validation
- Understand when to use cv=5 vs cv=10

**Part 2: Bias-Variance Tradeoff**
- Test Decision Trees with depths 1 to 20+
- Identify underfitting (High Bias) and overfitting (High Variance)
- Find the optimal model complexity (Sweet Spot)

## Key Results

| Metric | Value |
|--------|-------|
| cv=5 Score | 0.9667 ± 0.0211 |
| cv=10 Score | 0.9600 ± 0.0327 |
| Optimal Tree Depth | 3 |
| Test Accuracy | 0.9533 |

## Quick Reference

| Problem | Signal | Fix |
|---------|--------|-----|
| Underfitting | Low train + Low test accuracy | Increase complexity |
| Overfitting | High train + Low test accuracy | Reduce complexity |
| Sweet Spot | High train + High test, small gap | Perfect! |

## Files
- Cross Validation and Bias Variance Tradeoff.ipynb - Main notebook
- bias_variance_tradeoff.png - Generated plot
- README.md - This file

## Run it
pip install numpy pandas matplotlib scikit-learn jupyter
jupyter notebook

## Related Modules
- Linear Regression
- Feature Engineering

**Last Updated:** June 2026
