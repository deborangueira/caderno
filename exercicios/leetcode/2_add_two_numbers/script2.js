let l1 = [2, 4, 3];
let l2 = [5, 6, 4];

var addTwoNumbers = function (l1, l2) {
  let startingindex1 = l1.length - 1;
  let startingindex2 = l2.length - 1;

  let numero1 = Number(l1.reverse().join(""));
  let numero2 = Number(l2.reverse().join(""));

  let soma = numero1 + numero2;

  let lista = soma.toString().split("").reverse().map(Number);

  console.log(lista);
};
