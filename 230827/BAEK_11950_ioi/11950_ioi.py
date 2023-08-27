import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    total_count = 0
    total_count += flag[0].count('R') + flag[0].count('B')
    total_count += flag[N-1].count('W') + flag[N-1].count('B')

    change = []
    for i in range(1, N-1):
        for_change = []
        for_change.append(flag[i].count('B') + flag[i].count('R'))
        for_change.append(flag[i].count('W') + flag[i].count('R'))
        for_change.append(flag[i].count('W') + flag[i].count('B'))
        change.append(for_change)
    print(change, total_count)

    min_count = 2500
    while True:
        if min_count > count:
            min_count = count
        count = 0
        count