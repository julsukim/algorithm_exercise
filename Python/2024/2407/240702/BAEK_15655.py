from copy import deepcopy


def recur(cnt, output):
    if cnt == M:
        e = sorted(output)
        if e not in result:
            result.append(deepcopy(output))
        return
    
    for a in arr:
        if a not in output:
            output.append(a)
            recur(cnt+1, output)
            output.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [];
recur(0, [])

for i in result:
    print(' '.join(map(str, i)))
