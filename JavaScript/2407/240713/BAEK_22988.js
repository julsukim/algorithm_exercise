const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, X;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    [N, X] = line.split(' ').map(Number);
  } else {
    arr.push(...line.split(' ').map(Number));
  }
  idx++;
  if (idx === 2) {
    rl.close();
  }
}).on('close', () => {
  arr.sort((a, b) => a - b);

  let s = 0;
  let e = N-1;

  let remain = 0;
  let count = 0;

  while (s <= e) {
    if (arr[e] === X) {
      count += 1;
      e -= 1;
      continue;
    }

    if (s === e) {
      remain += 1;
      break;
    }

    if ((arr[s] + arr[e]) >= (X / 2)) {
      count += 1;
      s += 1;
      e -= 1;
    } else {
      s += 1;
      remain += 1;
    }
  }

  console.log(count + Math.floor(remain / 3));
});