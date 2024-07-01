import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    counts = [0] * 10

    for i in range(0, N):
        counts[cards[i]] += 1

    max_cards = 0
    max_num = 0
    for i in range(0, 10):
        if counts[i] >= max_cards:
            max_cards = counts[i]
            max_num = i

    print(f'#{tc} {max_num} {max_cards}')
