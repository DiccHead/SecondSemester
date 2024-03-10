from math import radians, tan, acos

all_x = []
all_y = []

for x in range (0, 11):
    x = x / 10
    #x = radians(x)
    y = x**2 * tan(x) + acos(x**2)**2
    all_x.append(x)
    all_y.append("{j:.3f}".format(j = y))

print(all_x)
print(all_y)