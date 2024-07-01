import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    TC, str_N = input().split()
    N = int(str_N)
    nums = list(input().split())
    sorted_nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = []

    for num in sorted_nums:
        for i in range(N):
            if num == nums[i]:
                result.append(nums[i])


    print(f'#{tc}')
    print(' '.join(result))
