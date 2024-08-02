const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M;
const arr1 = [];
const arr2 = [];
let idx = 0;

function countCards(N, cardNumbers, M, queryNumbers) {
  // 카드 숫자 빈도를 저장할 해시 맵 생성
  const cardCountMap = new Map();

  // 카드 숫자 빈도를 계산
  for (let i = 0; i < N; i++) {
      const number = cardNumbers[i];
      if (cardCountMap.has(number)) {
          cardCountMap.set(number, cardCountMap.get(number) + 1);
      } else {
          cardCountMap.set(number, 1);
      }
  }

  // 쿼리 숫자에 대해 카드 빈도를 조회하여 결과 배열 생성
  const result = [];
  for (let i = 0; i < M; i++) {
      const number = queryNumbers[i];
      if (cardCountMap.has(number)) {
          result.push(cardCountMap.get(number));
      } else {
          result.push(0);
      }
  }

  // 결과를 공백으로 구분된 문자열로 출력
  console.log(result.join(' '));
}

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else if (idx === 1) {
    arr1.push(...line.split(' ').map(Number));
  } else if (idx === 2) {
    M = parseInt(line);
  } else {
    arr2.push(...line.split(' ').map(Number));
    rl.close();
  }
  idx++;
}).on('close', () => {
  countCards(N, arr1, M, arr2);
});