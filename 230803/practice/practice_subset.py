import sys
sys.stdin = open('input_subset.txt')

T = int(input())
for tc in range(1, T+1):
    int_list = list(map(int, input().split()))
    N = len(int_list)

    ans = 0

    for i in range(1, 1<<N):
        subset_sum = 0
        for j in range(N):
            if i & (1<<j):
                subset_sum += int_list[j]
        if subset_sum == 0:
            ans = 1

    print(f'#{tc} {ans}')