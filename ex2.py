import math

#a = float(input("Введите A \n"))
#a = math.radians(a)


def functiona(a):
 step0:float = ((((((1 + a) + (round(math.pow(a,2),5))) / ((2 * a) + (round(math.pow(a,2),5)))) + 2) - (((1 - a) + (round(math.pow(a,2),5))) / ((2 * a) - (round(math.pow(a,2),5))))) * (5 - (2 * (round(math.pow(a,2),5)))))
 return step0


def functionb(a):
 step0:float = ((4 - (round(math.pow(a,2),5))) / 2)
 return step0
#z1 = (((1+a+a*a)/(2*a+a*a))+2-((1-a+a*a)/(2*a-a*a)))*(5-2*a*a)
#z2 = (4-a*a)/2

for a in range(10, 3601):
 a = a / 10
 a = math.radians(a)
 z1 = functiona(a)
 z2 = functionb(a)
 z1 = "{x:.2f}".format(x = z1)
 z2 = "{x:.2f}".format(x = z2)
 if z1 == z2:
    print(z1, z2, a)