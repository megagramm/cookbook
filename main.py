def make_cookbook():
    with open('recipes.txt') as file:
        cookbook = []
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
            cookbook.append({dishe_name: ingredients})
    return cookbook


print(*make_cookbook(), sep="\n")
print()


def get_shop_list_by_dishes(list_of_dishes: list, person_count: int):
    dishes = make_cookbook()
    shoping_list = dict()
    for dishe_dict in dishes:
        for dishe in dishe_dict.keys():
            if dishe in list_of_dishes:
                # print(dishe_dict.values())
                for ingredient in dishe_dict.get(dishe):
                    # print(ingredient)
                    if shoping_list.get(ingredient['ingredient_name']):
                        # print(ingredient['ingredient_name'], 'уже в словаре')
                        shoping_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                    else:
                        shoping_list.update({ingredient['ingredient_name']: {
                            'measure': ingredient['measure'],
                            'quantity': ingredient['quantity'] * person_count
                        }})
    print(shoping_list)


dishes_list = ['Запеченный картофель', 'Омлет']
get_shop_list_by_dishes(dishes_list, 2)
