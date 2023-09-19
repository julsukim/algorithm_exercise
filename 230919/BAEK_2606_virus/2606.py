import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(r):
    visited[r] = 1
    for w in arr[r]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)


V = int(input())
E = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

visited = [0]*(V+1)
dfs(1)
print(visited.count(1)-1)
