import sys
sys.stdin = open('algo3_in.txt')

def dfs(start, V, arr):
    stack = []
    visited = [False] * (V+1)

    v = start
    visited[v] = True
    result = []
    result.append(v)
    while True:
        for w in range(V+1):
            is_find = False
            if (arr[v][w] == True) and (visited[w] == False):
                stack.append(v)
                v = w
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
S = int(input())
arr = list(map(int, input().split()))

adj_arr = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    x = arr[i*2]
    y = arr[i*2 + 1]
    adj_arr[x][y] = 1
    adj_arr[y][x] = 1

result = dfs(S, V, adj_arr)
print(f'#1 {"-".join(map(str, result))}')