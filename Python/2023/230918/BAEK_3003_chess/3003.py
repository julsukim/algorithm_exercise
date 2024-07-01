pieces = list(map(int, input().split()))

N = 6
right = [1, 1, 2, 2, 2, 8]
to_correct = [0] * 6
for i in range(N):
    if pieces[i] == right[i]:
        continue
    elif pieces[i] > right[i]:
        to_correct[i] = -1 * abs(pieces[i] - right[i])
    else:
        to_correct[i] = abs(pieces[i] - right[i])

print(*to_correct)
