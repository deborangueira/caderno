# 🧭 Plano de Estudo — Overview de C++ em 4 Dias

## 🎯 Objetivo Geral
Construir uma visão clara e prática dos fundamentos de C++, com noções de estrutura, controle e funções.

---

## 🩵 Dia 1 — Estrutura e Organização do Código
**Tópicos:**
- File organization  
- Statements  

**Abordagem:**
1. 🗺️ **Mapa mental guiado:**  
   - Entenda como os arquivos `.cpp` e `.h` se relacionam.  
   - Resuma em uma frase o que são *statements* (instruções).  
2. 💻 **Mini-lab:**  
   - Crie um programa com `main.cpp` e um `utils.h`/`utils.cpp`.  
   - Escreva 2 ou 3 statements simples (`int x = 5;`, `std::cout << x;` etc.).  
3. 🧩 **Quiz narrado:**  
   - “O compilador precisa saber onde cada declaração está.”  
   - “Uma declaração e uma definição são a mesma coisa.” (verdadeiro ou falso?)

---

## 💚 Dia 2 — Escopo, Namespaces e Tipos
**Tópicos:**
- Scope and namespaces  
- Type  

**Abordagem:**
1. 🗺️ Faça um diagrama mostrando os níveis de escopo: **global → função → bloco**.  
2. 💻 Escreva exemplos de variáveis com o mesmo nome em escopos diferentes e observe o resultado.  
3. 💬 Teste conversões de tipos (implícitas e explícitas).  
4. 🧩 Reflita:  
   - “Por que o `std::` existe?”  
   - “O que acontece se eu não incluir `using namespace std;`?”

---

## 💛 Dia 3 — Lógica e Fluxo de Controle
**Tópicos:**
- Logical operators  
- Flow of control  

**Abordagem:**
1. 🗺️ Resuma o que cada operador lógico faz e o que significa *short-circuit evaluation*.  
2. 💻 Teste blocos `if`, `switch`, `while`, `for` e `do while`.  
3. 🧩 Explique o trecho abaixo para si mesma:
   ```cpp
   for (int i = 0; i < 5; ++i) {
       if (i == 2) continue;
       if (i == 4) break;
       std::cout << i << " ";
   }
4. 🎯 (Opcional) Desenhe o fluxo de execução com setas.

---

## 💛 Dia 4 — Funções e Bibliotecas
**Tópicos:**
- Functions
- Strings & characters
- Memory
- Math

**Abordagem:**
1. 🗺️ Liste os 3 modos de passagem de parâmetro e defina o que é recursão.
2. 💻 Escreva:
    - uma função recursiva (factorial);
    - uma que recebe std::string;
    - um exemplo de new e delete;
    - uma função que usa sqrt() e pow().
3. 🧩 Reflita:
    - “Por que new é perigoso se esquecido o delete?”
    - “O que é mais rápido: x * x ou pow(x, 2)?”
    - 💬 Finalize o dia com 5 frases sobre o que mais te chamou atenção.