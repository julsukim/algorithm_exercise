import sys
sys.stdin = open('input.txt')

def dfs(start, V, adj_arr):
    stack = []
    visited = [0] * V

    v = start
    visited[v] = 1

    while True:
        is_find = False
        for w in range(V):
            if adj_arr[v][w] == 1 and visited[w] == False:
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

    result = visited[99]
    return result


T = 10
for tc in range(1, T+1):
    TC, E = map(int, input().split())
    V = 100
    arr = list(map(int, input().split()))

    adj_arr = [[0] * V for _ in range(V)]
    for idx in range(E):
        x = arr[idx * 2]
        y = arr[idx * 2 + 1]
        adj_arr[x][y] = 1

    result = dfs(1, V, adj_arr)
    print(f'#{TC} {result}')