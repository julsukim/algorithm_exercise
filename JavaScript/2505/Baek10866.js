const fs = require('fs');

const input = fs
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input10866.txt')
  .toString().trim().split(/\r?\n/);

const N = +input[0];
const answer = [];

class Deque {
  constructor() {
    this.data = {};
    this.head = 0;
    this.tail = 0;
  }
  push_front(x) {
    this.data[--this.head] = x;
  }
  push_back(x) {
    this.data[this.tail++] = x;
  }
  pop_front() {
    if (this.head === this.tail) return -1;      // head==tail 이면 empty
    return this.data[this.head++];               // 포인터만 이동
  }
  pop_back() {
    if (this.head === this.tail) return -1;
    return this.data[--this.tail];
  }
  size() {
    return this.tail - this.head;                // 삽입된 원소 수
  }
  empty() {
    return this.head === this.tail ? 1 : 0;      // head===tail 이면 1
  }
  front() {
    return this.head === this.tail
      ? -1
      : this.data[this.head];
  }
  back() {
    return this.head === this.tail
      ? -1
      : this.data[this.tail - 1];
  }
}

const dq = new Deque();

for (let i = 1; i <= N; i++) {
  const [cmd, arg] = input[i].split(' ');
  switch (cmd) {
    case 'push_front':
      dq.push_front(arg);
      break;
    case 'push_back':
      dq.push_back(arg);
      break;
    case 'pop_front':
      answer.push(dq.pop_front());
      break;
    case 'pop_back':
      answer.push(dq.pop_back());
      break;
    case 'size':
      answer.push(dq.size());
      break;
    case 'empty':
      answer.push(dq.empty());
      break;
    case 'front':
      answer.push(dq.front());
      break;
    case 'back':
      answer.push(dq.back());
      break;
  }
}

console.log(answer.join('\n'));
