class Deque {
  constructor() {
      this.items = {};  // 큐의 요소들을 저장할 객체
      this.head = 0;    // 큐의 앞을 가리킬 인덱스
      this.tail = 0;    // 큐의 뒤를 가리킬 인덱스
  }

  push(value) {
      // 큐의 뒤에 요소를 추가합니다.
      this.items[this.tail] = value;
      this.tail++;
  }

  pop() {
      // 큐의 뒤에서 요소를 제거하고 반환합니다.
      if (this.isEmpty()) {
          return undefined;
      }
      this.tail--;
      const value = this.items[this.tail];
      delete this.items[this.tail];
      return value;
  }

  shift() {
      // 큐의 앞에서 요소를 제거하고 반환합니다.
      if (this.isEmpty()) {
          return undefined;
      }
      const value = this.items[this.head];
      delete this.items[this.head];
      this.head++;
      return value;
  }

  unshift(value) {
      // 큐의 앞에 요소를 추가합니다.
      if (this.head > 0) {
          this.head--;
          this.items[this.head] = value;
      } else {
          for (let i = this.tail; i > 0; i--) {
              this.items[i] = this.items[i - 1];
          }
          this.tail++;
          this.items[0] = value;
      }
  }

  isEmpty() {
      // 큐가 비어있는지 확인합니다.
      return this.tail === this.head;
  }

  size() {
      // 큐의 크기를 반환합니다.
      return this.tail - this.head;
  }

  clear() {
      // 큐를 초기화합니다.
      this.items = {};
      this.head = 0;
      this.tail = 0;
  }
}
