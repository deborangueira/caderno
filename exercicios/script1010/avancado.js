var input =  require('fs').readFileSync('exercicios/stdin','utf8');

var lines = input.trim().split(/\r?\n/); // transformo em um array onde cada string contem os dados de um produto e limpo essa string (remove strings vazias e com \r)

var product = {} // objeto para armazenar dados dos produtos identificados por com chaves dinâmicas
var total = 0

for(let i=0; i <lines.length; i++) { // acesso uma linha por vez do array lines
    let parts = lines[i].split(' ');
    let code = parts[0];
    let quantity = Number(parts[1]);
    let price = Number(parts[2]);
    product[code] = {quantidade: quantity, valorUnitario: price}; // guardo esses dados dentro do objeto produto e separo-os com base no código de cada produto.
}

for (let code in product) { // loop para percorrer as chaves de um objeto
    let quantity = product[code].quantidade;
    let price = product[code].valorUnitario;
    total += (quantity*price);
}

console.log(`VALOR A PAGAR: R$ ${total.toFixed(2)}`);
