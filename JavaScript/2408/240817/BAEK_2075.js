const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

class Heap {
    constructor() {
        this.items = [];
        this.size = 0;
    }

    swap(index1, index2) {
        const temp = this.items[index1];
        this.items[index1] = this.items[index2];
        this.items[index2] = temp;
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

class MinHeap extends Heap {
    // bubbleUp
    bubbleUp() {
        let index = this.size - 1;
        while (
            index > 0 &&
            this.parent(index) > this.items[index]
        ) {
            this.swap(index, this.parentIndex(index));
            index = this.parentIndex(index);
        }
    }

    // bubbleDown
    bubbleDown() {
        let index = 0;
        while (this.leftChildIndex(index) < this.size) {
            let smallerIndex = this.leftChildIndex(index);
            if (
                this.rightChildIndex(index) < this.size &&
                this.rightChild(index) < this.leftChild(index)
            ) {
                smallerIndex = this.rightChildIndex(index);
            }
            if (this.items[index] <= this.items[smallerIndex]) break;
            this.swap(index, smallerIndex);
            index = smallerIndex;
        }
    }

    // add
    add(item) {
        this.items[this.size] = item;  // Directly place item to avoid push
        this.size++;
        this.bubbleUp();
    }

    // poll
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

let n = 0;
let count = -1;
const minHeap = new MinHeap();

rl.on("line", function (line) {
    if (count === -1) {
        count = parseInt(line);
        n = count;
        return;
    }

    // 삽입 및 삭제하는 구문
    line.split(' ').forEach((value) => {
        const intValue = parseInt(value);
        if (minHeap.size < n) {
            minHeap.add(intValue);
        } else if (intValue > minHeap.peek()) {
            minHeap.poll();
            minHeap.add(intValue);
        }
    });

    count--;
    if (count === 0) rl.close();
}).on("close", function () {
    console.log(minHeap.peek());
    process.exit();
});