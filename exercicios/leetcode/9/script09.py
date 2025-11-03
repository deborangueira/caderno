class Solution(object):
    def isPalindrome(self, x):

        palindrome = 0


        if x < 0:

            x = x*(-1)

            while x > 0:
                
                digitoInvertido = x % 10 
                x = x // 10 

                palindrome = palindrome*10 + digitoInvertido

            x = x*(-1)
        else: 
            while x > 0:
                
                digitoInvertido = x % 10 
                x = x // 10 

                palindrome = palindrome*10 + digitoInvertido

            x = x*(-1)


        if x == palindrome: 
            return True
        