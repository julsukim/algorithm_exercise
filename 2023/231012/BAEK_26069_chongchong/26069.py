import sys
input = sys.stdin.readline

N = int(input().rstrip())
dancers = set()
dancers.add('ChongChong')
for _ in range(N):
    p1, p2 = input().rstrip().split()
    if p1 in dancers:
        dancers.add(p2)
    elif p2 in dancers:
        dancers.add(p1)
print(len(dancers))
