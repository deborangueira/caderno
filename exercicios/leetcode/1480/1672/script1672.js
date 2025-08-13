accounts = [
  [1, 5],
  [7, 3],
  [3, 5],
];

var wealth = 0;
var list = [];

for (i = 0; i < accounts.length; i++) {
  let client = accounts[i];

  for (i = 0; i < client.length; i++) {
    wealth += client[i];
    list.push(wealth)
  }
}

console.log(list)