var input =  require('fs').readFileSync('exercicios/stdin','utf8');
var lines = input.split('\n');


var produto1 = lines.shift().split(" ");
var code1 = produto1.shift();
var amount1 = Number(produto1.shift());
var price1 = Number(produto1.shift());

var produto2 = lines.shift().split(" ");
var code2 = produto2.shift();
var amount2 = Number(produto2.shift());
var price2 = Number(produto2.shift());

var finalPrice = ((amount1 * price1)+(amount2 * price2)).toFixed(2);

console.log("VALOR A PAGAR: R$ " + finalPrice)