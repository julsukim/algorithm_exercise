import sys
sys.stdin = open('input.txt')


def totalMoney(i, cnt, arr):
    if i == cnt-1:
        total.append(arr)
    pass


T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    cnt = 0
    for p in plans:
        if p != 0:
            cnt += 1

    total = []
    money = [0] * cnt
    for i in range(0, p):
        pass

