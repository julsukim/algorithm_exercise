const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let A, B

rl.on('line', (line) => {
  [A, B] = line.split(' ').map(Number)
  rl.close()
}).on('close', () => {
  console.log(gcd(A, B))
  console.log(lcm(A, B))
})

const gcd = (a, b) => {
  while (b !== 0) {
    let temp = b
    b = a % b
    a = temp
  }
  return a
}

const lcm = (a, b) => {
  return Math.abs(a * b) / gcd(a, b)
}
