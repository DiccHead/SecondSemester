from math import cos, sin, tan

a = float(input("Введите значение a: "))

z1 = (4-a**2)/2
#z2 = ((6-a-a**2)/(3+a))*((2*(a**2)+24+a**3+(12*a))/(a**2+12))*(1/2)
z2 = ((6+2*(a**2)-3*a-a**3)/(3+a**2))*((2*(a**2)+24+a**3+(12*a))/(a**2+12))*(1/2)

z1 = "{x:.2f}".format(x = z1)
z2 = "{x:.2f}".format(x = z2)

print("z1 = ", z1, " z2 = ", z2)

print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")