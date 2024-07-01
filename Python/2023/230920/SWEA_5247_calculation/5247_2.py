from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(n):
    visited[n] = 1
    dq.append(n)
    while len(dq) > 0:
        if visited[M] != 0:
            break
        t = dq.popleft()
        if t == M:
            break
        for i in [t+1, t-1, t*2, t-10]:
            if 0 < i <= 1000000 and visited[i] == 0:
                dq.append(i)
                visited[i] = visited[t]+1
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    dq = deque()

    bfs(N)
    print(f'#{tc} {visited[M]-1}')