import math

start = (192.79, 102.77)
end = (10, 120)

a = abs(end[1] - start[1])
b = abs(end[0] - start[0])

r = math.sqrt(a**2 + b**2)

radian = math.atan2(b, a)

print(r, math.degrees(radian)+180)
