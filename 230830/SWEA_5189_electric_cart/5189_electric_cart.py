import sys
sys.stdin = open('input.txt')


def start_move(idx, N, s):
    global min_loss
    if idx == N:
        print(s, 's')
        print(area, idx)
        s += loss[area[idx-1]-1][area[idx]-1]
        print(s, 's2')
        ss.append(s)
        if min_loss > s:
            min_loss = s
        return
    for swap_idx in range(idx, N):
        area[idx], area[swap_idx] = area[swap_idx], area[idx]
        print(loss[area[idx - 1] - 1][area[idx] - 1], area)
        s += loss[area[idx - 1] - 1][area[idx] - 1]
        start_move(idx+1, N, s)
        area[idx], area[swap_idx] = area[swap_idx], area[idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    loss = [list(map(int, input().split())) for _ in range(N)]

    min_loss = 50000
    area = list(range(1, N+1)) + [1]
    k = loss[area[0] - 1][area[1] - 1]
    min_loss_arr = []
    ss = []
    start_move(1, N, 0)
    print(min_loss, ss, k)