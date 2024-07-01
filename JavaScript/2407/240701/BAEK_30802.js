const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let N, T, P;
let arr;
let index = 0;

rl.on('line', (line) => {
  if (index === 0){
    N = parseInt(line)
  } else if (index === 1) {
    arr = line.split(' ').map(Number)
  } else if (index === 2) {
    [T, P] = line.split(' ').map(Number)
    rl.close()
  }
  index++
}).on('close', () => {
  let shirts = 0;
  arr.forEach((e, i) => {
    const shirtsSet = Math.ceil(e / T)
    shirts += shirtsSet
  })
  console.log(shirts)
  const penSet = Math.floor(N / P)
  const pens = N - (penSet * P)
  console.log(penSet, pens)
})
