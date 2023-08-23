import sys
sys.stdin = open('input.txt')

code_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{tc}', end=' ')

    zeros = '0' * M
    for i in arr:
        if i != zeros:
            codes = i
            break

    for i in range(M-1, -1, -1):
        if codes[i] == '1':
            end_i = i
            break

    pass_code = ''
    for i in range(end_i-55, end_i+1):
        pass_code += codes[i]

    nums = []
    for i in range(0, 8):
        output = ''
        for j in range(7 * i, 7 * (i + 1)):
            output += pass_code[j]
        if output in code_dict:
            nums.append(code_dict[output])
        else:
            print(0)
            break

    if len(nums) == 8:
        odd = 0
        even = 0
        for i in range(8):
            if i%2 == 0:
                odd += nums[i]
            else:
                even += nums[i]

        result = odd + even
        if (odd * 3 + even) % 10 == 0:
            print(result)
        else:
            print(0)

