// 처음의 접근 방법
// : 3개의 문자열이 주어지므로, 2개의 문자열의 LCS를 구하고
//   도출된 LCS와 마지막 문자열의 LCS를 구하기
// -> 첫 LCS에서 같은 길이의 여러 LCS가 도출될 수 있다
//    따라서 두번째 LCS에서 구한 LCS의 길이가 최장이지 않을 수 있음
// 정답 접근방법
// : 3차원 dp 테이블을 통해서 3개 문자열의 LCS를 구한다.

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let str1, str2, str3;
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    str1 = line.split('');
  } else if (idx === 1) {
    str2 = line.split('');
  } else {
    str3 = line.split('');
    rl.close();
  }
  idx++;
}).on('close', () => {
  const len1 = str1.length;
  const len2 = str2.length;
  const len3 = str3.length;

  const dp = Array.from({ length: len1 + 1 }, () =>
             Array.from({ length: len2 + 1}, () =>
             Array(len3 + 1).fill(0)));

  for (let i=1; i<len1+1; i++) {
    for (let j=1; j<len2+1; j++) {
      for (let k=1; k<len3+1; k++) {
        if (str1[i-1] === str2[j-1] && str1[i-1] === str3[k-1]) {
          dp[i][j][k] = dp[i-1][j-1][k-1] + 1;
        } else {
          dp[i][j][k] = Math.max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1]);
        }
      }
    }
  }

  console.log(dp[len1][len2][len3]);
});

// rl.on('line', (line) => {
//   if (idx === 0) {
//     str1 = line.split('');
//   } else if (idx === 1) {
//     str2 = line.split('');
//   } else {
//     str3 = line.split('');
//     rl.close();
//   }
//   idx++;
// }).on('close', () => {
//   const len1 = str1.length;
//   const len2 = str2.length;
//   const len3 = str3.length;

//   const dp1 = Array.from({ length: len1 + 1 }, () => Array(len2+1).fill(''));

//   for (let i=1; i<len1+1; i++) {
//     for (let j=1; j<len2+1; j++) {
//       if (str1[i-1] === str2[j-1]) {
//         dp1[i][j] = dp1[i-1][j-1] + str1[i-1];
//       } else {
//         dp1[i][j] = dp1[i-1][j].length >= dp1[i][j-1].length ? dp1[i-1][j] : dp1[i][j-1];
//       }
//     }
//   }

//   const str4 = dp1[len1][len2];
//   const len4 = dp1[len1][len2].length;

//   const dp2 = Array.from({ length : len4 + 1 }, () => Array(len3 + 1).fill(0));

//   for (let i=1; i<len4+1; i++) {
//     for (let j=1; j<len3+1; j++) {
//       if (str4[i-1] === str3[j-1]) {
//         dp2[i][j] = dp2[i-1][j-1] + 1;
//       } else {
//         dp2[i][j] = Math.max(dp2[i-1][j], dp2[i][j-1]);
//       }
//     }
//   }

//   console.log(dp2[len4][len3]);
// });