with open('recipes.txt') as file:
    dishes = []
    for line in file:
        first_line = line.strip()
        while first_line == "" or first_line == "\n":
            first_line = file.readline().strip()
        dishe_name = first_line
        dishe_count = int(file.readline())
        ingredients = []
        for _ in range(dishe_count):
            ingredients_tmp = file.readline().strip().split(' | ')
            product, product_count, product_measure = ingredients_tmp
            ingredients.append({'ingredient_name': product,
                              'quantity': int(product_count),
                              'measure': product_measure})
        file.readline()
        dishes.append({dishe_name: ingredients})

# print(*dishes, sep="\n")

# exit()


def get_shop_list_by_dishes(dishes_list: list, person_count: int):
    shoping_list = dict()
    # shoping_list.update({"Картофель": {'measure': 'кг', 'quantity': 2}})
    for dishe_dict in dishes:
        for dishe in dishe_dict.keys():
            if dishe in dishes_list:
                print(dishe_dict.values())
                for ingredient in dishe_dict.get(dishe):
                    print(ingredient)
                    if shoping_list.get(ingredient['ingredient_name']):
                        print(ingredient['ingredient_name'], 'уже в словаре')
                        shoping_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']*person_count
                    else:
                        shoping_list.update({ingredient['ingredient_name']:{ingredient['ingredient_name']: ingredient['measure'], 'quantity': ingredient['quantity']*person_count}})
    print(shoping_list)


dishes_list = ['Запеченный картофель', 'Омлет']
get_shop_list_by_dishes(dishes_list, 2)
