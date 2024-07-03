import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
visited = set()
queue = deque()
queue.append((A, 1))

while queue:
    now, cnt = queue.popleft()

    if now == B:
        print(cnt)
        sys.exit()

    for next in [int(str(now)+'1'), now*2]:
        if next > B:
            continue
        if next not in visited:
            visited.add(next)
            queue.append((next, cnt + 1))
print(-1)
