const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input;

rl.on('line', (line) => {
  input = line.toString();
  rl.close();
}).on('close', () => {
  let result = '';
  let word = '';
  let i = 0;

  while (i < input.length) {
    if (input[i] === '<') {
      result += word.split('').reverse().join('');
      word = '';

      while (input[i] !== '>') {
        result += input[i];
        i++;
      }
      result += '>';
      i++;
    } else if (input[i] === ' ') {
      result += word.split('').reverse().join('') + ' ';
      word = '';
      i++;
    } else {
      word += input[i];
      i++;
    }
  }

  result += word.split('').reverse().join('');

  console.log(result);
});