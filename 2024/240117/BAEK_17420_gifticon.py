# 기프티콘 N개 선물
# 기한이 있다~~ 연장할 때마다 30일씩 늘어난다
# 기한 연장 너무 귀차나..
# 기한 연장 최소한으로 사용할래
# 기한이 가장 적게 남은 기프티콘만 사용할 수 있다구~
# 기한이 가장 적게 남은 기프티콘이 여러개면 아무거나 선택 가능~~
# 하루에 여러 기프티콘을 사용하거나 연장하는 것 모두 가능해..!
# 기한 연장을 해야하는 최소 횟수를 출력하자!
import sys
import math
input = sys.stdin.readline


# 기프티콘의 수 1<=N<=100000
N = int(input())
# i번째 기프티콘의 남은 기한은 Ai일 1<=Ai<=1000000000
deadline = list(map(int, input().split()))
# i번째 기프티콘을 Bi일 뒤에 사용할 계획 1<=Bi<=1000000000
use_plan = list(map(int, input().split()))

match = []
for r, p in zip(deadline, use_plan):
    match.append([r, p])

gifticon = sorted(match, key= lambda x: (x[1], x[0]))

maximum = gifticon[0][0]
criterion = gifticon[0][1]
count = 0
for i in range(N):
    if criterion > gifticon[i][0]:
        temp = math.ceil((criterion - gifticon[i][0]) / 30)
        count += temp
        gifticon[i][0] += temp * 30

    maximum = max(maximum, gifticon[i][0])

    if i+1 < N and gifticon[i][1] != gifticon[i+1][1]:
        criterion = max(maximum, gifticon[i+1][1])
print(count)
