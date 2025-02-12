# import sys
# input = sys.stdin.readline
#
# T = int(input())
# answers = []
# for _ in range(T):
#     N = int(input())
#     cards = input().rstrip().split()
#
#     word = cards[0]
#     for i in range(1, N):
#         if ord(word[0]) - ord('A') >= ord(cards[i]) - ord('A'):
#             word = cards[i] + word
#         else:
#             word = word + cards[i]
#
#     answers.append(word)
#
# print('\n'.join(answers))


import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
answers = []

for _ in range(T):
    N = int(input())
    cards = input().split()
    dq = deque([cards[0]])  # 첫 카드를 덱에 추가

    for card in cards[1:]:
        # 덱의 왼쪽 끝 문자와 새 카드 비교 (파이썬에서는 문자 비교가 가능)
        if card <= dq[0]:
            dq.appendleft(card)
        else:
            dq.append(card)

    answers.append("".join(dq))  # 덱을 문자열로 변환

sys.stdout.write("\n".join(answers))
