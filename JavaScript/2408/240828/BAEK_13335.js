const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_13335.txt')
  .toString()
  .trim()
  .split('\n');

const [N, W, L] = input[0].split(' ').map(Number);
const trucks = input[1].split(' ').map(Number);

let time = 1;
let nextIndex = 1;
const bridgeQueue = Array(W).fill(0);
bridgeQueue[W-1] = trucks[0];

const move = (arr, W) => {
  const tmp = arr[0];
  arr[0] = 0;
  if (W > 1) {
    for (let i=1; i<W; i++) {
      arr[i-1] = arr[i];
    }
  }
  arr[W-1] = 0;
  return tmp;
}

while (nextIndex < N) {
  time++;
  const escape = move(bridgeQueue, W);
  const currentWeight = bridgeQueue.reduce((acc, cur) => acc + cur, 0);
  if (currentWeight + trucks[nextIndex] <= L) {
    bridgeQueue[W-1] = trucks[nextIndex];
    nextIndex++;
  }
}

console.log(time+W);

// 큐에 하나를 넣은 상태로 시작
// 시간이 흐르고 움직이기
// 트럭을 빼줄수있으면 빼주고 없으면 계속
// 무게를 확인하고 트럭을 더 넣을 수 있으면 넣기 (마지막), 인덱스도 증가
// 더 넣을 수 없다면 0을 삽입