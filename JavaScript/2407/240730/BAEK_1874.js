const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
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
  if (idx === N+1) rl.close();
}).on('close', () => {
  let current = 1;
  const stack = [];
  const result = [];
  let flag = false;

  for (const e of arr) {
    while (current <= e) {
      stack.push(current);
      result.push('+');
      current++;
    }
    if (stack[stack.length-1] === e) {
      stack.pop();
      result.push('-');
    } else {
      console.log('NO');
      flag = true;
      break;
    }
  }

  if (!flag) console.log(result.join('\n'));
});