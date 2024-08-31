class UnionFind {
  constructor(size) {
    this.parent = Array.from({ length: size }, (_, index) => index);
    this.rank = Array(size).fill(0);
  }

  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX !== rootY) {
      if (this.rank[rootX] > this.rank[rootY]) {
        this.parent[rootY] = rootX;
      } else if (this.rank[rootX] < this.rank[rootY]) {
        this.parent[rootX] = rootY;
      } else {
        this.parent[rootY] = rootX;
        this.rank[rootX] += 1;
      }
    }
  }

  connected(x, y) {
    return this.find(x) === this.find(y);
  }
}

const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1717.txt')
  // .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

let index = 0;
const [N, M] = input[index++].split(' ').map(Number);
const uf = new UnionFind(N+1);
const result = [];

for (const _ of Array(M)) {
  const [type, a, b] = input[index++].split(' ').map(Number);
  if (type === 0) {
    uf.union(a, b);
  } else if (type === 1) {
    if (uf.connected(a, b)) {
      result.push("YES");
    } else {
      result.push("NO");
    }
  }
}

console.log(result.join('\n'));