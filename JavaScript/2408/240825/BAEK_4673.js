const notSelfNumbers = new Set();
let notSelfNumber = 0
let number = 0;
while (true) {
  const numberArr = number.toString().split('').map(Number);
  notSelfNumber += number;
  for (let i=0; i<numberArr.length; i++) {
    notSelfNumber += numberArr[i];
  }
  if (notSelfNumber > 11000) {
    break;
  } else {
    number++;
    notSelfNumbers.add(notSelfNumber);
    notSelfNumber = 0;
  }
}
const result = [];
for (let i=1; i<=10000; i++) {
  if (!notSelfNumbers.has(i)) {
    result.push(i);
  }
}

console.log(result.join('\n'));