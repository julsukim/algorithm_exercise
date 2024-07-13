const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, D, K, C;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    [N, D, K, C] = line.split(' ').map(Number);
  } else {
    arr.push(parseInt(line));
  }
  idx++;
  if (idx === N+1) {
    rl.close();
  }
}).on('close', () => {

  let maxCount = 0;
  
  const getCountOf = (arr) => {
    const filteredSet = new Set(arr);
    const uniqueArray = [...filteredSet];

    return filteredSet.has(C) ? uniqueArray.length : uniqueArray.length+1;
  }

  if (K === N) {
    console.log([...new Set(arr)].length);
  } else {

    let extendedArr = arr.concat(arr);

    for (let s = 0; s <= N - K; s++) {
      const e = s + K;
      const count = getCountOf(extendedArr.slice(s, e));
      maxCount = Math.max(maxCount, count);
    }

    console.log(maxCount);
  }
});