const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N;
let members = [];
let index = 0;

rl.on('line', (line) => {
  if (index === 0) {
    N = parseInt(line);
  } else {
    members.push(line.split(' '));
  }
  index++;
  if (index > N) {
    rl.close();
  }
}).on('close', () => {
  members.sort((a, b) => {
    if (a[0] !== b[0]) {
      return a[0] - b[0];
    } else {
      return 0
    }
  });

  const result = [];

  members.forEach(e => {
    result.push(`${e[0]} ${e[1]}`);
  })

  console.log(result.join('\n'));
});