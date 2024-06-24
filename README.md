## Algorithm Exercise

---
### commit
- solve: 문제 풀이 성공
- add: 문제 추가
- docs: 문제 풀이 현황 작성
---

## 함수 및 기타 메서드 정리

<details>
<summary>deque from collections</summary>

```python
from collections import deque

# 덱 초기화
dq = deque([1, 2, 3, 4, 5])

# append와 appendleft
dq.append(6)
dq.appendleft(0)
print(dq)  # deque([0, 1, 2, 3, 4, 5, 6])

# pop과 popleft
right = dq.pop()
left = dq.popleft()
print(right, left)  # 6 0
print(dq)  # deque([1, 2, 3, 4, 5])

# extend와 extendleft
dq.extend([7, 8])
dq.extendleft([-1, -2])
print(dq)  # deque([-2, -1, 1, 2, 3, 4, 5, 7, 8])

# rotate
dq.rotate(2)
print(dq)  # deque([7, 8, -2, -1, 1, 2, 3, 4, 5])
dq.rotate(-2)
print(dq)  # deque([-2, -1, 1, 2, 3, 4, 5, 7, 8])

# remove
dq.remove(1)
print(dq)  # deque([-2, -1, 2, 3, 4, 5, 7, 8])

# count
count_2 = dq.count(2)
print(count_2)  # 1

# index
index_3 = dq.index(3)
print(index_3)  # 3
```
</details>

<details>
<summary>enumerate</summary>

```python
# enumerate(iterable, start=0)
# start 매개변수를 사용하여 인덱스를 다른 값부터 시작

# 리스트 예제
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 출력:
# 0 apple
# 1 banana
# 2 cherry
```
</details>

---

### 240524

- 백준 1149 : RGB거리 (다시풀기)
- 백준 1504 : 특정한 최단 경로 (다시풀기)
- 백준 1699 : 제곱수의 합
  - 다이나믹 프로그래밍
- 백준 14501 : 퇴사
  - 다이나믹 프로그래밍, 브루트포스
- 백준 15486 : 퇴사 2
  - 다이나믹 프로그래밍

### 240523

- 백준 17404 : RGB거리 2
  - 다이나믹 프로그래밍
- 백준 1600 : 말이 되고픈 원숭이
  - BFS (3차원)
- 백준 10844 : 쉬운 계단 수
  - 다이나믹 프로그래밍
- 백준 11723 : 집합
  - 비트마스킹
- 백준 12833 : XORXORXOR
  - 비트마스킹
- 백준 24389 : 2의 보수
  - 비트마스킹
- 백준 25166 : 배고픈 아리의 샌드위치 구매하기
  - 비트마스킹
- 백준 27960 : 사격 내기
  - 비트 마스킹

### 240522

- 백준 5972 : 택배 배송
  - 다익스트라
- 백준 12002 : Field Reduction (Silver)
  - 백트래킹, 브루트포스
- 백준 11726 : 2xn 타일링
  - 다이나믹 프로그래밍
- 백준 1149 : RGB거리
  - 다이나믹 프로그래밍
