import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    str_in = ''
    for _ in range(N):
        str_in += input().strip()

    print(f'#{tc}', end=' ')
    for i in range(0, 10):
        output = ''
        for j in range(7*i, 7*(i+1)):
            output += str_in[j]
        print(int(output, 2), end=' ')
    print()