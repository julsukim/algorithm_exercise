'''
3
1 2 3
4 5 6
7 8 9
'''
di = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0 # 모든 원소가 0 이상이라면...
for i in range(N): # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        s = arr[i][j]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]