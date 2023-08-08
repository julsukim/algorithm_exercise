import sys
sys.stdin = open('input.txt')


def row_palindrome(pal, N, M):    # 행에서 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(N - 1, j, -1):
                if (pal[i][j] == pal[i][k]) and ((k - j) == M - 1):
                    sp = j
                    ep = k
                    for l in range(0, (j + k) // 2 - 1):
                        if pal[i][j + l] != pal[i][k - l]:
                            break
                    else:
                        for q in range(sp, ep + 1):
                            print(f'{pal[i][q]}', end='')
                        print()


def col_palindrome(pal, N, M):
    for j in range(N):
        for i in range(N - M + 1):
            for k in range(N - 1, i, -1):
                if (pal[i][j] == pal[k][j]) and ((k - i) == M - 1):
                    sp = i
                    ep = k
                    for l in range(0, (i + k) // 2 - 1):
                        if pal[i + l][j] != pal[k - l][j]:
                            break
                    else:
                        for q in range(sp, ep + 1):
                            print(f'{pal[q][j]}', end='')
                        print()


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_list = [input() for _ in range(N)]

    print(f'#{tc}', end=' ')
    row_palindrome(str_list, N, M)
    col_palindrome(str_list, N, M)