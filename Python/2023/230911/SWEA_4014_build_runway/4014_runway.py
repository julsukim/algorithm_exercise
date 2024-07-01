import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    lines = N+N
    false_line = 0
    for i in range(N):
        is_down = False
        cnt = 1
        pre_h = area[i][0]
        for j in range(1, N):
            if abs(area[i][j] - pre_h) > 1:
                false_line += 1
                break
            if is_down == True:
                if area[i][j] == pre_h:
                    if j == (N-1) and (cnt+1) < X:
                        false_line += 1
                        break
                    else:
                        cnt += 1
                elif area[i][j] > pre_h:
                    is_down = False
                    if cnt < (2 * X):
                        false_line += 1
                        break
                    else:
                        cnt = 1
                else:
                    if (cnt < X) or (j == (N-1)):
                        false_line += 1
                        break
                    else:
                        cnt = 1
            else:
                if area[i][j] == pre_h:
                    cnt += 1
                elif area[i][j] > pre_h:
                    is_down = False
                    if cnt < X:
                        false_line += 1
                        break
                    else:
                        cnt = 1
                else:
                    if j == (N-1):
                        false_line += 1
                        break
                    else:
                        is_down = True
                        cnt = 1
            pre_h = area[i][j]

    for j in range(N):
        is_down = False
        cnt = 1
        pre_h = area[0][j]
        for i in range(1, N):
            if abs(area[i][j] - pre_h) > 1:
                false_line += 1
                break
            if is_down == True:
                if area[i][j] == pre_h:
                    if i == (N - 1) and (cnt+1) < X:
                        false_line += 1
                        break
                    else:
                        cnt += 1
                elif area[i][j] > pre_h:
                    is_down = False
                    if cnt < (2 * X):
                        false_line += 1
                        break
                    else:
                        cnt = 1
                else:
                    if (cnt < X) or (i == (N-1)):
                        false_line += 1
                        break
                    else:
                        cnt = 1
            else:
                if area[i][j] == pre_h:
                    cnt += 1
                elif area[i][j] > pre_h:
                    is_down = False
                    if cnt < X:
                        false_line += 1
                        break
                    else:
                        cnt = 1
                else:
                    if i == (N-1):
                        false_line += 1
                        break
                    else:
                        is_down = True
                        cnt = 1
            pre_h = area[i][j]

    print(f'#{tc} {lines - false_line}')
