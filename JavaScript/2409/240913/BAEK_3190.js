const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_3190.txt')
  .toString()
  .trim()
  .split('\n');

let idx = 0;
const N = parseInt(input[idx++]);
const K = parseInt(input[idx++]);

// 보드 초기화 (0: 빈칸, 1: 사과, 2: 뱀)
const board = Array.from({ length: N }, () => Array(N).fill(0));

// 사과 위치 설정
for (const _ of Array(K)) {
  const [x, y] = input[idx++].split(' ').map(Number);
  board[x-1][y-1] = 1;
}

const L = parseInt(input[idx++]);
const moves = [];
for (const _ of Array(L)) {
  const [time, direction] = input[idx++].trim().split(' ');
  moves.push([parseInt(time), direction]);
}

// 방향 벡터 (오른쪽, 아래, 왼쪽, 위)
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];
let direction = 0; // 초기 방향: 오른쪽
let time = 0;
let x = 0, y = 0; // 뱀의 머리 위치
let snake = [[x, y]]; // 뱀의 몸통 좌표 리스트 (꼬리는 맨 앞)
board[x][y] = 2; // 뱀이 있는 위치를 2로 표시

let moveIndex = 0;

while (true) {
  time++;
  const nx = x + dx[direction];
  const ny = y + dy[direction];

  // 보드 범위 내, 몸통이 없는 위치인지 확인
  if (nx >= 0 && nx < N && ny >= 0 && ny < N && board[nx][ny] !== 2) {
    if (board[nx][ny] === 1) {
      // 사과가 있는 경우
      board[nx][ny] = 2;
      snake.push([nx, ny]);
    } else {
      // 사과가 없는 경우
      board[nx][ny] = 2;
      snake.push([nx, ny]);
      const [tailX, tailY] = snake.shift(); // 꼬리 제거
      board[tailX][tailY] = 0; // 꼬리가 있던 자리 비우기
    }
  } else {
    // 벽이나 뱀의 몸통과 부딪힌 경우
    break;
  }

  x = nx;
  y = ny;

  // 방향 전환 시간이 되었는지 확인
  if (moveIndex < moves.length && time === moves[moveIndex][0]) {
    const turn = moves[moveIndex][1];
    if (turn === 'D') {
      // 오른쪽으로 90도 회전
      direction = (direction + 1) % 4;
    } else {
      // 왼쪽으로 90도 회전
      direction = (direction + 3) % 4;
    }
    moveIndex++;
  }
}

console.log(time);