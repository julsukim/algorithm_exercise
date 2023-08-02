N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 오른쪽 아래 방향 대각선 값의 총 합?
total1 = 0
for i in range(N):
    total1 += arr[i][i]

# 왼쪽 아래 방향 대각선 값의 총 합?
total2 = 0
for i in range(N):
    total2 += arr[i][N-1-i]