import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    change = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            count = 0
            for k in range(i+1):
                count += flag[k].count('W')
            for k in range(i+1, j+1):
                count += flag[k].count('B')
            for k in range(j+1, N):
                count += flag[k].count('R')
            change = max(change, count)

    print(N*M - change)
