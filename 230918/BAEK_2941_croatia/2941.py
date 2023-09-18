croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
result = 0
for i in croatia:
    word = word.replace(i, 'x')
print(len(word))
