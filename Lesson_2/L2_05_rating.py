my_list = [7, 5, 3, 3, 2]

while True:
    new_el = input("Введите новый элемент рейтинга: ")
    if new_el.isdigit():
        new_el = int(new_el)
        print(f"Начальное состояние рейтинга: {my_list}")

        if new_el > my_list[0]:
            pos = 0
        elif new_el < my_list[len(my_list)-1]:
            pos = len(my_list)
        else:
            pos = my_list.index(new_el)

        my_list.insert(pos, new_el)

        print(f"После добавления элемента: {my_list}")

        break
