string = input("Введите строку: ")

string_list = string.split(" ")

for i in range(len(string_list)):
    if len(string_list[i]) > 10:
        string_list[i] = string_list[i][:10]
    print(f"{i+1}: {string_list[i]}")
