const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];

const countSubtreeNode = (currentNode, parent, graph, subTree) => {
  subTree[currentNode] = 1;
  for (const node of graph[currentNode]) {
    if (node !== parent) {
      countSubtreeNode(node, currentNode, graph, subTree);
      subTree[currentNode] += subTree[node];
    }
  }
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  let idx = 0;
  const [N, R, Q] = input[idx++].split(' ').map(Number);
  const graph = Array.from({ length: N+1 }, () => []);
  for (let i=0; i<N-1; i++) {
    const [U, V] = input[idx++].split(' ').map(Number);
    graph[U].push(V);
    graph[V].push(U);
  }
  const result = [];
  const subTree = Array(N+1).fill(0);
  countSubtreeNode(R, -1, graph, subTree);
  for (let i=0; i<Q; i++) {
    result.push(subTree[parseInt(input[idx++])]);
  }
  console.log(result.join('\n'));
});