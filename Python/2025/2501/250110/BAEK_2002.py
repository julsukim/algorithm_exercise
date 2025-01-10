import sys
input = sys.stdin.readline

N = int(input())
in_nums = [input() for _ in range(N)]
out_nums = [input() for _ in range(N)]

exit_nums_set = set()
in_i = 0
out_i = 0

result = 0

while out_i < N:
    if in_nums[in_i] == out_nums[out_i]:
        in_i += 1
        out_i += 1
        continue
    else:
        if in_nums[in_i] in exit_nums_set:
            in_i += 1
        else:
            result += 1
            exit_nums_set.add(out_nums[out_i])
            out_i += 1

print(result)
