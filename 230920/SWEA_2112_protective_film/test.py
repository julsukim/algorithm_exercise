'''
6 8 3
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1

6 8 3
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1

[[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1]]
[[0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1]]
'''

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


D, W, K = map(int, input().split())
film = [list(map(int, input().split())) for _ in range(D)]

print(test(film))