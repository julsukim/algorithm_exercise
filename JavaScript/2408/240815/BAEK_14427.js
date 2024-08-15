const input = require('fs')
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input_14427.txt")
  .toString()
  .trim()
  .split("\n");

class SegmentTree {
  constructor(arr) {
    this.n = arr.length;
    this.tree = new Array(4 * this.n);
    this.build(arr, 0, 0, this.n - 1);
  }

  build(arr, node, start, end) {
    if (start === end) {
      this.tree[node] = { value: arr[start], index: start };
    } else {
      const mid = Math.floor((start + end) / 2);
      const leftNode = 2 * node + 1;
      const rightNode = 2 * node + 2;

      this.build(arr, leftNode, start, mid);
      this.build(arr, rightNode, mid + 1, end);

      this.tree[node] = this._minPair(this.tree[leftNode], this.tree[rightNode]);
    }
  }

  _minPair(a, b) {
    if (a.value < b.value) return a;
    if (b.value < a.value) return b;
    return a.index < b.index ? a : b;
  }

  update(index, value, node=0, start=0, end=this.n-1) {
    if (start === end) {
      this.tree[node] = { value: value, index: index };
    } else {
      const mid = Math.floor((start + end) / 2);
      const leftNode = 2 * node + 1;
      const rightNode = 2 * node + 2;

      if (index <= mid) {
        this.update(index, value, leftNode, start, mid);
      } else {
        this.update(index, value, rightNode, mid + 1, end);
      }

      this.tree[node] = this._minPair(this.tree[leftNode], this.tree[rightNode]);
    }
  }

  queryMin(node = 0, start = 0, end = this.n-1) {
    return this.tree[node].index;
  }
}

let index = 0;
const N = parseInt(input[index++]);
const arr = input[index++].split(' ').map(Number);
const segTree = new SegmentTree(arr);

const M = parseInt(input[index++]);
const result = [];
for (let q=0; q<M; q++) {
  const query = input[index++].split(' ').map(Number);
  if (query[0] === 1) {
    segTree.update(query[1] - 1, query[2]);
  } else {
    result.push(segTree.queryMin() + 1);
  }
}

console.log(result.join('\n'));