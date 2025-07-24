>[Question](https://resources.beecrowd.com/repository/UOJ_1087_en.html) | [My answer](https://github.com/deborangueira/caderno/blob/main/exercicios/1087/script1087.js)

### Understanding the problem 

- Each input's line is a test case with four integers that can range from 1 to 8: "X1 Y1 X2 Y2", where:
    - X1, Y1 is where the queen starts
    - X2, Y2 is where she wants to reach
- the output must be the smallest number of moves needed for the queen to do so.
    - Note: The Queen can move in any direction: in the same **line**, in the same **column** or in any of the **diagonals**
- The end of the input is indicated by a line containing four zeros



### Notes of experience

The stopping condition was the biggest challenge for me because I initially assumed that the line "0 0 0 0" would always be last one. So I wrote `for (i = 0; i < (lines.length - 1); i++)`, but Beecrowd didn’t accepted it and, later on, this led me to use a `break` statement instead.

I change this part because I understood that the first method I used only checks the number of lines, and that's a problem. Simply put, if it happens to appear extra lines with any kind of content (such as black spaces, extra numbers or text), they would be considered and that would lead to wrong outputs. Using a dynamic stop with `break` instead, lets the program check the actual content and stop **exactly** when the zero line appears. 

This made me realize that we can’t rely on our own assumptions when coding, but instead **we should define precise criterias in everything possible**. By doing so, I could create a code that handled unexpected input variations while avoiding the subtle error caused by guessing the input length.

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

*process information - the function*
- compare coordinate X (testCase[0] with testCase[2]) and coordinate Y(testCase[1] with testCase[3]) to see how they differ from each other.
    - if X and Y stay the same -> 0 moves are needed
    - if only X or Y change -> 1 move is needed
    - if both changes and we have a right triangle -> 1 move are needed.
    - for the rest of the cases -> at least 2 moves are needed 
- possible outputs: 0,1,2

  **Code**

    ```Javascript

    function compare(a, b, c, d) {

      if (a === c && b === d) { // se nenhuma coordenada mudar
        return 0; // nenhum movimento é necessário
      } else if (a !== c && b === d || a === c && b !== d ) { // se apenas uma coordenada mudar (respectivamente x, ou y)
        return 1; // um movimento na horizontal ou vertical é necessário
      } else if (Math.abs(c - a) === Math.abs(d - b)) { // se um triângulo retângulo se formar (catetos iguais)-> apliquei módulo na operação com o Math.abs()
        return 1; // um movimento na diagonal é necessário
      } else { // para todo o restante dos casos, serão necessários dois movimentos **no mínimo**
        return 2;
      }
    }
    ```

    <div align = 'center'>
    <img src = '../assets/notes1087.jpeg' style="width: 50%;">

    <sup>Notes I made when trying to figure out the logic behind the "compare" function, especially how to handle the cases when the queen does a diagonal move. Fun fact: I was in the traffic at that moment, trying hard to write as the car moved rsrs</sup>
    </div>


### Referências

**REIS, Ricardo**. Break JavaScript. Medium, 18 mai. 2020. Disponível em: https://ricardo-reis.medium.com/break-9a71e3121803. Acesso em: 24 jul. 2025.