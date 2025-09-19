# Notes

We don’t always have the same amount of labeled data for each class, and this can negatively affect the model’s training. 

Nesse caso: **precisão** > acuracia

How to deal with imbalanced datasets:

| Método              | Descrição curta                                    | Quando usar                     |
|---------------------|----------------------------------------------------|---------------------------------|
| Oversampling        | Replica ou gera exemplos da classe minoritária     | Poucos dados minoritários       |
| Undersampling       | Remove exemplos da classe majoritária              | Muitos dados majoritários       |
| Class Weight        | Atribui pesos maiores às classes minoritárias      | Modelos compatíveis com pesos   |
| Decision Threshold  | Ajusta limite de decisão da predição               | Quando há foco em recall/precisão|


**Definition**




# Refs

[Handling Imbalanced Datasets in Python](https://medium.com/@tam.tamanna18/handling-imbalanced-datasets-in-python-methods-and-procedures-7376f99794de)

[Tactics to Handle Class Imbalance](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)