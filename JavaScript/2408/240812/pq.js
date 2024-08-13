class PriorityQueue {
  constructor() {
    this.heap = [];
  }

  getParentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  getLeftChildIndex(index) {
    return 2 * index + 1;
  }

  getRightChildIndex(index) {
    return 2 * index + 2;
  }

  swap(index1, index2) {
    [this.heap[index1], this.heap[index2]] = [this.heap[index2], this.heap[index1]];
  }

  enqueue(element, priority) {
    // 힙의 마지막 위치에 삽입
    this.heap.push({ element, priority });
    // 재정렬
    this.bubbleUp(this.heap.length - 1);
  }

  bubbleUp(index) {
    let currentIndex = index;
    // 부모 노드 확인
    let parentIndex = this.getParentIndex(currentIndex);

    // 비교 및 교환
    // 자식을 부모 방향으로 이동시키기
    while (currentIndex > 0 && this.heap[currentIndex].priority < this.heap[parentIndex].priority) {
      this.swap(currentIndex, parentIndex);
      currentIndex = parentIndex;
      parentIndex = this.getParentIndex(currentIndex);
    }
  }

  dequeue() {
    if (this.heap.length === 0) {
      return null;
    }

    if (this.heap.length === 1) {
      return this.heap.pop().element;
    }

    // 루트 노드를 제거하고 마지막 노드를 루트로 올림
    const minElement = this.heap[0].element;
    this.heap[0] = this.heap.pop();
    // 재정렬
    this.bubbleDown(0);
    return minElement;
  }

  bubbleDown(index) {
    let currentIndex = index;
    // 자식 노드들
    let leftChildIndex = this.getLeftChildIndex(currentIndex);
    let rightChildIndex = this.getRightChildIndex(currentIndex);

    // 비교 및 교환
    // 부모를 자식 방향으로 이동시키기
    while (leftChildIndex < this.heap.length) {
      // 두 자식 중 작은 우선순위를 가진 자식 구하기
      let smallerChildIndex = leftChildIndex;

      if (rightChildIndex < this.heap.length && this.heap[rightChildIndex].priority < this.heap[leftChildIndex].priority) {
        smallerChildIndex = rightChildIndex;
      }

      // 자식들보다 우선순위가 낮은 경우 종료
      if (this.heap[currentIndex].priority <= this.heap[smallerChildIndex].priority) {
        break;
      }

      // 교환
      this.swap(currentIndex, smallerChildIndex);
      currentIndex = smallerChildIndex;
      leftChildIndex = this.getLeftChildIndex(currentIndex);
      rightChildIndex = this.getRightChildIndex(currentIndex);
    }
  }

  isEmpty() {
    return this.heap.length === 0;
  }
}


// --------test-----------


function minBreaksToReachEnd(N, M, maze) {
  const directions = [
      [0, 1],  // 오른쪽
      [1, 0],  // 아래쪽
      [0, -1], // 왼쪽
      [-1, 0]  // 위쪽
  ];

  const distance = Array.from({ length: N }, () => Array(M).fill(Infinity));
  const pq = new PriorityQueue();

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