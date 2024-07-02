const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function recur(number, output, result) {
  if (number === M) {
    result.push(output.join(' '));
    return;
  }

  for (let i=1; i<N+1; i++) {
    output.push(i);
    recur(number + 1, output, result);
    output.pop();
  }

}

let N, M;

rl.on('line', (line) => {
  [N, M] = line.split(' ').map(Number);
  rl.close();
}).on('close', () => {
  const result = [];
  recur(0, [], result);
  console.log(result.join('\n'));
});
