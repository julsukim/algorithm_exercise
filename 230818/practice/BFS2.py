'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, V):    # 시작정점 s, 마지막 정점 V
    visited = [0] * (V+1)
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        print(t)
        for w in range(1, V+1):
            if adj_m[t][w]==1 and visited[w]==0:
                queue.append(w)
                visited[w] = visited[t] + 1

    print(visited)


V, E = map(int, input().split())    # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접행렬 --------------------
adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

bfs(2, V)