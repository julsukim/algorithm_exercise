const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1748.txt')
  .toString()
  .trim()
  .split('\n');

const currentLength = input[0].split('').length;
const number = parseInt(input[0]);
let result = 0;
for (let l=1; l<currentLength; l++) {
  result += (9 * (10 ** (l-1))) * l; 
}
result += (number - (10 ** (currentLength-1)) + 1) * currentLength;
console.log(result);

// 83425라고 할 때, (현재의 자리수는 5)
// 자리수1 9개,
// 자리수2 90개,
// 자리수3 900개,
// 자리수4 9000개,
// 자리수5는 10000부터 83425까지
// 자리수 조사 -> 이전 자리수까지 더하기