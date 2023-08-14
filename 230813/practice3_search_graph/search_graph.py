import sys
sys.stdin = open('input.txt')

def dfs(start, V, arr):
    stack = []
    visited = [False] * (V+1)
    result = []

    v = start
    result.append(v)
    visited[v] = True

    while True:
        is_find = False
        for i in range(V+1):
            if arr[v][i] and visited[i] == False:
                stack.append(v)
                v = i
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

V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_arr = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    adj_i = arr[i*2]
    adj_j = arr[i*2+1]
    adj_arr[adj_i][adj_j] = 1
    adj_arr[adj_j][adj_i] = 1

result = dfs(1, V, adj_arr)
print(f'#1 {"-".join(map(str, result))}')
