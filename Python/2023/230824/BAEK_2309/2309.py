import sys
sys.stdin = open('input.txt')

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
tot = sum(dwarfs)
result = []
for i in range(9):
    for j in range(i+1, 9):
        if tot - (dwarfs[i] + dwarfs[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    result.append(dwarfs[k])
                    result.sort()
            else:
                break
    if len(result) == 7:
        break
result.sort()
for i in result:
    print(i)