import sys
sys.stdin = open('input.txt')

def dfs(start, goal, V, arr):
    stack = []
    visited = [0] * (V+1)

    v = start
    visited[v] = 1
    while True:
        is_find = False
        for i in range(V+1):
            if arr[v][i] == 1 and visited[i] == 0:
                stack.append(v)
                v = i
                visited[v] = 1
                is_find = True
                break
        if is_find == False:
            if len(stack) != 0:
                v = stack.pop()
            else:
                break

    result = visited[goal]
    return result

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj_arr = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        x = arr[i][0]
        y = arr[i][1]
        adj_arr[x][y] = 1

    result = dfs(S, G, V, adj_arr)
    print(result)