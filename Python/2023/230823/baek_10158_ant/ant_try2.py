import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    W, H = map(int, input().split())
    p, q = map(int, input().split())
    T = int(input())

    if W - (T + p) >= 0:
        r_p_t = T + p
    else:
        r_p_t = T - (W - p)
        p_cnt = 0
        while r_p_t - W >= 0:
            r_p_t -= W
            p_cnt += 1
        if p_cnt % 2 == 0:
            r_p_t = W - r_p_t

    if H - (T + q) >= 0:
        r_q_t = T + q
    else:
        r_q_t = T - (H - q)
        q_cnt = 0
        while r_q_t - H >= 0:
            r_q_t -= H
            q_cnt += 1
        if q_cnt % 2 == 0:
            r_q_t = H - r_q_t

    print(r_p_t, r_q_t)