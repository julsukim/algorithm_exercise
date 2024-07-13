const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N, D, K, C;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    [N, D, K, C] = line.split(' ').map(Number);
  } else {
    arr.push(parseInt(line));
  }
  idx++;
  if (idx === N + 1) {
    rl.close();
  }
}).on('close', () => {
  const countArr = new Array(D+1).fill(0);
  let currentCount = 0;
  let maxCount = 0;

  // 초기 윈도우의 종류 세기
  for (let i = 0; i < K; i++) {
    if (countArr[[arr[i]]] === 0) {
      currentCount++;
    }
    countArr[arr[i]]++;
  }
  // 쿠폰 미포함
  if (countArr[C] === 0) {
    currentCount++;
  }
  maxCount = currentCount;

  // 슬라이딩 윈도우
  for (let i = 0; i < N; i++) {
    // 윈도우에서 벗어남
    let removeIndex = i;
    // 윈도우에 추가 (원형 배열을 고려)
    let addIndex = (i + K) % N;

    // 벗어나는 인덱스를 삭제하는 경우 0이 되면,
    countArr[arr[removeIndex]]--;
    if (countArr[arr[removeIndex]] === 0) {
      currentCount--;
    }

    // 추가하는 인덱스가 0이라면,
    if (countArr[arr[addIndex]] === 0) {
      currentCount++;
    }
    countArr[arr[addIndex]]++;

    let currentMaxCount = currentCount;
    if (countArr[C] === 0) {
      currentMaxCount++;
    }

    maxCount = Math.max(maxCount, currentMaxCount);
  }

  console.log(maxCount);
});
