class PriorityQueue {
  constructor() {
    this.queue = [];
  }

  enqueue(element, priority) {
    this.queue.push({ element, priority });
    this.queue.sort((a, b) => a.priority - b.priority);
  }

  dequeue() {
    return this.queue.shift().element;
  }

  isEmpty() {
    return this.queue.length === 0;
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
  const [M, N] = input[idx++].split(' ').map(Number);
  const graph = [];
  for (let i=0; i<N; i++) {
    graph.push(input[idx++].split('').map(Number));
  }

  const distance = Array.from({ length: N }, () => Array(M).fill(Infinity));
  const pq = new PriorityQueue();

  distance[0][0] = 0;
  pq.enqueue([0, 0], 0);

  while (!pq.isEmpty()) {
    const [r, c] = pq.dequeue();

    for (const [dr, dc] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
      const nr = r + dr;
      const nc = c + dc;

      if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
        const nextDist = distance[r][c] + graph[nr][nc];

        if (nextDist < distance[nr][nc]) {
          distance[nr][nc] = nextDist;
          pq.enqueue([nr, nc], nextDist);
        }
      }
    }
  }

  const result = distance[N-1][M-1];
  console.log(result === Infinity ? 0 : result);
});