import sys
sys.stdin = open('input.txt')


def drive(i, v):
    global minimum
    if v > minimum:
        return
    if i == N:
        v -= 1
        if minimum > v:
            minimum = v
        return
    else:
        for w in stops[i]:
            if w != 0:
                v += 1
                drive(w, v)
                v -= 1
            else:
                return


T = int(input())
for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    stops = [0]*(N+1)
    for i in range(1, N):
        stops[i] = list(range(i+1, i + arr[i-1] + 1))
    minimum = 101

    drive(1, 0)
    if minimum == 101:
        minimum = 0
    print(f'#{tc} {minimum}')
