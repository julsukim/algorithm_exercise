class Heap {
  constructor() {
    this.items = [];
    this.size = 0;
  }

  swap(index1, index2) {
    [this.items[index1], this.items[index2]] = [this.items[index2], this.items[index1]];
  }

  parentIndex(index) {
    return Math.floor((index - 1) / 2);
  }
  
  parent(index) {
    return this.items[this.parentIndex(index)];
  }

  leftChildIndex(index) {
    return index * 2 + 1;
  }

  leftChild(index) {
    return this.items[this.leftChildIndex(index)];
  }

  rightChildIndex(index) {
    return index * 2 + 2;
  }

  rightChild(index) {
    return this.items[this.rightChildIndex(index)];
  }

  peek() {
    return this.items[0];
  }
}

class MinHeap extends Heap {
  bubbleUp() {
    let index = this.size;
    while (index > 0 && this.parent(index).priority > this.items[index].priority) {
      this.swap(index, this.parentIndex(index));
      index = this.parentIndex(index);
    }
  }

  bubbleDown() {
    let index = 0;
    while (this.leftChildIndex(index) < this.size) {
      let smallerIndex = this.leftChildIndex(index);
      if (this.rightChildIndex(index) < this.size && this.rightChild(index).priority < this.leftChild(index).priority) {
        smallerIndex = this.rightChildIndex(index);
      }
      if (this.items[index].priority <= this.items[smallerIndex].priority) break;
      this.swap(index, smallerIndex);
      index = smallerIndex;
    }
  }

  add(item) {
    this.items[this.size] = item;
    this.bubbleUp();
    this.size++;
  }

  poll() {
    const item = this.items[0];
    this.size--;
    if (this.size > 0) {
      this.items[0] = this.items[this.size];
      this.bubbleDown();
    }
    return item;
  }
}

class PriorityQueue {
  constructor() {
    this.heap = new MinHeap();
  }

  enqueue(item, priority) {
    const element = { item, priority };
    this.heap.add(element);
  }

  dequeue() {
    const element = this.heap.poll();
    return element ? element.item : null;
  }

  peek() {
    const element = this.heap.peek();
    return element ? element.item : null;
  }

  isEmpty() {
    return this.heap.size === 0;
  }
}

const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_14284.txt')
  .toString()
  .trim()
  .split('\n');

let index = 0;
const [N, M] = input[index++].split(' ').map(Number);
const graph = Array.from({ length: N+1 }, () => []);
for (let _ of new Array(M)) {
  const [a, b, c] = input[index++].split(' ').map(Number);
  graph[a].push([c, b]);
  graph[b].push([c, a]);
}
const [S, T]  =input[index++].split(' ').map(Number);


const dijkstra = (graph, start, target) => {
  const pq = new PriorityQueue();
  const dist = new Array(N+1).fill(Infinity);

  dist[start] = 0;
  pq.enqueue(start, 0);

  while (!pq.isEmpty()) {
    const current = pq.dequeue();

    for (let [priority, nextNode] of graph[current]) {
      const newDist = dist[current] + priority;

      if ((newDist < dist[nextNode])) {
        dist[nextNode] = newDist;
        pq.enqueue(nextNode, newDist);
      }
    }
  }

  return dist[target];
};

const result = dijkstra(graph, S, T);
console.log(result);
