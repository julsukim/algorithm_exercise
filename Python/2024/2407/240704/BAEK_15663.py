# def recur(cnt, output):
#     if cnt == M:
#         e = ' '.join(map(str, output))
#         if e not in result:
#             result.append(e)
#         return
#
#     for e in arr:
#         if e not in output:
#             output.append(e)
#             recur(cnt + 1, output)
#             output.pop()
#
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# result = []
# recur(0, [])
# print('\n'.join(result))


# def recur(cnt, output):
#     if cnt == M:
#         result.append(output)
#         return
#
#     for i in range(len(arr)):
#         if not used[i]:
#             used[i] = True
#             output.append(arr[i])
#             recur(cnt + 1, output)
#             output.pop()
#             used[i] = False
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# result = []
# used = [False] * N
# recur(0, [])
# result.sort()
# for e in result:
#     print(*e)


def solution():
    check = 0
    if len(answer) == M:
        print(*answer)
        return
    for i in range(N):
        if check != num[i] and visited[i] == 0:
            answer.append(num[i])
            visited[i] = 1
            check = num[i]
            solution()
            answer.pop()
            visited[i] = 0


N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0]*N
answer = []
solution()
