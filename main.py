MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0 # прибыль, суммируется от купленного кофе
}

#
# 1. Спросить о напитке - спрашивать бесконечно после окончания действия (изготовления напитка)
# 1.1. Если пишет off, выключать
#
# 2. Печатать отчет (остатки материала)
#
# 3. Проверить остатки ингредиентов для напитков. Если не хватает - вывести ошибку
#
# 4. Обработать деньги
# 4.1. Попросить вводить деньги: quarters, dimes, nickels, pennies
# 4.2. Посчитать сумму - хватает или нет
# 4.3. Вернуть сдачу
#
# 5. Изготовить кофе
# 5.1. Вычесть материалы
# 5.2. Написать, что кофе готов (вставить название)
#
# Начинаем заново
#

is_end = False

while not is_end:
    drink = input("What would you like? (espresso/latte/capuccino): ")

    if drink == "off":
        is_end = True
    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        ingredients = MENU[drink]["ingredients"]

        # проверка наличия ингредиентов
        for key in ingredients:
            if ingredients[key] > resources[key]:
                print(f"Sorry, there is not enough {key}")
                is_end = True

        if not is_end:
            # собираем бабки
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01 # in dollars
            coffee_cost = MENU[drink]["cost"]

            if total_money < coffee_cost:
                print("Not enough money. Money refunded")
                is_end = True
            else:
                # считаем бабки
                resources["money"] += coffee_cost
                change = total_money - coffee_cost

                # готовим кофий
                for key in ingredients:
                    resources[key] -= ingredients[key]


                # готовим кофий
                print(f"Here is ${format(change, '.2f')} in change")
                print(f"Here is your ${drink}. Enjoy!")





