def recur(idx, a, b, c, d, cost, use):
    global answer, ans_arr

    if P <= a and F <= b and S <= c and V <= d:
        if answer > cost:
            answer = cost
            ans_arr = use[:]
        return

    if idx == N:
        return

    use.append(idx+1)
    recur(idx+1, a+arr[idx][0], b+arr[idx][1], c+arr[idx][2], d+arr[idx][3], cost+arr[idx][4], use)
    use.pop()
    recur(idx+1, a, b, c, d, cost, use)


N = int(input())
P, F, S, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
ans_arr = []
recur(0, 0, 0, 0, 0, 0, [])

if answer != float('inf'):
    print(answer)
    print(*ans_arr)
else:
    print(-1)
