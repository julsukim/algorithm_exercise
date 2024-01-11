import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
meet = []
for _ in range(N):
    meet.append(list(map(int, input().split())))

meet.sort(key=lambda x:(x[1], x[0]))

res = [meet[0]]
num = 1
j = 0
for i in range(1, N):
    if meet[i][0] >= meet[j][1]:
        num += 1
        j = i
print(num)
