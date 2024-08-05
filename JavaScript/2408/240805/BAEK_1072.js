const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let X, Y;

rl.on('line', (line) => {
  [X, Y] = line.split(' ').map(Number);
  rl.close();
}).on('close', () => {
  let Z = Math.floor(Y*100/X);

  // console.log(29*100/50);
  // console.log(Math.floor(29/50*100));
  
  let cnt = Infinity;

  let left = 0;
  let right = X;

  while (left <= right) {
    let addition = Math.floor((left+right)/2);

    if (Math.floor((Y+addition)*100/(X+addition)) > Z) {
      cnt = Math.min(cnt, addition);
      right = addition - 1;
    } else {
      left = addition + 1;
    }
  }

  cnt === Infinity ? console.log(-1) : console.log(cnt);
});