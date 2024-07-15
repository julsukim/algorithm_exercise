// 세그먼트 트리

// 주어진 배열의 구간 질의를 효율적으로 처리하기 위해 고안된 자료구조.
// 주로 배열의 구간 합, 최소값, 최대값 등의 질의를 빠르게 해결하기 위해 사용.
// 완전 이진 트리의 형태를 가지며, 각 노드는 배열의 특정 구간 정보를 저장.

// 구조
// 1. 리프 노드 : 배열의 개별 요소를 저장
// 2. 내부 노드 : 특정 구간의 정보를 저장.
//    예를 들어 구간 합을 구하는 세그먼트 트리라면 각 내부 노드는 그 구간의 합을 저장

// 주요 연산
// 구간 질의 : 특정 구간의 합, 최소값, 최대값 등을 O(log N) 시간에 구할 수 있음
// 구간 업데이트 : 특정 인덱스의 값을 업데이트하고 그에 따른 구간 정보를 갱신하는 작업을 O(log N) 시간에 수행 가능

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

const arr = [1, 3, 5, 7, 9, 11];
const segTree = new SegmentTree(arr, (a, b) => a + b, 0);

console.log(segTree.query(1, 5)); // 3 + 5 + 7 + 9 = 24
segTree.update(2, 6); // arr[2] = 6
console.log(segTree.query(1, 5)); // 3 + 6 + 7 + 9 = 25