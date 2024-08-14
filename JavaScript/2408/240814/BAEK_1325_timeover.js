class Queue {
  constructor() {
    this.items = [];
    this.head = 0;
    this.tail = 0;
  }

  enqueue(value) {
    this.items[this.tail] = value;
    this.tail++;
  }

  dequeue() {
    if (this.isEmpty()) {
      return undefined;
    }
    const item = this.items[this.head];
    this.head++;
    return item;
  }

  isEmpty() {
    return this.tail === this.head;
  }

  size() {
    return this.tail - this.head;
  }
}


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
  const searchList = new Set();
  for (let i=0; i<M; i++) {
    const [n1, n2] = input[idx++].split(' ').map(Number);
    graph[n2].push(n1);
    searchList.add(n2);
  }

  const bfs = (node, graph) => {
    const queue = new Queue();
    queue.enqueue(node);
    let cnt = 1;
    const visited = Array(N+1).fill(false);
    visited[node] = true;
    while (!queue.isEmpty()) {
      const now = queue.dequeue();
      for (const next of graph[now]) {
        if (!visited[next]) {
          visited[next] = true;
          queue.enqueue(next);
          cnt++;
        }
      }
    }
    return cnt;
  }

  const count = Array(N+1).fill(-1);
  for (let i=1; i<N+1; i++) {
    if (count[i] === -1 && searchList.has(i)) {
      count[i] = bfs(i, graph);
    }
  }

  const max = Math.max(...count);
  const result = [];
  for (let i=1; i<N+1; i++) {
    if (count[i] === max) {
      result.push(i);
    }
  }

  console.log(result.join(' '));
});