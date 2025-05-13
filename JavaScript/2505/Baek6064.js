const fs = require('fs');

const input = fs
.readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input6064.txt')
.toString()
.trim()
.split('\n');

const T = parseInt(input[0], 10);
const output = [];

for (let i = 1; i <= T; i++) {
  const [M, N, x, y] = input[i].split(' ').map(Number);
  let k = x;
  let answer = -1;

  // N번 반복해도 못 찾으면 없는 것
  for (let j = 0; j < N; j++) {
    // (k mod N) === (y mod N) 인지 확인
    // JS의 음수 나머지 주의: ((k % N) + N) % N 로 정규화
    if (((k % N) + N) % N === ((y % N) + N) % N) {
      answer = k;
      break;
    }
    k += M;
  }

  output.push(answer);
}

// 결과 한 줄씩 출력
console.log(output.join('\n'));
