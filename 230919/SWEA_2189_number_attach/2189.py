import sys
sys.stdin = open('input.txt')


def seek(loc, cnt):
    if cnt == 7:
        result_result.append(str(result))
        return
    i, j = loc
    result[cnt] = arr[i][j]
    for k in range(4):
        ni, nj = i+d[k][0], j+d[k][1]
        if 0 <= ni < N and 0 <= nj < N:
            seek((ni, nj), cnt + 1)


d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [0]*7
    result_result = []

    for i in range(N):
        for j in range(N):
            seek((i, j), 0)

    print(f'#{tc} {len(set(result_result))}')
