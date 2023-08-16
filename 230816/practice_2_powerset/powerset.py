import sys
sys.stdin = open('input.txt')

def powerset(idx, s):
    global cnt
    if idx == N:
        if s == 10:
            cnt += 1
        return

    else:
        selected[idx] = 1
        powerset(idx + 1, s + arr[idx])
        selected[idx] = 0
        powerset(idx + 1, s)

    return cnt

T = 1
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    selected = [0] * N
    cnt = 0
    s = 0

    print(f'#{tc} {powerset(0, s)}')
