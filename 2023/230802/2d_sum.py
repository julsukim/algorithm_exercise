T = 10
for tc in range(1, T+1):
    TC = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0

    for i in range(N):
        row_max = 0
        for j in range(N):
            row_max += arr[i][j]
        if row_max > maximum:
            maximum = row_max

    for j in range(N):
        col_max = 0
        for i in range(N):
            col_max += arr[i][j]
        if col_max > maximum:
            maximum = col_max

    diag_sum = 0
    rev_diag_sum = 0
    for k in range(N):
        diag_sum += arr[k][k]
        rev_diag_sum += arr[k][N-1-k]

    if diag_sum > maximum:
        maximum = diag_sum
    if rev_diag_sum > maximum:
        maximum = rev_diag_sum

    print(f'#{TC} {maximum}')