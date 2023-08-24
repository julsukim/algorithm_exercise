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

T = int(input())
for tc in range(1, T+1):
    hexadecimal_arr = input()

    bit = ''
    for i in hexadecimal_arr:
        if i in hexadecimal_nums:
            num = hexadecimal_nums[i]
        else:
            num = int(i)
        for j in range(3, -1, -1):
            bit += str(num // 2 ** j)
            num = num % 2 ** j

    N = len(bit)//7
    print(f'#{tc}', end=' ')
    for i in range(N+1):
        decimal = ''
        if i == N:
            for j in range(N*7, len(bit)):
                decimal += bit[j]
        else:
            for j in range(i*7, i*7+7):
                decimal += bit[j]
        print(int(decimal, 2), end=' ')
    print()
