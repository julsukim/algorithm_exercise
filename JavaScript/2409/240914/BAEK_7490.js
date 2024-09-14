const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_7490.txt')
  .toString()
  .trim()
  .split('\n');

let idx = 0;
const tc = parseInt(input[idx++]);

for (let t = 0; t < tc; t++) {
  const N = parseInt(input[idx++]);
  const result = [];
  
  function dfs(num, exp) {
    if (num === N) {
      // Evaluate the expression
      const evalExp = exp.replace(/\s/g, '');
      if (evaluate(evalExp) === 0) {
        result.push(exp);
      }
      return;
    }

    dfs(num + 1, exp + ' ' + (num + 1));
    dfs(num + 1, exp + '+' + (num + 1));
    dfs(num + 1, exp + '-' + (num + 1));
  }

  function evaluate(exp) {
    let sum = 0;
    let numStr = '';
    let sign = 1;
    for (let i = 0; i < exp.length; i++) {
      if (exp[i] === '+') {
        sum += sign * parseInt(numStr);
        numStr = '';
        sign = 1;
      } else if (exp[i] === '-') {
        sum += sign * parseInt(numStr);
        numStr = '';
        sign = -1;
      } else {
        numStr += exp[i];
      }
    }
    sum += sign * parseInt(numStr);
    return sum;
  }

  dfs(1, '1');
  result.sort();
  console.log(result.join('\n'));
  if (t < tc - 1) console.log();
}
