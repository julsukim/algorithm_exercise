const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M;
const graph = [];
let idx = 0;
let result = 0;

const makeWall = (cnt, arr) => {
  if (cnt === 3) {
    let tmp = bfs(arr.map(row => row.slice()));
    result = Math.max(result, tmp);
    return;
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr[i][j] === 0) {
        arr[i][j] = 1;
        makeWall(cnt + 1, arr);
        arr[i][j] = 0;
      }
    }
  }
}

const bfs = (arr) => {
  let queue = [];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr[i][j] === 2) {
        queue.push([i, j]);
      }
    }
  }

  while (queue.length > 0) {
    const [pi, pj] = queue.shift();

    for (let [di, dj] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
      const ni = pi + di;
      const nj = pj + dj;

      if (0 <= ni && ni < N && 0 <= nj && nj < M && arr[ni][nj] === 0) {
        queue.push([ni, nj]);
        arr[ni][nj] = 2;
      }
    }
  }

  return arr.flat().filter(e => e === 0).length;
}

rl.on('line', (line) => {
  if (idx === 0) {
    [N, M] = line.split(' ').map(Number);
  } else {
    graph.push(line.split(' ').map(Number));
  }
  idx++;
  if (idx === N+1) {
    rl.close();
  }
}).on('close', () => {
  makeWall(0, graph);
  console.log(result);
})