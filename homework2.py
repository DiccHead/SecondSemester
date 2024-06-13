from random import randint

class Arr:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
        self.__val = [0]*(self.b-self.a+1)

    a = property(lambda self: self.__a)
    b = property(lambda self: self.__b)

    def __str__(self):
        return " ".join(map(str, self.__val))
    
    def arr_range(self):
        return range(self.a, self.b+1)
    
    def get(self, i):
        if self.a <= i <= self.b:
            return self.__val[i - self.a]
        else:
            print("Недопустимый индекс", i)

    def put(self, i, x):
        if self.a <= i <= self.b:
            self.__val[i - self.a] = x
        else:
            print("Недопустимый индекс", i)
    
    def put_random(self, a, b):
        for i in self.arr_range():
            self.put(i, randint(a, b))


class Mtt:
    def __init__(self, a, b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__val = list([0]*(self.b-self.a+1) for i in range(self.d-self.c+1))

    a = property(lambda self: self.__a)
    b = property(lambda self: self.__b)
    c = property(lambda self: self.__c)
    d = property(lambda self: self.__d)

    def __str__(self):
        output = "\n".join(map(str, (" ".join(map(str, self.__val[i])) for i in range(self.d-self.c+1))))
        return output
    
    def horizontal_range(self):
        return range(self.a, self.b+1)
    
    def vertical_range(self):
        return range(self.c, self.d+1)
    
    def get(self, x, y):
        if self.a <= x <= self.b:
            if self.a <= y <= self.b:
                return self.__val[y-self.c][x-self.a]
            else:
                print("Недопустимый индекс", y)
        else:
            print("Недопустимый индекс", x)

    def put(self, x, y, value):
        if self.a <= x <= self.b:
            if self.a <= y <= self.b:
                self.__val[y-self.c][x-self.a] = value
            else:
                print("Недопустимый индекс", y)
        else:
            print("Недопустимый индекс", x)



# Z = Arr(-5, 5)
# print(Z.a, Z.b)
# print(Z)
# for i in Z.arr_range():
#     Z.put_random(-100, 100)
# print(Z)

Z = Mtt(-5, 5, -5, 5)
for x in Z.horizontal_range():
    for y in Z.vertical_range():
        Z.put(x, y, x*y)
print(Z)


print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")