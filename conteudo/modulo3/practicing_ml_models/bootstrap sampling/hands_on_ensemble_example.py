## compare a single Decision Tree vs. a Random Forest (ensemble of trees)

# ensemble_comparison.py
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# 1. Create a harder synthetic dataset
X, y = make_classification(
    n_samples=1000, 
    n_features=20, 
    n_informative=5, 
    n_redundant=2,
    n_classes=2, 
    flip_y=0.3, 
    class_sep=0.8, 
    random_state=42
)

# 2. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. Define models
tree = DecisionTreeClassifier(random_state=42)
forest = RandomForestClassifier(n_estimators=100, # número de árvores
                                random_state=42)

# 4. Cross-validation scores
tree_scores = cross_val_score(tree, X, y, cv=5)
forest_scores = cross_val_score(forest, X, y, cv=5)

# 5. Results
print("Decision Tree CV Accuracy: %.3f ± %.3f" % (np.mean(tree_scores), np.std(tree_scores)))
print("Random Forest CV Accuracy: %.3f ± %.3f" % (np.mean(forest_scores), np.std(forest_scores)))
