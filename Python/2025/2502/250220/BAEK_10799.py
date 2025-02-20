import sys
input = sys.stdin.readline

arr = list(input()) + ['end']
n = len(arr)

cnt = 0
curr = 0
is_laser = False
for i in range(n):
    if arr[i+1] == 'end':
        break
    if is_laser:
        is_laser = False
        continue
    if arr[i] == '(' and arr[i+1] == ')':
        is_laser = True
        if curr != 0:
            cnt += curr
    elif arr[i] == '(' and arr[i+1] == '(':
        cnt += 1
        curr += 1
    elif arr[i] == ')':
        curr -= 1

print(cnt)
