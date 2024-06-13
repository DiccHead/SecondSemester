class Record:
    __discipline_list = ["Матем. анал.", "Лин. ал.", "Информатика"]


    def __init__(self, discipline, group):
        if discipline in self.__discipline_list:
            self.__discipline = discipline
        else:
            print("Дисциплины нет в списке!")
        self.__group = group
        self.__content = {}

    def __str__(self):
        print("Предмет: ", self.__discipline, "Группа: ", self.__group)
        for i in self.__content.keys():
            print(i+":", self.__content[i])
        return "done."
    
    def count(self):
        return len(self.__content.keys())
    
    def names(self):
        return list(self.__content.keys())


    def put(self, student, grade):
        if grade in ["отлично", "хорошо", "удовл.", "неудовл.", "н/я"]:
            self.__content[student] = grade
        else:
            print("Недопустимая оценка:", grade)

    def get(self, student):
        if student in self.__content:
            return self.__content[student]
        else:
            print("Студента", student, "нет в ведомости.")
    
    def change(self, student, grade):
        if student in self.__content:
            self.__content[student] = grade
        else:
            print("Студента", student, "нет в ведомости.")

    def delete(self, student):
        if student in self.__content:
            del self.__content[student]
        else:
            print("Студента", student, "нет в ведомости.")

    def result(self):
        grades = []
        for i in self.__content.keys():
            grades.append(self.__content[i])
        return (grades.count("отлично"), grades.count("хорошо"), grades.count("удовл."), grades.count("неудовл."), grades.count("н/я"))
    

print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")