"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def salary(hours: int, rate: int, bonus: int):
    """
    Вычисляет заработную плату по формуле: (выработка в часах * ставка в час) + премия
    :param hours: int
    :param rate: int
    :param bonus: int
    :return: int
    """
    return hours * rate + bonus


try:
    file, hours_arg, rate_arg, bonus_arg = argv
except ValueError:
    print("Invalid args")
    exit()

try:
    print(salary(hours=int(hours_arg), rate=int(rate_arg), bonus=int(bonus_arg)))
except ValueError:
    print("Invalid type of arguments")
    exit()

assert salary(hours=3, rate=100, bonus=22) == 322, "salary"
