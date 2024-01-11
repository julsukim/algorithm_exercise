T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    ML = list(map(int, input().split()))

    loc = [0] * (N+1)

    for i in range(0, M):
        loc[ML[i]] += 1

    here = 0
    count = 0
    cnt = 0
    while True:
        if here == N:
            break
        elif here+K >= N:
            break
        elif cnt == K:
            count = 0
            break
        elif loc[(here+K)] == 1:
            here += K
            cnt = 0
            count += 1
        elif loc[(here+K)] != 1:
            here -= 1
            cnt += 1


    print(f'#{tc} {count}')