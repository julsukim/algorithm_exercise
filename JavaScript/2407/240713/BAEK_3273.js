const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, X;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else if (idx === 1) {
    arr.push(...line.split(' ').map(Number));
  } else if (idx === 2) {
    X = parseInt(line);
  }
  idx++;
  if (idx === 3) {
    rl.close();
  }
}).on('close', () => {
  arr.sort((a, b) => a - b); // Array.prototype.sort() 메서드 <기본 유니코드 포인트 -> compareFunction> , 원 배열이 정렬

  let start = 0;
  let end = N - 1;

  let count = 0;

  while (start < end) {
    let sum = arr[start] + arr[end];

    if (sum === X) {
      count++;
    }
    
    if (sum >= X) {
      end--;
    } else if (sum < X) {
      start++;
    }
  }

  console.log(count);
});