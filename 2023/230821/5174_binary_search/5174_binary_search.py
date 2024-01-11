import sys
sys.stdin = open('input.txt')


def binary_search(r, N):
    global count, root, n_node
    if r <= N:
        binary_search(r*2, N)
        count += 1
        if r == 1:
            root = count
        if r == (N//2):
            n_node = count
        binary_search(r*2+1, N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(range(1, N+1))
    count = 0
    root = 999
    n_node = 888

    binary_search(1, N)
    print(f'#{tc} {root} {n_node}')