const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1475.txt')
  .toString()
  .trim()
  .split('\n');

const arr = input[0].split('').map(Number);

const numbers = new Map();
const numberSet = Array(10).fill(0); 
for (const num of arr) {
  numberSet[num] += 1;
}
let setElse = 0;
numberSet.forEach((e, i) => {
  if (i !== 6 && i !== 9) {
    setElse = Math.max(setElse, e)
  }
})
let set69 = numberSet[6] + numberSet[9];
set69 = Math.ceil(set69 / 2);

console.log(Math.max(setElse, set69));