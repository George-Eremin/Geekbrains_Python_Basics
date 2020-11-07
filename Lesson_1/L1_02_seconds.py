seconds_amount = int(input("Введите общее количество секунд: "))

hours = seconds_amount // 3600  # Количество часов
minutes = (seconds_amount - hours * 3600) // 60  # Количество минут
seconds = seconds_amount % 60    # Количество секунд

print(f"{seconds_amount} секунд - это {hours}:{minutes}:{seconds}")
