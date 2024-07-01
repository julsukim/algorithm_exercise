import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    target = input()
    p_len = len(pattern)
    t_len = len(target)

    p_idx = 0
    t_idx = 0
    while (p_idx < p_len) and (t_idx < t_len):
        if target[t_idx] == pattern[p_idx]:
            t_idx += 1
            p_idx += 1
        else:
            t_idx = t_idx - p_idx + 1
            p_idx = 0

    print(f'#{tc}', end=' ')
    if p_idx == p_len:
        print(1)
    else:
        print(0)