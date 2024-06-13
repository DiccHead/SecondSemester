all_x = []
all_y = []


for x in range(-40, 41):
    x = x / 4
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


for i in range(len(all_x)):
    print(f"x = {all_x[i]}, y = {all_y[i]}")


print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")