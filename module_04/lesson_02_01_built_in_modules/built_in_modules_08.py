from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
print(ar)
ad = degrees(ar)
print(ad)

print(ar == pi / 2)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
