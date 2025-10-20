## Function

Creating reusable code that everytime it is called the code to be run will come from the same source. Remeber that python uses significant indentation  to identify code blocks.

```Python

def greet(name) -> None: #the function receives a paremeter called name and doesn't return nothing (None)
    print(f'Hello,{name}!')

greet('Jimin')
greet ('J-hope')

def add(a,b) -> float: #the function receives two parameters and return a float
    return a+b

add(1,2)

```

## Class

- Simplify the process of creating objects, or code that has to be duplicated a lot. 
- "self" refers to the instance of the class

```Python

Class Car:

    # a initializer is used to set up an instance for the class. It means that it will be created an object with a specific caracteristics for each atribute.
    def __init__(self,colour: str, hoursepower: int) -> None:
        self.colour = colour
        self.hoursepower = hoursepower

volvo: car = Car('red', 200) # Volvo is an instance/object of the class 
print(volvo.colour)
print(volvo.horsepower)

```

**Methods**

They are functions inside a class

```Python

Class Car:

    def __init__(self,brand: str, hoursepower: int) -> None:
        self.brand = brand
        self.hoursepower = hoursepower

    def drive(self) -> None:
        print(f'{self.brand} Mis driving')

    def get_info(self) -> None: #we can add more parameters after the self, like: get_info(self, var: int)
        print(f'{self.brand} with {self.horsepower} horsepower')

volvo: car = Car('Volvo', 200)
volvo.drive()
volvo.get_info() # if we added parameters in the function, we could call this function like this: volvo.get_info(10)

bmw: Car = Car('BMW', 240)

```

##  Data Types

```Python

number: int = 10
decimal: float = 2.5
text: str = 'Hello, world' # or "Hello, world"
active: bool = False

names: list = ['Jimin', 'J-hope'] # multable and we can perform many operations
coordinates: tulple = (1.5, 2.5) # unmultable
unique: set = {1, 4, 2, 9} # can not have duplicates (everythink is unique)
data: dict = {'name': 'Jimin', 'style': 'contemporary'} # key-value


```

## Type hints (anotação de tipo)

```Python
# Sem type hint
    def finalValueAfterOperations(self, operations):

# Com type hint
    def finalValueAfterOperations(self, operations: list) -> int:

        # self: o primeiro parâmetro de um método dentro de uma classe.
        # operations: list: o argumento operations deve ser uma lista.
        # -> int: a função retorna um inteiro.(identificado por ":rtype")

```


Não muda o comportamento do código, mas serve para:
- melhorar a legibilidade,
- ajudar IDEs (como VSCode ou PyCharm) a detectar erros,
- gerar documentação automática.

## Othe topics

### Listas []

- homogeneous aggregate: we can store different data types
- Muttable: we can use edit methods to change the list and its values.

```Python
courses = ['Design', 'Computação', 'Matemática', 'Liderança', 'Negócios']
electives = ['Photography', 'IA']
nums = [3,5,4,1,7]
grade = [9, 8, 10, 9, 10]
```

**Access methods**

```Python
print(couses) # output: ['Design', 'Computação', 'Matemática', 'Liderança', 'Negócios']
print(len(courses)) # output: 5

print(courses[0]) # output: Design
print(courses[-1]) # output: Negócios
print(couses[2:]) # ['Matemática', 'Liderança', 'Negócios'] // índice do lado da esquerda é inclusivo
print(couses[:2]) # ['Design', 'Computação'] // índice do lado da direita é exclusivo
```

**Edit methods**
```Python
courses.append('Arte') # adiciona no fim
courses.insert(0, 'Filosofia') # adiciona em um índice em específico
courses.extend(electives) # adiciona uma lista onde cada dado se torna um elemento do primeiro array

print(courses) # output: ['Filosofia', 'Design', 'Computação', 'Matemática', 'Liderança', 'Negócios', 'Arte', 'Photography', 'IA']
```

**sorting lists**

```Python
couses.reverse() # reverse the list
couses.sort() # numbers in ascending order and words in alphabetical
print(courses) # output: ['Filosofia', 'Design', 'Computação', 'Matemática', 'Liderança', 'Negócios', 'Arte', 'Photography', 'IA']

print(max(nums)) # output: 7
print(min(nums)) # 1
print(sum(nums)) # 20

print(couses.index('Computação')) # output: 1
print('história' in course) # outpute: false (aquela string não está na lista course)
```

**Looping**
```Python
for course in courses: # acess each value as we're looping through. "Course" is just a key world to refer to each item in the list.
    print(course)

for index, course in enumarate (courses, start=1)
    print(index, course)

```

**Dynamic outputs**

- O uso do `f` permite executar código Python dentro de uma string, desde que esse código esteja dentro de {}

```Python

print(f'A nota de {courses[0]} foi {grade[0]}.' )

```

**Spliting values**

```Python
new_list_of_courses = ' - '.join(courses)
revert_courses_list = new_list_of_courses.split(' - ')
```

### Tuplas ()

- They're immutable: Unlike lists, we can't change tulples (like using editing methods or doing new assignments to items)
- Still, we can loop through it and acess values.

### Dictionaries {}

- Allow us to work with **Key-value pairs**
    - Key: unique identifier. It can be any unmutable data type
    - Value: our data itself

```Python

student = {
    'name' = 'Débora',
    'age' = 22,
    'courses' = ['Math', 'CompSci']
}
```

**Updating the dictionary**

```Python
student.update({'name' = 'Jimin', 'phone' = '555-5555' }) # I'm changing the value of the key name and adding a new key in the end of the dictionary
del student ['age'] # delete a key
```

**Especifying the key we wanna access:**

```Python
student['name'] # output: Débora
# or
student.get('phone') # output: None (writing with 'get' make the output come with a clear mensage insted of an huge erro msg!)
```

**Different acesses**

```Python
len(student) # output: 3
student.keys() # output: 'name', 'age', 'courses'
student.values() # output: 'debora', '22', ['Math', 'CompSci']
student.items() # output: [('name' = 'Débora'),('age' = 22),('courses' = ['Math', 'CompSci')] --> they're are given in PAIRS!

```

**Loop**

```Python
for Key, value in student.item()
    print(key, value)
```
## Loops

### for

- Used to iterate over elements of a sequence, such as lists, strings, or even dictionaries.

```Python
ingredientes = ["farinha", "açúcar", "ovos", "leite"]

for ingrediente in ingredientes:
    print(f"{ingrediente} is in the list")
```


# References

[Dictionary](https://www.youtube.com/watch?v=daefaLgNkw0)\
[Lists and tulpes](https://www.youtube.com/watch?v=W8KRzm-HUcc)\
[Important Concepts -> the perfect video](https://www.youtube.com/watch?v=Gx5qb1uHss4&list=WL&index=2&t=189shttps://www.youtube.com/watch?v=Gx5qb1uHss4&list=WL&index=2&t=189s)\
[Loop -> the perfect article!](https://www.rocketseat.com.br/blog/artigos/post/loops-python-explicados#25d1fa7d41e0433fa3ebd17ef485f5c4)