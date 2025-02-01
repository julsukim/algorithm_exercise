import sys


def is_balanced(line):
    stack = []
    bracket_pairs = {')': '(', ']': '['}

    for char in line:
        if char in "([":  # 여는 괄호면 스택에 추가
            stack.append(char)
        elif char in ")]":  # 닫는 괄호면 짝 검사
            if not stack or stack[-1] != bracket_pairs[char]:
                return "no"
            stack.pop()

    return "yes" if not stack else "no"


while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break
    print(is_balanced(line))
