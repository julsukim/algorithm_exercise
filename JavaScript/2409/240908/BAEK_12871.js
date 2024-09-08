const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let idx = 0;
let s, t;

// 두 수의 최대공약수를 구하는 함수
function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}

// 두 수의 최소공배수를 구하는 함수
function lcm(a, b) {
  return (a * b) / gcd(a, b);
}

// 문제를 해결하는 함수
function isSameInfiniteString(s, t) {
  const lenS = s.length;
  const lenT = t.length;

  // s와 t의 길이의 최소 공배수를 구한다
  const lcmLength = lcm(lenS, lenT);

  // s와 t를 각각 최소공배수 길이까지 반복
  const repeatedS = s.repeat(lcmLength / lenS);
  const repeatedT = t.repeat(lcmLength / lenT);

  // 두 반복된 문자열이 같으면 1, 다르면 0 반환
  return repeatedS === repeatedT ? 1 : 0;
}

rl.on('line', (line) => {
  if (idx === 0) {
    s = line;
  } else {
    t = line;
    rl.close();
  }
  idx++;
}).on('close', () => {
  console.log(isSameInfiniteString(s, t));
});