let nums = [1,2,3,4]

let result = [nums[0]];

for (i = 1; i < nums.length; i++) {
    let soma = nums[i] + result[i-1]
    result.push(soma);
}

console.log(result)