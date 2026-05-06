### Cold Start (o desafio da falta de dados)

- Dificuldade que um sistema de recomendação enfrenta quando não possui dados iniciais suficientes para fornecer resultados precisos
- Um dos maiores desafios para os algorítimos de **filtragem colaborativa**, que **dependem fundamentalmente de interações** passadas para gerar sugestões

**Tipos**
    1. Cold Start de Produto (ou Item)
    - Ocorre quando um novo item é inserido no catálogo e ainda não recebeu avaliações ou interações de usuários, nesse caso, o item torna-se "invisível" para o algoritmo pois não tem histórico.

    2. Cold Start de Usuário (ou Visitante)
    - Acontece quando um novo usuário acessa a plataforma e o sistema ainda não possui um perfil ou histórico de suas preferências, nesse caso, o algorítimo não consegue saber o que o usuário gosta

**Estratégias de mitigação**
- Filtragem **Baseada em Conteúdo**: Utiliza metadados e atributos dos itens (como gênero, descrição ou características técnicas)
- Estratégias de **Popularidade**: Mostrar o que é tendência
- Informações **Contextuais**: Coletar dados imediatos como geolocalização (IP/GPS), tipo de dispositivo, navegador e o site de origem para personalizar
- Sistemas **Híbridos**: sistemas podem usar, por exemplo, análises de áudio e Processamento de Linguagem Natural (NLP) para entender as características de novas músicas e "aquecer" o processo de recomendação

### Personalização baseada em Machine Learning

Como transformar grandes volumes de dados brutos em sugestões personalizadas. Consiste em um pipeline de 4 fases:

1. COLETA: dados **explícitos** (fornecidos diretamente pelo usuário), dados **implicitos** (comportamento do usuário que são rastreados pelo sistema); e **atributos** (informações demográficas, psicográficas e metadados dos ítens)

2. ARMAZENAMENTO: **Bancos**, data **lakes**, data **warehouses**...

3. ANÁLISE: em **lote/batch** (uma vez por dia); **quase em tempo real** (em intervalos de min ou seg, permitindo gerar recomendações durante a sessão de navegação); **em tempo real** (fluxos de streaming, permite reações imediatas a cada clique)

4. FILTRAGEM: baseada em **conteúdo** (foca nas características dos itens que o usuário gostou); **colaborativa** (encontra padrões entre diferentes usuários).

### Filtragem Baseada em Conteúdo - CBF

- cria perfis baseados em metadados: gênero, diretor, autor ou descrição.
- Perfil do Item: É uma representação das suas características (metadados)
- Premissa: se um usuário gostou de um item no passado, ele provavelmente gostará de itens similares no futuro

**Benefícios**
1. Fim do Cold Start de ítens
2. Independência de Usuários
3. Transparência e explicabilidade: é fácil de justificar pro usuário o pq daquela recomendação, aumentando a confiabilidade no sistema
4. Estabilidade já que os metadados não mudam

**Riscos**
- Super-especialização, onde o usuário fica preso em uma "bolha" de itens muito parecidos, sem descobrir novos gêneros ou interesses

**Implementação Técnica: O uso de Vetores**

### Espaço latente

- Quando os atributos são transformados em vetores no espaço latente permitindo que o sistema calcule matematicamente quais itens estão geometricamente "mais próximos" um do outro
- A grande utilidade é a redução de dimensionalidade, permitindo que o sistema substitua milhares de atributos superficiais (como cada ator ou palavra de uma descrição) por um número reduzido de dimensões (como 50 ou 100 fatores) que explicam a variância dos dados de forma eficiente

**Fatores Ocultos**   

No espaço latente, as informações são organizadas em fatores latentes, que são **características que o algoritmo descobre automaticamente a partir dos padrões de dados**, mesmo que elas não tenham sido explicitamente 

**Criação via Fatoração**   

Esse espaço é gerado por técnicas de fatoração de matrizes, como a SVD (Decomposição em Valores Singulares), que decompõe a grande matriz original de avaliações em matrizes menores de "usuário-recurso" e "item-recurso"   
Na matemática do SVD, os valores singulares (geralmente representados na matriz diagonal Σ) indicam a força ou importância de cada fator latente

**A recomendação**   

Uma vez que os itens e usuários estão mapeados nesse espaço vetorial latente, o sistema pode calcular a similaridade entre eles medindo a distância ou o ângulo (cosseno) entre seus vetores, facilitando a recomendação de itens que estão "geometricamente próximos" aos gostos do usuário

### TF-IDF (Term Frequency-Inverse Document Frequency)

- Funcionamento: Essa técnica identifica palavras ou outra característica que são frequentes em um ítem específico, mas raras no restante, atribuindo a elas um peso maior por serem "características" daquele ítem.
- Cálculo de Similaridade (Similaridade de Cosseno): Após transformar cada ítem em um vetor numérico, o sistema calcula a similaridade entre todos os pares de livros no catálogo utilizando **Similaridade de Cossen**(ângulo entre os vetores no espaço latente), se dois ítens possuem descrições com temas e palavras-chave parecidas, seus vetores estarão próximos e o valor do cosseno será próximo de 1.
