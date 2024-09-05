const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_7682.txt')
  .toString()
  .trim()
  .split('\n');

const result = [];

const checkWinner = (board, player) => {
  // 가로 검사
  for (let i = 0; i < 9; i += 3) {
    if (board[i] === player && board[i + 1] === player && board[i + 2] === player) {
      return true;
    }
  }
  // 세로 검사
  for (let i = 0; i < 3; i++) {
    if (board[i] === player && board[i + 3] === player && board[i + 6] === player) {
      return true;
    }
  }
  // 대각선 검사
  if ((board[0] === player && board[4] === player && board[8] === player) ||
      (board[2] === player && board[4] === player && board[6] === player)) {
    return true;
  }
  
  return false;
}

for (const tc of input) {
  if (tc === 'end') break;

  const board = tc.split('');
  let xCount = 0, oCount = 0;
  
  // X와 O의 개수 세기
  for (const ch of board) {
    if (ch === 'X') xCount++;
    if (ch === 'O') oCount++;
  }

  // 기본적인 X와 O의 개수 규칙 검사
  if (xCount < oCount || xCount > oCount + 1) {
    result.push('invalid');
    continue;
  }

  const xWin = checkWinner(board, 'X');
  const oWin = checkWinner(board, 'O');

  // 승리 조건 체크
  if (xWin && oWin) {
    // 동시에 둘 다 승리할 수는 없다.
    result.push('invalid');
  } else if (xWin) {
    // X가 이겼다면 X는 O보다 1개 더 많아야 한다.
    if (xCount === oCount + 1) {
      result.push('valid');
    } else {
      result.push('invalid');
    }
  } else if (oWin) {
    // O가 이겼다면 X와 O의 개수는 같아야 한다.
    if (xCount === oCount) {
      result.push('valid');
    } else {
      result.push('invalid');
    }
  } else {
    // 승자가 없을 경우 빈 칸이 남아있는지 확인
    if (xCount + oCount === 9) {
      result.push('valid');
    } else {
      result.push('invalid');
    }
  }
}

console.log(result.join('\n'));
