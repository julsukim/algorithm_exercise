const PriorityQueue = require('js-priority-queue');

function minBreaksToReachEnd(N, M, maze) {
  const directions = [
      [0, 1],  // 오른쪽
      [1, 0],  // 아래쪽
      [0, -1], // 왼쪽
      [-1, 0]  // 위쪽
  ];

  const distance = Array.from({ length: N }, () => Array(M).fill(Infinity));
  const pq = new PriorityQueue({ comparator: (a, b) => a.priority - b.priority});

  // 시작점 (0, 0)
  distance[0][0] = 0;
  pq.enqueue([0, 0], 0);

  while (!pq.isEmpty()) {
      const [x, y] = pq.dequeue();

      for (const [dx, dy] of directions) {
          const nx = x + dx;
          const ny = y + dy;

          if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
              const nextDist = distance[x][y] + maze[nx][ny];

              if (nextDist < distance[nx][ny]) {
                  distance[nx][ny] = nextDist;
                  pq.enqueue([nx, ny], nextDist);
              }
          }
      }
  }

  return distance[N-1][M-1];
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
  
  let result = minBreaksToReachEnd(N, M, graph);
  console.log(result === Infinity ? 0 : result);
});