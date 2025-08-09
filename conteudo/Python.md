## Listas

```Python
courses = ['Design', 'Computação', 'Matemática', 'Liderança', 'Negócios']
electives = ['Photography', 'IA']
```

```Python
print(couses) # output: ['Design', 'Computação', 'Matemática', 'Liderança', 'Negócios']
print(len(courses)) # output: 5

print(courses[0]) # output: Design
print(courses[-1]) # output: Negócios
print(couses[2:]) # ['Matemática', 'Liderança', 'Negócios'] // índice do lado da esquerda é inclusivo
print(couses[:2]) # ['Design', 'Computação'] // índice do lado da direita é exclusivo
```

```Python
courses.append('Arte') # adiciona no fim
courses.insert(0, 'Filosofia') # adiciona em um índice em específico
courses.extend(electives) # adiciona uma lista onde cada dado se torna um elemento do primeiro array

print(courses) # output: ['Filosofia', 'Design', 'Computação', 'Matemática', 'Liderança', 'Negócios', 'Arte', 'Photography', 'IA']
```

## Tuplas

## Dicionários