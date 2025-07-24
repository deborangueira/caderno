var input = require("fs").readFileSync("exercicios/stdin", "utf8");
var lines = input.split('\n');

function compare(a, b, c, d) {

  if (a === c && b === d) { // se nenhuma coordenada mudar
    return 0; // nenhum movimento é necessário
  } else if (a !== c && b === d || a === c && b !== d ) { // se apenas uma coordenada mudar (respectivamente x, ou y)
    return 1; // um movimento na horizontal ou vertical é necessário
  } else if (Math.abs(c - a) === Math.abs(d - b)) { // condição para se formar um triângulo retângulo onde os catetos são iguais fazendo com que seja possível ir na diagonal -> utilizei módulo para a operação com o Math.abs()
    return 1; // um movimento na diagonal é necessário
  } else { // para todo o restante dos casos, serão necessários dois movimentos **no mínimo**
    return 2;
  }
}

for (i = 0; i < lines.length; i++) {

  let testCase = lines[i].split(" ").map(Number);

  if (testCase.every(n => n === 0)) break; // condição de parada: o CONTEÚDO da string ser "0 0 0 0"

  let X1 = testCase[0];
  let Y1 = testCase[1];
  let X2 = testCase[2];
  let Y2 = testCase[3];

  let totalMoves = compare(X1, Y1, X2, Y2);

  console.log(totalMoves);

}




