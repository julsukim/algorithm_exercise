case_w = ['WBWBWBWB', 'BWBWBWBW'] * 4
case_b = ['BWBWBWBW', 'WBWBWBWB'] * 4


def coloring(si, sj):
    case_w_count = 0
    case_b_count = 0
    for i in range(8):
        for j in range(8):
            if case_w[i][j] != board[si+i][sj+j]:
                case_w_count += 1
            if case_b[i][j] != board[si+i][sj+j]:
                case_b_count += 1
    return min(case_w_count, case_b_count)


N, M = map(int, input().split())
board = [input() for _ in range(N)]

minimum = int(1e9)
for i in range(N):
    if i + 8 > N:
        break
    for j in range(M):
        if j + 8 > M:
            break
        tmp = coloring(i, j)
        if tmp < minimum:
            minimum = tmp

print(minimum)
