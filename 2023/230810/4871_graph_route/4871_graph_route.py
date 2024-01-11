import sys
sys.stdin = open('input.txt')

def dfs(start, goal, V, adj_arr):
    stack = []
    visited = [0] * (V+1)

    v = start
    visited[v] = 1

    while True:
        is_find = False
        for w in range(V+1):
            if adj_arr[v][w] == 1 and visited[w] == 0:
                stack.append(v)
                v = w
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
    for idx in range(E):
        x = arr[idx][0]
        y = arr[idx][1]
        adj_arr[x][y] = 1

    result = dfs(S, G, V, adj_arr)
    print(f'#{tc} {result}')