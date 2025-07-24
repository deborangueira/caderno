### Understanding the problem | [**link**](https://resources.beecrowd.com/repository/UOJ_1087_en.html)


- Each input's line is a test case with four integers that can range from 1 to 8: "X1 Y1 X2 Y2", where:
    - X1, Y1 is where the queen starts
    - X2, Y2 is where she wants to reach
- the output must be the smallest number of moves needed for the queen to do so.
    - Note: The Queen can move in any direction: in the same **line**, in the same **column** or in any of the **diagonals**
- The end of input is indicated by a line containing four zeros

### Notes of experience

The stopping condition was the biggest challenge for me because I initially assumed the line "0 0 0 0" would always be last. So I wrote `for (i = 0; i < lines.length - 1; i++)`, but Beecrowd didn’t accepted it and, later on, this led me to use a `break` statement instead.

I did it because I understood that the first method I used only checks the number of lines, and that's a problem. Simply put, if it happens to appear extra lines with any kind of content (such as white spaces, numbers or text), they would be considered and that would lead to wrong outputs. Using a dynamic stop with `break` instead, lets the program check the actual content and stop **exactly** when the zero line appears. 

This made me realize that we can’t rely on our own assumptions when coding, but instead **we should define precise criterias in everything possible**. By doing so, I could create a code that handled unexpected input variations correctly while avoiding the subtle error caused by guessing the input length.

### roadmap

*to get the input*
- Read string
    - separate it by `\n` creating a array  
        - separate each given string by `" "` creating a new array with four strings
        - turn them into numbers
        - Identify them by the coordinate each one represents
        - process logic
    - Process function for each one of them -> `for(i =...){}`
        - stops loop when the line with four zeros is reached -> `if(){break;}`
- print output

*process information*
- compare coordinate X (testCase[0] with testCase[2]) and coordinate Y(testCase[1] with testCase[3]) to see how they differ from eachother.
    - if X and Y stay the same -> 0 moves are needed
    - if only X or Y change -> 1 move is needed
    - if both changes and we have a right triangle -> 1 move are needed.
    - for the rest of the cases -> at least 2 moves are needed 
    
    > possible outputs: 0,1,2

### Referências

**REIS, Ricardo**. Break JavaScript. Medium, 18 mai. 2020. Disponível em: https://ricardo-reis.medium.com/break-9a71e3121803. Acesso em: 24 jul. 2025.