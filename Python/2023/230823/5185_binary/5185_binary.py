import sys
sys.stdin = open('input.txt')

hexd = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

T = int(input())
for tc in range(1, T+1):
    N, str_in = input().split()

    converted = ''
    for i in range(int(N)):
        if str_in[i] in hexd:
            num = hexd[str_in[i]]
        else:
            num = int(str_in[i])
        for j in range(3, -1, -1):
            converted += str(num // 2**j)
            num = num % 2**j
    print(f'#{tc} {converted}')