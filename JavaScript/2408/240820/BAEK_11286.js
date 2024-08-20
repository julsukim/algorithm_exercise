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

class AbsMinHeap extends Heap {
  bubbleUp() {
    let index = this.size - 1;
    while (index > 0) {
      let parentIndex = this.parentIndex(index);
      let parentValue = this.items[parentIndex];
      let currentValue = this.items[index];

      if (
        Math.abs(parentValue) > Math.abs(currentValue) || 
        (Math.abs(parentValue) === Math.abs(currentValue) && parentValue > currentValue)
      ) {
        this.swap(index, parentIndex);
        index = parentIndex;
      } else {
        break;
      }
    }
  }

  bubbleDown() {
    let index = 0;
    while (this.leftChildIndex(index) < this.size) {
      let leftChildIndex = this.leftChildIndex(index);
      let rightChildIndex = this.rightChildIndex(index);
      let smallerIndex = leftChildIndex;

      if (rightChildIndex < this.size) {
        let leftChildValue = this.items[leftChildIndex];
        let rightChildValue = this.items[rightChildIndex];

        if (
          Math.abs(rightChildValue) < Math.abs(leftChildValue) || 
          (Math.abs(rightChildValue) === Math.abs(leftChildValue) && rightChildValue < leftChildValue)
        ) {
          smallerIndex = rightChildIndex;
        }
      }

      let smallerValue = this.items[smallerIndex];
      let currentValue = this.items[index];

      if (
        Math.abs(currentValue) < Math.abs(smallerValue) || 
        (Math.abs(currentValue) === Math.abs(smallerValue) && currentValue <= smallerValue)
      ) {
        break;
      }

      this.swap(index, smallerIndex);
      index = smallerIndex;
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
const absMinHeap = new AbsMinHeap();
const result = [];

rl.on('line', (line) => {
  if (index === 0) {
    N = parseInt(line);
  } else {
    const num = parseInt(line);
    if (num === 0) {
      result.push(absMinHeap.poll());
    } else {
      absMinHeap.add(num);
    }
  }
  index++;
}).on('close', () => {
  console.log(result.join('\n'));
});
