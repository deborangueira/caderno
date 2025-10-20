# Comparativo entre Python e JavaScript

## Operadores lógicos

**Python**
```python
if a and b:
    # executa se ambos forem verdadeiros
if a or b:
    # executa se algum for verdadeiro
if not a:
    # executa se “a” for falso
```

**JavaScript**

```Javascript
if (a && b) {
    // executa se ambos forem verdadeiros
}
if (a || b) {
    // executa se algum for verdadeiro
}
if (!a) {
    // executa se “a” for falso
}
```

## Comparadores

**Python**
```python
if a == b:
    # valor igual
if a != b:
    # valor diferente
if a < b and b <= c:
    # comparações compostas
if a is b:
    # identidade (mesmo objeto)

```

**JavaScript**

```Javascript
if (a === b) {
    // valor e tipo iguais
}
if (a !== b) {
    // não iguais em valor ou tipo
}
if (a < b && b <= c) {
    // comparações compostas
}

```

## if – elif – else

**Python**
```python
if condicao1:
    # bloco 1
elif condicao2:
    # bloco 2
else:
    # bloco final

``` 

**JavaScript**

```Javascript
if (condicao1) {
    // bloco 1
} else if (condicao2) {
    // bloco 2
} else {
    // bloco final
}
```

## Loops

**Python**
```python

# Contagem
for i in range(0, 5):
    print(i)

# Coleção
for item in lista:
    print(item)

# Chaves/índices
for idx, item in enumerate(lista):
    print(idx, item)

```


**JavaScript**

```Javascript

// Contagem

for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Coleção

for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Chaves/índices

for (const key in objeto) {
    console.log(key, objeto[key]);
}


```

## while

**Python**
```python
while condicao:
    # bloco de repetição
    # usar break ou continue quando necessário

```

**JavaScript**

```Javascript
while (condicao) {
    // bloco de repetição
    // break ou continue possíveis
}

```

## Função

**Python**
```python

def minha_funcao(a, b=0):
    # bloco de código
    return a + b

```

**JavaScript**

```Javascript

function minhaFuncao(a, b = 0) {
    // bloco de código
    return a + b;
}


```

## Classe e instância (POO)

**Python**
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return f"Oi, {self.nome}!"

# instância
p = Pessoa("Ana")
print(p.falar())

```

**JavaScript**

```Javascript
class Pessoa {
    constructor(nome) {
        this.nome = nome;
    }

    falar() {
        return `Oi, ${this.nome}!`;
    }
}

// instância
const p = new Pessoa("Ana");
console.log(p.falar());

```
