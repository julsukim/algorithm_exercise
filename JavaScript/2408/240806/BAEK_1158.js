const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N, K;

rl.on('line', (line) => {
  [N, K] = line.split(' ').map(Number);
  rl.close();
}).on('close', () => {
  
  const josephus = (n, k) => {
    const people = Array.from({ length: N }, (e, i) => ++i);
    const result = [];
    let index = 0;

    while (people.length > 0) {
      index = (index + k - 1) % people.length;
      result.push(people.splice(index, 1)[0]);
    }

    return result;
  }

  console.log(`<${josephus(N, K).join(', ')}>`);
});