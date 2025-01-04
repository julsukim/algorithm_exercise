from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
word_list = [input().rstrip() for _ in range(N)]
first_word = word_list[0]
similar_cnt = 0

for i in range(1, N):
    diff = Counter(word_list[i])
    diff.subtract(first_word)

    abs_diff_cnt = sum(abs(x) for x in diff.values())
    diff_cnt = sum(diff.values())

    if abs_diff_cnt > 2:
        continue

    if abs(diff_cnt) > 1:
        continue

    similar_cnt += 1

print(similar_cnt)
