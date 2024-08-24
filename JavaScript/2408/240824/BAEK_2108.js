const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_2108.txt')
  .toString()
  .trim()
  .split('\n');

let index = 0;
const N = parseInt(input[index++]);
const arr = [];
let sum = 0;
const frequencies = new Map();
for (let i=0; i<N; i++) {
  const num = parseInt(input[index++]);
  arr.push(parseInt(num));
  sum += num;
  if (frequencies.has(num)) {
    frequencies.set(num, frequencies.get(num) + 1);
  } else {
    frequencies.set(num, 1);
  }
}
arr.sort((a, b) => a - b);

const average = Math.round(sum / N);
console.log(average === 0 ? 0 : average);

console.log(arr[Math.floor(N / 2)]);

let maxCount = Math.max(...frequencies.values());
const mostFrequentArr = [];
frequencies.forEach((v, k) => {
  if (v === maxCount) {
    mostFrequentArr.push(k);
  }
})
mostFrequentArr.sort((a, b) => a - b);
console.log(mostFrequentArr.length === 1 ? mostFrequentArr[0] : mostFrequentArr[1]);

const minimum = arr[0];
const maximum = arr[N-1];
console.log(Math.abs(maximum - minimum));