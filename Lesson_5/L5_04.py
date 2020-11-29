"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
eng_rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open("text_04_source.txt", encoding='utf-8') as file_source:
        # Читаем строки
        content = file_source.readlines()
        # Переводим в список
        file_list = [[line.split(' — ')[0], line.split(' — ')[1]] for line in content]
        # print(file_list)

except IOError:
    print("Ошибка ввода-вывода")


try:
    with open("text_04_target.txt", "w", encoding='utf-8') as file_target:
        # Для каждой строки ищем в словаре перевод для нулевого элемента, добавляем разделитель и первый элемент,
        # и пишем в файл
        for el in range(len(file_list)):
            file_target.write(
                eng_rus_dict.get(file_list[el][0]) +
                ' — ' + file_list[el][1])

except IOError:
    print("Ошибка ввода-вывода")
