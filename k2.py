

class Publication:
    def  __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "Название: {x}, Автор: {y}".format(x=self.title, y=self.author)
    
    def print_info(self):
        print(self.__class__.__name__+": "+str(self))

    def search(self, info_type, info):
        if info_type == "Название":
            if self.title == info:
                return True
        if info_type == "Автор":
            if self.author == info:
                return True


class Book(Publication):
    def __init__(self, title, author, year_of_publishing, publishing):
        super().__init__(title, author)
        self.year_of_publishing = year_of_publishing
        self.publishing = publishing

    def __str__(self):
        return "{x}, Год издания: {y}, Издательство: {z}".format(x = super().__str__(), y = self.year_of_publishing, z = self.publishing)

    def search(self, info_type, info):
        if super().search(info_type, info) == True:
            return True
        if info_type == "Год издания":
            if self.year_of_publishing == info:
                return True
        if info_type == "Издательство":
            if self.publishing == info:
                return True


class Article(Publication):
    def __init__(self, title, author, magazine, issue, year_of_publishing):
        super().__init__(title, author)
        self.magazine = magazine
        self.issue = issue
        self.year_of_publishing = year_of_publishing

    def __str__(self):
        return "{x}, Журнал: {y}, Выпуск: {z}, Год издания: {w}".format(x = super().__str__(), y = self.magazine, z = self.issue, w = self. year_of_publishing)
    
    def search(self, info_type, info):
        if super().search(info_type, info) == True:
            return True
        if info_type == "Журнал":
            if self.magazine == info:
                return True
        if info_type == "Выпуск":
            if self.issue == info:
                return True
        if info_type == "Год издания":
            if self.year_of_publishing == info:
                return True


class DigitalSource(Publication):
    def __init__(self, title, author, link, annotation):
        super().__init__(title, author)
        self.link = link
        self.annotation = annotation

    def __str__(self):
        return "{x}, Ссылка: {y}, Аннотация: {z}".format(x = super().__str__(), y = self.link, z = self.annotation)
    
    def search(self, info_type, info):
        if super().search(info_type, info) == True:
            return True
        if info_type == "Ссылка":
            if self.link == info:
                return True
        if info_type == "Аннотация":
            if self.annotation == info:
                return True


book1 = Book("Сердца в Атлантиде", "Стивен Кинг", "2018", "АСТ")
book2 = Book("Сияние", "Стивен Кинг", "2024", "Neoclassic")
book3 = Book("Повелитель мух", "Голдинг Уильям", "2024", "Neoclassic")
article1 = Article("Что будет если надуть воздушный шарик в бутылке", "Афанасий 7на8 8на7", "Идиотские факты", "12", "2017")
article2 = Article("Новогодние праздники: Послевкусие", "Афанасий 7на8 8на7", "Идиотские факты Шипуден", "43", "2020")
digitalsource1 = DigitalSource("ЕГЭ Информатика: Личный опыт", "Сандаль Борисович", "https://youtu.be/dQw4w9WgXcQ?si=nyLMih2cMtNX1fSV", "О том, почему Артём ни за что не сдаст информатику на 80 баллов.")

publication_list = [book1, book2, book3, article1, article2, digitalsource1]

for i in publication_list:
    i.print_info()


author = input("Введите искомого автора: ")
for j in publication_list:
    if j.search("Автор", author):
        j.print_info()


print("Работу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")