import sys
sys.stdin = open('input.txt')


def min_sum(idx, s):
    global minimum

    if s > minimum:
        return
    if idx == N:
        if minimum > s:
            minimum = s

    for swap_idx in range(idx, N):
        selected[idx], selected[swap_idx] = selected[swap_idx], selected[idx]
        min_sum(idx + 1, s + arr[idx][selected[idx]])
        selected[idx], selected[swap_idx] = selected[swap_idx], selected[idx]

    return minimum


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    selected = list(range(0, N))
    minimum = 987654321

    print(f'#{tc} {min_sum(0, 0)}')