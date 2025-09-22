# Notes

- Parâmtros que são importantes para o modelo mas não podem ser definidos por meio dos dados ou de treinamento

## Tuning
- Processo iterativo de experimentar várias combinações de hiperparâmetros pra ver quais dão o melhor resultado.
- Encontrar um hiperparâmetro ótimo muda o desempenho do modelo inteiro e garante que ele tenha um alto desempenho.
- Técnicas

    | Método              | Descrição curta                                    |
    |---------------------|----------------------------------------------------
    | Grid Search        | Testar **todas** as combinações possíveis     | 
    | Random Search       | Testa **algumas** combinações que são **aleatórias**              |
    | Bayesian Optimization        | Técnica que, ao testarmos algumas configurações, aprende de quais partes do espaço de hiperparâmetros parecem resultar em bom desempenho, e foca os testes futuros nessas regiões promissoras. Usa **estatísticas**/probabilidades.     |

**Hiperparâmetros comuns**

- Epochs — quantas vezes o modelo vê os dados de treino por completo.
- Min batch size — quantos exemplos de dados são usados em cada passo de atualização do modelo. 

## Refs

[Ajuste de hiperparâmetros](https://aws.amazon.com/what-is/hyperparameter-tuning/?nc1=h_ls)