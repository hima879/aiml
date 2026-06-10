# Decision Tree Classifier - Iris Dataset

## What this notebook covers

**Models Implemented:**
- Gini Impurity (depth=1, 3, 5)
- Entropy (depth=3)

**Key Concepts:**
- Gini Impurity: Measures node purity (0 = pure, 0.5 = impure)
- Train-test split (70% train, 30% test)
- Feature importance analysis
- Tree visualization

## Results

| Model | Accuracy |
|-------|----------|
| Gini (depth=3) | 0.9778 (Best) |
| Entropy (depth=3) | 0.9333 |
| Gini (depth=5) | 0.9333 |
| Gini (depth=1) | 0.6667 |

## Feature Importance

| Feature | Importance |
|---------|------------|
| petal length | 0.5509 |
| petal width | 0.4491 |
| sepal length | 0.0000 |
| sepal width | 0.0000 |

## Files
- Practical.ipynb - Main notebook
- decision_tree_iris.png - Visualized decision tree

## Run it
pip install numpy pandas matplotlib scikit-learn jupyter
jupyter notebook Practical.ipynb

**Last Updated:** June 2026
