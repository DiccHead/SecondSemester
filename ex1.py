from math import cos, radians

print(f"Введите через запятую с пробелом все данные h, S1, S2, a")
all_in = input()
h, S1, S2, a = all_in.split(", ")
h = int(h)
S1 = int(S1)
S2 = int(S2)
a = int(a)

V = h/3 * (S1 + (S1*S2)**0.5 + S2)

SB = (S1 - S2) / cos(radians(a))
SB = abs(SB)

print("{x:.2f}".format(x = V), "{x:.2f}".format(x = SB))

print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")