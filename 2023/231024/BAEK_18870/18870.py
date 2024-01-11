import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr2 = list(set(arr))
arr2.sort()

dic = {}
for i in range(len(arr2)):
    dic[arr2[i]] = i

for j in arr:
    print(dic[j], end=' ')