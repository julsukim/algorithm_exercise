const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else {
    arr.push(...line.split(' ').map(Number));
    rl.close();
  }
  idx++;
}).on('close', () => {
  let left = 0;
  let right = 0;
  let sum = arr[0];
  let result = 0;

  while (right < N) {
    if (sum === M) {
      result++;
      sum += arr[++right];
    } else if (sum < M) {
      sum += arr[++right];
    } else {
      sum -= arr[left++];
    }
  }

  console.log(result);
});