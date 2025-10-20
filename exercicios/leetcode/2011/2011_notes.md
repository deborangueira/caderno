# Understanding

### Details

- Initialize X at zero
- Operations is a **list** with **strings**
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

# Related content

- List 
- Loop
- Conditional
- Math operations