from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dq = deque()
dq.append(N)
distance = [0] * 100001
result, cnt = 0, 0

while dq:
    now = dq.popleft()
    temp = distance[now]
    if now == K:
        result = temp
        cnt += 1
        continue

    for next in [now-1, now+1, now*2]:
        if 0 <= next < 100001 and (distance[next] == 0 or distance[next] == distance[now] + 1):
            distance[next] = distance[now] + 1
            dq.append(next)

print(result)
print(cnt)
