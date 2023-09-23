from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    dq = deque()
    dq.append(start)
    if visited[start] == 0:
        visited[start] = 1
    while dq:
        now = dq.popleft()
        check = visited[now]

        for next in arr[now]:
            if visited[next] == 0:
                dq.append(next)
                if check == 1:
                    visited[next] = 2
                else:
                    visited[next] = 1
            elif visited[next] == 1:
                if check == 1:
                    print("NO")
                    return False
            elif visited[next] == 2:
                if check == 2:
                    print("NO")
                    return False

    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        arr[v1].append(v2)
        arr[v2].append(v1)
    visited = [0]*(V+1)

    for k in range(1, V+1):
        if not bfs(k):
            break
    else:
        print("YES")
