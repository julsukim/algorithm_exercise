const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input_2258.txt')
  .toString()
  .trim()
  .split('\n');

let idx = 0;
const [N, M] = input[idx++].split(' ').map(Number);
const arr = [];
for (let i=0; i<N; i++) {
  arr.push(input[idx++].split(' ').map(Number));
}

arr.sort((a, b) => {
  if (a[1] === b[1]) {
    return b[0] - a[0];
  } else {
    return a[1] - b[1];
  }
});

let answer = Infinity;
let totalWeight = 0;
let same = 0;
let flag = false;

for (let i=0; i<N; i++) {
  totalWeight += arr[i][0];
  if (i >= 1 && arr[i][1] === arr[i-1][1]) {
    same += arr[i][1];
  } else {
    same = 0;
  }
  if (totalWeight >= M) {
    answer = Math.min(answer, arr[i][1] + same);
    flag = true;
  }
}

console.log(flag ? answer : -1);