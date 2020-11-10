my_list = []
el = None

# Получаем список
while True:
    el = input("Введите следующий элемент списка. Для остановки нажмите Enter. >>>")
    if el != "":
        if el.isdigit():
            el = int(el)
        my_list.append(el)
    else:
        break

print("Список до перестановки: ")
print(my_list)


# Меняем попарно значения между элементами
i = 0
while i < len(my_list):
    if i < len(my_list) - 1:
        # print("Меняем местами {} и {}".format(my_list[i],my_list[i+1]))
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        # print("Теперь это {} и {}".format(my_list[i], my_list[i + 1]))
    i += 2

# Выводим результат
print("Список после перестановки: ")
print(my_list)
