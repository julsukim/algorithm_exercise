from itertools import combinations
import sys
input = sys.stdin.readline

tc = 1
result = []

while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    numbers = arr[1:]
    if n == 0:
        break
    if tc > 1:
        result.append('')

    for i in list(combinations(numbers, 6)):
        ans = sorted(i)
        result.append(ans)

    tc += 1

for r in result:
    print(*r)
