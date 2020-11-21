"""
Задание:
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

В данном файле реализован скрипт #2
"""
from itertools import cycle

source_list = 'Абра-швабра-кадабра-!'.split('-')

counter = 0
for word in cycle(source_list):
    if counter > 11:
        break
    print(word)
    counter += 1
