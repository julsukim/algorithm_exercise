const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_9465.txt')
  .toString()
  .trim()
  .split('\n');

let idx = 0;
const TC = parseInt(input[idx++]);
const result = [];

for (let _ of Array(TC)) {
  const N = parseInt(input[idx++]);
  const sticker = [];
  sticker.push(input[idx++].split(' ').map(Number));
  sticker.push(input[idx++].split(' ').map(Number));
  
  const dp = Array.from({ length: 2 }, () => Array(N).fill(0));

  dp[0][0] = sticker[0][0];
  dp[1][0] = sticker[1][0];

  for (let i=1; i<N; i++) {
    dp[0][i] = Math.max(dp[1][i-1], dp[1][i-2] || 0) + sticker[0][i];
    dp[1][i] = Math.max(dp[0][i-1], dp[0][i-2] || 0) + sticker[1][i];
  }

  result.push(Math.max(dp[0][N-1], dp[1][N-1]));
}

console.log(result.join('\n'));