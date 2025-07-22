var input = require("fs").readFileSync("exercicios/stdin", "utf8");
var lines = input.split(/\r?\n/);

var coordinate = {};

for (i = 0; i < lines.length; i++) {
  let parts = lines[i].split(" ");
  let X1 = parts[0];
  let Y1 = parts[1];
  let X2 = parts[2];
  let Y2 = parts[3];
  coordinate[i] = { X1: X1, Y1: Y1, X2: X2, Y2: Y2 };
}

function compare(a, b, c, d) {
  if (a === c && b === d) {
    return 0;
  } else if (a != c || b != d) {
    return 1;
  } else {
    return 2;
  }
}

for (let i in coordinate) {
  var x1 = coordinate[i].X1;
  var y1 = coordinate[i].Y1;
  var x2 = coordinate[i].X2;
  var y2 = coordinate[i].Y2;
  var totalMoves = compare(x1, y1, x2, y2);
  console.log(totalMoves);
}
