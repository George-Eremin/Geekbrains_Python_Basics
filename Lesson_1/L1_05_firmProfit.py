income = int(input("Введите значение выручки за год: "))
costs = int(input("Введите значение издержек за год: "))

profit = income - costs

if profit > 0:
    print("Фирма закончила год с прибылью размером {}".format(profit))
    employees = int(input("Введите количество сотрудников: "))
    print("Прибыль в расчете на 1 сотрудника составляет: {}".format((profit/employees).__round__(2)))
elif profit < 0:
    print("Фирма закончила год с убытком размером {}".format(-profit))
else:
    print("Фирма закончила год с нулевым балансом")