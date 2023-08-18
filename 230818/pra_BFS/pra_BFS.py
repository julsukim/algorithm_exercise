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


def bfs(s, V):
    visited = [0] * E
    enQueue(s)
    visited[s] = 1
    visit_list = []
    visit_list.append(s)
    while not is_empty():
        t = deQueue()
        for w in range(1, V+1):
            if adj_m[t][w]==1 and visited[w]==0:
                enQueue(w)
                visited[w] = 1
                visit_list.append(w)

    return visit_list


T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    queue = [0] * E
    front = -1
    rear = -1

    adj_m = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adj_m[v1][v2] = 1
        adj_m[v2][v1] = 1

    ans = bfs(1, V)
    print(f'#{tc} {" ".join(map(str, ans))}')