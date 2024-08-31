const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1063.txt')
  .toString()
  .trim()
  .split('\n')
  .map(line => line.trim());

let index = 0;
const [K, S, N] = input[index++].split(' ');
const column = new Map([
  ['A', 0],
  ['B', 1],
  ['C', 2],
  ['D', 3],
  ['E', 4],
  ['F', 5],
  ['G', 6],
  ['H', 7],
  [0, 'A'],
  [1, 'B'],
  [2, 'C'],
  [3, 'D'],
  [4, 'E'],
  [5, 'F'],
  [6, 'G'],
  [7, 'H'],
]);
let kingLoc = [parseInt(K.split('')[1]) - 1, column.get(K.split('')[0])];
let stoneLoc = [parseInt(S.split('')[1]) - 1, column.get(S.split('')[0])];
const delta = new Map([
  ['R', [0, 1]],
  ['L', [0, -1]],
  ['B', [-1, 0]],
  ['T', [1, 0]],
  ['RT', [1, 1]],
  ['LT', [1, -1]],
  ['RB', [-1, 1]],
  ['LB', [-1, -1]],
]);
// R, L, B, T, RT, LT, RB, LB

for (const _ of Array(parseInt(N))) {
  const command = input[index++];
  const [di, dj] = delta.get(command);
  const [ni, nj] = [kingLoc[0] + di, kingLoc[1] + dj];
  if (0 <= ni && ni < 8 && 0 <= nj && nj < 8) {
    if (ni === stoneLoc[0] && nj === stoneLoc[1]) {
      const [nsi, nsj] = [stoneLoc[0] + di, stoneLoc[1] +dj];
      if (0 <= nsi && nsi < 8 && 0 <= nsj && nsj < 8) {
        stoneLoc = [nsi, nsj];
        kingLoc = [ni, nj];
      }
    } else {
      kingLoc = [ni, nj];
    }
  }
}
kingLoc = column.get(kingLoc[1]) + (kingLoc[0] + 1).toString();
stoneLoc = column.get(stoneLoc[1]) + (stoneLoc[0] + 1).toString();
console.log(kingLoc);
console.log(stoneLoc);

// 8*8 체스판
// 행 1~8, 열 A~H
