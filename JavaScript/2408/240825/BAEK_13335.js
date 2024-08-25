const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_13335.txt')
  .toString()
  .trim()
  .split('\n');

const [N, W, L] = input[0].split(' ').map(Number);
const weights = input[1].split(' ').map(Number);

let result = 0;
let currentWeight = 0;
while (weights.length > 0) {
  let currentIndex = 0;
  let onWeight = 0;
  let onCount = 0;
  if (onWeight + weights[currentIndex] <= L && onCount + 1 <= W) {
    onWeight += weights[currentIndex];
    onCount++;
  }

}