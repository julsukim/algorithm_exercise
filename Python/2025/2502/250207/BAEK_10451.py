import sys
input = sys.stdin.readline

T = int(input())
answers = []
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        curr = i
        if visited[curr]:
            continue

        while True:
            if visited[curr]:
                break
            visited[curr] = True
            curr = arr[curr]

        cnt += 1

    answers.append(str(cnt))

print('\n'.join(answers))
