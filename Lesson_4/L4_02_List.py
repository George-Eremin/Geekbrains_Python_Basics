from random import randint

# Генерируем исходный список
start_list = [randint(0, 99) for _ in range(10)]
# start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_list = [start_list[i+1] for i in range(len(start_list) - 1) if start_list[i+1] > start_list[i]]

print(f'Исходный список: {start_list}')
print(f'Результат: {result_list}')
