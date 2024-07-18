const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

const input = [];

rl.on('line', (line) => {
  // if (line === '') rl.close();
  input.push(line);
}).on('close', () => {
  const [M, N, K] = input[0].split(' ').map(Number);

  const graph = Array.from({ length: N }, () => Array(M).fill(0));

  for (let r = 1; r <= K; r++) {
    const [minI, minJ, maxI, maxJ] = input[r].split(' ').map(Number);
    for (let i = minI; i < maxI; i++) {
      for (let j = minJ; j < maxJ; j++) {
        graph[i][j] = 1;
      }
    }
  }

  let cnt = 0;
  const dimens = [];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j] === 1) continue;

      const queue = [[i, j]];
      graph[i][j] = 1;
      cnt++;
      let tmp = 1;

      while (queue.length > 0) {
        const [pi, pj] = queue.shift();

        for (let [di, dj] of [[-1, 0], [0, 1], [1, 0], [0, -1]]) {
          const ni = pi + di;
          const nj = pj + dj;

          if (ni >= 0 && ni < N && nj >= 0 && nj < M && graph[ni][nj] !== 1) {
            queue.push([ni, nj]);
            graph[ni][nj] = 1;
            tmp++;
          }
        }
      }

      dimens.push(tmp);
    }
  }

  dimens.sort((a, b) => a - b);
  console.log(cnt);
  console.log(...dimens);
})