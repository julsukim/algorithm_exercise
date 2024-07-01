import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    W, H = map(int, input().split())
    p, q = map(int, input().split())
    T = int(input())

    if W - (T + p) >= 0:
        x = T + p
    else:
        r_x_t = T - (W - p)
        x = r_x_t % W
        x_cnt = r_x_t // W
        if x_cnt % 2 == 0:
            x = W - x

    if H - (T + q) >= 0:
        y = T + q
    else:
        r_y_t = T - (H - q)
        y = r_y_t % H
        y_cnt = r_y_t // H
        if y_cnt % 2 == 0:
            y = H - y

    print(x, y)