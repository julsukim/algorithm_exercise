import sys
input = sys.stdin.readline


def vps(arr):
    stack = []
    for c in arr:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                prev = stack.pop()
                if prev == "(":
                    continue
    if stack:
        return False
    else:
        return True


T = int(input())
for _ in range(T):
    ps = list(input().rstrip())
    result = vps(ps)
    if result:
        print("YES")
    else:
        print("NO")
