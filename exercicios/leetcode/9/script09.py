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

        if numerOriginal == resultado and x>=0: print(True)
        else: print(False)

# --- Chamada do método ---
x = 10
Solution().isPalindrome(x)