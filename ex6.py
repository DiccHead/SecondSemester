

class number_operations:
    "При указани чисел в какой либо системе счисления, указывайте их в формате 'nba'. Где n - это номер системы счисления, b - это служебный символ, указывающий на разделение, а а - это число в этой системе счисления."



    def __init__(self):
        print("При указани чисел в какой либо системе счисления, указывайте их в формате 'nba'. Где n - это номер системы счисления, b - это служебный символ, указывающий на разделение, а а - это число в этой системе счисления.")

    @classmethod
    def convert_to_n(cls, a: int, n: int):
        s = ''
        while a > 0:
            c = a % n

            if c < 10:
                s = str(c) + s
            else:
                s = chr(ord('A')+c-10) + s

            a //= n
        
        return s

    @classmethod
    def convert_from_n(cls, a: str, n: int):
        power = 0
        s = 0
        for i in a[::-1]:

            if i < 'A':
                s += int(i) * (n**power)
            else:
                s += (ord(i)-ord('A')+10) * (n**power)

            power += 1
        
        return s
    
    @classmethod
    def convert_to_n_float(cls, a: float, n: int):
        s = ''
        sf = ''
        sd = ''
        af = int(a)
        while af > 0:
            c = af % n
            if c < 10:
                sf = str(c) + sf
            else:
                sf = chr(ord('A')+c-10) + sf
            af //= n
        
        ad = a - int(a)
        
        to_count = True
        while to_count:
            ad = ad * n

            if int(ad) < 10:
                sd = sd + str(int(ad))
            else:
                sd = sd + chr(ord('A')+int(ad)-10)
            
            if int(ad) == 0:
                to_count = False

            ad = ad - int(ad)
        
            

        s = sf + "." + sd
        return s
    
    @classmethod
    def get_slices(cls, i: str):
        n = int(i[:i.index('b')])
        a = i[i.index('b')+1:]
        return n, a

    @classmethod
    def find_equals(cls, sp: list):
        converted_list = []
        for i in sp:
            n, a = cls.get_slices(i)
            converted_list.append(cls.convert_from_n(a, n))

        new_list = converted_list
        for j in converted_list:
            if j != "None":
                equals = sp[converted_list.index(j)]
                new_list[new_list.index(j)] = "None"
                for k in new_list:
                    if str(k) == str(j):
                        equals = equals + '=' + sp[converted_list.index(k)]
                        new_list[new_list.index(k)] = "None"

                print(equals)
        
    @classmethod
    def find_sum_in_n(cls, sp: list, n1: int):
        converted_list = []
        for i in sp:
            n, a = cls.get_slices(i)
            converted_list.append(cls.convert_from_n(a, n))
        answer = sum(converted_list)
        answer = cls.convert_to_n(answer, n1)
        print(answer)
        




print("Задание 1:")
number_operations.find_equals(['16b11', '8b6', '4b013', '2b111'])
print('')

print("Задание 2:")
number_operations.find_sum_in_n(["2b1101", "4b22", "16bA"], 16)
print('')

print("Задание 3:")
print(number_operations.convert_to_n(150, 2))
print(number_operations.convert_to_n(150, 16))
print(number_operations.convert_to_n(150, 8))
print('')

print("Задание 4:")
print("1011 в десятичной системе счисления:", number_operations.convert_from_n("1011", 2))
print("10 в десятичной системе счисления:", number_operations.convert_from_n("10", 2))
print("1101 в десятичной системе счисления:", number_operations.convert_from_n("1101", 2))
print("Следовательно, знак между ними: +")
print('')

print("Задание 5:")
a = 5/3
b = 2/9
c = a + b
c = number_operations.convert_to_n_float(c, 3)
print(c[:c.index(".")]+c[c.index("."):c.index(".")+4])

print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")

#print(ins.convert_from_n("11", 16), ins.convert_from_n("6", 8), ins.convert_from_n("013", 4), ins.convert_from_n("111", 2))

# print(ins.convert_to_n(23, 16))
# print(ins.convert_to_n(23, 12))
# print(ins.convert_to_n(23, 9))
# print(ins.convert_to_n(15, 5))
# print(ins.convert_to_n(15, 7))
# ins.find_equals(['16b17', '5b12', '12b1B', '9b25', '5b30', '7b21'])