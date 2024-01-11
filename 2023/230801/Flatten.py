T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    dump = 1
    arr.sort()
    while dump <= N:
        if arr[-1] - arr[0] <= 1:
            break
        else:
            arr[-1] -= 1
            arr[0] += 1
            arr.sort()
            dump += 1

    result = arr[-1] - arr[0]

    print(f'#{tc} {result}')