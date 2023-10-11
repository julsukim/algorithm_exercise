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


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

adj_arr = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            adj_arr[i].append(j)

result = [[0]*N for _ in range(N)]

for i in range(N):
    visited = [0] * N
    stack = []
    dfs(i)

for i in range(N):
    print(*result[i])
