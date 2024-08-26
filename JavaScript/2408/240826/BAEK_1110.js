input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1110.txt')
  .toString()
  .trim()
  .split('\n');

const N = parseInt(input[0]);
let number = N;

let cycles = 1;

const makeNumber = (number) => {
  let num1, num10, numSum;
  if (number < 10) {
    num1 = number;
    numSum = number;
  } else {
    num10 = Math.floor(number / 10);
    num1 = number % 10;
    numSum = num10 + num1;
  }

  const newNumber = (num1 * 10) + (numSum % 10);

  return newNumber;
}

while (true) {
  number = makeNumber(number);
  if (number === N) {
    break;
  } else {
    cycles++;
  }
}

console.log(cycles);