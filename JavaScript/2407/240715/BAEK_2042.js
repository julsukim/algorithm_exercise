class SegmentTree {
  // 생성자. 세그먼트 트리를 초기화하고 빌드
  // arr: 원본 배열
  // operation : 구간 질의에 사용할 함수. 예를 들어 구간합이면 ((a, b) => a + b)
  // defaultValue : 초기값. 예를 들어 구간 합이면 0
  constructor(arr, operation, defaultValue) {
    this.n = arr.length; // 배열의 길이
    this.tree = new Array(2 * this.n); // 트리 배열
    this.operation = operation; // 구간 질의에 사용할 연산 함수
    this.defaultValue = defaultValue; // 초기값 (예 : 구간 합이면 0)

    // 트리를 초기값으로 초기화
    for (let i = 0; i < 2 * this.n; i++) {
      this.tree[i] = defaultValue;
    }

    // 트리 빌드
    this.buildTree(arr);
  }

  // 배열의 리프 노드를 트리의 하단에 저장하고, 내부 노드를 구간 정보를 이용해 채운다.
  buildTree(arr) {
    // 리프 노드 초기화
    for (let i = 0; i < this.n; i++) {
      this.tree[this.n + i] = arr[i];
    }

    // 내부 노드 초기화
    for (let i = this.n - 1; i > 0; i--) {
      this.tree[i] = this.operation(this.tree[i * 2], this.tree[i * 2 + 1]);
    }
  }

  // 특정 인덱스의 값을 업데이트하고, 그에 따른 내부 노드의 값을 갱신한다.
  update(index, value) {
    // 리프 노드 업데이트
    index += this.n;
    this.tree[index] = value;

    // 내부 노드 업데이트
    while (index > 1) {
      index = Math.floor(index / 2);
      this.tree[index] = this.operation(this.tree[2 * index], this.tree[index * 2 + 1]);
    }
  }

  // 특정 구간 left, right의 구간 합, 최소값, 최대값 등을 구한다.
  query(left, right) {
    left += this.n;
    right += this.n;
    let result = this.defaultValue;

    while (left < right) {
      if (left % 2 === 1) {
        result = this.operation(result, this.tree[left]);
        left++;
      }
      if (right % 2 === 1) {
        right--;
        result = this.operation(result, this.tree[right]);
      }
      left = Math.floor(left / 2);
      right = Math.floor(right / 2);
    }

    return result;
  }
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin
});

let input = [];

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [N, M, K] = input[0].split(' ').map(Number);
  const arr = [];
  for (let i = 1; i <= N; i++) {
    arr.push(BigInt(input[i]));
  }

  const segTree = new SegmentTree(arr, (a, b) => a + b, BigInt(0));

  const result = [];
  for (let i = N + 1; i < input.length; i++) {
    const [a, b, c] = input[i].split(' ').map(Number);

    if (a === 1) {
      segTree.update(b - 1, BigInt(c));
    } else if (a === 2) {
      result.push(segTree.query(b - 1, c).toString());
    }
  }

  console.log(result.join('\n'));
});