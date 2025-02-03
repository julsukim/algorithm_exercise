# import sys
# input = sys.stdin.readline
#
# S = input().strip()
# N = len(S)
# prefix = [[0] * (N + 1) for _ in range(26)]
#
# for i in range(N):
#     c_index = ord(S[i]) - ord('a')
#     for j in range(26):
#         prefix[j][i+1] = prefix[j][i]
#     prefix[c_index][i+1] += 1
#
# q = int(input())
# answers = []
# for _ in range(q):
#     query = list(input().split())
#     word = query[0]
#     s = int(query[1])
#     e = int(query[2]) + 1
#     idx = ord(word) - ord('a')
#     count = prefix[idx][e] - prefix[idx][s]
#     answers.append(str(count))
#
# print('\n'.join(answers))


import sys
import itertools

input = sys.stdin.readline

s = input().rstrip()
n = len(s)
# 각 알파벳에 대한 누적합을 딕셔너리에 저장
prefix = {}
for ch in "abcdefghijklmnopqrstuvwxyz":
    # 각 알파벳 ch에 대해, s의 각 문자와 비교하여 1/0 값을 만든 후 누적합 계산
    prefix[ch] = [0] + list(itertools.accumulate(1 if c == ch else 0 for c in s))

q = int(input().rstrip())
for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    print(prefix[alpha][r + 1] - prefix[alpha][l])
