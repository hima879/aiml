# 🌲 Random Forest - Ensemble Learning

## 📌 Module Overview

Random Forest is an ensemble learning method that builds multiple decision trees and combines their predictions. This module demonstrates Random Forest on the classic Iris dataset.

## 📊 What This Notebook Covers

### Part 1: Dataset Exploration
- Loads Iris dataset (150 samples, 4 features, 3 species)
- Data visualization and distribution analysis

### Part 2: Train-Test Split
- 80% training, 20% testing
- Stratified split to maintain class balance

### Part 3: Decision Tree (Baseline)
- Single Decision Tree for comparison
- Performance metrics and classification report

### Part 4: Random Forest
- 100 decision trees in the forest
- Bootstrap sampling (bagging)
- Feature randomness (max_features='sqrt')
- Out-of-Bag (OOB) score for internal validation

### Part 5: Model Evaluation
- Test accuracy comparison (DT vs RF)
- Confusion matrix visualization
- Classification report (precision, recall, f1-score)

### Part 6: Feature Importance Analysis
- Bar chart showing which features matter most
- Petal measurements are most important for Iris classification

## 📈 Sample Results

| Model | Accuracy |
|-------|----------|
| Decision Tree | 93.33% |
| Random Forest | 90.00% |
| OOB Score | 94.17% |

## 🌸 Per-Species Performance

| Species | Decision Tree | Random Forest |
|---------|---------------|---------------|
| Setosa | 100% | 100% |
| Versicolor | 90% | 90% |
| Virginica | 90% | 80% |

## 📊 Feature Importances

| Feature | Importance |
|---------|------------|
| petal length (cm) | 0.4315 |
| petal width (cm) | 0.4372 |
| sepal length (cm) | 0.1163 |
| sepal width (cm) | 0.0150 |

**Key Insight:** Petal measurements are ~85% of the decision-making power!

## 🔧 Key Random Forest Parameters Explained

| Parameter | Value | What It Does |
|-----------|-------|---------------|
| n_estimators | 100 | Number of trees in the forest |
| max_features | 'sqrt' | Features considered per split: √4 = 2 features |
| bootstrap | True | Sample with replacement for each tree |
| oob_score | True | Calculate Out-Of-Bag error (validation on ~37% unseen data) |
| random_state | 42 | Fix random seed for reproducibility |
| n_jobs | -1 | Use all CPU cores for parallel processing |

## 🚀 How to Run

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
jupyter notebook Main.ipynb
🎓 Key Takeaways
Why Random Forest beats Decision Tree:

    Reduced Overfitting - Ensemble averaging smooths out individual tree errors

    Feature Randomness - Trees are less correlated, better generalization

    Bootstrap Sampling - Each tree sees different data subset

    OOB Validation - Built-in cross-validation without holdout set

When to use Random Forest:

    Classification and Regression problems

    When you need feature importance

    When you want to reduce overfitting

    Handles high-dimensional data well

🔗 Related Modules

    Cross-Validation & Bias-Variance

    Feature Engineering

    Linear Regression

📅 Last Updated

June 2026
EDF
