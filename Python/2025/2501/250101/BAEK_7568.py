N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
rank = [1] * N
for i in range(N):
    for j in range(i, N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i] += 1
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            rank[j] += 1

print(*rank)
