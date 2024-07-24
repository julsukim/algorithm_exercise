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
  const result = [];

  for (const num of arr) {
    let left = 0, right = result.length;

    // 이진 탐색을 통해 num이 들어갈 위치를 찾음
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (result[mid] < num) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    // result[left]를 업데이트하거나 새로운 요소 추가
    if (left < result.length) {
      result[left] = num;
    } else {
      result.push(num);
    }
  }

  console.log(result.length);
});