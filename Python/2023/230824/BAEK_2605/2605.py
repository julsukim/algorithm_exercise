import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))

result = []

for i in range(N):
    result.insert(nums[i], i+1)

for i in range(N-1, -1, -1):
    print(result[i], end=' ')
print()