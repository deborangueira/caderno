
# Boas Práticas de Nomenclatura

> As orientações abaixo consistem em um padrão de nomeação que é importante para manter a clareza, consistência e facilidade de manutenção do código.

## 🗂️ Pastas e Arquivos

- letras minusculas
- separar com hífen (snake_case: underline)
- sem caracteres especiais
- sem espaço

## Funções e variáveis: 

- **camelcase** (a primeira palavra em minúscula e as seguintes iniciando em maiúscula)
- **funções**: iniciar com **verbo**, indicando ação (calcularTotal, buscarUsuario)
- **variáveis** com dados: nomeadar com **substantivos**, indicando conteúdo (quantidade, usuario)

- sem nomes que sejam palavras reservadas da linguagem
- sem caracteres especiais
- sem espaço ou hífem

```javascript
// Errado:
function Minha_Funcao() {}

// Certo:
function minhaFuncao() {}
```

