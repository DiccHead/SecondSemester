from math import log


def f(x):
    return (0.5+x**0.5)/(1+log(x)**2)


a = 2
b = 4
eps = 0.001

def get_area(a, b, n):
    deltaX = (b - a) / n
    
    multiplicator = 1
    if str(deltaX).count(".") != 0:
        multiplicator = 10**len(str(deltaX).split(".")[1])

    full_sum = 0
    for i in range(a*multiplicator+int(deltaX*multiplicator), b*multiplicator+1, int(deltaX*multiplicator)):
        i = i / multiplicator
        s = f(i-deltaX/2)*deltaX
        full_sum += s
    
    return full_sum


def calculate(a, b, eps):
    done = False
    full_sum = 0
    n = 1

    while done != True:
        S1 = get_area(a, b, n)
        n = n * 2
        S2 = get_area(a, b, n)

        if abs(S2-S1) < eps:
            full_sum = S2
            done = True


    print(full_sum)


calculate(a, b, eps)