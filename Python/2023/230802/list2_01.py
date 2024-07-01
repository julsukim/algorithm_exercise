N = 2 # 행의 크기
M = 4 # 열의 크기
arr = [[0, 1, 2, 3],[4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j])
print('-')
for j in range(M):
    for i in range(N):
        print(arr[i][j])
print('-')
for i in range(N):
    for j in range(M):
        if i%2: # 홀수번 행인 경우
        else:

# 열의 크기가 다른 경우
for i in arr2:
    for j  in range(arr[i]):
        pass
for i in range(N2):
    for j  in range(len(N2[i])):
        pass

# 0으로 채운 2차원 배열 생성
arr = [[0]*M for _ in range(N)]
arr2 = [[0]*M]*N # 안됨
arr[0][0] = 1
arr2[0][0] = 1

# 위치 신경쓰기
max_v = 0
for i in range(N):
    row_total = 0
    for j in range(M):
        row_total += arr[i][j]
    if max_v < row_total:
        max_v = row_total
