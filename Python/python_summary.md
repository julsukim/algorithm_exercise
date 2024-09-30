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