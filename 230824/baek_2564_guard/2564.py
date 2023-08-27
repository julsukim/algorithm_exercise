'''
시계방향, 반시계방향
최단거리의 합
'''
import sys
sys.stdin = open('input.txt')

# 블록 동서남북 번호에 따른 맞은편 번호
b_num = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

W, H = map(int, input().split())
N = int(input())

stores = []
for i in range(N+1):        # 가게의 블록 위치, 좌표 값으로 정리하기
    b_dir, dis = map(int, input().split())
    loc = {
        1: (1, 0, dis),
        2: (2, H, dis),
        3: (3, dis, 0),
        4: (4, dis, W)
    }
    stores.append(loc[b_dir])

gb, gx, gy = stores.pop()   # 경비원의 현재 위치
distance = 0
for store in stores:
    b, x, y = store
    if store[0] != b_num[gb]:       # 가게가 반대편 블록에 있지 않으면
        distance += abs(x - gx)
        distance += abs(y - gy)
    else:                           # 가게가 반대편 블록에 있으면
        if gb == 1 or gb == 2:
            distance += H
            if y + gy > (W - y) + (W - gy):     # 시계방향이 빠르다면
                distance += (W - y) + (W - gy)
            else:
                distance += y + gy
        else:
            distance += W
            if x + gx > (H - x) + (H - gx):
                distance += (H - x) + (H - gx)
            else:
                distance += x + gx
print(distance)
