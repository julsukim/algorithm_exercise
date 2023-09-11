import math

S = (0, 0)
T = (20, 10)
H = (30, 30)
r = 5.73/2

x = abs(H[0] - S[0])
y = abs(H[1] - S[1])

a = math.sqrt(x**2 + y**2)
b = math.sqrt((abs(H[0] - T[0]))**2 + (abs(H[1] - T[1]))**2)
c = math.sqrt((abs(T[0] - S[0]))**2 + (abs(T[1] - S[1]))**2)

ga = math.atan(y/x)
da = math.acos((a**2 + b**2 - c**2)/(2*a*b))

d = math.sqrt((a*math.sin(da))**2 + ((b+2*r) - (a*math.cos(da)))**2)

na = math.acos((a**2 + d**2 - (b+2*r)**2)/(2*a*d))

direction = math.degrees(ga) + math.degrees(na)
print(direction)
