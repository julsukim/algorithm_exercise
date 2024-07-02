const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const recur = (cnt, output, usedNum) => {
  if (cnt === M) {
    const sortedOutput = output.slice().sort((a, b) => a - b).join(' ');
    if (!resultSet.has(sortedOutput)) {
      resultSet.add(sortedOutput);
      result.push(output.join(' '));
      return;
    }
  }
  for (const e of arr) {
    if (!usedNum.has(e)) {
      output.push(e);
      usedNum.add(e);
      recur(cnt+1, output, usedNum);
      output.pop();
      usedNum.delete(e);
    }
  }
}

let N, M;
let arr;
const result = [];
const resultSet = new Set();
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
  recur(0, [], new Set());
  console.log(result.join('\n'));
})