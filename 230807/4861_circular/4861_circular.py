import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    letters = [list(input()) for _ in range(N)]

    result_let = ''
    for i in range(0, N):
        let = ''
        for j in range(0, N//2):
            if letters[i][j] == letters[i][N-1-j]:
                let += letters[i][j]
                print(let)
                if len(let) >= M//2:
                    result_let = let

    print(f'#{tc} {result_let}')