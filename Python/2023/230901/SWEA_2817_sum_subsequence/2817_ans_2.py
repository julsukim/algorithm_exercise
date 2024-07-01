import sys
sys.stdin = open('input.txt')


def f(i, N, s, K, rs):
    global cnt
    global call
    call += 1
    if i==N:
        if s==K:
            cnt += 1
    elif s>K:           # 이미 넘어 버렸어
        return
    elif s+rs<K:        # 남은걸 다 더해도 못해
        return
    else:
        f(i+1, N, s+arr[i], K, rs-arr[i])
        f(i+1, N, s, K, rs-arr[i])


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    call = 0
    cnt = 0
    f(0, N, 0, K, sum(arr))

    print(f'#{tc} {cnt} {call}')
