import math

my = (0, 0)
target = (20, 10)
hole = (30, 30)
r = 5.73/2

# 내 공과 홀 거리 x, y, a
x = abs(hole[0] - my[0])
y = abs(hole[1] - my[1])
a = math.sqrt(x**2 + y**2)
print(a)

# 타겟과 홀 거리 b
b = math.sqrt((abs(hole[0] - target[0]))**2 + (abs(hole[1] - target[1]))**2)
print(b)

# 내 공과 타겟 거리 c
c = math.sqrt((abs(target[0] - my[0]))**2 + (abs(target[1] - my[1]))**2)
print(c)

# 홀과 내 공의 각도 ga
ga = math.atan(y/x)
print(math.degrees(ga))

# 홀과 내 공의 직선과 홀과 타겟의 직선의 각도 da
da = math.acos((a**2 + b**2 - c**2)/(2*a*b))
print(math.degrees(da))

# 내 공과 움직여야할 지점의 거리 d
print('da', math.sin(da))
print((a*(math.sin(da)))**2)
print(((b+2*r) - (a*(math.cos(da))))**2)
d = math.sqrt((a*(math.sin(da)))**2 + ((b+2*r) - (a*(math.cos(da))))**2)
print('d', d)

# 홀과 내 공의 직선과 내 공과 타겟의 직선의 각도 na
na = math.acos(((a**2) + (d**2) - ((b + 2*r)**2)) / (2*a*d))
print('na', math.degrees(na))

direction = math.degrees(ga) + math.degrees(na)
print(direction)
