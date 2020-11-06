secondsAmount = int(input("Введите общее количество секунд: "))

hours = secondsAmount // 3600  # Количество часов
minutes = (secondsAmount - hours * 3600) // 60  # Количество минут
seconds = secondsAmount % 60    # Количество секунд

print(f"{secondsAmount} секунд - это {hours}:{minutes}:{seconds}")
