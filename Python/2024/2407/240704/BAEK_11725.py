from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

visited = [-1]*(N+1)
queue = deque()
queue.append(1)
visited[1] = 0
while queue:
    now = queue.popleft()

    for next in arr[now]:
        if visited[next] == -1:
            visited[next] = now
            queue.append(next)

print('\n'.join(map(str, visited[2:])))
