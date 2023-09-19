import sys
sys.stdin = open('input.txt')


def max_pro(i, v):
    global maximum
    if v < maximum:
        return
    if i == N:
        if maximum < v:
            maximum = v
            return
    for j in range(N):
        if visited[j] == 0 and pro[i][j] != 0:
            visited[j] = 1
            max_pro(i + 1, v * (pro[i][j]/100))
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pro = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    maximum = 0

    max_pro(0, 1)
    print(f"#{tc} {(maximum*100):.6f}")
