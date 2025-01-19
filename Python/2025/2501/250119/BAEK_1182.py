import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))


def recur(i, total, pk):
    global result
    if i >= N:
        if pk > 0 and total == S:
            result += 1
        return
    recur(i+1, total + arr[i], pk + 1)
    recur(i+1, total, pk)
    return


result = 0
recur(0, 0, 0)
print(result)
