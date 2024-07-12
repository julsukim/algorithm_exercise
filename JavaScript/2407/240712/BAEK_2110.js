const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, C;
const arr = [];
idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    [N, C] = line.split(' ').map(Number);
  } else {
    arr.push(parseInt(line));
  }
  idx++;
  if (idx === N + 1) {
    rl.close();
  }
}).on('close', () => {
  
  arr.sort((a, b) => a - b);

  let start = 1;
  let end = arr[arr.length - 1] - arr[0];

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let current = arr[0];
    let count = 1;

    for (let i=1; i<arr.length; i++) {
      if (arr[i] >= current + mid) {
        count += 1;
        current = arr[i];
      }
    }

    if (count >= C) {
      start = mid + 1;
      result = mid;
    } else {
      end = mid - 1;
    }
  }

  console.log(result)
});