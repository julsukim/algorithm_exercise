'''
V E (Vertex(노드 개수), Edge(간선 개수))
v1 w1 v2 w2 ... (간선 표현)
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(start, V, adj_m):
    stack = []
    visited = [0] * (V+1)
    visited[start] = 1
    n = start
    while True:
        for w in range(1, V+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)
