import sys
sys.stdin = open('input.txt')


def quickSort(arr, i, j):
    if i < j:
        s = partition(arr, i, j)
        quickSort(arr, i, s-1)
        quickSort(arr, s+1, j)


def partition(arr, i, j):
    p = arr[i]
    pi = i
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pi], arr[j] = arr[j], arr[pi]
    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quickSort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')
