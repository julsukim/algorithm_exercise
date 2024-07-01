N = 9
arr = [[0]*N for _ in range(N)]
arr[4][4] = 1

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            cnt = 0
            for k in range(4):
                cnt += 1
                for l in range(0, k):
                    arr[i-k+l][j+l] = cnt
                    arr[i+l][j+k-l] = cnt
                    arr[i+k-l][j-l] = cnt
                    arr[i-l][j-k+l] = cnt

print(arr)