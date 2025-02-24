import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

L, C = map(int, input().split())
chars = input().split()
chars.sort()

vowels = {'a', 'e', 'i', 'o', 'u'}
result = []


def backtrack(start, current, v_count, c_count):
    # 현재 선택한 문자의 개수가 L이면
    if len(current) == L:
        if v_count >= 1 and c_count >= 2:
            result.append(current)
        return

    for i in range(start, C):
        if chars[i] in vowels:
            backtrack(i + 1, current + chars[i], v_count + 1, c_count)
        else:
            backtrack(i + 1, current + chars[i], v_count, c_count + 1)


backtrack(0, "", 0, 0)
print("\n".join(result))
