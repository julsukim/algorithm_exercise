import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0
for i in range(len(P)):
    result += sum(P[:i+1])
print(result)
