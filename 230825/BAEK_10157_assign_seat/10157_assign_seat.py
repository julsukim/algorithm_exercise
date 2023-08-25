import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    C, R = map(int, input().split())
    K = int(input())
    audit = [[0]*C for _ in range(R)]

    if C*R < K:
        print(0)
    else:
