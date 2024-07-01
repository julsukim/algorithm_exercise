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
  const people = Array.from({ length: N }, (_, i) => i + 1);
  const result = [];
  let index = 0;

  while (people.length > 0) {
    index = (index + K - 1) % people.length;
    result.push(people[index]);
    people.splice(index, 1);
  }

  console.log(`<${result.join(', ')}>`);
});

// 1 2 3 4 5 6 7
//     1     2
//   3         4
//         5
//      
// 6
//      
//       
//      7
