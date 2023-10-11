def dfs(k):
    s = k
    while True:
        for w in adj_arr[s]:
            if visited[w] == 0:
                stack.append(s)
                result[k][w] = 1
                s = w
                visited[s] = 1
                break
        else:
            if len(stack) != 0:
                s = stack.pop()
            else:
                break
    return


def dfs2(s, k):
    for w in adj_arr[k]:
        if visited[w] == 0:
            visited[w] = 1
            result[s][w] = 1
            dfs2(s, w)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

adj_arr = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            adj_arr[i].append(j)

result = [[0]*N for _ in range(N)]

for i in range(N):
    stat = i
    visited = [0] * N
    stack = []
    dfs2(stat, i)

for i in range(N):
    print(*result[i])
