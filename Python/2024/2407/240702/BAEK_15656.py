def recur(cnt, output):
    if cnt == M:
        result.append(' '.join(map(str, output)))
        return
    
    for e in arr:
        output.append(e)
        recur(cnt+1, output)
        output.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
recur(0, [])
print('\n'.join(result))


# def recur(cnt, output):
#     if cnt == M:
#         print(*output)
#         return
    
#     for e in arr:
#         output.append(e)
#         recur(cnt+1, output)
#         output.pop()


# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# recur(0, [])
