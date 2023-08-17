import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):
    TC = int(input())
    arr = list(map(int, input().split()))

    cQsize = 9
    cQ = [0] * cQsize

    for i in range(len(arr)):
        cQ[i+1] = arr[i]

    front = 0
    rear = 8
    i = 0

    while cQ[rear] > 0:
        if i == 5:
            i = 0
        i += 1
        front = (front + 1) % cQsize
        rear = (rear + 1) % cQsize
        cQ[rear] = cQ[front] - i
    cQ[rear] = 0

    print(f'#{tc}', end=' ')
    for i in range(front+1, cQsize):
        print(cQ[i], end=' ')
    for i in range(0, front):
        print(cQ[i], end=' ')
    print()