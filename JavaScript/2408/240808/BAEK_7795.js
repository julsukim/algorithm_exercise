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
    const [N, M] = input[index++].split(' ').map(Number);
    const arr1 = input[index++].split(' ').map(Number);
    const arr2 = input[index++].split(' ').map(Number);

    let result = 0;
    arr2.sort((a, b) => a - b);

    for (const target of arr1) {
      let left = 0;
      let right = M-1;
      let tmp = 0;
      
      while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (arr2[mid] < target) {
          left = mid + 1;
          tmp = Math.max(tmp, mid);
        } else {
          right = mid - 1;
        }
      }
      result += tmp;
    }

    console.log(result);
    t++;
  }
});