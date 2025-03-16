import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

ans = []
for row in range(N):
    tmp_row = []
    for i in range(K):
        tmp = 0
        for j in range(M):
            tmp += A[row][j] * B[j][i]
        tmp_row.append(str(tmp))
    ans.append(' '.join(tmp_row))

print('\n'.join(ans))
