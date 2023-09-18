import sys
sys.stdin = open('input.txt')


def seekMinimum(month, s):
    global minimum
    if minimum < s:
        return
    if month >= 12:
        if minimum > s:
            minimum = s
        return
    else:
        seekMinimum(month + 1, s + (plans[month] * prices[0]))
        seekMinimum(month + 1, s + prices[1])
        seekMinimum(month + 3, s + prices[2])


T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    minimum = prices[3]
    seekMinimum(0, 0)
    print(f'#{tc} {minimum}')