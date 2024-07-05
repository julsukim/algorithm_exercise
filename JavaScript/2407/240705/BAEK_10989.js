const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else {
    arr.push(parseInt(line));
  }
  idx++;
  if (idx > N) {
    rl.close();
  }
}).on('close', () => {
  arr.sort((a, b) => a-b);
  console.log(arr.join('\n'));
});
