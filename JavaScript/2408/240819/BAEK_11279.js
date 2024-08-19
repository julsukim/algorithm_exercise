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

  leftChildIndex(index) {
    return index * 2 + 1;
  }

  rightChildIndex(index) {
    return index * 2 + 2;
  }

  parent(index) {
    return this.items[this.parentIndex(index)];
  }

  leftChild(index) {
    return this.items[this.leftChildIndex(index)];
  }

  rightChild(index) {
    return this.items[this.rightChildIndex(index)];
  }

  peek() {
    return this.items[0];
  }
}

class MaxHeap extends Heap {
  bubbleUp() {
    let index = this.size - 1;
    while (index > 0 && this.parent(index) < this.items[index]) {
      this.swap(index, this.parentIndex(index));
      index = this.parentIndex(index);
    }
  }

  bubbleDown() {
    let index = 0;
    while (this.leftChildIndex(index) < this.size) {
      let biggerIndex = this.leftChildIndex(index);

      if (this.rightChildIndex(index) < this.size && this.rightChild(index) > this.leftChild(index)) {
        biggerIndex = this.rightChildIndex(index);
      }

      if (this.items[index] >= this.items[biggerIndex]) break;
      this.swap(index, biggerIndex);
      index = biggerIndex;
    }
  }

  add(item) {
    this.items[this.size] = item;
    this.size++;
    this.bubbleUp();
  }

  poll() {
    if (this.size === 0) return 0;
    const item = this.items[0];
    this.size--;
    if (this.size > 0) {
      this.items[0] = this.items[this.size];
      this.bubbleDown();
    }
    return item;
  }
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N;
let index = 0;
const maxHeap = new MaxHeap();
const result = [];

rl.on('line', (line) => {
  if (index === 0) {
    N = parseInt(line);
  } else {
    const num = parseInt(line);
    if (num === 0) {
      result.push(maxHeap.poll());
    } else {
      maxHeap.add(num);
    }
  }
  index++;
}).on('close', () => {
  console.log(result.join('\n'));
});