import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    cnt = 0
    for i in range(1, 1 << N):
        subset_list = []
        subset_sum = 0
        for j in range(N):
            if i & (1 << j):
                subset_list.append(num_list[j])
                subset_sum += num_list[j]
        if len(subset_list) == N and subset_sum == K:
            cnt += 1

    print(f'#{tc} {cnt}')
