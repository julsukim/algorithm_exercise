from collections import deque
import sys
input = sys.stdin.readline

words = input().rstrip()
M = int(input().rstrip())
arr = [list(input().rstrip().split()) for _ in range(M)]


def solution(string, m, queries):
    left_stack = deque(list(string))
    right_stack = deque()

    for query in queries:
        if query[0] == "L":
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif query[0] == "D":
            if right_stack:
                left_stack.append(right_stack.popleft())
        elif query[0] == "B":
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(query[1])
    return "".join(map(str, list(left_stack) + list(right_stack)))


print(solution(words, M, arr))
