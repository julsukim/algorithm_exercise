# import sys
# sys.stdin = open('input.txt')

def movemove(loc, d):
    global cnt
    if loc == (N-1, N-1):
        cnt += 1
        return

    i, j = loc
    if d == 1:
        if (j+1)<N:
            if arr[i][j+1] == 0:
                movemove((i, j+1), 1)
            else:
                return
        if (i+1)<N and (j+1)<N:
            if arr[i][j+1] == 0 and arr[i+1][j+1] == 0 and arr[i+1][j] == 0:
                movemove((i+1, j+1), 3)

    elif d == 2:
        if (i+1)<N:
            if arr[i+1][j] == 0:
                movemove((i+1, j), 2)
            else:
                return
        if (i + 1) < N and (j + 1) < N:
            if arr[i][j + 1] == 0 and arr[i + 1][j + 1] == 0 and arr[i + 1][j] == 0:
                movemove((i + 1, j + 1), 3)

    elif d == 3:
        if (j + 1) < N:
            if arr[i][j + 1] == 0:
                movemove((i, j + 1), 1)

        if (i + 1) < N:
            if arr[i + 1][j] == 0:
                movemove((i + 1, j), 2)

        if (i + 1) < N and (j + 1) < N:
            if arr[i][j + 1] == 0 and arr[i + 1][j + 1] == 0 and arr[i + 1][j] == 0:
                movemove((i + 1, j + 1), 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
movemove((0, 1), 1)
print(cnt)
