s1 = 'abc'
s2 = 'abc'
s5 = s1[:2] + 'c'
print(s1, s2, s5)
if s1 == s5:
    print('s1 == s5')
else:
    print('s1 != s5')
if s1 is s5:
    print('s1 is s5')
else:
    print('s1 is not s5')

if s1 == s2:
    print('s1 == s2')
else:
    print('s1 != s2')
if s1 is s2:
    print('s1 is s2')
else:
    print('s1 is not s2')