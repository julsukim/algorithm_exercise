const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let S;
rl.on('line', (line) => {
  S = line;
  rl.close();
}).on('close', () => {
  let position = 0;
  for (let N = 1; ; N++) {
    let s_N = N.toString();
    for (let c of s_N) {
      if (c === S[position]) {
        position++;
        if (position === S.length) {
          console.log(N);
          return;
        }
      }
    }
  }
});
