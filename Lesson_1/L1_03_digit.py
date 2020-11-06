while True:
    digit = input("Введите цифру: ")
    if 0 <= int(digit) <= 9:
        break
    print("Нужно ввести целое число от 0 до 9.")

print(digit + " + " + digit*2 + " + " + digit*3 + " = " + str(int(digit) + int(digit*2) + int(digit*3)) )