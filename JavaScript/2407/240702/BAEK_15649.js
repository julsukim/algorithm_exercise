const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N, M;
const result = [];

function recur(number, output) {
  if (number === M) {
    result.push(Array.from(output).join(' '));
    return;
  }

  for (let i=1; i<(N+1); i++) {
    if (!output.has(i)) {
      output.add(i);
      recur(number+1, output);
      output.delete(i);
    }
  }
}

rl.on('line', (line) => {
  [N, M] = line.split(' ').map(Number);
  rl.close();
}).on('close', () => {
  recur(0, new Set());
  console.log(result.join('\n'));
});


// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// function recur(number, output, usedSet) {
//   if (number === M) {
//     result.push(output.join(' '));
//     return;
//   }

//   for (let i=1; i<(N+1); i++) {
//     if (!usedSet.has(i)) {
//       output.push(i);
//       usedSet.add(i);
//       recur(number+1, output, usedSet);
//       output.pop();
//       usedSet.delete(i);
//     }
//   }
// }

// let N, M;
// const result = [];

// rl.on('line', (line) => {
//   [N, M] = line.split(' ').map(Number);
//   rl.close();
// }).on('close', () => {
//   recur(0, [], new Set());
//   console.log(result.join('\n'));
// });
