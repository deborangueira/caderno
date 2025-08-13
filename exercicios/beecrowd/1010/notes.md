**roadmap**

1. read a code of a product 2. read number of units of product 1
2. read price for one unit of product 1
3. read a code of product 2
4. read number of units of product 2
5. read price for one unit of product 2
6. Calculate amount*price
7. show total to be payed:
"VALOR A PAGAR: R$ " + total

**Proposta do código avançado**

1. lidar quando tem N produtos
2. utilizar um objeto (json) para guardar as informações dos N produtos
3. não utilizar shift

**explicações**

- `input.split('\n');` pega o input e transforma em lista separando os elementos em dois conjuntos numéricos indicado pela quebra de linha
- `lines.shift().split(" ")` - pego a primeira linha (shift) e separo os valores considerando os espaços (split)
- `shift()` pega os elementos na ordem: código, quantidade, valor unitário
- `Number()` converte as strings em números com decimais.
- `.toFixed(2)` deixa o valor final com 2 casas decimais