const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_3085.txt')
  .toString()
  .trim()
  .split('\n');

const N = parseInt(input[0]);
let board = [];
for (let i=1; i<=N; i++) {
  board.push(input[i].trim().split(''));
}

// 최대 연속 부분 확인
const maxContinue = (board, N) => {
  let maxCount = 0;

  // 각 행에서 연속된 사탕 계산
  for (let i = 0; i < N; i++) {
    let count = 1;
    for (let j = 1; j < N; j++) {
      if (board[i][j] === board[i][j - 1]) {
        count++;
      } else {
        count = 1;
      }
      maxCount = Math.max(maxCount, count);
    }
  }

  // 각 열에서 연속된 사탕 계산
  for (let j = 0; j < N; j++) {
    let count = 1;
    for (let i = 1; i < N; i++) {
      if (board[i][j] === board[i - 1][j]) {
        count++;
      } else {
        count = 1;
      }
      maxCount = Math.max(maxCount, count);
    }
  }

  return maxCount;
};

let result = maxContinue(board, N);

// 바꾸면서 최대 값을 찾기 (열)
for (let i=0; i<N; i++) {
  for (let j=1; j<N; j++) {
    if (board[i][j-1] !== board[i][j]) {
      [board[i][j-1], board[i][j]] = [board[i][j], board[i][j-1]];
      result = Math.max(result, maxContinue(board, N));
    }
    [board[i][j-1], board[i][j]] = [board[i][j], board[i][j-1]];
  }
}
// 바꾸면서 최대 값을 찾기 (행)
for (let j=0; j<N; j++) {
  for (let i=1; i<N; i++) {
    if (board[i-1][j] !== board[i][j]) {
      [board[i-1][j], board[i][j]] = [board[i][j], board[i-1][j]];
      result = Math.max(result, maxContinue(board, N));
    }
    [board[i-1][j], board[i][j]] = [board[i][j], board[i-1][j]];
  }
}

console.log(result);