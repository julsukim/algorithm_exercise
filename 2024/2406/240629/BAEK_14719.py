import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))
highest = max(arr)
pre_high = arr[0]
next_high = arr[-1]
rains = 0

fw_index = 0
bw_index = 0
for i in range(1, W):
    if arr[i] == highest:
        fw_index = i
        break
    if arr[i] < pre_high:
        rains += pre_high - arr[i]
    else:
        pre_high = arr[i]

for j in range(W-1, -1, -1):
    if arr[j] == highest:
        bw_index = j
        break
    if arr[j] < next_high:
        rains += next_high - arr[j]
    else:
        next_high = arr[j]

if fw_index == bw_index:
    print(rains)
else:
    for k in range(fw_index, bw_index):
        if arr[k] < highest:
            rains += highest - arr[k]
    else:
        print(rains)
