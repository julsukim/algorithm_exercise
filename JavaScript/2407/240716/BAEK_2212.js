const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, K;
const arr = [];
let idx = 0;

rl.on('line', (line) => {

  if (idx === 0) {
    N = parseInt(line);
  } else if (idx === 1) {
    K = parseInt(line);
  } else {
    arr.push(...line.split(' ').map(Number));
    rl.close();
  }

  idx++;

}).on('close', () => {
  arr.sort((a, b) => a - b);
  // 3, 6, 7, 8, 10, 12, 14, 15, 18, 20
  //  3, 1, 1, 2, 2, 2, 1, 3, 2
  //  3, 3, 2, 2, 2, 2, 1, 1, 1
  //  0, 0, 0, 0, 2, 2, 1, 1, 1
  //  7
  const diff = [];
  for (let i = 1; i < N; i++) {
    diff.push(arr[i] - arr[i - 1]);
  }
  diff.sort((a, b) => b - a);
  console.log(diff.slice(K-1).reduce((acc, cur) => acc + cur, 0));
});