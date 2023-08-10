import sys
sys.stdin = open('input.txt')

def paper(n):
    global memo
    if n<3:
        return memo[n]
    else:
        if memo[n]==0:
            memo[n] = paper(n-2) * 2 + paper(n-1)
        return memo[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    memo = [0] * (N + 1)
    memo[1] = 1
    memo[2] = 3
    print(f'#{tc} {paper(N//10)}')