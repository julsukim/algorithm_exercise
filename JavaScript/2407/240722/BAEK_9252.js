const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let str1, str2;
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    str1 = line.split('');
  } else {
    str2 = line.split('');
    rl.close();
  }
  idx++;
}).on('close', () => {
  const len1 = str1.length;
  const len2 = str2.length;

  const dp = Array.from({ length: len1 + 1 }, () => Array(len2 + 1).fill(''));
  
  for (let i=1; i<len1+1; i++) {
    for (let j=1; j<len2+1; j++) {
      if (str1[i-1] === str2[j-1]) {
        dp[i][j] = dp[i-1][j-1] + str1[i-1];
      } else {
        dp[i][j] = dp[i-1][j].length >= dp[i][j-1].length ? dp[i-1][j] : dp[i][j-1];
      }
    }
  }

  console.log(dp[len1][len2].length);
  console.log(dp[len1][len2]);
});