"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
try:
    with open("text_02.txt", encoding='utf-8') as file:
        lines_counter = 0
        content = file.readlines()
        print(f'В файле {len(content)} строк')
        for lines in content:
            lines_counter += 1
            lines = lines.replace("\n", "")
            words_counter = len(lines.split(" ")) if lines != '' else 0     # Если пустая строка, то количество слов = 0
            print(f'Количество слов в строке #{lines_counter} "{lines}"    - {words_counter}')

except IOError:
    print("Ошибка ввода-вывода")
