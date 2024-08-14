const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

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

const [N, M] = input.shift().split(' ').map(Number);
const graph = Array.from({ length: N + 1 }, () => []);
for (let i = 0; i < M; i++) {
  let [n1, n2] = input[i].split(' ').map(Number);
  graph[n2].push(n1);
}

const count = Array(N + 1).fill(0);

const bfs = (start) => {
  const queue = new Queue();
  queue.enqueue(start);
  const visited = Array(N + 1).fill(false);
  visited[start] = true;
  let cnt = 0;

  while (!queue.isEmpty()) {
    let now = queue.dequeue();
    cnt++;
    // for (const next of graph[now]) {
    //   if (!visited[next]) {
    //     visited[next] = true;
    //     queue.push(next);
    //   }
    // }
    for (let i=0; i<graph[now].length; i++) {
      const value = graph[now][i];
      if (!visited[value]) {
        visited[value] = true;
        queue.enqueue(value);
      }
    }
  }

  return cnt;
}

let max = 0;
for (let i = 1; i < N + 1; i++) {
  count[i] = bfs(i);
  if (count[i] > max) {
    max = count[i];
  }
}

const answer = [];
for (let i = 1; i < N + 1; i++) {
  if (count[i] === max) {
    answer.push(i);
  }
}

console.log(answer.join(' '));
