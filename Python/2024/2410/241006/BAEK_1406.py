import sys
input = sys.stdin.readline

words = input().rstrip()
M = int(input().rstrip())
arr = [list(input().rstrip().split()) for _ in range(M)]


def solution(string, m, queries):
    cursor = len(string)
    str_list = [0] + list(string)
    for query in queries:
        if query[0] == "L":
            if cursor > 0:
                cursor -= 1
        elif query[0] == "D":
            if cursor < len(string):
                cursor += 1
        elif query[0] == "B":
            if cursor > 0:
                str_list = str_list[:cursor] + str_list[cursor+1:]
                cursor -= 1
        else:
            str_list = str_list[:cursor+1] + [query[1]] + str_list[cursor+1:]
            cursor += 1
    return "".join(map(str, str_list[1:]))


print(solution(words, M, arr))
