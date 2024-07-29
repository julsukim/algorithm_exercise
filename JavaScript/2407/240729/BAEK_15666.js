const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M;
const arr = [];
let idx = 0;
const resultSet = new Set();

const solution = (idx, len, tmp) => {
  if (len === M) {
    resultSet.add(tmp.join(' '));
    return;
  }

  for (let i=idx; i<arr.length; i++) {
    tmp.push(arr[i]);
    solution(i, len+1, tmp);
    tmp.pop();
  }
}

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else {
    const inputSet = new Set(line.split(' ').map(Number));
    arr.push(...Array.from(inputSet));
    rl.close();
  }
  idx++;
}).on('close', () => {
  arr.sort((a, b) => a - b);
  solution(0, 0, []);

  console.log(Array.from(resultSet).join('\n'));
});