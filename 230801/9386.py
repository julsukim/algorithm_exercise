T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    max_count = 0
    count_one = 0
    for i in range(0, N):
        if arr[i] == 1:
            count_one += 1
            if count_one > max_count:
                max_count = count_one
        else:
            count_one = 0

    print(f'#{tc} {max_count}')