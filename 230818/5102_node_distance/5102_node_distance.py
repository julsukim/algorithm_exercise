import sys
sys.stdin = open('input.txt')


def enQueue(value):
    global front
    front += 1
    queue[front] = value


def deQueue():
    global rear
    rear += 1
    return queue[rear]


def is_empty():
    return front == rear


def bfs(start, goal, V):
    visited = [0] * (V+1)
    enQueue(start)
    visited[start] = 1
    while not is_empty():
        t = deQueue()
        for w in range(V+1):
            if adj_arr[t][w] == 1 and visited[w] == 0:
                enQueue(w)
                visited[w] = visited[t] + 1
                if w == goal:
                    return visited[w] - 1

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj_arr = [[0]*(V+1) for _ in range(V+1)]
    for k in range(E):
        i = arr[k][0]
        j = arr[k][1]
        adj_arr[i][j] = 1
        adj_arr[j][i] = 1

    queue = [0] * 100
    front = -1
    rear = -1

    ans = bfs(S, G, V)
    print(f'#{tc} {ans}')