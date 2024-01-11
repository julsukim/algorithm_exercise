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


def bfs(start, V):
    visited = [0] * (V+1)
    enQueue(start)
    visited[start] = 1
    max_call = 0
    while not is_empty():
        t = deQueue()
        for w in range(1, V+1):
            if adj_arr[t][w] == 1 and visited[w] == 0:
                enQueue(w)
                visited[w] = visited[t] + 1
                if max_call < visited[w]:
                    max_call = visited[w]

    max_call_list = []
    for i in range(V+1):
        if max_call == visited[i]:
            max_call_list.append(i)

    return max_call_list[-1]


T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    V = 100

    adj_arr = [[0] * (V+1) for _ in range(V+1)]
    for k in range(N//2):
        i, j = arr[k*2], arr[k*2+1]
        adj_arr[i][j] = 1

    queue = [0] * 10000
    front = -1
    rear = -1

    ans = bfs(S, V)
    print(f'#{tc} {ans}')
