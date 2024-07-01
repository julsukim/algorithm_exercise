const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let index = 0;
let N, Q, K;
let installs = [];
let products = [];

rl.on('line', function (line) {
  if (index === 0) {
    [N, Q, K] = line.split(' ').map(Number);
  } else if (index === 1) {
    installs = line.split(' ').map(Number);
  } else {
    products.push(line.split(' ').map(Number));
  }
  index++;
}).on('close', function () {
  let useCounts = new Array(N).fill(0);

  for (let i = 0; i < Q; i++) {
    const start = products[i][0];
    const end = products[i][1];
    for (let j = 0; j < N; j++) {
      if (installs[j] >= start && installs[j] <= end) {
        useCounts[j]++;
      }
    }
  }

  let result = [];
  for (let i = 0; i < N; i++) {
    result.push([useCounts[i], installs[i]]);
  }

  // 정렬 함수 수정 (사용 횟수에 따라 내림차순 정렬, 사용 횟수가 같으면 설치 순서 오름차순 정렬)
  result.sort((x, y) => {
    if (x[0] !== y[0]) {
      return y[0] - x[0];
    } else {
      return x[1] - y[1];
    }
  });

  // K번째 제품의 설치 순서 출력
  console.log(result[K - 1][1]);
});

// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// let input = [];
// let index = 0;

// rl.on('line', function (line) {
//   input.push(line);
// }).on('close', function () {
//   const [N, Q, K] = input[index++].split(' ').map(Number);

//   const installs = input[index++].split(' ').map(Number);

//   let products = [];
//   for (let i = 0; i < Q; i++) {
//     products.push(input[index++].split(' ').map(Number));
//   }

//   let useCounts = new Array(N).fill(0); // 설치된 제품의 수(N)만큼 배열 초기화

//   for (let i = 0; i < Q; i++) {
//     const start = products[i][0];
//     const end = products[i][1];
//     for (let j = 0; j < N; j++) {
//       if (installs[j] >= start && installs[j] <= end) {
//         useCounts[j]++;
//       }
//     }
//   }

//   let result = [];
//   for (let i = 0; i < N; i++) {
//     result.push([useCounts[i], installs[i]]);
//   }

//   // 정렬 함수 수정
//   result.sort((x, y) => {
//     if (x[0] !== y[0]) { // 사용 횟수가 다르면
//       return y[0] - x[0]; // 내림차순 정렬
//     } else { // 사용 횟수가 같으면
//       return x[1] - y[1]; // 설치 순서에 따라 오름차순 정렬
//     }
//   });

//   // 결과 출력
//   console.log(result[K][1]);
// });