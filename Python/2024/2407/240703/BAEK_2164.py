from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque(range(1, N+1))

for _ in range(N-1):
    arr.popleft()
    i = arr.popleft()
    arr.append(i)

print(arr[0])
