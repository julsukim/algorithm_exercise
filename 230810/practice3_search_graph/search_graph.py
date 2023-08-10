import sys
sys.stdin = open('input.txt')

def dfs(start, V, adj_arr):
    stack = []
    visited = [False] * (V+1)
    result = []

    v = start
    result.append(v)
    visited[v] = True

    while True:
        is_find = False
        for idx in range(V+1):
            if adj_arr[v][idx] and visited[idx] == False:
                stack.append(v)
                v = idx
                result.append(v)
                visited[v] = True
                is_find = True
                break

        if is_find == False:
            if len(stack) != 0:
                v = stack.pop()
            else:
                break

    return result

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_arr = [[0] * (V+1) for _ in range(V+1)]
    for idx in range(E):
        x = arr[idx*2]
        y = arr[idx*2 + 1]
        adj_arr[x][y] = 1
        adj_arr[y][x] = 1

    result = dfs(1, V, adj_arr)
    print(f'#{tc} {"-".join(map(str, result))}')