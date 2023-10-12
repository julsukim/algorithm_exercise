import sys, copy
sys.stdin = open('input.txt')


def test(arr):
    for j in range(W):
        mc = 0
        cnt = 1
        for i in range(1, D):
            if arr[i-1][j] == arr[i][j]:
                cnt += 1
                if i + 1 == D:
                    if mc < cnt:
                        mc = cnt
            elif arr[i-1][j] != arr[i][j]:
                if mc < cnt:
                    mc = cnt
                if i + 1 == D:
                    if mc < cnt:
                        mc = cnt
                cnt = 1
        else:
            if mc < K:
                return False
    else:
        return True


def infusion(arr, c):
    global minimum
    if c >= minimum:
        return
    if test(arr):
        if minimum > c:
            minimum = c
        return
    else:
        for i in range(D):
            if visited[i]:
                continue
            visited[i] = 1
            c0_arr = copy.deepcopy(arr)
            c1_arr = copy.deepcopy(arr)
            c0_arr[i] = [0]*W
            infusion(c0_arr, c + 1)
            c1_arr[i] = [1]*W
            infusion(c1_arr, c + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    minimum = K
    visited = [0]*D

    print(f'#{tc}', end=' ')
    if test(film):
        print(0)
    else:
        infusion(film, 0)
        print(minimum)
