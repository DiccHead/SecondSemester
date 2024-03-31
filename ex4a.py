a1 = [1, -2, 3, -4, 5]
a2 = [1, -2, -3, 4, 5]
a3 = [1, 2, 3, 4, 5]
a4 = [1, 2, 3, 4, 5]
a5 = [1, 2, 3, 4, 5]

A = [a1, a2, a3, a4, a5]

for i in A:
    print(i)

lines = []
line_count = 1
for a in A:
    count = 0
    for i in a:
        if i < 0:
            count += 1
    if count == 2:
        lines.append(line_count)
    line_count += 1

if len(lines) > 0:
    print("Отрицательные числа имеются в строчках под номерами: ")
    for i in lines:
        print(i)
else:
    print("Строк с отрицательными элементами не найдено")