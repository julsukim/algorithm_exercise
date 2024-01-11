X = int(input())

line = 0
maximum = 0
while X > maximum:
    line += 1
    maximum += line

i = maximum - X
if line % 2 == 0:
    f = line - i
    s = i + 1
else:
    f = i + 1
    s = line - i

print(f'{f}/{s}')
