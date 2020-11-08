while True:
    number_original = int(input("Введите целое положительное число: "))
    if number_original >= 0:
        break

number = number_original
max_digit = 0

if number <=9:
    max_digit = number

while number >= 10:
    next_digit = number % 10
    if max_digit < next_digit:
        max_digit = next_digit
    number = number // 10

print(f"Наибольшая цифра в числе {number_original}: {max_digit}")
