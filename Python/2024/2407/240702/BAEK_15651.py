def recur(number, output):
    if number == M:
        result.append(' '.join(map(str, output)))
        return
    
    for i in range(1, N+1):
        output.append(i)
        recur(number+1, output)
        output.pop()


N, M = map(int, input().split())
result = []
recur(0, [])
print('\n'.join(result))
