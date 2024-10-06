import sys
input = sys.stdin.readline

TC = int(input().rstrip())
result = []


def solution(string):
    string_list = list(string)
    N = len(string_list)

    data = [''] * (N+2)
    prev = [-1] * (N+2)
    next = [-1] * (N+2)

    unused = 1
    cursor = 0

    for query in string_list:
        if query == '<':
            if prev[cursor] != -1:
                cursor = prev[cursor]
        elif query == '>':
            if next[cursor] != -1:
                cursor = next[cursor]
        elif query == '-':
            if cursor != 0:
                if prev[cursor] == 0:
                    next[prev[cursor]] = next[cursor]
                    prev[next[cursor]] = prev[cursor]
                elif next[cursor] == -1:
                    next[prev[cursor]] = -1
                elif next[cursor] != -1:
                    next[prev[cursor]] = next[cursor]
                    prev[next[cursor]] = prev[cursor]
                cursor = prev[cursor]
        else:
            data[unused] = query
            prev[unused] = cursor
            next[unused] = next[cursor]
            if next[cursor] != -1:
                prev[next[cursor]] = unused
            next[cursor] = unused
            cursor = unused
            unused += 1

    result = []
    idx = next[0]
    while idx != -1:
        result.append(data[idx])
        idx = next[idx]

    return ''.join(result)


for _ in range(TC):
    words = input().rstrip()
    result.append(solution(words))

print('\n'.join(result))
