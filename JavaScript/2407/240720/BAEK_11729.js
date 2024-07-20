const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N;

// 하노이 탑 문제를 재귀적으로 해결하는 함수
function hanoi(n, from, to, via, moves) {
  if (n === 0) return;
  
  // n-1개의 원판을 'from'에서 'via'로 옮긴다 (목표: 'to')
  hanoi(n - 1, from, via, to, moves);
  
  // 가장 큰 원판(n번째 원판)을 'from'에서 'to'로 옮긴다
  moves.push([from, to]);
  
  // n-1개의 원판을 'via'에서 'to'로 옮긴다 (목표: 'from')
  hanoi(n - 1, via, to, from, moves);
}

// 하노이 탑 문제를 해결하는 함수
function solveHanoi(n) {
  const moves = [];
  
  // 총 이동 횟수 계산: 2^n - 1
  const totalMoves = Math.pow(2, n) - 1;
  console.log(totalMoves);
  
  // 재귀적 하노이 탑 이동 과정 시작
  hanoi(n, 1, 3, 2, moves);
  
  // 저장된 모든 이동을 한 번에 출력
  console.log(moves.map(move => move.join(" ")).join("\n"));
}


rl.on('line', (line) => {
  N = parseInt(line);
  rl.close();
}).on('close', () => {
  solveHanoi(N);
});