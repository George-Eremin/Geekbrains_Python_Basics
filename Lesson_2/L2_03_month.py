seasons_dict = {12: "Зима", 1: "Зима", 2: "Зима",
                3: "Весна", 4: "Весна", 5: "Весна",
                6: "Лето", 7: "Лето", 8: "Лето",
                9: "Осень", 10: "Осень", 11: "Осень"}

seasons_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]

# Наверняка есть более элегантное и короткое решение, но мне придумать не удалось (

while True:
    month = input("Введите номер месяца (1..12): ")
    if month.isdigit():
        month = int(month)
        if 1 <= month <= 12:
            break

print(f"Согласно словарю, месяц #{month} относится к времени года {seasons_dict.get(month)}.")
print(f"А согласно списку, месяц #{month} относится к времени года {seasons_list[month-1]}.")
