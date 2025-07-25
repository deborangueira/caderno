var input = require("fs").readFileSync("exercicios/stdin", "utf8");

var lines = input.split("\n"); // no beecrowd essa linha deve ser trocada para: var lines = input.trim().split(/\r?\n/);

var product = {}
var total = 0;

for (let i = 0; i < lines.length; i++) {
  // acesso uma linha por vez do array lines

  let parts = lines[i].split(" ");

  let code = parts[0];
  let quantity = Number(parts[1]);
  let price = Number(parts[2]);

  total += quantity * price;

  product[code] = { quantidade: quantity, valorUnitario: price }; // guardo esses dados dentro do objeto produto e separo-os com base no código de cada produto.
}

console.log(`VALOR A PAGAR: R$ ${total.toFixed(2)}`);
