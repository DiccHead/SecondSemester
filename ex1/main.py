import math

print(f"Введите через запятую с пробелом все данные h, S1, S2, a")
all_in = input()
h, S1, S2, a = all_in.split(", ")
h = int(h)
S1 = int(S1)
S2 = int(S2)
a = int(a)

V = h/3 * (S1 + (S1*S2)**0.5 + S2)

SB = (S1 - S2) / math.cos(math.radians(a))
SB = abs(SB)

print(V, SB)