import sys
input = sys.stdin.readline


def dfs(s, v):
    global cnt
    visited[s] = cnt
    while True:
        for w in arr[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                cnt += 1
                visited[s] = cnt
                break
        else:
            if len(stack) != 0:
                s = stack.pop()
            else:
                break
    return


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    v, v2 = map(int, input().split())
    arr[v].append(v2)
    arr[v2].append(v)

cnt = 1
for l in arr:
    l.sort()
visited = [0] * (N+1)
stack = []

dfs(R, N)
for k in range(1, N+1):
    print(visited[k])
