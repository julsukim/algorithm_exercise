const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

let a, b, c

rl.on('line', (line) => {
  [a, b, c] = line.split(' ').map(Number)

  if (a === 0) {
    rl.close()
    return
  }

  const maxSide = Math.max(a, b, c)

  let side1, side2
  if (maxSide === a) {
    side1 = (b**2)+(c**2)
    side2 = a**2
  } else if (maxSide === b) {
    side1 = (a**2)+(c**2)
    side2 = b**2
  } else {
    side1 = (a**2)+(b**2)
    side2 = c**2
  }

  if (side1 === side2) {
    console.log('right')
  } else {
    console.log('wrong')
  }
})