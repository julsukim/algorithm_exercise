import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    dic = {}
    for i in range(M):
        dic[i+1] = cheese[i]

    cQ = list(range(N+1))
    cQsize = N+1

    front = 0
    rear = N
    done = []
    while len(done) < M:
        front = (front+1) % cQsize
        rear = (rear+1) % cQsize
        dic[cQ[front]] = dic[cQ[front]] // 2
        if dic[cQ[front]] == 0 and cQ[front] not in done:
            done.append(cQ[front])
            if len(done) + (N-1) < M:
                cQ[front] = len(done) + N
            cQ[rear] = cQ[front]
        else:
            cQ[rear] = cQ[front]

    print(f'#{tc} {done[-1]}')