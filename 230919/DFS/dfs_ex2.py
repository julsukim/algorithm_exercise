'''
V E (Vertex(노드 개수), Edge(간선 개수))
v1 w1 v2 w2 ... (간선 표현)
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(s, V):
    visited = [False for _ in range(V+1)]
    print(visited)
    stack = []
    visited[s] = True
    stack.append(s)
    while True:
        is_find = False
        for w in adj_list[s]:
            if not visited[w]:
                stack.append(w)
                s = w
                print(s)
                visited[s] = True
                is_find = True
                break

        if not is_find:
            if stack:
                s = stack.pop()
            else:
                break
    return


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_list = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

dfs(1, V)
