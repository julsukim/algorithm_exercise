import sys

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{tc}: {A + B}')
