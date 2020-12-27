"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class OwnExceptionZeroDivision(Exception):
    message = 'Делитель не может равняться нулю, введите ненулевое значение'

    def __str__(self):
        return self.message


while True:
    div_source = input('Введите делимое: ')
    if div_source.isdigit():
        div_source = float(div_source)
        break
    else:
        print('Введите число')

while True:
    div_by = input('Введите делитель: ')
    if div_by.isdigit():
        try:
            div_by = float(div_by)
            if div_by == 0:
                raise OwnExceptionZeroDivision
            break
        except OwnExceptionZeroDivision as err:
            print(err)
    else:
        print('Введите число')


print(f'Частное: {div_source / div_by}')
