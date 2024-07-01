string = input().strip(' ')
if string == '':
    P = 0
else:
    P = 1
print(string.count(' ') + P)
