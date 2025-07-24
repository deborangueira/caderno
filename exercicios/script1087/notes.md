[**site**](https://resources.beecrowd.com/repository/UOJ_1087_en.html)

### Understanding the problem

- Each input's line is a test case with four integers that can range from 1 to 8: "X1 Y1 X2 Y2"
- X1, Y1 is where the queen starts
- X2, Y2 is where the queen wants to reach
- the output must be the smallest number of moves needed for the queen to do so.
- Note: The Queen can move in any direction: in the same **line**, in the same **column** or in any of the **diagonals**
- The end of input is indicated by a line containing four zeros, separated by spaces.

### roadmap

*get the input*
- Read string
- separate by line  
- separate the strings and identifies them by coordinates
- stops reading when reach the line with four zeros

*process information*
- compare coordinate X ([0] with [2]) and coordinate Y([1] with [3]) to see how they differ from eachother.
- if X and Y stay the same -> 0 moves are needed
- if only X or Y change -> 1 move is needed
- if both changes -> 2 moves are needed.

> possible outputs: 0,1,2

