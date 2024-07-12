const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M;
let arr = [];
let prefixSum = [];
let idx = 0;

const getPrefix = (N, arr) => {
  const prefixSum = new Array(N + 1).fill(0);

  for (let i = 1; i <= N; i++) {
    prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
  }

  return prefixSum;
}

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else if (idx === 1) {
    arr = line.split(' ').map(Number);
    prefixSum = getPrefix(N, arr);
  } else {
    const [i, j] = line.split(' ').map(Number);
    console.log(prefixSum[j] - prefixSum[i - 1]);
  }

  idx++;

  if (idx > M + 1) {
    process.exit();
  }
});
