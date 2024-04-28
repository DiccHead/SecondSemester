x0 = -10
xn = 10
deltaX = 0.25

def function(x0, xn, deltaX):
    if deltaX < 1:
        x0 = int(x0 / deltaX)
        xn = int(xn / deltaX)
    all_x = []
    all_y = []
    for x in range(x0, xn+1):
        if deltaX < 1:
            x *= deltaX
        if x > 1.75:
            if x != 2 and x != -3:
                y = ((x + 5) * (x - 6)) / ((x - 2)*(x + 3))
                all_x.append(x)
                all_y.append("{j:.3f}".format(j = y))
            else:
                all_x.append(x)
                all_y.append("none")
        if x <= 1.75:
            if x != 1:
                y = (x*x + 2*x + 4)/(x*x - 2*x +1)
                all_x.append(x)
                all_y.append("{j:.3f}".format(j = y))
            else:
                all_x.append(x)
                all_y.append("none")
    return all_x, all_y


all_x, all_y = function(x0, xn, deltaX)

for i in range(len(all_x)):
    print(f"x = {all_x[i]}, y = {all_y[i]}")