const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (line) => {
  const input = line.split('');
  const L = input.length;
  let result = true;
  
  for (let i=0; i<Math.floor(L/2); i++) {
    if (input[i] !== input[L-i-1]) {
      result = false;
    }
  }
  console.log(result);
  rl.close();
});