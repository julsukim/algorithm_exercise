import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(s):
    global cnt
    visited[s] = cnt
    for w in arr[s]:
        if visited[w] == 0:
            cnt += 1
            dfs(w)


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    v, v2 = map(int, input().split())
    arr[v].append(v2)
    arr[v2].append(v)

cnt = 1
for l in arr:
    l.sort(reverse=True)
visited = [0] * (N+1)

dfs(R)
for k in range(1, N+1):
    print(visited[k])
