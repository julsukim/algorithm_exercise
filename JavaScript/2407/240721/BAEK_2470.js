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
    arr.push(...line.split(' ').map(Number));
    rl.close();
  }
  idx++;
}).on('close', () => {
  arr.sort((a, b) => a - b);

  let left = 0;
  let right = N-1;

  let closeSum = Infinity;
  let closePair = [arr[left], arr[right]];

  while (left < right) {
    let currentSum = arr[left] + arr[right];

    if (Math.abs(currentSum) < Math.abs(closeSum)) {
      closeSum = currentSum;
      closePair = [arr[left], arr[right]];
    }

    if (currentSum > 0) {
      right -= 1;
    } else if (currentSum < 0) {
      left += 1;
    } else {
      break;
    }
  }

  closePair.sort((a, b) => a - b);
  console.log(closePair.join(' '));
});