N = int(input())
checkers = []
x_nodes = []
y_nodes = []

for i in range(N):
    x, y = map(int, input().split())
    checkers.append([x, y])
    x_nodes.append(x)
    y_nodes.append(y)

ans = [-1] * N

for x in x_nodes:
    for y in y_nodes:
        dist = []
        for ex, ey in checkers:
            dist.append(abs(x - ex) + abs(y - ey))
        dist.sort()

        temp = 0
        for i in range(len(dist)):
            temp += dist[i]
            if ans[i] == -1:
                ans[i] = temp
            else:
                ans[i] = min(ans[i], temp)
print(*ans)

# x_nodes.sort()
# y_nodes.sort()
#
# ranges = [[[] for _ in range(1000001)] for _ in range(1000001)]
# print(ranges)
# for i in x_nodes:
#     for j in y_nodes:
#         for checker in checkers:
#             ranges[i][j].append(abs(checker[0] - i) + abs(checker[1] - j))
#         ranges[i][j].sort()
#
# print(0, end=' ')
# for i in range(1, N+1):
#     min_range = int(1e9)
#     for j in x_nodes:
#         for k in y_nodes:
#             temp_range = sum(ranges[j][k][:i+1])
#             if temp_range < min_range:
#                 min_range = temp_range
#     print(min_range, end=' ')
# print()

# checkers = [list(map(int, input().split())) for _ in range(N)]
#
# x_ranges = [[] for _ in range(N)]
# y_ranges = [[] for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         x_ranges[i].append(abs(checkers[i][0] - checkers[j][0]))
#         y_ranges[i].append(abs(checkers[i][1] - checkers[j][1]))
#
# for i in range(N):
#     x_ranges[i] = sorted(x_ranges[i])
#     y_ranges[i] = sorted(y_ranges[i])
#
# print(0, end=' ')
# if N > 1:
#     for i in range(1, N):
#         min_x = 1000001
#         min_y = 1000001
#         for j in range(N):
#             temp_x = sum(x_ranges[j][:i+1])
#             temp_y = sum(y_ranges[j][:i+1])
#             if temp_x < min_x:
#                 min_x = temp_x
#             if temp_y < min_y:
#                 min_y = temp_y
#         print(min_x + min_y, end=' ')
# print()

# ranges = [[] for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         x_range = abs(checkers[i][0] - checkers[j][0])
#         y_range = abs(checkers[i][1] - checkers[j][1])
#         ranges[i].append(x_range + y_range)
#
# for i in range(N):
#     ranges[i] = sorted(ranges[i])
#
# if N == 1:
#     print(0)
# else:
#     print(0, end=' ')
#     for i in range(1, N):
#         min_range = 1000001
#         for j in range(N):
#             temp_range = sum(ranges[j][:i+1])
#             if temp_range < min_range:
#                 min_range = temp_range
#         print(min_range, end=' ')
# print()
# for range in ranges:
#     print(range)

