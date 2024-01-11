'''
10 7 9일 때, 안사는 이유.
이후의 가격이 더 싸기 때문.
이후에 더 비싼 것이 있으면 일단 사자
언제 팔까?
가장 가격이 비쌀 때
ex 3 5 9
3 -> 9 이익 +6
5 -> 9 이익 +4

누적 이익 ans
모든 날 i, 1~N일 동안
i+1 -> N일 사이
    i일 이후의 최댓값 max_v 찾기
if price[i] < max_v
    ans += max_v - price[i]

N-1일 까지는 사도되지만, 마지막 N일에는 팔수없으니까 사면 안됨

ans = 0
    for i : 0 -> N-1 -1
        imax-v = price[i+1]
        for j: i+2 -> N-1
            if ... # 최댓값 찾기
-> 이렇게 하면 시간 초과...

오른쪽 부터 최대 가격 구하기
(중복 검사를 없애기 위해서..!)
연산량을 줄이기

imax_v = price[N-1] # i+1 -> N-1까지의 최대가격
for i : N-2 -> 0
    # if imax_v > price[i]:
    #     ans += imax_v - price[i] # 그 날의 이익
    ans += max(imax_v - price[i], 0) # 이익이 0보다 크면 이익, 작으면 0
    imax_v = max(price[i], imax_v) # 구간의 최대가격으로
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    total_b = 0
    max_price = prices[N-1]
    for i in range(N-2, -1, -1):
        if max_price > prices[i]:
            total_b += max_price - prices[i]
        else:
            max_price = prices[i]

    print(f'#{tc} {total_b}')