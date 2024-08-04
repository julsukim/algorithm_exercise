const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [N, M] = input[0].split(' ').map(Number);
  const arr = input[1].split(' ').map(Number);

  let min = Math.max(...arr);
  let max = arr.reduce((acc, cur) => acc + cur, 0);
  let result = Infinity;

  while (min <= max) {
    let mid = Math.floor((max + min) / 2);

    // 검사
    let tmp = 0;
    let cnt = 1;
    for (const e of arr) {
      if (tmp + e <= mid) {
        tmp += e;
      } else {
        cnt++;
        tmp = e;
      }
    }

    if (cnt <= M) {
      result = Math.min(result, mid);
      max = mid - 1;
    } else {
      min = mid + 1;
    }
  }

  console.log(result);
});