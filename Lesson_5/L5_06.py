"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
subject_statistics_dict = {}
try:
    with open("text_06.txt", encoding='utf-8') as file_source:
        content = file_source.readlines()
        for line in content:
            subject = line.split(':')[0]

            line_list = line.split(' ')

            lections_amount = line_list[1].replace('(л)', '')
            lections_amount = int(lections_amount) if lections_amount.isdigit() else 0

            practicum_amount = line_list[2].replace('(пр)', '')
            practicum_amount = int(practicum_amount) if practicum_amount.isdigit() else 0

            lab_amount = line_list[3].replace('\n', '')
            lab_amount = lab_amount.replace('.', '')
            lab_amount = lab_amount.replace('(лаб)', '')
            lab_amount = int(lab_amount) if lab_amount.isdigit() else 0

            total_amount = lections_amount + practicum_amount + lab_amount

            subject_statistics_dict[subject] = total_amount

    print(subject_statistics_dict)

except IOError:
    print("Ошибка ввода-вывода")
