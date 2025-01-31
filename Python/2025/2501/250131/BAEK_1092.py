import bisect
import sys
input = sys.stdin.readline

N = int(input())
weight_limits = list(map(int, input().split()))
M = int(input())
box_weights = list(map(int, input().split()))

weight_limits.sort()
box_weights.sort()
crain_points = [-1] * N
visited = set()

if weight_limits[-1] < box_weights[-1]:
    print(-1)
else:
    time = 0
    for i in range(N):
        idx = bisect.bisect_right(box_weights, weight_limits[i]) - 1
        if idx >= 0:
            crain_points[i] = idx

    while len(visited) < M:
        for i in range(N):
            idx = crain_points[i]
            while idx >= 0:
                if idx not in visited:
                    visited.add(idx)
                    crain_points[i] = idx
                    break
                idx -= 1

        time += 1

    print(time)
