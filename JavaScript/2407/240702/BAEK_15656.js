const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const recur = (cnt, output) => {
  if (cnt === M) {
    result.push(output.join(' '));
    return;
  }
  for (const e of arr) {
    output.push(e);
    recur(cnt + 1, output);
    output.pop();
  }
}

let N, M;
let arr;
const result = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else {
    arr = Array.from(line.split(' ').map(Number));
  }
  idx++;
  if (idx > 1) {
    rl.close();
  }
}).on('close', () => {
  arr.sort((a, b) => a - b);
  recur(0, []);
  console.log(result.join('\n'));
});