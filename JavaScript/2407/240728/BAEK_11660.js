const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M;
let arr = [];
let idx = 0;
let prefixSum = [];
const queries = [];

const makePrefixSum = (matrix) => {
  const prefixSum = Array.from({ length: N+1 }, () => Array(N+1).fill(0));

  for (let i=1; i<N+1; i++) {
    for (let j=1; j<N+1; j++) {
      prefixSum[i][j] =
        matrix[i - 1][j - 1] +
        prefixSum[i - 1][j] +
        prefixSum[i][j - 1] -
        prefixSum[i - 1][j - 1];
    }
  }

  return prefixSum;
}

const getPrefixSum = (prefixSum, i, j, k, l) => {
  return (
    prefixSum[k + 1][l + 1] -
    prefixSum[i][l + 1] -
    prefixSum[k + 1][j] +
    prefixSum[i][j]
  );
}

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else if (idx < N+1) {
    arr.push(line.split(' ').map(Number));
  } else if (idx === N+1) {
    prefixSum = makePrefixSum(arr);
    queries.push(line.split(' ').map(Number));
  } else {
    queries.push(line.split(' ').map(Number));
  }
  idx++;
  if (idx >= N+M+1) {
    rl.close();
  }
}).on('close', () => {
  const result = [];
  for (let [i, j, k, l] of queries) {
    let sum = getPrefixSum(prefixSum, i-1, j-1, k-1, l-1);
    result.push(sum);
  }
  console.log(result.join('\n'));
});