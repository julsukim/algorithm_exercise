def paper(n):
    global memo
    if n<3:
        return memo[n]
    else:
        if memo[n]==0:
            memo[n] = paper(n-2) + paper(n-1)
        return memo[n]


N = int(input())
memo = [0] * (N + 3)
memo[1] = 1
memo[2] = 2
print(paper(N) % 10007)
