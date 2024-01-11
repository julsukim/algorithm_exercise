'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, V):    # 시작정점 s, 마지막 정점 V
    visited = [0] * (V+1)       # visited 생성
    queue = []                  # queue 생성
    queue.append(s)             # 시작점 enQ
    visited[s] = 1              # 시작점 방문표시
    while queue:                # queue에 정점이 남아있으면 front != rear
        t = queue.pop(0)        # deQ
        print(t)                # 방문한 정점에서 할 일
        for w in adj_l[t]:      # 인접한 정점 중 enQ되지 않은 정점 w가 있으면
            if visited[w]==0:
                queue.append(w) # enQ(w), enQ되었음을 표시
                visited[w] = visited[t] + 1


V, E = map(int, input().split())    # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 --------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

bfs(1, 7)
print(adj_l)