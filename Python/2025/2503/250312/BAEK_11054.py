n = int(input())
arr = list(map(int, input().split()))

# 증가하는 부분 수열 길이
dp_inc = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

# 감소하는 부분 수열 길이 계산
dp_dec = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

# 바이토닉 최대 길이 계산
max_length = 0
for i in range(n):
    max_length = max(max_length, dp_inc[i] + dp_dec[i] - 1)

print(max(dp_inc[i] + dp_dec[i] - 1 for i in range(n)))
