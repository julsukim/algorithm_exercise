import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = 5
    letters = [list(input()) for _ in range(N)]
    longest = 0
    for k in range(N):
        if longest < len(letters[k]):
            longest = len(letters[k])

    print(f'#{tc}', end=' ')
    for j in range(longest):
        for i in range(N):
            try:
                print(letters[i][j], end='')
            except IndexError:
                continue
    print()
