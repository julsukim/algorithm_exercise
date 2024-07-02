def recur(idx, sour, bitter, use):
    global answer

    if idx == N:
        if use > 0:
            answer = min(answer, abs(sour - bitter))
        return

    recur(idx+1, sour * arr[idx][0], bitter + arr[idx][1], use + 1)

    recur(idx+1, sour, bitter, use)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
recur(0, 1, 0, 0)
print(answer)
