const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const recur = (hintIdx, number) => {
  if (hintIdx === N) {
    answer += 1;
    recur(0, number+1);
    return;
  }
  if (number > 999) return;

  if (checker(hintIdx, number)) {
    recur(hintIdx+1, number);
  } else {
    recur(0, number+1);
  }
}

const checker = (hintIdx, number) => {
  strNum = String(number);

  if (strNum.includes('0')) {
    return false;
  }

  const numSet = new Set();
  for (const char of strNum) {
    if (numSet.has(char)) {
      return false;
    } else {
      numSet.add(char);
    }
  }

  let strikeCount = 0;
  let ballCount = 0;

  const strHint = String(hints[hintIdx][0]);

  if (strNum[0] === strHint[0]) {
    strikeCount += 1;
  } else if (strNum[0] === strHint[1] || strNum[0] === strHint[2]) {
    ballCount += 1;
  }
  if (strNum[1] === strHint[1]) {
    strikeCount += 1;
  } else if (strNum[1] === strHint[0] || strNum[1] === strHint[2]) {
    ballCount += 1;
  }
  if (strNum[2] === strHint[2]) {
    strikeCount += 1;
  } else if (strNum[2] === strHint[0] || strNum[2] === strHint[1]) {
    ballCount += 1;
  }

  if (strikeCount === hints[hintIdx][1] && ballCount === hints[hintIdx][2]) {
    return true;
  } else {
    return false;
  }
}

let N;
const hints = [];
let idx = 0;
let answer = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else {
    hints.push(line.split(' ').map(Number));
  }
  idx++;
  if (idx > N) {
    rl.close();
  }
}).on('close', () => {
  recur(0, 100);
  console.log(answer);
});