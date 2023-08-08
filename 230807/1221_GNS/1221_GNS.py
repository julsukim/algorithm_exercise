import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()
    str_nums = list(input().split())
    len_nums = int(M)
    new_nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    sorted_list = []

    for i in new_nums:
        for j in range(0, len_nums):
            if str_nums[j] == i:
                sorted_list.append(str_nums[j])

    print(f'#{tc}')
    for i in sorted_list:
        print(i, end=' ')
    print()