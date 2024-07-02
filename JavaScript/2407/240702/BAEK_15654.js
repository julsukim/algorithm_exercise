const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const recur = (number, output, usedSet) => {
  if (number === M) {
    result.push(output.join(' '));
    return;
  }
  for (const e of arr) {
    if (!usedSet.has(e)) {
      output.push(e);
      usedSet.add(e);
      recur(number + 1, output, usedSet);
      output.pop();
      usedSet.delete(e);
    }
  }
}

let N, M;
let arr;
const result = [];
let index = 0;

rl.on('line', (line) => {
  if (index === 0) {
    [N, M] = line.split(' ').map(Number);
  } else {
    arr = Array.from(line.split(' ').map(Number));
  }
  index++;
  if (index > 1) {
    rl.close();
  }
}).on('close', () => {
  arr.sort((a, b) => a - b);
  recur(0, [], new Set());
  console.log(result.join('\n'));
});