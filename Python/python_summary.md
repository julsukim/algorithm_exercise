## 함수 및 기타 메서드 정리

---

<details>
<summary><strong>string</strong></summary>


1. `str.upper()`
   - 문자열을 모두 대문자로 변환합니다.
   - ```python
     text = "hello"
     print(text.upper())  # HELLO
     ```

2. `str.lower()`
   - 문자열을 모두 소문자로 변환합니다.
   - ```python
     text = "HELLO"
     print(text.lower())  # hello
     ```

3. `str.capitalize()`
   - 문자열의 첫 글자를 대문자로 변환합니다.
   - ```python
     text = "hello world"
     print(text.capitalize())  # Hello world
     ```

4. `str.title()`
   - 각 단어의 첫 글자를 대문자로 변환합니다.
   - ```python
     text = "hello world"
     print(text.title())  # Hello World
     ```

5. `str.strip()`
   - 문자열 양쪽 끝의 공백이나 특정 문자를 제거합니다.
   - ```python
     text = "  hello  "
     print(text.strip())  # "hello"
     ```

6. `str.lstrip()` / `str.rstrip()`
   - 왼쪽(lstrip()) 또는 오른쪽(rstrip())의 공백을 제거합니다.
   - ```python
     text = "  hello  "
     print(text.lstrip())  # "hello  "
     print(text.rstrip())  # "  hello"
     ```

7. `str.replace(old, new)`
   - 문자열 내의 특정 부분을 다른 문자열로 대체합니다.
   - ```python
     text = "hello world"
     print(text.replace("world", "Python"))  # hello Python
     ```

8. `str.split(sep)`
   - 문자열을 특정 구분자를 기준으로 나누어 리스트로 반환합니다.
   - ```python
     text = "apple,banana,cherry"
     print(text.split(","))  # ['apple', 'banana', 'cherry']
     ```

9. `str.join(iterable)`
   - 문자열 리스트를 특정 구분자로 연결하여 하나의 문자열로 만듭니다.
   - ```
     words = ['apple', 'banana', 'cherry']
     print(", ".join(words))  # apple, banana, cherry
     ```

10. `str.find(sub)`
    - 문자열 내에서 특정 부분 문자열을 찾아 인덱스를 반환합니다. 찾지 못하면 -1을 반환합니다.
    - ```python
      text = "hello world"
      print(text.find("world"))  # 6
      ```

11. `str.count(sub)`
    - 문자열 내에서 특정 부분 문자열이 몇 번 등장하는지 셉니다.
    - ```python
      text = "banana"
      print(text.count("a"))  # 3
      ```

12. `str.startswith(prefix)` / `str.endswith(suffix)`
    - 문자열이 특정 문자열로 시작하거나 끝나는지 여부를 반환합니다.
    - ```python
      text = "hello world"
      print(text.startswith("hello"))  # True
      print(text.endswith("world"))    # True
      ```

13. `str.isdigit()` / `str.isalpha()` / `str.isalnum()`
    - 문자열이 숫자(isdigit()), 알파벳(isalpha()), 또는 알파벳과 숫자로만 이루어져 있는지(`isalnum()`) 확인합니다.
    - ```python
      text = "12345"
      print(text.isdigit())  # True
      print(text.isalpha())  # False
      ```

14. `str.zfill(width)`
    - 문자열을 특정 길이로 맞추고, 앞쪽을 0으로 채웁니다.
    - ```python
      text = "42"
      print(text.zfill(5))  # 00042
      ```

</details>

---

<details>
<summary><strong>deque from collections</strong></summary>

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
<summary><strong>Counter from collections</strong></summary>

- `Counter` 클래스는 특정 요소의 등장 횟수를 셀 수 있는 클래스

1. 리스트나 문자열에서 요소의 등장 횟수 세기
```python
from collections import Counter

string = "hello world"
counter = Counter(string)
print(counter)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
counter = Counter(fruits)
print(counter)
# Counter({'apple': 3, 'banana': 2, 'orange': 2})
```

2. 요소별로 개수 접근하기
```python
from collections import Counter

fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
counter = Counter(fruits)

print(counter['apple'])  # 3
print(counter['banana']) # 2

print(counter['pear']) # 0
# 존재하지 않는 요소에 접근하면, 기본적으로 0을 반환
```

3. 가장 많이 등장한 요소 찾기
```python
from collections import Counter

fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
counter = Counter(fruits)

print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]
```

4. 요소 추가 및 업데이트
```python
from collections import Counter

fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
counter = Counter(fruits)

# 직접 요소의 빈도수 수정
counter['banana'] += 1
print(counter)  # Counter({'apple': 3, 'banana': 3, 'orange': 2})
```
- `update()` 메서드를 사용하여 업데이트
```python
from collections import Counter

counter = Counter("apple")
print(counter)  # Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})

# 문자열로 update
counter.update("banana")
print(counter)  # Counter({'a': 4, 'p': 2, 'n': 2, 'l': 1, 'e': 1, 'b': 1})

counter = Counter(['apple', 'banana'])
print(counter)  # Counter({'apple': 1, 'banana': 1})

# 리스트로 update
counter.update(['apple', 'orange'])
print(counter)  # Counter({'apple': 2, 'banana': 1, 'orange': 1})

counter = Counter("apple")
print(counter)  # Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})

# 딕셔너리로 update
counter.update({'p': 3, 'a': 2})
print(counter)  # Counter({'p': 5, 'a': 3, 'l': 1, 'e': 1})

counter1 = Counter("apple")
counter2 = Counter("banana")

# 다른 Counter로 update
counter1.update(counter2)
print(counter1)  # Counter({'a': 4, 'p': 2, 'n': 2, 'l': 1, 'e': 1, 'b': 1})
```

5. 카운터 간의 연산
- `Counter`는 수학적 연산도 지원.
- 객체 간의 덧셈, 뺄셈, 교집합, 합집합 등의 연산을 할 수 있음

```python
from collections import Counter

counter1 = Counter(['a', 'b', 'c', 'a'])
counter2 = Counter(['a', 'b', 'b', 'd'])

result = counter1 + counter2
print(result)  # Counter({'a': 3, 'b': 3, 'c': 1, 'd': 1})

result = counter1 - counter2
print(result)  # Counter({'c': 1, 'a': 1})

result = counter1 & counter2
print(result)  # Counter({'a': 1, 'b': 1})

result = counter1 | counter2
print(result)  # Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})
```

6. Counter 객체를 리스트로 변환
- `elements()` 메서드를 사용하면 각 요소를 등장 횟수만큼 반복하여 리스트로 변환

```python
counter = Counter({'a': 2, 'b': 3, 'c': 1})
elements_list = list(counter.elements())
print(elements_list)  # ['a', 'a', 'b', 'b', 'b', 'c']
```

7. 빈도수 0 이하의 값 제거
- `Counter` 객체는 0 이하의 빈도수를 허용하지만, 0 이하의 항목을 제거하고 싶을 때는 `+` 연산을 사용

```python
counter = Counter({'a': 2, 'b': -1, 'c': 0})
counter += Counter()  # 0 이하 값 제거
print(counter)  # Counter({'a': 2})
```

</details>

<details>
<summary><strong>enumerate</strong></summary>

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
<summary><strong>lambda</strong></summary>

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
<summary><strong>list comprehension</strong></summary>

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
<summary><strong>itertools</strong></summary>

`itertools.product()`
- 두 개 이상의 리스트나 iterable에서 가능한 모든 조합을 생성

```python
import itertools
# itertools.product(*iterables, repeat=1)

# 두 리스트의 데카르트 곱
result = list(itertools.product([1, 2], ['A', 'B']))
print(result)  # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

# 같은 iterable을 2번 반복하여 데카르트 곱을 구함
result = list(itertools.product([1, 2], repeat=2))
print(result)  # [(1, 1), (1, 2), (2, 1), (2, 2)]
```

`itertools.permutations()`
- 순열을 생성. 주어진 순서에 따라 원소를 나열

```python
# itertools.permutations(iterable, r=None)
# r : 선택할 원소의 수 (기본값은 iterable의 전체 길이)

# 순열 생성 (길이 지정 가능, 기본값은 전체 길이)
result = list(itertools.permutations([1, 2, 3]))
print(result)  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 순열에서 2개씩 선택하는 경우
result = list(itertools.permutations([1, 2, 3], 2))
print(result)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

`itertools.combinations()`
- 조합을 생성. 순서 고려하지 않음, 지정된 크기의 조합을 반환

```python
# itertools.combinations(iterable, r)
# r : 선택할 원소의 수. 필수로 지정해야 한다.

# 2개씩 조합 생성
result = list(itertools.combinations([1, 2, 3], 2))
print(result)  # [(1, 2), (1, 3), (2, 3)]
```

`itertools.combinations_with_replacement()`
- 중복을 허용한 조합 생성

```python
result = list(itertools.combinations_with_replacement([1, 2, 3], 2))
print(result)  # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

```
</details>
