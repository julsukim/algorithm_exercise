import sys
input = sys.stdin.readline


def get_prefix(N, arr):
    prefixSum = [0] * (N+1)
    for i in range(1, N+1):
        prefixSum[i] = prefixSum[i-1] + arr[i-1]
    return prefixSum


N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefixSum = get_prefix(N, arr)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefixSum[j] - prefixSum[i-1])
