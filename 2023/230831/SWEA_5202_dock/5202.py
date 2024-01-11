import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr = [[0, 0]] + arr
    arr.sort(key=lambda x:x[1])
    print(arr)

    S = []
    j = 0
    for i in range(1, N + 1):
        if arr[i][0] >= arr[j][1]:  # si >= fj
            S.append(i)
            j = i
    print(f'#{tc} {len(S)}')