const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1783.txt')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

const [N, M] = [input[0], input[1]];

const solution = (N, M) => {
  if (N === 1) {
    return 1;
  } else if (N === 2) {
    return Math.min(Math.floor((M+1)/2), 4);
  } else {
    if (M < 7) {
      return Math.min(M, 4);
    } else {
      return M - 7 + 5;
    }
  }
};

console.log(solution(N, M));