var input = require("fs").readFileSync("exercicios/stdin", "utf8");
var lines = input.split('\n');

function compare(a, b, c, d) {

  if (a === c && b === d) { 
    return 0; 
  } else if (a !== c && b === d || a === c && b !== d ) { 
    return 1; 
  } else if (Math.abs(c - a) === Math.abs(d - b)) { 
    return 1; 
  } else {
    return 2;
  }
}

for (i = 0; i < lines.length; i++) {

  let testCase = lines[i].split(" ").map(Number);

  if (testCase.every(n => n === 0)) break;

  let X1 = testCase[0];
  let Y1 = testCase[1];
  let X2 = testCase[2];
  let Y2 = testCase[3];

  let totalMoves = compare(X1, Y1, X2, Y2);

  console.log(totalMoves);

}



