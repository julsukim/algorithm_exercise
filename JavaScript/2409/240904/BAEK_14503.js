const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_14503.txt')
  .toString()
  .trim()
  .split('\n');

const [N, M] = input[0].split(' ').map(Number);
const [r, c, d] = input[1].split(' ').map(Number);
const room = [];
for (let i = 2; i < N + 2; i++) {
  room.push(input[i].split(' ').map(Number));
}

// 방향 설정: 0: 북, 1: 동, 2: 남, 3: 서
const delta = [
  [-1, 0], // 북
  [0, 1],  // 동
  [1, 0],  // 남
  [0, -1]  // 서
];

const backDelta = [
  [1, 0],  // 북 -> 남으로 후진
  [0, -1], // 동 -> 서로 후진
  [-1, 0], // 남 -> 북으로 후진
  [0, 1]   // 서 -> 동으로 후진
];

const cleaned = Array.from({ length: N }, () => Array(M).fill(false));

// 현재 위치를 청소
const cleaning = (i, j, room, cleaned) => {
  if (room[i][j] !== 1 && !cleaned[i][j]) {
    cleaned[i][j] = true;
    return true;
  }
  return false;
}

// 주변에 청소할 곳이 있는지 확인
const lookAround = (i, j, room, cleaned) => {
  for (let k = 0; k < 4; k++) {
    const [di, dj] = delta[k];
    const ni = i + di;
    const nj = j + dj;
    if (0 <= ni && ni < N && 0 <= nj && nj < M) {
      if (!cleaned[ni][nj] && room[ni][nj] === 0) {
        return false; // 청소되지 않은 공간이 있음
      }
    }
  }
  return true; // 주변에 청소할 공간이 없음
}

// 전방에 청소할 공간이 있는지 확인
const lookForward = (i, j, dir, room, cleaned) => {
  const [di, dj] = delta[dir];
  const ni = i + di;
  const nj = j + dj;
  if (0 <= ni && ni < N && 0 <= nj && nj < M) {
    if (room[ni][nj] === 0 && !cleaned[ni][nj]) {
      return true; // 전방에 청소할 공간이 있음
    }
  }
  return false;
};

let row = r;
let col = c;
let dir = d;
let cleanCnt = 0;

while (true) {
  // 1. 현재 위치 청소
  if (cleaning(row, col, room, cleaned)) {
    cleanCnt++;
  }

  // 2. 주변에 청소할 공간이 있는지 확인
  if (!lookAround(row, col, room, cleaned)) {
    let rotated = 0;
    while (rotated < 4) {
      // 왼쪽으로 회전
      dir = (dir + 3) % 4;
      
      // 앞쪽에 청소할 공간이 있으면 전진
      if (lookForward(row, col, dir, room, cleaned)) {
        const [di, dj] = delta[dir];
        row += di;
        col += dj;
        break;
      }
      rotated++;
    }

    // 네 방향 모두 청소할 공간이 없을 경우 후진
    if (rotated === 4) {
      const [di, dj] = backDelta[dir];
      const ni = row + di;
      const nj = col + dj;

      // 후진할 공간이 벽일 경우 종료
      if (room[ni][nj] === 1) {
        break;
      }

      // 후진
      row = ni;
      col = nj;
    }
  } else {
    // 후진할 공간이 없으면 종료
    const [di, dj] = backDelta[dir];
    const ni = row + di;
    const nj = col + dj;
    if (room[ni][nj] === 1) {
      break;
    }
    row = ni;
    col = nj;
  }
}

console.log(cleanCnt);
