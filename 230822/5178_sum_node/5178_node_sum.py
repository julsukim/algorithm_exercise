import sys
sys.stdin = open('input.txt')


def node_sum(l, N):
    if l <= N:
        a = node_sum(l*2, N)
        b = node_sum(l*2+1, N)
        if a != None and b == None:
            return a
        elif a != None and b != None:
            return a+b
        else:
            return tree[l]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        arr = list(map(int, input().split()))
        tree[arr[0]] = arr[1]

    result = node_sum(L, N)
    print(f'#{tc} {result}')