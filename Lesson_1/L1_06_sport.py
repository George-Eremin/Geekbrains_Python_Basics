result_start = int(input("Введите стартовый результат: "))
result_end = int(input("Введите итоговый результат: "))

days_counter = 1
result_current = result_start

while result_current < result_end:
    result_current *= 1.1
    days_counter += 1
    # print(str(days_counter) +': ' + str(result_current))

print(f"На {days_counter}-й день спортсмен достиг результата - не менее {result_end} км.")
