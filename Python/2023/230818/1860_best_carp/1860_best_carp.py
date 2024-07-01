import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    visit = list(map(int, input().split()))
    visit.sort()

    print(f'#{tc}', end=' ')
    for i in range(N):
        if (visit[i] // M) * K - (i+1) <= 0:
            print('Impossible')
            break
    else:
        print('Possible')
