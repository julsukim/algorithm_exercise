const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N, M;
let idx = 0;
const arr = [];

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else {
    arr.push(parseInt(line));
  }
  idx++;
  if (idx === M + 1) {
    rl.close();
  }
}).on('close', () => {
  let start = 1;
  let end = Math.max(...arr);
  const total = arr.reduce((a, b) => a + b, 0);

  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    let tmp = 0
    for (const e of arr) {
      tmp += Math.ceil(e / mid);
    }

    if (tmp <= N) {
      end = mid - 1
    } else {
      start = mid + 1
    }
  }

  console.log(start);
});