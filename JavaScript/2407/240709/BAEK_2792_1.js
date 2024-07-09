const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N, M;
let idx = 0;
const arr = [];

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else {
    arr.push(parseInt(line));
  }
  idx++;
  if (idx === M+1) {
    rl.close();
  }
}).on('close', () => {
  let start = 1;
  let end = Math.max(...arr);

  const canDistribute = (maxJealousy) => {
    let requiredStudents = 0;
    for (const jewel of arr) {
      requiredStudents += Math.ceil(jewel / maxJealousy);
    }
    return requiredStudents <= N;
  };

  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    if (canDistribute(mid)) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  console.log(start);
});
