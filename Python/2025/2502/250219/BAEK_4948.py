import sys
input = sys.stdin.readline

maximum = 123457 * 2

matrix = [True] * maximum
matrix[0] = matrix[1] = False

for i in range(2, int(maximum**0.5) + 1):
    if matrix[i]:
        for j in range(i*i, maximum, i):
            matrix[j] = False

# 직접 세지 않고 누적합 배열을 만들어 둔다.
prefix = [0] * maximum
for i in range(1, maximum):
    prefix[i] = prefix[i-1] + (1 if matrix[i] else 0)

while True:
    N = int(input())
    if N == 0:
        break

    # cnt = matrix[N+1:(2 * N + 1)].count(True)
    print(prefix[2*N] - prefix[N])
