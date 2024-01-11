import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    deadlock = 0
    for j in range(N):
        magnetics = []
        for i in range(N):
            if table[i][j] == 2 and len(magnetics) != 0:
                previous = magnetics.pop()
                if previous == 1:
                    deadlock += 1
                magnetics.append(table[i][j])
            elif table[i][j] == 1:
                magnetics.append(table[i][j])

    print(f'#{tc} {deadlock}')
