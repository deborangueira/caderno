## Listas []

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

## Tuplas ()

- They're immutable: Unlike lists, we can't change tulples (like using editing methods or doing new assignments to items)
- Still, we can loop through it and acess values.

## Dicionários {}

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


# References

[Dictionary](https://www.youtube.com/watch?v=daefaLgNkw0)\
[Lists and tulpes](https://www.youtube.com/watch?v=W8KRzm-HUcc)