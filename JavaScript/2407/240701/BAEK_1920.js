const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let input = [];
rl.on('line', (line) => {
  input.push(line)
}).on('close', () => {
  const N = parseInt(input[0])
  const arrN = input[1].split(' ').map(Number)
  const M = parseInt(input[2])
  const arrM = input[3].split(' ').map(Number)

  const setN = new Set(arrN)
  const result = arrM.map(e => setN.has(e) ? 1 : 0)

  console.log(result.join('\n'))
})

// console.log I/O 작업 중에서 느린 편에 속함 => 최대한 적게 출력하자

// const readline = require('readline');

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// let input = [];
// rl.on('line', (line) => {
//   input.push(line)
// }).on('close', () => {
//   const N = parseInt(input[0])
//   const arrN = input[1].split(' ').map(Number)
//   const M = parseInt(input[2])
//   const arrM = input[3].split(' ').map(Number)

//   const setN = new Set(arrN);
//   let result = [];

//   arrM.forEach((e) => {
//     if (setN.has(e)) {
//       result.push(1);
//     } else {
//       result.push(0);
//     }
//   });

//   console.log(result.join('\n'));
// });

// let N, M
// let arrN, arrM
// let index = 0

// rl.on('line', (line) => {
//   if (index === 0) {
//     N = parseInt(line)
//   } else if (index === 1) {
//     arrN = line.split(' ').map(Number)
//   } else if (index === 2) {
//     M = parseInt(line)
//   } else {
//     arrM = line.split(' ').map(Number)
//     rl.close()
//   }
//   index++
// }).on('close', () => {
//   const setN = new Set(arrN)
//   arrM.forEach((e) => {
//     if (setN.has(e)) {
//       console.log(1)
//     } else {
//       console.log(0)
//     }
//   })
// })

// rl.on('line', (line) => {
//   if (index === 0) {
//     N = parseInt(line)
//   } else if (index === 1) {
//     arrN = line.split(' ').map(Number)
//   } else if (index === 2) {
//     M = parseInt(line)
//   } else {
//     arrM = line.split(' ').map(Number)
//     rl.close()
//   }
//   index++
// }).on('close', () => {
//   arrM.forEach((e, i) => {
//     if (typeof(arrN.find(num => num === e)) !== 'undefined') {
//       console.log(1)
//     } else {
//       console.log(0)
//     }
//   })
// })