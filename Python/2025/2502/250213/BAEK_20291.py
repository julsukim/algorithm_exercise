import sys
input = sys.stdin.readline

N = int(input())

arr = [input().rstrip().split('.') for _ in range(N)]

dict = {}
for i in range(N):
    if arr[i][1] in dict:
        dict[arr[i][1]] = dict[arr[i][1]] + 1
    else:
        dict[arr[i][1]] = 1

dict_arr = [f'{key} {value}' for key, value in sorted(dict.items(), key=lambda x: x[0])]
print('\n'.join(dict_arr))
