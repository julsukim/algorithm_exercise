import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    done = []
    d = 0
    cnt = 0
    while len(done) != M-1:
        if cnt == N + d:
            cnt = 0
        else:
            if cnt not in done and cheese[cnt] == 0:
                done.append(cnt)
                if len(done) > M - N:
                    d = M-N
                else:
                    d = len(done)
            cheese[cnt] = cheese[cnt] // 2
            cnt += 1
