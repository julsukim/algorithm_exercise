const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N;
const nodes = [];
let index = 0;

rl.on('line', (line) => {
  if (index === 0) {
    N = parseInt(line);
  } else {
    nodes.push(line.split(' ').map(Number));
  }
  index++;
  if (index > N) {
    rl.close();
  }
}).on('close', () => {
  nodes.sort((a, b) => {
    if (a[0] !== b[0]) {
      return a[0] - b[0]
    } else {
      return a[1] - b[1]
    }
  });
  const result = [];
  nodes.forEach(e => {
    console.log(`${e[0]} ${e[1]}`);
  });
  // console.log(result.join('\n'));
});
