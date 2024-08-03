const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else if (idx === 1) {
    M = parseInt(line);
  } else {
    arr.push(...line.split(' ').map(Number));
    rl.close();
  }
  idx++;
}).on('close', () => {
  arr.sort((a, b) => a - b);

  let result = 0;
  let left = 0;
  let right = N-1;

  while (left < right) {
    if (arr[left] + arr[right] === M) {
      result++;
      right--;
    } else if (arr[left] + arr[right] > M) {
      right--;
    } else {
      left++;
    }
  }

  console.log(result);
});