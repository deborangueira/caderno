# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python []
class Solution(object):
    def isPalindrome(self, x):

        numerOriginal = x

        def inverter(x):

            palindrome = 0

            while x > 0:
                        
                digito = x % 10 
                x = x // 10 

                palindrome = palindrome*10 + digito

            return palindrome

        resultado = inverter(x)

        if numerOriginal == resultado and x>=0 or x == 0: return True
        else: return False

```