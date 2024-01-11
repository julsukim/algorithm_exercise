from collections import deque


def makeone(s):
    global cnt
    dq.append(s)
    visited = [0]*(N+1)
    visited[s] = 1
    while dq:
        cnt += 1
        n = dq.popleft()
        if n == 1:
            break
        if n%2==0 and visited[n//2]==0:
            visited[n//2] = visited[n] + 1
            dq.append(n//2)
        if n%3==0 and visited[n//3]==0:
            visited[n//3] = visited[n] + 1
            dq.append(n//3)
        if visited[n-1]==0:
            visited[n-1] = visited[n] + 1
            dq.append(n-1)

    cnt = visited[1]


N = int(input())

cnt = 0
dq = deque()
makeone(N)
print(cnt-1)
