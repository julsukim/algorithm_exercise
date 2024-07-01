from collections import deque

N = int(input())
arr = list(map(int, input().split()))
balloons = deque((i+1, val) for i, val in enumerate(arr))

result = []

i, move = balloons.popleft()
result.append(i)

while balloons:
    if move > 0:
        move = (move - 1) % len(balloons)
    else:
        move = move % len(balloons)

    balloons.rotate(-move)
    i, move = balloons.popleft()
    result.append(i)

print(*result)
