import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0

    for i in range(N):
        last += 1
        heap[last] = arr[i]
        parent = last // 2
        child = last

        while heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2

    ni = last
    count = 0
    while ni != 0:
        ni = ni // 2
        count += heap[ni]

    print(f'#{tc} {count}')
