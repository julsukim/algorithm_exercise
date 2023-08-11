import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop = [int(input()) for _ in range(P)]

    stops = [0]*5001
    for i in range(N):
        for j in range(line[i][0], line[i][1]+1):
            stops[j] += 1

    print(f'#{tc}', end=' ')
    for i in stop:
        print(stops[i], end=' ')
    print()