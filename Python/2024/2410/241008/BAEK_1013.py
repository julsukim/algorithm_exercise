import re

TC = int(input())
pattern = re.compile('(100+1+|01)+')
for _ in range(TC):
    wave = input().strip()
    if pattern.fullmatch(wave):
        print('YES')
    else:
        print('NO')
