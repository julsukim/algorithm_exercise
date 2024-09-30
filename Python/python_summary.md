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

<details>
<summary>lambda</summary>

```python
# lambda 매개변수 : 표현식

# 일반 함수와 lambda 함수의 정의 차이
def add(x, y):
    return x + y
print(add(2, 3)) # 5

add = lambda x, y: x + y
print(add(2, 3)) # 5

# sort, sorted() 함수와 lambda
# 각 요소의 두 번째 값을 기준으로 정렬
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
data.sort(key=lambda x: x[1])
print(data)
# 출력: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

```
</details>

<details>
<summary>list comprehension</summary>

```python
# 리스트를 간결하고 효율적으로 생성할 수 있는 문법
[표현식 for 항목 in iterable]

# 1부터 5까지 숫자의 제곱을 구하여 새로운 리스트 생성
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 조건을 추가하여 짝수만 리스트에 추가
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)  # [4, 16]
```
</details>

<details>
<summary>itertools</summary>
`itertools.product()`

```python
import itertools

# 두 리스트의 데카르트 곱
result = list(itertools.product([1, 2], ['A', 'B']))
print(result)  # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```
</details>
