const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const recur = (number, output, lastNum) => {
  if (number === M) {
    result.push(output.join(' '));
    return;
  }
  for (let i=lastNum; i<N+1; i++) {
    output.push(i);
    recur(number + 1, output, i);
    output.pop();
  }
}

let N, M;
const result = [];

rl.on('line', (line) => {
  [N, M] = line.split(' ').map(Number);
  rl.close();
}).on('close', () => {
  recur(0, [], 1);
  console.log(result.join('\n'));
});