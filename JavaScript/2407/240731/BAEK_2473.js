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

  let closestSum = Infinity;
  let result = [];

  mainLoop : for (let i=0; i<N-2; i++) {
    let left = i+1;
    let right = N-1;

    while (left < right) {
      let currentSum = arr[i] + arr[left] + arr[right];

      if (Math.abs(currentSum) < Math.abs(closestSum)) {
        closestSum = currentSum;
        result = [arr[i], arr[left], arr[right]];
      }

      if (currentSum < 0) {
        left++;
      } else if (currentSum > 0) {
        right--;
      } else {
        break mainLoop;
      }
    }
  }

  console.log(result.join(' '));
});