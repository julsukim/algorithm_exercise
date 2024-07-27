const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let T, N;
let idx = 0;
let cnt = 0;

const solution = (num, acc) => {
  if (acc >= num) {
    if (acc === num) {
      cnt++;
      return;
    }
    return;
  }

  solution(num, acc+1);
  solution(num, acc+2);
  solution(num, acc+3);
}

rl.on('line', (line) => {
  if (idx === 0) {
    T = parseInt(line);
  } else {
    cnt = 0;
    N = parseInt(line);
    solution(N, 0);
    console.log(cnt);
  }
  idx++;
  if (idx > T) {
    rl.close();
  }
});