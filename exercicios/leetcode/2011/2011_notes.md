# Understanding

### Details

- Initialize X at zero
- Operations is a **list** of **strings**
- Increment 1 if
- Decrement 1 if 
- Return a **int**

### Logic

- For each element in the list (for ___ in ___)
- If it is equal to ... (if), sum 1 to X
- If it is equal to ... (else), subtract 1 from X
- Return X

# Code

### First try

```Python

class Solution(object):
    def finalValueAfterOperations(self, operations):

        x = 0

        for string in operations:
            if string == 'X++' or string == '++X':
                x += 1 
            if string == 'X--' or string == '--X':
                x -= 1

        return x

```

### Second try - Thinking as a performance engeneering

**Otimization: going from 4ms to 0ms**

- I noticed that there is time waste in the comparisons per string, so I need to look for a single point of difference between all 4 statements to lower the number of comparisons:

    when using string[i] I'm taking the i° element of that specific string. In this case the middle element is the same in both cases of increment: "+", and the same in the cases of decrement "-". So it would take only one condition to compare now and make the respective opperation! Lowering the need to verify multiple conditions.\

    | Conclusion -> **The central character (string[1]) always indicates whether it is an increment or decrement**

```Python

    for string in operations:
        if string[1] == "+":
            x += 1
        else:
            x -=1

```


# Related content

- List 
- Loop
- Conditional
- Math operations