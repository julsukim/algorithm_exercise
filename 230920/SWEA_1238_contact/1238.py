from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(r):
    visited[r] = 1
    dq.append(r)
    while len(dq)!=0:
        t = dq.popleft()
        for w in arr[t]:
            if visited[w] == 0:
                dq.append(w)
                visited[w] = visited[t] + 1
    last = max(visited)
    last_list = []
    for i in range(101):
        if last == visited[i]:
            last_list.append(i)
    return max(last_list)


T = 10
for tc in range(1, T+1):
    E, R = map(int, input().split())
    e_in = list(map(int, input().split()))

    arr = [[] for _ in range(101)]
    for i in range(E//2):
        arr[e_in[i*2]].append(e_in[i*2+1])
    visited = [0]*101
    dq = deque()

    print(f'#{tc} {bfs(R)}')
