"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
# Не очень понятно сформулировано задание ((


class Date:
    date: str
    day: int
    month: int
    year: int

    def __init__(self, date: str):
        self.date = date

    @staticmethod
    def dateValueCheck(day: int, month: int, year: int):
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            return True
        else:
            return False

    @classmethod
    def dateExtract(cls, date: str):
        """
        Возвращает день, месяц и год, если строка в формате 'DD-MM-YYYY'
        """
        day: int
        month: int
        year: int

        if date[0:2].isdigit() \
            and date[2:3] == '-' \
            and date[3:5].isdigit() \
            and date[5:6] == '-' \
            and date[6:10].isdigit() \
            and 6 <= len(date) <= 10:
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:10])
            if Date.dateValueCheck(day, month, year):
                return f'День: {day}, Месяц: {month}, Год: {year}'
            else:
                return 'Неверная дата'
        else:
            return 'Дата должна быть в формате "DD-MM-YYYY"'

    def __str__(self):
        return f'{self.date}'


date_1 = Date('01-12-2020')
print(Date.dateExtract('01-12-2020'))
print(Date.dateExtract('01-12-202'))
print(Date.dateExtract('01-12-22'))
print(Date.dateExtract('01-12-2'))
print(Date.dateExtract('abracadabra'))
print(Date.dateExtract('55-12-2020'))
print(Date.dateExtract('01-55-2020'))
print(Date.dateExtract('01-12-0'))
