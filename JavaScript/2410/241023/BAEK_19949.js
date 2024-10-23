const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_19949.txt')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

const N = input.length;
let result = 0;

const solution = (idx, score, p, pp) => {
  if (score < idx - 5) return; 
  if (idx === N) {
    if (score >= 5) {
      result++;
      return;
    }
    return;
  }

  for (let i=1; i<=5; i++) {
    if (p === pp && p === i) continue;
    if (input[idx] === i) {
      solution(idx+1, score+1, i, p);
    } else {
      solution(idx+1, score, i, p);
    }
  }
};

solution(0, 0, 0, 0);

console.log(result);