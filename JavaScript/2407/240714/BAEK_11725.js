const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N;
let graph = [];
let parent = [];
let idx = 0;

const dfs = (node, prev) => {
  parent[node] = prev;

  for (const next of graph[node]) {
    if (next === prev) continue;
    dfs(next, node);
  }
}

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
    graph = Array.from({ length: N+1 }, () => []);
    parent = Array.from({ length: N+1 }, () => 0);
  } else {
    const [a, b] = line.split(' ').map(Number);
    graph[a].push(b);
    graph[b].push(a);
  }

  idx++;
  if (idx === N) {
    rl.close();
  }

}).on('close', () => {
  dfs(1, 0);

  console.log(parent.slice(2).join('\n'));
});