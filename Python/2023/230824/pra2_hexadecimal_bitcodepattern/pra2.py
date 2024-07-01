import sys
sys.stdin = open('input.txt')

hexadecimal_nums = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

pattern_code = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001001': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

T = int(input())
for tc in range(1, T+1):
    hexadecimal = input().strip()

    converted = ''
    for i in hexadecimal:
        if i in hexadecimal_nums:
            num = hexadecimal_nums[i]
        else:
            num = int(i)
        for j in range(3, -1, -1):
            converted += str(num//2**j)
            num = num % 2**j

    N = len(converted)
    last = 0
    for i in range(N-1, -1, -1):
        if converted[i] == '1':
            last = int(i)
            break

    result = []
    M = (N - (N-last)) // 6
    for i in range(M):
        code = ''
        for j in range(last-i*6, last-(i*6+6), -1):
            code += converted[j]
        code = code[::-1]
        result.append(pattern_code[code])

    print(f'#{tc}', end=' ')
    for i in range(M-1, -1, -1):
        print(result[i], end=' ')
    print()
