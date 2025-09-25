from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Criar um dataset pequeno
X, y = make_classification(
    n_samples=10, n_features=4, n_informative=2, n_redundant=0,
    n_classes=2, flip_y=0.2, random_state=42
)

# Treinar Random Forest com poucas árvores
forest = RandomForestClassifier(n_estimators=5, random_state=42)
forest.fit(X, y)

# Previsões de cada árvore individual
all_tree_predictions = np.array([tree.predict(X) for tree in forest.estimators_])

print("Previsões individuais de cada árvore:")
print(all_tree_predictions)

# Previsão final por votação da maioria
final_prediction = forest.predict(X)
print("\nPrevisão final do Random Forest (votação da maioria) - veja que para cada amostra, o RF escolheu a classe mais votada.")
print(final_prediction)
