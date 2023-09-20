from collections import deque
import sys
sys.stdin = open('input.txt')


# def calculate(n, cnt):
#     global minimum
#     if cnt > minimum:
#         return
#     if n == M:
#         if minimum > cnt:
#             minimum = cnt
#             return
#     for w in [n+1, n-1, n*2, n-10]:
#         if 0 < w < 1000000:
#             calculate(w, cnt + 1)


def bfs(n, c):
    global minimum
    dq.append([n])
    cnt = c
    visited.add(n)
    while True:
        if cnt > minimum:
            break
        r = []
        for v in dq[cnt]:
            if v == M:
                if minimum > cnt:
                    minimum = cnt
                    continue
            if 0 < v < (M + 11):
                for w in [v+1, v-1, v*2, v-10]:
                    if 0 < w < (M + 11) and w not in visited:
                        visited.add(w)
                        r.append(w)
        else:
            dq.append(r)
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    minimum = abs(N-M)

    visited = set()
    dq = deque()
    bfs(N, 0)

    print(f'#{tc} {minimum}')
