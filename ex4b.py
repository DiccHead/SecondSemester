from random import randint
# a1 = [1, -2, 3, -4, 5]
# a2 = [1, -2, -3, 4, 5]
# a3 = [1, 2, 3, 4, 5]
# a4 = [1, 2, 3, 4, 5]
# a5 = [1, 2, 3, 4, 5]

# A = [a1, a2, a3, a4, a5]


def generation(n, m):
    A = []
    for i in range(m):
        a = []
        for j in range(n):
            k = randint(-100, 100)
            a.append(k)
        A.append(a)
    return A
        
A = generation(5, 5)


for i in A:
    print(i)


def count_lines(A):
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
        return "Отрицательные числа имеются в строчках под номерами: ", str([i for i in lines])
    else:
        return "Строк с отрицательными элементами не найдено"


print(count_lines(A))