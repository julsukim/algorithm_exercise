const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else {
    arr.push(line.split(' ').map(Number));
  }
  idx++;
  if (idx === N+1) {
    rl.close();
  }
}).on('close', () => {
  arr.push(arr[0]);
  let xS = 0;
  let yS = 0;
  for (let i=0; i<N; i++) {
    xS += arr[i][0] * arr[i+1][1];
    yS += arr[i][1] * arr[i+1][0];
  }
  const result = Math.abs((xS - yS))/2;
  console.log(result.toFixed(1));
});