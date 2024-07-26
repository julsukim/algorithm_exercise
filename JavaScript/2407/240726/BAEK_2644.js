const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N, M, S, E;
let graph = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
    graph = Array.from({ length : N+1 }, () => []);
  } else if (idx === 1) {
    [S, E] = line.split(' ').map(Number);
  } else if (idx === 2) {
    M = parseInt(line);
  } else {
    [n1, n2] = line.split(' ').map(Number);
    graph[n1].push(n2);
    graph[n2].push(n1);
  }
  idx++;
  if (idx >= M+3) {
    rl.close();
  }
}).on('close', () => {

  const dist = new Array(N+1).fill(-1);
  const queue = [S];
  dist[S] = 0;

  while (queue.length > 0) {
    const now = queue.shift();

    if (now === E) break;

    for (const next of graph[now]) {
      if (dist[next] == -1) {
        dist[next] = dist[now] + 1;
        queue.push(next);
      }
    }
  }

  console.log(dist[E]);
})