import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    W, H = map(int, input().split())
    p, q = map(int, input().split())
    T = int(input())

    r_time = T
    p_time = 0
    dir = 1
    while True:
        if dir == 1:
            movep = W - p
            moveq = H - q
            if movep < moveq:
                dir = 4
                move = movep
            elif movep == moveq:
                dir = 3
                move = movep
            else:
                dir = 2
                move = moveq
            if r_time - move > 0:
                r_time -= move
                p_time += move
                p += move
                q += move
            else:
                move = T - p_time
                p += move
                q += move
                break

        elif dir == 2:
            movep = W - p
            moveq = q
            if movep < moveq:
                dir = 3
                move = movep
            elif movep == moveq:
                dir = 4
                move = movep
            else:
                dir = 1
                move = moveq
            if r_time - move > 0:
                r_time -= move
                p_time += move
                p += move
                q -= move
            else:
                move = T - p_time
                p += move
                q -= move
                break

        elif dir == 3:
            movep = p
            moveq = q
            if movep < moveq:
                dir = 2
                move = movep
            elif movep == moveq:
                dir = 1
                move = movep
            else:
                dir = 4
                move = moveq
            if r_time - move > 0:
                r_time -= move
                p_time += move
                p -= move
                q -= move
            else:
                move = T - p_time
                p -= move
                q -= move
                break

        else:
            movep = p
            moveq = H - q
            if movep < moveq:
                dir = 1
                move = movep
            elif movep == moveq:
                dir = 2
                move = movep
            else:
                dir = 3
                move = moveq
            if r_time - move > 0:
                r_time -= move
                p_time += move
                p -= move
                q += move
            else:
                move = T - p_time
                p -= move
                q += move
                break

    print(p, q)