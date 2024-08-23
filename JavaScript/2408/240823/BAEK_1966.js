const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1966.txt')
  .toString()
  .trim()
  .split('\n');

let index = 0;
const TC = parseInt(input[index++]);
const result = [];
for (let i=0; i<TC; i++) {
  const [N, M] = input[index++].split(' ').map(Number);
  const priorities = input[index++].split(' ').map(Number);
  
  let queue = priorities.map((priority, idx) => [priority, idx]);
  let count = 0;

  while (queue.length > 0) {
    const current = queue.shift();

    if (queue.some(doc => doc[0] > current[0])) {
      queue.push(current);
    } else {
      count++;
      if (current[1] === M) {
        result.push(count);
        break;
      }
    }
  }
}
console.log(result.join('\n'));