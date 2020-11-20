goods = []
goods_names_list = []
goods_prices_list = []
goods_amounts_list = []
goods_units_list = []

# Ввод данных
counter = 1
while True:
    new_good_name = input(f"Введите название товара #{counter}. Для прекращения нажмите Enter. ")
    if new_good_name == "":
        break

    while True:
        new_good_price = input(f"Введите цену товара #{counter}: ")
        if new_good_price.isdigit():
            new_good_price = int(new_good_price)
            break

    while True:
        new_good_amount = input(f"Введите количество товара #{counter}: ")
        if new_good_amount.isdigit():
            new_good_amount = int(new_good_amount)
            break

    new_good_unit = input(f"Введите единицу измерения товара #{counter}: ")

    # Добавление в структуру
    new_good_dict = dict(название=new_good_name, цена=new_good_price, количество=new_good_amount, eд=new_good_unit)
    new_good_tuple = (counter, new_good_dict)
    goods.append(new_good_tuple)
    counter += 1

# Аналитика
for good in goods:
    goods_names_list.append(good[1].get("название"))
    goods_prices_list.append(good[1].get("цена"))
    goods_amounts_list.append(good[1].get("количество"))
    goods_units_list.append(good[1].get('eд'))

# Убираем дубликаты единиц измерения
goods_units_list = list(set(goods_units_list))

goods_analysis_data = dict(название=goods_names_list,
                           цена=goods_prices_list,
                           количество=goods_amounts_list,
                           eд=goods_units_list)

print(goods_analysis_data)
