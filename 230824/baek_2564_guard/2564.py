'''
시계방향, 반시계방향
최단거리의 합
'''
import sys
sys.stdin = open('input.txt')

block = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

W, H = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N+1)]

stores = []
for i in range(N+1):
    k = arr[i][1]
    loc = {
        1: (1, 0, k),
        2: (2, H, k),
        3: (3, k, 0),
        4: (4, k, W)
    }
    stores.append(loc[arr[i][0]])

B, X, Y = stores.pop()
dis = 0
for i in stores:
    b, x, y = i
    if i[0] != block[B]:
        dis += abs(x - X)
        dis += abs(y - Y)
    else:
        if B == 1 or B == 2:
            dis += H
            if y + Y > (W - y) + (W - Y):
                dis += abs((W - y) + (W - Y))
            else:
                dis += y + Y
        else:
            dis += W
            if x + X > (H - x) + (H - X):
                dis += abs((H - x) + (H - X))
            else:
                dis += x + X
print(dis)