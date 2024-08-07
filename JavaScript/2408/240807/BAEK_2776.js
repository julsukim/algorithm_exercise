const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  let index = 0;
  const TC = parseInt(input[index++]);

  let t = 0;
  while (t < TC) {
    const N = parseInt(input[index++]);
    const arr1 = input[index++].split(' ').map(Number);
    const M = parseInt(input[index++]);
    const arr2 = input[index++].split(' ').map(Number);

    arr1.sort((a, b) => a - b);

    const resultList = [];
    for (const target of arr2) {
      let left = 0;
      let right = N-1;
      let result = 0;

      while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (arr1[mid] === target) {
          result = 1;
          break;
        } else if (arr1[mid] > target) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }

      resultList.push(result);
    }

    t++;
    console.log(resultList.join('\n'));
  }
});