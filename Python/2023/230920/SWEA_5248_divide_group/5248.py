import sys
sys.stdin = open('input.txt')


def find_set(x):
    if parent[x] == x:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    m_in = list(map(int, input().split()))

    parent = list(range(N + 1))
    for i in range(M):
        n1, n2 = m_in[i*2], m_in[i*2+1]
        union(n1, n2)

    group_cnt = set()
    for i in range(1, N+1):
        group_cnt.add(find_set(parent[i]))

    print(f'#{tc} {len(group_cnt)}')
