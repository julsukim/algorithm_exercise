const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  let idx = 0;
  const [N, M] = input[idx++].split(' ').map(Number);
  const graph = [];
  for (let i=0; i<N; i++) {
    graph.push(input[idx++].split(' ').map(Number));
  }

  const visited = Array.from({ length: N }, () => Array(M).fill(0));
  let cnt = 0;
  let area = 0;

  const bfs = (i, j, visited) => {
    const queue = [];
    queue.push([i, j]);
    visited[i][j] = 1;
    let extent = 1;

    while (queue.length > 0) {
      const [ci, cj] = queue.shift();

      for (let [di, dj] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
        const ni = ci + di;
        const nj = cj + dj;

        if (0 <= ni && ni < N && 0 <= nj && nj < M) {
          if (visited[ni][nj] === 0 && graph[ni][nj] === 1) {
            visited[ni][nj] = visited[ci][cj] + 1;
            queue.push([ni, nj]);
            extent++;
          }
        }
      }
    }

    return extent;
  }

  for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
      if (graph[i][j] === 1 && visited[i][j] === 0) {
        cnt++;
        area = Math.max(area, bfs(i, j, visited));
      }
    }
  }

  console.log(cnt);
  console.log(area);
});