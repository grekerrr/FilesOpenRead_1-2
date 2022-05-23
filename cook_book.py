import os
from pprint import pprint


PATH = os.getcwd()
FILE_NAME = 'Recipes.txt'
path = os.path.join(PATH, FILE_NAME)


def recipes(file_name):
    with open(path, encoding='UTF-8') as COOK_BOOK:
        menu = {}
        for txt in COOK_BOOK.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            ingredients = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            menu[name] = ingredients
    return menu

print('Рецепты:')
pprint(recipes('Recipes.txt'))
print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in recipes('Recipes.txt'):
            ingredients = recipes('Recipes.txt')[dish]
            for ingredient in ingredients:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list.update({ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}})
        else:
            print(f'Блюдо {dish} отсутсвует в книге рецептов, проверьте!')
    print(f'Для приготовления блюд {dishes} на {person_count} человек необходимо:')
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))