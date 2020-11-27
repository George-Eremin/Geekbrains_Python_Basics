"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

# Генерим файл с 4 случайными целыми числами от 1 до 10
try:
    with open("text_05.txt", "w") as file_target:
        for _ in range(4):
            file_target.write(str(randint(1, 10)) + ' ')

except IOError:
    print("Ошибка ввода-вывода")

# Читаем файл и считаем сумму
numbers_sum = 0
try:
    with open("text_05.txt") as file_source:
        numbers = file_source.read().split(' ')
        for number in numbers:
            if number != '':
                numbers_sum += int(number)
        print(numbers_sum)

except IOError:
    print("Ошибка ввода-вывода")
