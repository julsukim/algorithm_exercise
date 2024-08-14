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
  const graph = Array.from({ length: N+1 }, () => []);
  for (let i=0; i<M; i++) {
    const [n1, n2] = input[idx++].split(' ').map(Number);
    graph[n2].push(n1);
  }

  const count = Array(N+1).fill(0);
  
  for (let i=1; i<=N; i++) {
    const queue = [i];
    const visited = Array(N+1).fill(false);
    visited[i] = 0;
    while (queue.length > 0) {
      const now = queue.shift();
      for (const next of graph[now]) {
        if (!visited[next]) {
          visited[next] = true;
          queue.push(next);
        }
      }
    }
    count[i] = visited.filter(v => v).length;
  }

  const maximum = Math.max(...count);
  const result = [];
  for (let i=1; i<=N; i++) {
    if (count[i] === maximum) {
      result.push(i);
    }
  }
  console.log(result.join(' '));
});