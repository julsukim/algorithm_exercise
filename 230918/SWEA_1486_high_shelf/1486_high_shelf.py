import sys
sys.stdin = open('input.txt')


def top(i, s, arr):
    if s >= B:
        arr.append(s)
    if i == N:
        return
    else:
        top(i + 1, s + heights[i], arr)
        top(i + 1, s, arr)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    arr = []
    top(0, 0, arr)
    print(f'#{tc} {min(arr) - B}')