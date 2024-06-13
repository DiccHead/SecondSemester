class Lenght:
    def __init__(self, value, unit):
        self.__value = value
        self.__unit = unit

    def __get_unit(self):
        return self.__unit

    def __change_unit(self, unit):
        unit_dict = {"мм":0.1, "см":1, "дм":10, "м":100, "км":1000 }
        if unit in unit_dict:
            multiplicator = unit_dict[self.__unit]/unit_dict[unit]
            self.__value *= multiplicator
            self.__unit = unit

    def __get_value(self):
        if self.__value % 1 == 0:
            return int(self.__value)
        else:
            return self.__value

    unit = property(__get_unit, __change_unit)
    value = property(__get_value)


len1 = Lenght(100, "см")
print(len1.value)
len1.unit = "м"
print(len1.value)
len1.unit = "дм"
print(len1.value)
len1.unit = "км"
print(len1.value)
len1.unit = "мм"
print(len1.value)


print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")