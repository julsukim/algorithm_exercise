'''
카운트 2차원 배열 활용
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
ground = [[0] * 101 for _ in range(101)]
cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if ground[i][j] == 0:
                cnt += 1
                ground[i][j] = 1
print(cnt)