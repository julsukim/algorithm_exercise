const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.on('line', (line) => {
  const input = line.split('');
  const L = input.length;
  const alphabets = new Map();
  for (const a of input) {
    alphabets.set(a, (alphabets.get(a) || 0) + 1);
  }
  // 전체 길이 홀수
  // 홀수가 하나만 존재해야한다.
  // 전체 길이 짝수
  // 홀수가 없어야 한다.
  let oddCnt = 0;
  let flag = false;
  const halfP = [];
  let mid = '';

  for (const [key, value] of alphabets) {
    // 홀수 번 등장
    if (value % 2 === 1) {
      oddCnt++;
      mid = key;
      if (oddCnt > 1) {
        flag = true;
        break;
      } else if (oddCnt === 1 && L % 2 === 0) {
        flag = true;
        break;
      }
      if (value > 1) {
        for (const _ of Array(Math.floor(value / 2))) {
          halfP.push(key);
        }
      }
    } else {
      for (const _ of Array(value / 2)) {
        halfP.push(key);
      }
    }
  }

  halfP.sort((a, b) => a.localeCompare(b));
  console.log(flag ? "I'm Sorry Hansoo" : halfP.join('') + mid + [...halfP].sort((a, b) => b.localeCompare(a)).join(''));
  rl.close();
});