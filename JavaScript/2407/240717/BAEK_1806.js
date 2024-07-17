const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, S;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    [N, S] = line.split(' ').map(Number);
  } else {
    arr.push(...line.split(' ').map(Number));
    rl.close();
  }

  idx++;
}).on('close', () => {

  let leng = Infinity;
  let start = 0;
  let currentSum = 0;

  for (let end = 0; end < N; end++) {
    currentSum += arr[end];

    while (currentSum >= S) {
      leng = Math.min(leng, end - start + 1);
      currentSum -= arr[start];
      start++;
    }
  }

  console.log(leng === Infinity ? 0 : leng);

});