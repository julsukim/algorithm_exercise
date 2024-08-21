// const input = require('fs')
//   .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_5430.txt')
//   .toString()
//   .trim()
//   .split('\n');

// let index = 0;
// const TC = parseInt(input[index++]);
// const result = [];
// for (let i=0; i<TC; i++) {
//   const queries = input[index++].split('');
//   const N = parseInt(input[index++]);
//   const arr = JSON.parse(input[index++]);

//   let flag = false;

//   for (const query of queries) {
//     if (query === 'R') {
//       arr.reverse();
//     } else if (query === 'D') {
//       if (arr.length === 0) {
//         flag = true;
//         break;
//       } else {
//         arr.shift();
//       }
//     }
//   }

//   result.push(flag ? 'error' : `[${arr.join(',')}]`);
// }

// console.log(result.join('\n'));


const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_5430.txt')
  .toString()
  .trim()
  .split('\n');

let index = 0;
const TC = parseInt(input[index++]);
const result = [];
for (let i = 0; i < TC; i++) {
  const queries = input[index++].split('');
  const N = parseInt(input[index++]);
  const arr = JSON.parse(input[index++]);

  let reverse = false;
  let front = 0;
  let back = N;
  let flag = false;

  for (const query of queries) {
    if (query === 'R') {
      reverse = !reverse;
    } else if (query === 'D') {
      if (front === back) {
        flag = true;
        break;
      }
      if (reverse) {
        back--;
      } else {
        front++;
      }
    }
  }

  if (flag) {
    result.push('error');
  } else {
    let slicedArr = arr.slice(front, back);
    if (reverse) {
      slicedArr.reverse();
    }
    result.push(`[${slicedArr.join(',')}]`);
  }
}

console.log(result.join('\n'));
