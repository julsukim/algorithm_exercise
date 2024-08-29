const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_20055.txt')
  .toString()
  .trim()
  .split('\n');

const [N, K] = input[0].split(' ').map(Number);
const durabilities = input[1].split(' ').map(Number);

let stage = 1;
let destroyedCnt = 0;

const robotStatus = Array(N*2).fill(0);

const moveBelt = (belt, robot) => {
  
  // 벨트 이동
  let previous = belt[0];
  let now = 0;
  for (let i=0; i<N*2; i++) {
    now = belt[i];
    belt[i] = previous;
    previous = now;
  }
  belt[0] = previous;

  // 로봇 이동
  for (let i=N-1; i>0; i--) {
    robot[i] = robot[i-1];
    // 현재 칸이 내리는 위치가 아니면
    if (i === N-1) {
      robot[i] = 0;
    }
  }
  robot[0] = 0;
}

const moveRobot = (belt, robot) => {

  for (let i=N-1; i>0; i--) {
    // 현재 칸 파악 (현재 칸으로 이동이 가능한 지)
    if (robot[i] === 0 && belt[i] > 0) {
      // 이전 칸 파악 (이동할 로봇이 존재하는 지)
      if (robot[i-1] === 1) {
        robot[i-1] = 0;
        belt[i]--;
        // 현재 칸이 내리는 위치가 아니면
        if (i !== N-1) {
          robot[i] = 1;
        }
        // 이동 후 현재 칸의 벨트 내구도 확인
        if (belt[i] === 0) {
          destroyedCnt++;
        }
      }
    }
  }
}

while (destroyedCnt < K) {
  moveBelt(durabilities, robotStatus);
  moveRobot(durabilities, robotStatus);
  if (durabilities[0] > 0) {
    robotStatus[0] = 1;
    durabilities[0]--;
    if (durabilities[0] < 1) destroyedCnt++;
  }
  if (destroyedCnt >= K) break;
  stage++;
}

console.log(stage);

// 1. 1칸씩 이동
// 2. 로봇 이동 (이동칸 내구도 확인, 로봇있는지 확인)
// 3. 올리는 위치 내구도 확인, 로봇 올리기
// 4. 내구도 0인 칸 개수 K개 이상이면 과정을 종료