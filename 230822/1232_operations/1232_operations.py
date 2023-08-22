import sys
sys.stdin = open('input.txt')


def operation(n):
    if n:
        a = operation(ch1[n])
        b = operation(ch2[n])
        if tree[n] in operations:
            if tree[n] == '+':
                return int(a) + int(b)
            elif tree[n] == '*':
                return int(a) * int(b)
            elif tree[n] == '-':
                return int(a) - int(b)
            else:
                return int(a) // int(b)
        else:
            return tree[n]


operations = '+-/*'

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    for _ in range(N):
        try:
            arr = list(input().split())
            tree[int(arr[0])] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
        except IndexError:
            pass

    result = operation(1)
    print(f'#{tc} {result}')