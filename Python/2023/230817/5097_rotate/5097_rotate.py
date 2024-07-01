import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    cQ = [0]
    for i in arr:
        cQ.append(i)

    front = 0
    rear = N

    cnt = 0
    while cnt < M%N:
        front = (front+1) % (N+1)
        rear = (rear+1) % (N+1)
        cQ[rear] = cQ[front]
        cnt += 1

    print(f'#{tc} {cQ[(front+1) % (N+1)]}')