import sys
sys.stdin = open('input.txt')


def row_palindrome(pal, N, M):
    count = 0
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M//2):
                if pal[i][j + k] != pal[i][j + M - k - 1]:
                    break
            else:
                count += 1
    return count


def col_palindrome(pal, N, M):
    count = 0
    for j in range(N):
        for i in range(N - M + 1):
            for k in range(M // 2):
                if pal[i + k][j] != pal[i + M - k - 1][j]:
                    break
            else:
                count += 1
    return count


T = 10
for tc in range(1, T + 1):
    N = 8
    M = int(input())
    letter_board = [input() for _ in range(N)]

    total_count = 0
    total_count += row_palindrome(letter_board, N, M)
    total_count += col_palindrome(letter_board, N, M)

    print(f'#{tc} {total_count}')